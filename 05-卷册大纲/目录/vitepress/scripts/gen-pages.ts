/**
 * 页面生成：按 outline.txt（显示真值）生成 75 个卷页＋539 个章页（站点根下 vNN/）。
 *
 * 2026-11-20 批次（ykla 令“最大化适配装配页，排除墨水屏”）：
 *  ①锚点统一为装配页式（vol-N／vol-N-ch-M／vol-N-ch-M-sec-A-B／…-sub-K），装配页深链可直接落到站点同锚；
 *  ②章页排印保留标题语义（节＝h2、小节＝h3），由 outline.css 复刻悬挂缩进与节号等宽——
 *    代价是节／小节不再是纯 `ul.sections > li` 列表，收益是 VitePress 右栏“本页目录”仍可用；
 *  ③溯源注改“默认收起＋注徽标”结构，三色分类在构建期判定（判据同 doc.js 块 3），
 *    无脚本时由 `html.js` 门控自动展开（`.js` class 由 head 内联脚本加），故 noscript 仍可读全文；
 *  ④卷页复刻卷段：导言 p.vol-overview、卷级定位注 p.vol-note 常显、章目 h3.chapter ＋计数徽标。
 *
 * 生成件（vitepress/.gitignore 的 v*\/ 排除），装配源零改动；结构与 SUMMARY 由 verify 门禁锁一致。
 */
import { mkdirSync, writeFileSync, rmSync } from 'node:fs'
import { createHash } from 'node:crypto'
import path from 'node:path'
import { SITE_ROOT, readCatalogJson, readOutline, readUiStrings, segs } from './lib/source'
import { NOTE_CLASS, chAnchor, htmlEsc, noteKind, secAnchor, subAnchor, volAnchor } from './lib/notes'

const OUT = SITE_ROOT
const PUB = path.join(SITE_ROOT, 'public')

