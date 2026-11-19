/**
 * 三源互证：SUMMARY.md（结构）↔ outline.txt（内容）↔ 装配产物 index.html（装配事实）。
 * 装配产物只作对照件，不参与站点渲染；任一判据失败 exit 1 并打印前 10 项差异。
 * 判据：
 *   V1 四数全等（卷／章／节／小节）：SUMMARY vs outline vs 装配页 doc-metrics
 *   V2 号序逐位相等：章号、节号、小节号
 *   V3 装配页有序 (号, 题名) 序列 == outline 序列（剥标签＋实体反解后逐位比对）
 *   V4 装配页章题序列 == outline 章题序列
 */
import { readFileSync } from 'node:fs'
import {
  ASSEMBLED_PATH, readOutline, readSummary, parseMetrics, parseAssembledTitles, plain,
} from './lib/source'

function head<T>(arr: T[], n = 10): string {
  return arr.slice(0, n).map((x) => '    ' + JSON.stringify(x)).join('\n')
}

const outline = readOutline()
const summary = readSummary()
const html = readFileSync(ASSEMBLED_PATH, 'utf8')
const metrics = parseMetrics(html)
const assembled = parseAssembledTitles(html)

const fails: string[] = []
const oc = outline.counts

// ---- V1：三源四数
const sCounts = {
  vols: summary.filter((n) => n.level === 0).length,
  chs: summary.filter((n) => n.level === 1).length,
  secs: summary.filter((n) => n.level === 2).length,
  subs: summary.filter((n) => n.level === 3).length,
}
if (sCounts.vols !== oc.vols || sCounts.chs !== oc.chs || sCounts.secs !== oc.secs || sCounts.subs !== oc.subs) {
  fails.push(`V1 SUMMARY≠outline：SUMMARY ${JSON.stringify(sCounts)} vs outline ${JSON.stringify(oc)}`)
}
if (!metrics) {
  fails.push('V1 装配页 doc-metrics 未解析到')
} else {
  if (metrics.vols !== oc.vols || metrics.chs !== oc.chs || metrics.secs !== oc.secs || metrics.subs !== oc.subs) {
    fails.push(`V1 装配页≠outline：装配 ${JSON.stringify(metrics)} vs outline ${JSON.stringify(oc)}`)
  }
  // 第五数口径：装配页「溯源标注」＝有注小节数（非注文组数），故比 sectionsWithNotes
  if (metrics.notes !== oc.sectionsWithNotes) {
    fails.push(
      `V1 第五数（溯源标注＝有注小节）不一致：装配 ${metrics.notes} vs outline ${oc.sectionsWithNotes}`,
    )
  }
}

// ---- V2：号序
const oSec = outline.vols.flatMap((v) => v.chs.flatMap((c) => c.secs.map((s) => s.num)))
const oSub = outline.vols.flatMap((v) => v.chs.flatMap((c) => c.secs.flatMap((s) => s.subs.map((x) => x.num))))
const oCh = outline.vols.flatMap((v) => v.chs.map((c) => String(c.no)))
const sCh = summary.filter((n) => n.level === 1).map((n) => String(n.num))
const sSec = summary.filter((n) => n.level === 2).map((n) => String(n.num))
const sSub = summary.filter((n) => n.level === 3).map((n) => String(n.num))

function seqDiff(name: string, a: string[], b: string[]) {
  const diffs: Array<{ i: number; a?: string; b?: string }> = []
  const n = Math.max(a.length, b.length)
  for (let i = 0; i < n && diffs.length < 200; i++) if (a[i] !== b[i]) diffs.push({ i, a: a[i], b: b[i] })
  if (diffs.length) fails.push(`V2 ${name} 号序不一致（${diffs.length}${diffs.length >= 200 ? '+' : ''} 项）\n${head(diffs)}`)
}
seqDiff('章号 outline vs SUMMARY', oCh, sCh)
seqDiff('节号 outline vs SUMMARY', oSec, sSec)
seqDiff('小节号 outline vs SUMMARY', oSub, sSub)

