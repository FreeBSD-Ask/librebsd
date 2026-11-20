/**
 * 全站检索索引重建（分卷构建的合并步专用）。
 *
 * 背景：VitePress localSearch 的索引是构建期虚拟模块，只覆盖本次构建的 `siteConfig.pages`；
 * 站点按 76 分片构建，各片索引互不相通，合并后客户端只会取到最后一片的索引。故在合并步用
 * 与客户端 `loadLocalSearchIndex()` **同一 MiniSearch 口径**（fields／storeFields／tokenize）
 * 从内容源重造一份全站索引，覆盖分片产出的数据 chunk（chunk 文件名固定，见 config.mts 插件）。
 *
 * 文档切分与 VitePress 的 splitPageIntoSections 语义对齐：一个标题一条记录，
 * `titles`＝祖先标题链、`title`＝本条标题、`text`＝该标题下的正文（注文／小节题名）。
 */
import MiniSearch from 'minisearch'
import type { OutlineTree } from './source'

const SPACE_OR_PUNCTUATION_RE = /[\n\r\p{Z}\p{P}]+/u
const UNSPACED_RUN_RE = /[\p{scx=Han}\p{scx=Hiragana}\p{scx=Katakana}]+|[^\p{scx=Han}\p{scx=Hiragana}\p{scx=Katakana}]+/gu
const UNSPACED_START_RE = /^[\p{scx=Han}\p{scx=Hiragana}\p{scx=Katakana}]/u
let segmenter: Intl.Segmenter | null = null

/** 与 vitepress/dist/node 内 tokenizeSearchText 逐行同构（中文按词切分，其余按空格／标点）。 */
function tokenizeSearchText(text: string): string[] {
  const terms = text.split(SPACE_OR_PUNCTUATION_RE)
  if (typeof Intl.Segmenter !== 'function') return terms
  segmenter ??= new Intl.Segmenter(undefined, { granularity: 'word' })
  return terms.flatMap(
    (term) =>
      term.match(UNSPACED_RUN_RE)?.flatMap((run) =>
        UNSPACED_START_RE.test(run) ? Array.from(segmenter!.segment(run), (p) => p.segment) : run,
      ) ?? term,
  )
}

export interface SearchDoc {
  id: string
  title: string
  titles: string[]
  text: string
}

const pad = (n: number) => String(n).padStart(2, '0')
const plain = (t: string) => t.replace(/⟦en:([^⟧]*)⟧/g, '$1')
const volTitle = (v: OutlineTree['vols'][number]) => `第${v.roman}卷 ${plain(v.title)}`
const chTitle = (c: { no: number; title: string }) => `第 ${c.no} 章 ${plain(c.title)}`

/** 从内容源构造检索文档集（卷／章／节／小节四级，共 23 895 条）。 */
export function buildSearchDocs(tree: OutlineTree): SearchDoc[] {
  const docs: SearchDoc[] = []
  for (const v of tree.vols) {
    const vPath = `/v${pad(v.no)}/`
    const vt = volTitle(v)
    docs.push({
      id: `${vPath}#vol-${v.no}`,
      title: vt,
      titles: [],
      text: [...v.intro, ...v.posnotes, ...v.chs.map(chTitle)].join(' '),
    })
    for (const c of v.chs) {
      const chPath = `${vPath}c${pad(c.no)}`
      const ct = chTitle(c)
      docs.push({
        id: `${chPath}#vol-${v.no}-ch-${c.no}`,
        title: ct,
        titles: [vt],
        text: c.secs.map((s) => `${s.num} ${plain(s.title)}`).join(' '),
      })
      for (const s of c.secs) {
        const secId = `${chPath}#vol-${v.no}-ch-${c.no}-sec-${s.num.replace(/\./g, '-')}`
        docs.push({
          id: secId,
          title: plain(s.title),
          titles: [vt, ct],
          text: [...s.notes, ...s.subs.map((x) => plain(x.title))].join(' '),
        })
        s.subs.forEach((x, i) => {
          docs.push({
            id: `${secId}-sub-${i + 1}`,
            title: plain(x.title),
            titles: [vt, ct, plain(s.title)],
            text: x.notes.join(' '),
          })
        })
      }
    }
  }
  return docs
}

export interface SearchIndexResult {
  /** chunk 文件内容：`export default "<json>"`（与 VitePress 产出的数据 chunk 同式） */
  module: string
  /** MiniSearch 序列化 JSON 文本（供断言解析） */
  json: string
  docs: number
  bytes: number
}

/** 生成整站索引 chunk 内容。 */
export function buildSearchIndex(tree: OutlineTree): SearchIndexResult {
  const index = new MiniSearch({
    fields: ['title', 'titles', 'text'],
    storeFields: ['title', 'titles'],
    tokenize: tokenizeSearchText,
  })
  const docs = buildSearchDocs(tree)
  index.addAll(docs)
  const json = JSON.stringify(index)
  const module = `export default ${JSON.stringify(json)};\n`
  return { module, json, docs: docs.length, bytes: Buffer.byteLength(module) }
}
