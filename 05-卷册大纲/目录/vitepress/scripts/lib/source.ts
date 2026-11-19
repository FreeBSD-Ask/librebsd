/**
 * 站点共享解析层：outline.txt（显示真值：题名＋注文＋卷注）与 SUMMARY.md（目录结构与侧边栏）。
 * 判据（2026-11-19 全库实测 23 895 节点）：
 *   ①四数全等 75／539／3 918／19 363；②章／节／小节号序逐位相等；
 *   ③题名归一律：SUMMARY 丢弃 ⟦en:X⟧ 标记外壳（保留 X），小节题把 “：”／“/”／“／”／“–”／“—” 统一为 “-”，
 *     并把文件名非法的 “*” 写作全角 “＊”；故归一后 99.75% 全等，残余为 SUMMARY 未再生的真实陈旧项。
 * 结论：结构取 SUMMARY，文本取 outline.txt；两者不一致由 verify-assembly.ts 判失败。
 */
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const HERE = path.dirname(fileURLToPath(import.meta.url))
/**
 * 盘符形式规范化：本机（Windows＋网络映射）下 `import.meta.url` 可能给出 UNC 形式
 * `\\desktop-m5p610n\d\librebsd\…`，作为子进程 cwd 传入后与 VitePress 的相对路径解析叠加会
 * 生成 `…/desktop-m5p610n/d/desktop-m5p610n/d/…` 双重前缀，导致 config 静默加载失败并回落默认值。
 * 一律归一回 `D:\…` 盘符形式；无 UNC 前缀时原样返回（跨平台安全）。
 */
function toDriveForm(p: string): string {
  const m = p.match(/^\\\\[^\\]+\\([A-Za-z])\\(.*)$/)
  if (m) return `${m[1].toUpperCase()}:\\${m[2]}`
  const s = p.match(/^\/\/[^/]+\/([A-Za-z])\/(.*)$/)
  if (s) return `${s[1].toUpperCase()}:\\${s[2]}`
  return p
}
export const SITE_ROOT = toDriveForm(path.resolve(HERE, '..', '..'))
export const CATALOG_DIR = toDriveForm(path.resolve(SITE_ROOT, '..'))
export const OUTLINE_PATH = path.join(CATALOG_DIR, 'data', 'outline.txt')
export const SUMMARY_PATH = path.resolve(CATALOG_DIR, '..', 'SUMMARY.md')
export const ASSEMBLED_PATH = path.join(CATALOG_DIR, 'index.html')
export const UI_STRINGS_PATH = path.join(CATALOG_DIR, 'data', 'ui-strings.json')
export const CATALOG_JSON_PATH = path.join(CATALOG_DIR, 'data', 'catalog.json')
export const DOC_CSS_PATH = path.join(CATALOG_DIR, 'assets', 'doc.css')
export const FAVICON_PATH = path.join(CATALOG_DIR, 'assets', 'favicon.ico')

/** 题名分段：⟦en:X⟧ → en 段，供组件渲染 <span lang="en">，避免 v-html。 */
export type Seg = { t: 'zh' | 'en'; s: string }
export function segs(title: string): Seg[] {
  const out: Seg[] = []
  const re = /⟦en:([^⟧]*)⟧/g
  let last = 0
  let m: RegExpExecArray | null
  while ((m = re.exec(title))) {
    if (m.index > last) out.push({ t: 'zh', s: title.slice(last, m.index) })
    out.push({ t: 'en', s: m[1] })
    last = m.index + m[0].length
  }
  const tail = title.slice(last)
  if (tail) out.push({ t: 'zh', s: tail })
  return out.length ? out : [{ t: 'zh', s: title }]
}

/** 去标注后的纯文本题名（检索与比对用）。 */
export function plain(title: string): string {
  return title.replace(/⟦en:([^⟧]*)⟧/g, '$1')
}

export interface SubNode { num: string; title: string }
export interface SecNode { num: string; title: string; notes: string[]; subs: SubNode[] }
export interface ChNode { no: number; title: string; secs: SecNode[] }
export interface VolNode {
  no: number; roman: string; title: string; intro: string[]; posnotes: string[]; chs: ChNode[]
}
export interface OutlineTree {
  vols: VolNode[]
  counts: { vols: number; chs: number; secs: number; subs: number; notes: number }
  sectionNotes: Map<string, string[]>
}

