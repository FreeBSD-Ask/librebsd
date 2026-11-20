/**
 * 工具面数据层与导出器（浏览器端）：导出六格式、节级时间线、结构修订史、跨卷关联图谱。
 *
 * 数据源＝构建期产物 `public/data/catalog-data.json`（gen-pages.ts 生成），惰性取用一次并缓存；
 * 完整性按装配页 data blob 的等价做法校验：manifest 给出 SHA-256，取回后自算比对，不符即拒用。
 * 导出格式逐项对齐装配页 doc.js（SUMMARY／JSON／CSV／TXT 四文本格式的抬头、缩进、防公式注入；
 * PDF 走打印；HTML 本体走同源 download）。
 */
import { withBase } from 'vitepress'
import { chAnchor, secAnchor, subAnchor, volAnchor } from '../../../scripts/lib/notes'

export interface NoteT {
  k: "xref" | "mig" | "src"
  t: string
}
export interface SubT {
  num: string
  title: string
}
export interface SecT {
  num: string
  title: string
  notes: NoteT[]
  subs: SubT[]
}
export interface ChT {
  no: number
  title: string
  secs: SecT[]
}
export interface VolT {
  no: number
  roman: string
  title: string
  intro: string[]
  posnotes: string[]
  chs: ChT[]
}
export interface CatalogT {
  version: string
  counts: { vols: number; chs: number; secs: number; subs: number; notes: number; sectionsWithNotes: number }
  revs: unknown[][]
  ui: Record<string, string>
  vols: VolT[]
}

let pending: Promise<CatalogT> | null = null

/** Uint8Array → base64（分块，避免 apply 参数上限）。 */
function u8ToB64(u8: Uint8Array): string {
  let out = ''
  const CH = 0x8000
  for (let i = 0; i < u8.length; i += CH) {
    out += String.fromCharCode(...u8.subarray(i, i + CH))
  }
  return btoa(out)
}

async function sha256b64(text: string): Promise<string> {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text))
  return u8ToB64(new Uint8Array(buf))
}

/** 取工具面数据：manifest 先行，SHA-256 自算比对（不依赖 HTTP 层 SRI，静态托管也可失败关闭）。 */
export function loadCatalog(): Promise<CatalogT> {
  if (pending) return pending
  pending = (async () => {
    const mRes = await fetch(withBase('/data/catalog-manifest.json'), { cache: 'no-cache' })
    if (!mRes.ok) throw new Error(`manifest HTTP ${mRes.status}`)
    const manifest = (await mRes.json()) as { file: string; bytes: number; sha256: string }
    const res = await fetch(withBase(`/data/${manifest.file}`), { cache: 'no-cache' })
    if (!res.ok) throw new Error(`data HTTP ${res.status}`)
    const text = await res.text()
    if (crypto.subtle && typeof TextEncoder !== 'undefined') {
      const got = await sha256b64(text)
      if (got !== manifest.sha256) throw new Error('数据文件完整性校验失败（SHA-256 不符）')
    }
    const cat = JSON.parse(text) as CatalogT
    if (!cat.vols?.length) throw new Error('数据文件无卷目')
    return cat
  })()
  // 失败不缓存，允许重试
  pending.catch(() => {
    pending = null
  })
  return pending
}

/* ---- 结构视图（buildStructure 等价物；导出四文本格式共用） ---- */
export interface StructSec {
  id: string
  num: string
  title: string
  note: string
  subs: Array<{ id: string; num: string; title: string; note: string }>
}
export interface StructCh {
  id: string
  no: number
  title: string
  sections: StructSec[]
}
export interface StructVol {
  id: string
  no: number
  title: string
  chapters: StructCh[]
}

/** 卷题显示形（与装配页 h2 文本一致：第N卷＋题名；N 取罗马数字原文）。 */
export function volDisplay(v: VolT): string {
  return `第${v.roman}卷  ${v.title}`
}

