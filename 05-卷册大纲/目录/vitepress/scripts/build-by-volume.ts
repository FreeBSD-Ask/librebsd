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
const urls = htmlRels
  .map((r) => (r === 'index.html' ? `${origin}/` : `${origin}/${r.replace(/\.html$/, '')}`))
  .sort()
  .map((u) => `  <url><loc>${u}</loc></url>`)
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

// ---- 4. 报告
const indexOk = existsSync(path.join(DIST, 'index.html'))
// 1 壳首页 ＋ 每卷 1 卷页 ＋ 章页（404 不计入 htmlRels）
const expectHtml =
  1 + volNos.length + tree.vols.filter((v) => volNos.includes(v.no)).reduce((a, v) => a + v.chs.length, 0)
console.log(
  `[build] PASS 合并 ${files} 件 → .vitepress/dist（分片 ${shards.length}，用时 ${((Date.now() - t0) / 1000).toFixed(0)}s）`,
)
console.log(
  `         首页 ${indexOk ? '在' : '缺'}；HTML ${htmlRels.length}（预期 ≥ ${expectHtml}）；hashmap ${Object.keys(hashmap).length} 项；sitemap ${urls.length} 条`,
)
if (!indexOk) {
  console.error('[build] FAIL 合并后缺 index.html')
  process.exit(1)
}
if (collisions.length) {
  console.warn(`[build] WARN 合并冲突 ${collisions.length} 件（同名不同内容，保留先到）：${collisions.slice(0, 8).join('、')}`)
}
if (clean) rmSync(BUILD, { recursive: true, force: true })