/** Markdown 行内转义（题名进 `##` 标题时用；反斜杠转义交给 markdown-it）。 */
function escMd(s: string): string {
  return s.replace(/([\\`*_[\]<>|#])/g, '\\$1')
}
/** 题名 → Markdown 标题行内 HTML（⟦en:X⟧ 渲染为 <span lang="en">，其余按 md 规则转义）。 */
function inlineMd(title: string): string {
  return segs(title)
    .map((x) => (x.t === 'en' ? `<span lang="en">${escMd(x.s)}</span>` : escMd(x.s)))
    .join('')
}
/** 题名 → 纯 HTML 片段（卷页章目等 HTML 块用；实体直接转义，不经 markdown）。 */
function inlineHtml(title: string): string {
  return segs(title)
    .map((x) => (x.t === 'en' ? `<span lang="en">${htmlEsc(x.s)}</span>` : htmlEsc(x.s)))
    .join('')
}
const pad = (n: number, w = 2) => String(n).padStart(w, '0')
const plainOf = (t: string) => segs(t).map((x) => x.s).join('')

const tree = readOutline()
let chFiles = 0
let volFiles = 0

/** 供工具面（导出／时间线／图谱／修订史）惰性取用的全站数据；标题取纯文本（剥 ⟦en:⟧）。 */
const UI = readUiStrings() as Record<string, string>
const catalog = {
  version: UI['shell.page_version'] ?? '',
  counts: tree.counts,
  revs: readCatalogJson().revs as unknown[][],
  // 非正文文案真值源是 ui-strings.json，工具面板文案一律随数据下发，不在组件里另抄一份
  ui: UI,
  vols: [] as Array<Record<string, unknown>>,
}

for (const v of tree.vols) {
  const vdir = path.join(OUT, `v${pad(v.no)}`)
  // 只清理本卷目录（生成件），绝不触碰站点其他文件
  rmSync(vdir, { recursive: true, force: true })
  mkdirSync(vdir, { recursive: true })

  const secCount = v.chs.reduce((a, c) => a + c.secs.length, 0)
  const subCount = v.chs.reduce((a, c) => a + c.secs.reduce((b, s) => b + s.subs.length, 0), 0)

  // ---- 卷页：装配式卷块复刻（ykla 令“点击章/节/小节效果与 index.html 一致”）——
  // section.doc-block 包裹（卷题 h1 可折叠）、章 h3.chapter（▾ 点击折叠本章节列表）、
  // ul.sections > li（节号＋题＋注徽标）＋ ul.subsections（小节行内注），与装配页 DOM 同构；
  // 章页深链保留（章 id 不变，锚直达），折叠交互由 FoldLayer.vue 承担。
  const volLines: string[] = []
  volLines.push('---')
  volLines.push(`title: ${JSON.stringify(`第${v.roman}卷 ${plainOf(v.title)}`)}`)
  volLines.push('outline: false')
  volLines.push('---')
  volLines.push('')
  volLines.push(`<section class="doc-block" id="${volAnchor(v.no)}">`)
  volLines.push(`<h1>第${v.roman}卷  ${inlineHtml(v.title)}<span class="page-version" title="页面版本（UTC+8，YYYY.MM.DD-HH:MM）">${plainOf(catalog.version)}</span></h1>`)
  for (const p of v.intro) volLines.push(`<p class="vol-overview">${htmlEsc(p)}</p>`)
  for (const p of v.posnotes) volLines.push(`<p class="vol-note">${htmlEsc(p)}</p>`)
  volLines.push(`<p class="vol-count">本卷含 <strong>${v.chs.length}</strong> 章／<strong>${secCount}</strong> 节／<strong>${subCount}</strong> 小节。</p>`)
  for (const c of v.chs) {
    volLines.push(`<h3 class="chapter" id="${chAnchor(v.no, c.no)}">第 ${c.no} 章  ${inlineHtml(c.title)}</h3>`)
    volLines.push('<ul class="sections">')
    for (const s of c.secs) {
      const badge = s.notes.length
        ? `<button type="button" class="note-badge" aria-expanded="false" title="展开/折叠溯源注">注</button><span class="src ${NOTE_CLASS[noteKind(s.notes)]}">${htmlEsc(s.notes.join(' '))}</span>`
        : ''
      volLines.push(`<li id="${secAnchor(v.no, c.no, s.num)}"><span class="sec-num">${s.num}</span> ${inlineHtml(s.title)}${badge}`)
      if (s.subs.length) {
        volLines.push('<ul class="subsections">')
        s.subs.forEach((x, i) => {
          const subBadge = x.notes.length
            ? `<span class="src ${NOTE_CLASS[noteKind(x.notes)]}">${htmlEsc(x.notes.join(' '))}</span>`
            : ''
          volLines.push(
            `<li id="${subAnchor(v.no, c.no, s.num, i + 1)}"><span class="sec-num">${x.num}</span> ${inlineHtml(x.title)}${subBadge}</li>`,
          )
        })
        volLines.push('</ul>')
      }
      volLines.push('</li>')
    }
    volLines.push('</ul>')
  }
  volLines.push('</section>')
  volLines.push('')
  writeFileSync(path.join(vdir, 'index.md'), volLines.join('\n'), 'utf8')
  volFiles++

  const volData = {
    no: v.no,
    roman: v.roman,
    title: plainOf(v.title),
    intro: v.intro,
    posnotes: v.posnotes,
    chs: [] as Array<Record<string, unknown>>,
  }
  catalog.vols.push(volData)

  // ---- 章页：章题 h1 ＋ 节 h2（悬挂缩进）＋ 注徽标块 ＋ 小节 h3
  for (const c of v.chs) {
    const L: string[] = []
    const sc = c.secs.length
    const uc = c.secs.reduce((b, s) => b + s.subs.length, 0)
    L.push('---')
    L.push(`title: ${JSON.stringify(`第 ${c.no} 章 ${plainOf(c.title)}`)}`)
    L.push('outline: [2, 3]')
    L.push('---')
    L.push('')
    L.push(`# 第 ${c.no} 章 ${inlineMd(c.title)} {#${chAnchor(v.no, c.no)}}`)
    L.push('')
    L.push(`[← 返回第${v.roman}卷](./index.md) · ${sc} 节／${uc} 小节`)
    L.push('')
    for (const s of c.secs) {
      L.push(`## <span class="sec-num">${s.num}</span> ${inlineMd(s.title)} {#${secAnchor(v.no, c.no, s.num)}}`)
      L.push('')
      if (s.notes.length) {
        const kind = noteKind(s.notes)
        L.push(
          `<p class="sec-note"><button type="button" class="note-badge" aria-expanded="false" title="展开/折叠溯源注">注</button><span class="src ${NOTE_CLASS[kind]}">${htmlEsc(s.notes.join(' '))}</span></p>`,
        )
        L.push('')
      }
      s.subs.forEach((x, i) => {
        L.push(
          `### <span class="sec-num">${x.num}</span> ${inlineMd(x.title)} {#${subAnchor(v.no, c.no, s.num, i + 1)}}`,
        )
        L.push('')
        if (x.notes.length) {
          // 小节注：装配页为 li 内行内 .src（无徽标，仅全局“注”展开时可见），此处同理
          L.push(
            `<p class="sub-note"><span class="src ${NOTE_CLASS[noteKind(x.notes)]}">${htmlEsc(x.notes.join(' '))}</span></p>`,
          )
          L.push('')
        }
      })
    }
    writeFileSync(path.join(vdir, `c${pad(c.no)}.md`), L.join('\n'), 'utf8')
    chFiles++

    ;(volData.chs as Array<Record<string, unknown>>).push({
      no: c.no,
      title: plainOf(c.title),
      secs: c.secs.map((s) => ({
        num: s.num,
        title: plainOf(s.title),
        notes: s.notes.map((t) => ({ k: noteKind(s.notes), t })),
        subs: s.subs.map((x) => ({
          num: x.num,
          title: plainOf(x.title),
          notes: x.notes.map((t) => ({ k: noteKind(x.notes), t })),
        })),
      })),
    })
  }
}

// ---- 工具面数据（导出／时间线／图谱共用一份，惰性取用）：public/data/
mkdirSync(path.join(PUB, 'data'), { recursive: true })
const json = JSON.stringify(catalog)
writeFileSync(path.join(PUB, 'data', 'catalog-data.json'), json, 'utf8')
const sha = createHash('sha256').update(json, 'utf8').digest('base64')
writeFileSync(
  path.join(PUB, 'data', 'catalog-manifest.json'),
  `${JSON.stringify({ file: 'catalog-data.json', bytes: Buffer.byteLength(json), sha256: sha })}\n`,
  'utf8',
)

console.log(`[gen] PASS 卷页 ${volFiles} ＋ 章页 ${chFiles} → vNN/（站点根）`)
console.log(
  `[gen] PASS 工具面数据 ${(Buffer.byteLength(json) / 1024).toFixed(0)} KB → public/data/catalog-data.json（sha256 已落 manifest）`,
)