export function buildStructure(cat: CatalogT): StructVol[] {
  return cat.vols.map((v) => ({
    id: volAnchor(v.no),
    no: v.no,
    title: volDisplay(v),
    chapters: v.chs.map((c) => ({
      id: chAnchor(v.no, c.no),
      no: c.no,
      title: `第 ${c.no} 章 ${c.title}`,
      sections: c.secs.map((s) => ({
        id: secAnchor(v.no, c.no, s.num),
        num: s.num,
        title: s.title,
        note: s.notes.map((n) => n.t).join(' '),
        subs: s.subs.map((x, i) => ({
          id: subAnchor(v.no, c.no, s.num, i + 1),
          num: x.num,
          title: x.title,
          note: x.notes.map((n) => n.t).join(' '),
        })),
      })),
    })),
  }))
}

export function exportFileName(cat: CatalogT, ext: string): string {
  const v = (cat.version || '').replace(/:/g, '-')
  return `目录-${v}.${ext}`
}

/** 文本文件下载（Blob＋a[download]）。 */
export function download(name: string, text: string, type: string): void {
  const blob = new Blob([text], { type: `${type};charset=utf-8` })
  const a = document.createElement('a')
  a.href = URL.createObjectURL(blob)
  a.download = name
  document.body.appendChild(a)
  a.click()
  a.remove()
  setTimeout(() => URL.revokeObjectURL(a.href), 1000)
}

/** SUMMARY（Markdown）：抬头四行＋`## 正文`＋`### 卷题`／`- [章]`／`  - [节]`／`    - [小节]`＋统计行。 */
export function exportSummaryText(cat: CatalogT): string {
  const ui = cat.ui
  const U = (k: string, d = '') => ui[k] ?? d
  const lines: string[] = []
  lines.push('# Summary')
  lines.push('')
  lines.push(U('ui.export.sum_title'))
  lines.push(U('ui.export.sum_source'))
  lines.push(U('ui.export.sum_note'))
  lines.push(U('ui.export.sum_time') + new Date().toLocaleString('zh-CN', { hour12: false }))
  lines.push('')
  lines.push(U('ui.export.sum_head', '## 正文'))
  lines.push('')
  let chCount = 0
  let secCount = 0
  cat.vols.forEach((v, vi) => {
    const vNo = String(vi + 1).padStart(2, '0')
    lines.push(`### ${volDisplay(v)}`)
    lines.push('')
    for (const c of v.chs) {
      chCount++
      const chTitle = `第 ${c.no} 章 ${c.title}`
      const chDir = `第${vNo}卷/第${c.no}章`
      lines.push(`- [${chTitle}](./${chDir}/概述.md)`)
      for (const s of c.secs) {
        secCount++
        lines.push(`  - [${s.num} ${s.title}](./${chDir}/${s.num}.md)`)
        for (const x of s.subs) {
          lines.push(`    - [${x.num} ${x.title}](./${chDir}/${x.num}.md)`)
        }
      }
    }
    lines.push('')
  })
  lines.push('')
  lines.push('---')
  lines.push('')
  lines.push(
    U('ui.export.stats_fmt', '统计：{v} 卷 {c} 章 {s} 节。')
      .replace('{v}', String(cat.vols.length))
      .replace('{c}', String(chCount))
      .replace('{s}', String(secCount)),
  )
  return lines
    .join('\n')
    .replace(/\u3000/g, ' ')
    .replace(/\u00a0/g, ' ')
    .replace(/[ \t]+$/gm, '')
}

/** JSON：`{volumes, metrics}`，缩进 1（装配页同式）。 */
export function exportJsonText(cat: CatalogT): string {
  const structure = buildStructure(cat)
  return JSON.stringify(
    {
      volumes: structure,
      metrics: {
        volumes: cat.vols.length,
        chapters: cat.vols.reduce((a, v) => a + v.chs.length, 0),
        sections: cat.vols.reduce((a, v) => a + v.chs.reduce((b, c) => b + c.secs.length, 0), 0),
      },
    },
    null,
    1,
  )
}