const CN_DIGITS: Record<string, number> = { 零: 0, 一: 1, 二: 2, 三: 3, 四: 4, 五: 5, 六: 6, 七: 7, 八: 8, 九: 9 }
/** 中文数字（一至百）→ 阿拉伯数字；用于“第N卷”卷号。 */
export function cnToNum(s: string): number {
  if (/^\d+$/.test(s)) return Number(s)
  if (s === '十') return 10
  if (s.includes('十')) {
    const [a, b] = s.split('十')
    return (a ? CN_DIGITS[a] ?? 1 : 1) * 10 + (b ? CN_DIGITS[b] ?? 0 : 0)
  }
  if (s.includes('百')) {
    const [a, rest] = s.split('百')
    return (CN_DIGITS[a] ?? 1) * 100 + (rest ? cnToNum(rest.startsWith('零') ? rest.slice(1) : rest) : 0)
  }
  return CN_DIGITS[s] ?? 0
}

/** 拆 “@@” 后的注文组（〔…〕 逐条）。 */
function noteGroups(tail: string): string[] {
  const out: string[] = []
  const re = /〔[^〕]*〕/g
  let m: RegExpExecArray | null
  while ((m = re.exec(tail))) out.push(m[0])
  const rest = tail.replace(re, '').trim()
  if (rest) out.push(rest)
  return out
}

export function parseOutline(text: string): OutlineTree {
  const vols: VolNode[] = []
  const counts = { vols: 0, chs: 0, secs: 0, subs: 0, notes: 0 }
  const sectionNotes = new Map<string, string[]>()
  let vol: VolNode | null = null
  let ch: ChNode | null = null
  let sec: SecNode | null = null
  let mode: 'none' | 'intro' | 'posnote' = 'none'

  const flushSec = () => {
    if (sec && ch) { ch.secs.push(sec); if (sec.notes.length) sectionNotes.set(sec.num, sec.notes) }
    sec = null
  }
  const flushCh = () => { flushSec(); if (ch && vol) vol.chs.push(ch); ch = null }
  const flushVol = () => { flushCh(); if (vol) vols.push(vol); vol = null; mode = 'none' }

  for (const raw of text.split('\n')) {
    const line = raw.replace(/\s+$/, '')
    if (!line.trim()) continue
    if (line.startsWith('# ')) {
      flushVol()
      const body = line.slice(2).trim()
      const m = body.match(/^第([一二三四五六七八九十百零\d]+)卷\s+(.*)$/)
      counts.vols++
      vol = { no: m ? cnToNum(m[1]) : counts.vols, roman: m ? m[1] : String(counts.vols), title: m ? m[2] : body, intro: [], posnotes: [], chs: [] }
      mode = 'intro'
      continue
    }
    if (line.startsWith('## ')) {
      flushCh()
      mode = 'none'
      const body = line.slice(3).trim()
      const m = body.match(/^第\s*(\d+)\s*章\s+(.*)$/)
      counts.chs++
      ch = { no: m ? Number(m[1]) : counts.chs, title: m ? m[2] : body, secs: [] }
      continue
    }
    let m = line.match(/^- (\d+(?:\.\d+)+)(?:\s+(.*))?$/)
    if (m && !line.startsWith('  - ')) {
      flushSec()
      mode = 'none'
      const rest = (m[2] ?? '').trim()
      const [title, noteTail] = rest.split('@@')
      const notes = noteTail ? noteGroups(noteTail) : []
      counts.secs++
      counts.notes += notes.length
      sec = { num: m[1], title: (title ?? '').trim(), notes, subs: [] }
      continue
    }
    m = line.match(/^  - (\d+(?:\.\d+)+)(?:\s+(.*))?$/)
    if (m) {
      mode = 'none'
      const rest = (m[2] ?? '').trim()
      const title = rest.split('@@')[0].trim()
      counts.subs++
      sec?.subs.push({ num: m[1], title })
      continue
    }
    if (line.startsWith('> ')) { vol?.intro.push(line.slice(2).trim()); mode = 'intro'; continue }
    if (line.startsWith('! ')) { vol?.posnotes.push(line.slice(2).trim()); mode = 'posnote'; continue }
    if (mode === 'intro' && vol) { vol.intro.push(line.trim()); continue }
    if (mode === 'posnote' && vol) { vol.posnotes.push(line.trim()); continue }
  }
  flushVol()
  return { vols, counts, sectionNotes }
}

