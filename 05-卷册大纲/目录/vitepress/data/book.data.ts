/**
 * 构建期数据加载：目录树（outline.txt 内容真值）＋口径计数＋界面文案子集（ui-strings.json）。
 * 消费方：theme/components/CatalogApp.vue（首页目录应用）。只在首页加载。
 */
import { defineLoader } from 'vitepress'
import {
  OUTLINE_PATH, UI_STRINGS_PATH, readOutline, readUiStrings, segs, type Seg,
} from '../scripts/lib/source'

export interface SubD { num: string; title: Seg[] }
export interface SecD { num: string; title: Seg[]; notes: string[]; subs: SubD[] }
export interface ChD { no: number; title: Seg[]; secs: SecD[] }
export interface VolD {
  no: number; roman: string; title: Seg[]; intro: string[]; posnotes: string[]; chs: ChD[]
}
export interface BookData {
  vols: VolD[]
  counts: { vols: number; chs: number; secs: number; subs: number; notes: number }
  ui: Record<string, string>
}

declare const data: BookData
export { data }

export default defineLoader({
  watch: [OUTLINE_PATH, UI_STRINGS_PATH],
  load(): BookData {
    const tree = readOutline()
    const ui = readUiStrings() as Record<string, string>
    return {
      counts: tree.counts,
      ui: {
        bookTitle: ui['shell.book_title'] ?? '',
        pageVersion: ui['shell.page_version'] ?? '',
        metricVol: ui['shell.metric.vol.label'] ?? '总卷数',
        metricCh: ui['shell.metric.ch.label'] ?? '总章数',
        metricSec: ui['shell.metric.sec.label'] ?? '总节数',
        metricSub: ui['shell.metric.sub.label'] ?? '总小节数',
        metricNote: '题名注文',
        searchTitle: ui['shell.btn.search.title'] ?? '检索',
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
            notes: s.notes,
            subs: s.subs.map((x) => ({ num: x.num, title: segs(x.title) })),
          })),
        })),
      })),
    }
  },
})