/** CSV：抬头 ui.export.csv_header；小节行章列留空；BOM＋CRLF；单元格防公式注入。 */
export function exportCsvText(cat: CatalogT): string {
  const U = (k: string, d = '') => cat.ui[k] ?? d
  const cell = (x: unknown): string => {
    let s = String(x)
    if (/^[=+\-@\t\r]/.test(s)) s = `'${s}`
    return `"${s.replace(/"/g, '""')}"`
  }
  const lines = [U('ui.export.csv_header', '卷,章,节号,节名,溯源注')]
  for (const v of cat.vols) {
    const vt = volDisplay(v)
    for (const c of v.chs) {
      const ct = `第 ${c.no} 章 ${c.title}`
      for (const s of c.secs) {
        lines.push([cell(vt), cell(ct), cell(s.num), cell(s.title), cell(s.notes.map((n) => n.t).join(' '))].join(','))
        for (const x of s.subs) {
          lines.push([cell(vt), cell(''), cell(x.num), cell(x.title), cell(x.notes.map((n) => n.t).join(' '))].join(','))
        }
      }
    }
  }
  return `\ufeff${lines.join('\r\n')}`
}

/** TXT（纯文本，Markdown 样式、无地址）：`# 卷`／`  ## 章`／`    - 节`／`      - 小节`；抬头与 doc.js 逐字同。 */
export function exportTxtText(cat: CatalogT): string {
  const L: string[] = ['# 给我自由—一部 BSD 史 完整目录（纯文本）']
  for (const v of cat.vols) {
    L.push(`# ${volDisplay(v)}`)
    for (const c of v.chs) {
      L.push(`  ## 第 ${c.no} 章 ${c.title}`)
      for (const s of c.secs) {
        L.push(`    - ${s.num} ${s.title}`)
        for (const x of s.subs) L.push(`      - ${x.num} ${x.title}`)
      }
    }
  }
  return L.join('\n')
}

/** PDF：打印（装配页 exportPdf 的主通道；打印样式见 outline.css @media print）。 */
export function printPdf(): void {
  window.print()
}

/** HTML 本体：http 通道以同源 a[download] 直取当前页原始文档（剥离 hash/query）。 */
export function exportHtmlSelf(cat: CatalogT): void {
  const a = document.createElement('a')
  a.download = exportFileName(cat, 'html')
  if (String(location.protocol) === 'file:') {
    a.href = URL.createObjectURL(
      new Blob([`<!DOCTYPE html>\n${document.documentElement.outerHTML}`], { type: 'text/html;charset=utf-8' }),
    )
  } else {
    a.href = String(location.href).split('#')[0].split('?')[0]
  }
  document.body.appendChild(a)
  a.click()
  a.remove()
}

/* ---- 时间线（F4）：节名＋章题抽首个 1600—2049 年份，按年聚簇 ---- */
const YEAR_RE = /(1[6-9]\d\d|20[0-4]\d)/g

export interface TimelineRow {
  year: string
  vol: string
  num: string
  title: string
  href: string
}
export function buildTimeline(cat: CatalogT): { rows: TimelineRow[]; years: number; total: number } {
  const rows: TimelineRow[] = []
  let total = 0
  for (const v of cat.vols) {
    for (const c of v.chs) {
      for (const s of c.secs) {
        total++
        const m = `${s.title} ${c.title}`.match(YEAR_RE)
        if (!m) continue
        rows.push({
          year: m[0],
          vol: volDisplay(v),
          num: s.num,
          title: s.title,
          href: withBase(`/v${String(v.no).padStart(2, '0')}/c${String(c.no).padStart(2, '0')}#${secAnchor(v.no, c.no, s.num)}`),
        })
      }
    }
  }
  rows.sort((a, b) => Number(a.year) - Number(b.year))
  return { rows, years: new Set(rows.map((r) => r.year)).size, total }
}

