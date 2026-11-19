/**
 * 分卷构建再合并：站点壳（home）＋ 75 卷逐卷独立构建，产物按路径合并进 .vitepress/dist。
 *
 * 为什么分卷：一次性把 614 页塞进单次构建时，SSR 与打包串成一整块，Wall time 与内存不可控、
 * 失败即全废、也无法按卷排障。分卷后每卷 1—12 页，单卷实测 6—8 s，失败只影响该卷。
 *
 * 为什么顺序：VitePress 的临时目录固定为 `<root>/.vitepress/.temp`，同根并行会互删中间件
 * （实测报 ENOENT … .temp/v01_c10.md.js）；而隔离根另起一份根目录又需自带 node_modules
 * （主题入口以绝对路径引用），机制成本高于收益。故顺序分卷，全量约 9—12 分钟。
 *
 * 合并步的整站再生：hashmap.json 取各分片并集（客户端路由按源路径查页数据，缺项会影响跨卷跳转）；
 * sitemap.xml 按合并后的实际 HTML 全量重生成（分片自产的只覆盖自身）。
 *
 * 用法：
 *   bun scripts/build-by-volume.ts              全量（home ＋ 75 卷）
 *   bun scripts/build-by-volume.ts --only 1-3   指定卷号区间（试点／排障）
 *   bun scripts/build-by-volume.ts --no-clean   保留 .build 中间树
 */
import {
  cpSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync,
} from 'node:fs'
import path from 'node:path'
import { spawn } from 'node:child_process'
import { SITE_ROOT, readOutline } from './lib/source'
import { sanitizeDist } from './lib/sanitize-dist'

const args = process.argv.slice(2)
const argOf = (k: string) => (args.includes(k) ? args[args.indexOf(k) + 1] : null)
const only = argOf('--only')
const clean = !args.includes('--no-clean')

const BUILD = path.join(SITE_ROOT, '.build')
const DIST = path.join(SITE_ROOT, '.vitepress', 'dist')
const VP_BIN = path.join(SITE_ROOT, 'node_modules', 'vitepress', 'bin', 'vitepress.js')
const HOST = 'https://freebsd-ask.github.io'
const BASEP = '/librebsd/'
const pad = (n: number) => String(n).padStart(2, '0')

const tree = readOutline()
let volNos = tree.vols.map((v) => v.no)
if (only) {
  const [a, b] = only.split('-').map(Number)
  volNos = volNos.filter((n) => n >= a && n <= (Number.isFinite(b) ? b : a))
}

/** --only 试点构建：日志标注「部分构建」，全集构建时须覆盖全部卷。 */
const partial = volNos.length !== tree.vols.length

type Shard = { key: string; label: string; pagesSrc: string | null }
const shards: Shard[] = [
  { key: 'home', label: '站点壳', pagesSrc: null },
  ...volNos.map((n) => ({ key: `v${pad(n)}`, label: `第${pad(n)}卷`, pagesSrc: path.join(SITE_ROOT, `v${pad(n)}`) })),
]

// ---- 1. 逐分片构建（同根顺序，srcDir/outDir 由 VP_SHARD 切换）
rmSync(BUILD, { recursive: true, force: true })
mkdirSync(BUILD, { recursive: true })

const failures: string[] = []
let done = 0
const t0 = Date.now()

for (const s of shards) {
  const src = path.join(BUILD, s.key)
  mkdirSync(src, { recursive: true })
  if (s.pagesSrc) {
    if (!existsSync(s.pagesSrc)) {
      failures.push(`${s.label}（缺卷页源，先跑 bun run gen）`)
      continue
    }
    cpSync(s.pagesSrc, path.join(src, path.basename(s.pagesSrc)), { recursive: true })
  } else {
    cpSync(path.join(SITE_ROOT, 'index.md'), path.join(src, 'index.md'))
  }

  const code = await new Promise<number>((resolve) => {
    const child = spawn(process.execPath, [VP_BIN, 'build'], {
      cwd: SITE_ROOT,
      env: { ...process.env, VP_SHARD: s.key },
      stdio: ['ignore', 'pipe', 'pipe'],
    })
    let out = ''
    child.stdout?.on('data', (d) => (out += d))
    child.stderr?.on('data', (d) => (out += d))
    child.on('close', (c) => {
      if (c !== 0) console.error(`[build] ✗ ${s.label} exit=${c}\n${out.split('\n').slice(-14).join('\n')}`)
      resolve(c ?? 1)
    })
  })
  done++
  const secs = ((Date.now() - t0) / 1000).toFixed(0)
  if (code === 0) console.log(`[build] ${String(done).padStart(3)}/${shards.length} ✓ ${s.label}（累计 ${secs}s）`)
  else failures.push(s.label)
}