// ---- V3：装配页题名序列
const oPairs: Array<[string, string]> = []
for (const v of outline.vols) for (const c of v.chs) for (const s of c.secs) {
  oPairs.push([s.num, plain(s.title)])
  for (const x of s.subs) oPairs.push([x.num, plain(x.title)])
}
if (assembled.pairs.length !== oPairs.length) {
  fails.push(`V3 装配页题名对数不等：装配 ${assembled.pairs.length} vs outline ${oPairs.length}`)
}
const pDiff: Array<{ i: number; outline?: [string, string]; assembled?: [string, string] }> = []
for (let i = 0; i < Math.max(assembled.pairs.length, oPairs.length) && pDiff.length < 200; i++) {
  const a = oPairs[i]
  const b = assembled.pairs[i]
  if (!a || !b) { pDiff.push({ i, outline: a, assembled: b }); continue }
  if (a[0] !== b[0] || a[1].replace(/\s+/g, ' ') !== b[1].replace(/\s+/g, ' ')) pDiff.push({ i, outline: a, assembled: b })
}
if (pDiff.length) fails.push(`V3 题名序列不一致（${pDiff.length}${pDiff.length >= 200 ? '+' : ''} 项）\n${head(pDiff)}`)

// ---- V4：章题序列
const oChTitle = outline.vols.flatMap((v) => v.chs.map((c) => plain(c.title).replace(/\s+/g, ' ').trim()))
const aChTitle = assembled.chs.map((t) => t.replace(/\s+/g, ' ').trim())
if (aChTitle.length !== oChTitle.length) fails.push(`V4 章题数不等：装配 ${aChTitle.length} vs outline ${oChTitle.length}`)
const cDiff: Array<{ i: number; outline?: string; assembled?: string }> = []
for (let i = 0; i < Math.max(aChTitle.length, oChTitle.length) && cDiff.length < 100; i++) {
  if (oChTitle[i] !== aChTitle[i]) cDiff.push({ i, outline: oChTitle[i], assembled: aChTitle[i] })
}
if (cDiff.length) fails.push(`V4 章题不一致（${cDiff.length} 项）\n${head(cDiff)}`)

// ---- V5：SUMMARY 题名漂移（只报数，不作判失败依据；结构判据已由 V2 号序承担）
const norm = (t: string) => t.replace(/⟦en:([^⟧]*)⟧/g, '$1')
const sTitles: string[] = []
let lastVol = 0
for (const n of summary) {
  if (n.level === 0) lastVol = Number(n.num ?? lastVol + 1)
  else if (n.level === 1) sTitles.push(norm(n.text.replace(/^第\d+章[-－]/, '')))
}
const oTitles = outline.vols.flatMap((v) => v.chs.map((c) => norm(c.title).trim()))
const drift: Array<{ i: number; summary: string; outline: string }> = []
for (let i = 0; i < Math.min(sTitles.length, oTitles.length); i++) {
  const a = sTitles[i].replace(/[：:／\/–—－]/g, '-').replace(/\s+/g, '')
  const b = oTitles[i].replace(/[：:／\/–—－]/g, '-').replace(/\s+/g, '')
  if (a !== b) drift.push({ i, summary: sTitles[i], outline: oTitles[i] })
}

// ---- 报告
const line = `卷 ${oc.vols}／章 ${oc.chs}／节 ${oc.secs}／小节 ${oc.subs}／注文 ${oc.notes}`
if (fails.length) {
  console.error(`[verify] FAIL（三源互证未通过）：${line}`)
  for (const f of fails) console.error('  ✗ ' + f)
  process.exit(1)
}
console.log(`[verify] PASS 三源互证全绿：${line}`)
console.log(`          SUMMARY 四数 ${JSON.stringify(sCounts)}；装配页题名对 ${assembled.pairs.length}；章题 ${aChTitle.length}`)
console.log(
  `          注文：${oc.notes} 组／有注小节 ${oc.sectionsWithNotes}（装配页第五数＝后者）`,
)
if (drift.length) {
  console.log(
    `          INFO SUMMARY 章题与 outline 漂移 ${drift.length} 项（不作失败判据；示例 ${JSON.stringify(drift[0])}）`,
  )
}