/** SUMMARY.md → 结构骨架（层级与序号序列），题名仅作比对与侧边栏兜底。 */
export interface SummaryNode { level: 0 | 1 | 2 | 3; text: string; num: string | null }
export function parseSummary(text: string): SummaryNode[] {
  const out: SummaryNode[] = []
  for (const raw of text.split('\n')) {
    const line = raw.replace(/\s+$/, '')
    const m = line.match(/^(\s*)-\s+(.*)$/)
    if (!m || line.startsWith('#')) continue
    const level = ([0, 4, 8, 12] as const).includes(m[1].length as 0 | 4 | 8 | 12)
      ? ([0, 4, 8, 12] as const).indexOf(m[1].length as 0 | 4 | 8 | 12)
      : m[1].length < 4 ? 0 : m[1].length < 8 ? 1 : m[1].length < 12 ? 2 : 3
    let text2 = m[2].trim()
    if (text2.endsWith('.md')) text2 = text2.slice(0, -3)
    const nm = text2.match(/^(\d+(?:\.\d+)*)/)
    const num = level >= 2 ? (nm ? nm[1] : null) : (text2.match(/^第(\d+)(?:卷|章)/)?.[1] ?? null)
    out.push({ level: level as 0 | 1 | 2 | 3, text: text2, num })
  }
  return out
}

/** SUMMARY 题名的文件名归一：还原为可与 outline 比对的形态。 */
export function summaryTitleToDisplay(t: string, level: 0 | 1 | 2 | 3): string {
  let s = t
  if (level === 3) {
    s = s.replace(/[：／–—－]/g, '-')
    s = s.replace(/＊/g, '*')
  }
  return s
}

/** outline 题名 → SUMMARY 侧的比对形态（丢弃 ⟦en:⟧ 外壳、小节题分隔符归一）。 */
export function outlineTitleToSummaryForm(t: string, level: 0 | 1 | 2 | 3): string {
  let s = plain(t)
  if (level === 3) s = s.replace(/[：/／–—－]/g, '-')
  return s
}

/** 剥 HTML 标签＋反转义实体：装配页题名提取用。 */
export function stripHtml(s: string): string {
  return s
    .replace(/<[^>]+>/g, '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/\s+/g, ' ')
    .trim()
}

/** 装配页 doc-metrics 五数提取。 */
export function parseMetrics(html: string): { vols: number; chs: number; secs: number; subs: number; notes: number } | null {
  const i = html.indexOf('class="doc-metrics"')
  if (i < 0) return null
  const seg = html.slice(i, i + 2000)
  const nums = [...seg.matchAll(/<strong>(\d[\d \u00a0\u202f]*)<\/strong>/g)].map((m) => Number(m[1].replace(/[^\d]/g, '')))
  if (nums.length < 5) return null
  return { vols: nums[0], chs: nums[1], secs: nums[2], subs: nums[3], notes: nums[4] }
}

/** 装配页有序 (节号, 题名) 与小节序列提取。 */
export function parseAssembledTitles(html: string): { pairs: Array<[string, string]>; chs: string[] } {
  const pairs: Array<[string, string]> = []
  for (const m of html.matchAll(/<span class="sec-num">(\d+(?:\.\d+)*)<\/span>\s*(.*?)<\/a>/g)) {
    pairs.push([m[1], stripHtml(m[2])])
  }
  const chs: string[] = []
  for (const m of html.matchAll(/<div class="toc-sec-title">(.*?)<\/div>/g)) {
    chs.push(stripHtml(m[1]).replace(/^第\s*\d+\s*章\s*/, ''))
  }
  return { pairs, chs }
}

export function readOutline() { return parseOutline(readFileSync(OUTLINE_PATH, 'utf8')) }
export function readSummary() { return parseSummary(readFileSync(SUMMARY_PATH, 'utf8')) }
export function readUiStrings(): Record<string, unknown> { return JSON.parse(readFileSync(UI_STRINGS_PATH, 'utf8')) }
export function readCatalogJson(): { persons: unknown[]; refs: Record<string, string>; revs: unknown[] } {
  return JSON.parse(readFileSync(CATALOG_JSON_PATH, 'utf8')) as never
}