if (failures.length) {
  console.error(`[build] FAIL ${failures.length} 个分片失败：${failures.join('、')}`)
  process.exit(1)
}

// ---- 2. 合并
rmSync(DIST, { recursive: true, force: true })
mkdirSync(DIST, { recursive: true })
const collisions: string[] = []
const DERIVED = ['hashmap.json', 'sitemap.xml', '404.html']
let files = 0

function mergeInto(from: string, to: string) {
  for (const name of readdirSync(from)) {
    const srcF = path.join(from, name)
    const dst = path.join(to, name)
    if (statSync(srcF).isDirectory()) {
      mkdirSync(dst, { recursive: true })
      mergeInto(srcF, dst)
      continue
    }
    const relDst = path.relative(DIST, dst).replace(/\\/g, '/')
    if (existsSync(dst)) {
      const a = readFileSync(srcF)
      const b = readFileSync(dst)
      if (!DERIVED.includes(relDst) && (a.length !== b.length || !a.equals(b))) collisions.push(relDst)
      continue
    }
    cpSync(srcF, dst)
    files++
  }
}
mergeInto(path.join(BUILD, 'out', 'home'), DIST)
for (const n of volNos) mergeInto(path.join(BUILD, 'out', `v${pad(n)}`), DIST)

// ---- 3. 整站派生物再生
const hashmap: Record<string, string> = {}
for (const s of shards) {
  const f = path.join(BUILD, 'out', s.key, 'hashmap.json')
  if (!existsSync(f)) continue
  Object.assign(hashmap, JSON.parse(readFileSync(f, 'utf8')) as Record<string, string>)
}
writeFileSync(path.join(DIST, 'hashmap.json'), `${JSON.stringify(hashmap)}\n`, 'utf8')

const htmlRels: string[] = []
function walkHtml(dir: string, rel = '') {
  for (const name of readdirSync(dir)) {
    const full = path.join(dir, name)
    const r = rel ? `${rel}/${name}` : name
    if (statSync(full).isDirectory()) walkHtml(full, r)
    else if (name.endsWith('.html') && name !== '404.html') htmlRels.push(r)
  }
}
walkHtml(DIST)
const origin = `${HOST}${BASEP.replace(/\/$/, '')}`
/** 合并后 HTML → cleanUrls 路由：`index.html`→`/`、`vNN/index.html`→`/vNN/`、`vNN/cMM.html`→`/vNN/cMM`。 */
function routeOf(rel: string): string {
  if (rel === 'index.html') return '/'
  if (rel.endsWith('/index.html')) return `/${rel.slice(0, -'index.html'.length)}`
  return `/${rel.replace(/\.html$/, '')}`
}
const routes = htmlRels.map(routeOf).sort()
const urls = routes.map((r) => `  <url><loc>${origin}${r}</loc></url>`)
writeFileSync(
  path.join(DIST, 'sitemap.xml'),
  '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    `${urls.join('\n')}\n</urlset>\n`,
  'utf8',
)

// ---- 3c. 产物净化：撞 `.bak` 判据的内容哈希片段改名＋引用回写
const san = sanitizeDist(DIST)
if (san.renamed.length) {
  console.log(`[build] 净化 ${san.renamed.length} 件撞名产物（引用回写 ${san.touched} 件）：${san.renamed.slice(0, 3).join('、')}`)
}

// ---- 4. 完整性断言（集合级，非仅计数）
const problems: string[] = []

// 4a. 预期路由集合：首页 ＋ 每卷 1 卷页 ＋ 各自章页（与 SUMMARY 号序由 verify 锁死，此处按树展开）
const volOf = (n: number) => tree.vols.find((v) => v.no === n)
const expected = new Set<string>(['/'])
for (const n of volNos) {
  expected.add(`/v${pad(n)}/`)
  for (const c of volOf(n)?.chs ?? []) expected.add(`/v${pad(n)}/c${pad(c.no)}`)
}
const actual = new Set(htmlRels.map(routeOf))
const missingPages = [...expected].filter((r) => !actual.has(r))
const extraPages = [...actual].filter((r) => !expected.has(r))
if (missingPages.length) problems.push(`缺页 ${missingPages.length} 项：${missingPages.slice(0, 5).join('、')}`)
if (extraPages.length) problems.push(`多页 ${extraPages.length} 项：${extraPages.slice(0, 5).join('、')}`)

