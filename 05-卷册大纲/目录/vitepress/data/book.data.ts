/**
 * 构建期数据加载：目录树（outline.txt 内容真值）＋口径计数＋界面文案子集（ui-strings.json）。
 * 消费方：theme/components/CatalogApp.vue（首页目录应用）。只在首页加载。
 *
 * 2026-11-20：口径与装配器 assemble_index.py 的 compute_metrics 对齐——
 *   ⑤ 溯源标注＝有注小节数（sectionsWithNotes＝装配页 1797），不是注文组数（2 257）；
 *   ⑥ 未决项＝注文以〔待补／〔待重建起首的小节（与装配器同一收紧判据），零时不渲染；
 *   另附章分项（正章／卷末书目述评章）与注三色图例计数（判据同 doc.js 块 3）。
 */
import { defineLoader } from 'vitepress'
import {
  OUTLINE_PATH, UI_STRINGS_PATH, readOutline, readUiStrings, segs, type Seg,
} from '../scripts/lib/source'
import { classifyNote, type NoteKind } from '../scripts/lib/notes'

export interface NoteD { k: NoteKind; t: string }
export interface SubD { num: string; title: Seg[]; notes: NoteD[] }
export interface SecD { num: string; title: Seg[]; notes: NoteD[]; subs: SubD[] }
export interface ChD { no: number; title: Seg[]; secs: SecD[] }
export interface VolD {
  no: number; roman: string; title: Seg[]; intro: string[]; posnotes: string[]; chs: ChD[]
}
export interface BookData {
  vols: VolD[]
  counts: {
    vols: number
    chs: number
    secs: number
    subs: number
    /** 有注小节数（装配页第五数“溯源标注”同口径） */
    src: number
    /** 注文组总数（图例合计；不与第五数混用） */
    noteGroups: number
    /** 未决项：注文以〔待补／〔待重建起首的小节 */
    pending: number
    chMain: number
    chBiblio: number
  }
  legend: { xref: number; mig: number; src: number; total: number }
  version: string
  ui: Record<string, string>
}

declare const data: BookData
export { data }

export default defineLoader({
  watch: [OUTLINE_PATH, UI_STRINGS_PATH],
  load(): BookData {
    const tree = readOutline()
    const ui = readUiStrings() as Record<string, string>
    let chBiblio = 0
    let pending = 0
    const legend = { xref: 0, mig: 0, src: 0, total: 0 }
    for (const v of tree.vols) {
      for (const c of v.chs) {
        if (c.title.includes('卷末书目述评')) chBiblio++
        for (const s of c.secs) {
          if (!s.notes.length) continue
          const kind = classifyNote(s.notes.join(' '))
          legend[kind]++
          legend.total++
          if (/^〔(?:待补|待重建)/.test(s.notes[0])) pending++
        }
      }
    }
    return {
      counts: {
        vols: tree.counts.vols,
        chs: tree.counts.chs,
        secs: tree.counts.secs,
        subs: tree.counts.subs,
        src: tree.counts.sectionsWithNotes,
        noteGroups: tree.counts.notes,
        pending,
        chMain: tree.counts.chs - chBiblio,
        chBiblio,
      },
      legend,
      version: ui['shell.page_version'] ?? '',
      ui: {
        bookTitle: ui['shell.book_title'] ?? '',
        pageVersion: ui['shell.page_version'] ?? '',
        metricVol: ui['shell.metric.vol.label'] ?? '总卷数',
        metricVolNote: ui['shell.metric.vol.note'] ?? '',
        metricCh: ui['shell.metric.ch.label'] ?? '总章数',
        metricChNote: ui['shell.metric.ch.note'] ?? '',
        metricSec: ui['shell.metric.sec.label'] ?? '总节数',
        metricSecNote: ui['shell.metric.sec.note'] ?? '',
        metricSub: ui['shell.metric.sub.label'] ?? '总小节数',
        metricSubNote: ui['shell.metric.sub.note'] ?? '',
        // 第五格与装配页“溯源标注”同口径＝有注小节数（判据见文件头）
        metricSrc: ui['shell.metric.src.label'] ?? '溯源标注',
        metricSrcNote: ui['shell.metric.src.note'] ?? '',
        metricPending: ui['shell.metric.pending.label'] ?? '未决项',
        metricPendingNote: ui['shell.metric.pending.note'] ?? '',
        legendX: ui['ui.legend.x'] ?? '分工注（跨卷指向）',
        legendM: ui['ui.legend.m'] ?? '迁移注（历史沿革）',
        legendS: ui['ui.legend.s'] ?? '史料注（ref 编号）',
        legendTotal: ui['ui.legend.total'] ?? '合计 ',
        legendUnit: ui['ui.legend.unit'] ?? ' 处',
        selfcheckOk: ui['ui.selfcheck.ok'] ?? '目录自校验通过：节号连续 · 章号连续 · 述评恒末',
        selfcheckBad: ui['ui.selfcheck.bad_fmt'] ?? '目录自校验：发现 {n} 处异常',
        selfcheckPlaceholder: ui['shell.selfcheck.placeholder'] ?? '目录自校验 …',
        searchTitle: ui['shell.btn.search.title'] ?? '检索',
        notesTitle: ui['shell.btn.notes.title'] ?? '显示/隐藏全部溯源注',
      },
      vols: tree.vols.map((v) => ({
        no: v.no,
        roman: v.roman,
        title: segs(v.title),
        intro: v.intro,
        posnotes: v.posnotes,
        chs: v.chs.map((c) => ({
          no: c.no,
          title: segs(c.title),
          secs: c.secs.map((s) => ({
            num: s.num,
            title: segs(s.title),
            notes: s.notes.map((t) => ({ k: classifyNote(s.notes.join(' ')), t })),
            subs: s.subs.map((x) => ({
              num: x.num,
              title: segs(x.title),
              notes: x.notes.map((t) => ({ k: classifyNote(x.notes.join(' ')), t })),
            })),
          })),
        })),
      })),
    }
  },
})