/* ---- 跨卷关联图谱（F6）----
   判据复刻装配页：doc.js 块 2 只把 `第〔中文数字〕卷第N章〔A.B〕`／`本章第N章〔A.B〕`／
   `同卷第N章〔A.B〕` 三种形态链接化（CN 表仅到“二十七”，且目标章须实存——装配页原样 quirks），
   buildGraph 对每节只取第一条 data-xref 链接、且跨卷才计边。站点按同一判据在注文本上复算，
   不做“凡是第X卷都算”的放宽统计（实测装配口径约 259 处，放宽口径会虚增约 3.7 倍）。 */
const XREF_CN: Record<string, number> = {
  一: 1, 二: 2, 三: 3, 四: 4, 五: 5, 六: 6, 七: 7, 八: 8, 九: 9, 十: 10,
  十一: 11, 十二: 12, 十三: 13, 十四: 14, 十五: 15, 十六: 16, 十七: 17, 十八: 18, 十九: 19,
  二十: 20, 二十一: 21, 二十二: 22, 二十三: 23, 二十四: 24, 二十五: 25, 二十六: 26, 二十七: 27,
}
const XREF_RE =
  /第([一二三四五六七八九十]+)卷第\s?(\d+)\s?章\s?(\d+\.\d+)?|(?:本章第\s?(\d+)\s?章\s?(\d+\.\d+)?)|第\s?(\d+)\s?章\s?(\d+\.\d+)/g

export interface GraphData {
  nodes: Array<{ no: number; label: string; title: string; href: string; ch: number; secs: number }>
  edges: Array<{ a: number; b: number; w: number }>
  maxW: number
  total: number
}
export function buildGraph(cat: CatalogT): GraphData {
  /** 章号在目标卷是否实存（doc.js resolve 的存在性判据；节是否存在只改锚不改卷号）。 */
  const chExists = (volNo: number, chNo: number): boolean =>
    cat.vols.some((v) => v.no === volNo && v.chs.some((c) => c.no === chNo))
  const weights = new Map<string, number>()
  for (const v of cat.vols) {
    for (const c of v.chs) {
      for (const s of c.secs) {
        const text = s.notes.map((n) => n.t).join(' ')
        // 每节只取第一条可解析的链接（doc.js querySelector(':scope > .src a[data-xref]) 的首链语义）
        for (const m of text.matchAll(XREF_RE)) {
          const [, cv, cch, , , bch, , sch, ssec] = m
          let target: number | null = null
          if (cv && XREF_CN[cv] && cch) target = chExists(XREF_CN[cv], Number(cch)) ? XREF_CN[cv] : null
          else if (bch) target = chExists(v.no, Number(bch)) ? v.no : null
          else if (sch && String(sch) === String(c.no)) target = chExists(v.no, Number(sch)) ? v.no : null
          if (target === null) continue
          if (target !== v.no) {
            const k = `${Math.min(v.no, target)}-${Math.max(v.no, target)}`
            weights.set(k, (weights.get(k) ?? 0) + 1)
          }
          break
        }
      }
    }
  }
  const edges = [...weights].map(([k, w]) => {
    const [a, b] = k.split('-').map(Number)
    return { a, b, w }
  })
  const nodes = cat.vols.map((v) => ({
    no: v.no,
    label: `第${v.roman}卷`,
    title: v.title,
    href: withBase(`/v${String(v.no).padStart(2, '0')}/`),
    ch: v.chs.length,
    secs: v.chs.reduce((a, c) => a + c.secs.length, 0),
  }))
  return {
    nodes,
    edges,
    maxW: edges.reduce((a, e) => Math.max(a, e.w), 1),
    total: edges.reduce((a, e) => a + e.w, 0),
  }
}