// 4b. hashmap：键集合须覆盖全部内容页，且每个值都能解析到 assets 下的页数据 chunk
const keyOf = (r: string) =>
  r === '/' ? 'index.md' : `${r.replace(/^\//, '').replace(/\//g, '_').replace(/_$/, '_index')}.md`
const expectKeys = new Set([...expected].map(keyOf))
const hmKeys = new Set(Object.keys(hashmap))
const hmMissing = [...expectKeys].filter((k) => !hmKeys.has(k))
const hmExtra = [...hmKeys].filter((k) => !expectKeys.has(k))
if (hmMissing.length) problems.push(`hashmap 缺键 ${hmMissing.length} 项：${hmMissing.slice(0, 5).join('、')}`)
if (hmExtra.length) problems.push(`hashmap 多键 ${hmExtra.length} 项：${hmExtra.slice(0, 5).join('、')}`)
const noChunk = [...hmKeys].filter((k) => !existsSync(path.join(DIST, 'assets', `${k}.${hashmap[k]}.js`)))
if (noChunk.length) problems.push(`hashmap 指向的页数据缺失 ${noChunk.length} 项：${noChunk.slice(0, 3).join('、')}`)

// 4c. sitemap：实写文件的 URL 集合须与预期路由集合逐条相等
const smText = readFileSync(path.join(DIST, 'sitemap.xml'), 'utf8')
const smRoutes = new Set(
  [...smText.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1].slice(origin.length) || '/'),
)
if (smRoutes.size !== expected.size) problems.push(`sitemap 条数 ${smRoutes.size} ≠ 预期 ${expected.size}`)
for (const r of expected) if (!smRoutes.has(r)) problems.push(`sitemap 缺 ${r}`)
for (const r of smRoutes) if (!expected.has(r)) problems.push(`sitemap 多 ${r}`)

// 4d. base 双前缀：全 dist 文本件（html/js/css/json/xml）两种错形态
const DUP = [`${BASEP}${BASEP.slice(1)}`, '//librebsd/', `${BASEP.slice(1)}//`]
const dupHits: string[] = []
function walkText(dir: string, rel = '') {
  for (const name of readdirSync(dir)) {
    const full = path.join(dir, name)
    const r = rel ? `${rel}/${name}` : name
    if (statSync(full).isDirectory()) { walkText(full, r); continue }
    if (!/\.(html|js|mjs|css|json|xml)$/i.test(name)) continue
    const t = readFileSync(full, 'utf8')
    if (DUP.some((d) => t.includes(d))) dupHits.push(r)
  }
}
walkText(DIST)
if (dupHits.length) problems.push(`base 双前缀 ${dupHits.length} 件：${dupHits.slice(0, 3).join('、')}`)

// 4e. 合并冲突（同名不同内容）一律判失败：内容不可判定，不得静默保留先到
if (collisions.length) problems.push(`合并冲突 ${collisions.length} 件：${collisions.slice(0, 5).join('、')}`)

const indexOk = existsSync(path.join(DIST, 'index.html'))
if (!indexOk) problems.push('合并后缺 index.html')
console.log(
  `[build] ${partial ? '部分构建' : 'PASS'} 合并 ${files} 件 → .vitepress/dist（分片 ${shards.length}${partial ? `／全集 ${tree.vols.length} 卷` : ''}，用时 ${((Date.now() - t0) / 1000).toFixed(0)}s）`,
)
console.log(
  `         首页 ${indexOk ? '在' : '缺'}；HTML ${htmlRels.length}（预期 = ${expected.size}）；hashmap ${hmKeys.size} 项；sitemap ${smRoutes.size} 条`,
)

// 4f. 全集构建须覆盖全部卷（partial 在顶部声明；此处只做集合完整性断言）
if (!partial && new Set(volNos).size !== tree.vols.length) problems.push('全集构建卷号集合不完整')

if (problems.length) {
  console.error('[build] FAIL 合并后完整性断言：')
  for (const x of problems.slice(0, 20)) console.error('  ✗ ' + x)
  process.exit(1)
}
if (clean) rmSync(BUILD, { recursive: true, force: true })
