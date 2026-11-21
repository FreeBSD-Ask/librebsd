<script setup lang="ts">
/**
 * 目录应用：四级树浏览（卷→章→节→小节）＋溯源注＋检索＋口径指标条＋自校验。
 * 数据来自构建期 loader（data/book.data.ts），不硬编码任何口径数字。
 *
 * 2026-11-20（ykla 令“最大化适配装配页”）：
 *  ①书名区复刻（logo＋书名＋版本号上标）；②指标条改装配页 5 格口径（含 small 注、去千分位、
 *    第五格＝有注小节数），未决项非零时追加第六格（装配页 IF:N_PENDING 同判据）；
 *  ③注三色图例；④溯源注改徽标收起（无脚本时由 html.js 门控自动展开）；
 *  ⑤自校验胶囊按装配页五判据实现（节号连续·章号连续·述评恒末·章题唯一）。
 */
import { computed, ref, shallowRef } from 'vue'
import { withBase } from 'vitepress'
import { data as book } from '../../../data/book.data'
import { data as catalogData } from '../../../data/catalog.data'
import { chAnchor, secAnchor, subAnchor, volAnchor } from '../../../scripts/lib/notes'

/** 自校验④的 ref 号表与⑤人名数（首页已加载 DATA 段，不额外取数）。 */
const refMap: Record<string, string> = Object.fromEntries(catalogData.refs)
const personsN = catalogData.persons.length

type Hit = {
  kind: '卷' | '章' | '节' | '小节'
  num: string
  text: string
  path: string
  href: string
}

const plain = (segs: Array<{ t: string; s: string }>) => segs.map((s) => s.s).join('')
const num = (n: number, w = 2) => String(n).padStart(w, '0')
const chHref = (v: number, ch: number) => withBase(`/v${num(v)}/c${num(ch)}`)

/** 指标条：标签与 small 注全部取 ui-strings，数字取构建期口径（与装配页同源，不做千分位）。 */
const metrics = computed(() => {
  const c = book.counts
  const list = [
    { label: book.ui.metricVol, value: c.vols, note: book.ui.metricVolNote },
    {
      label: book.ui.metricCh,
      value: c.chs,
      note: book.ui.metricChNote
        .replace('{{N_CH_MAIN}}', String(c.chMain))
        .replace('{{N_CH_BIBLIO}}', String(c.chBiblio)),
    },
    { label: book.ui.metricSec, value: c.secs, note: book.ui.metricSecNote },
    { label: book.ui.metricSub, value: c.subs, note: book.ui.metricSubNote },
    { label: book.ui.metricSrc, value: c.src, note: book.ui.metricSrcNote },
  ]
  if (c.pending > 0) {
    list.push({ label: book.ui.metricPending, value: c.pending, note: book.ui.metricPendingNote })
  }
  return list
})

const legend = computed(() => [
  { cls: 'a', label: book.ui.legendX, n: book.legend.xref },
  { cls: 'b', label: book.ui.legendM, n: book.legend.mig },
  { cls: 'c', label: book.ui.legendS, n: book.legend.src },
])

/* ---- 自校验（装配页 E7 六项判据；按 doc.js 块 11 的原判据实现） ----
   ①节号连续／章号连续／述评恒末（合并为一项）②注分类齐备 ③章题唯一（**卷内**）
   ④ref 可解析 ⑤人名 ⑥年份。 */
const selfcheck = computed(() => {
  const bad: string[] = []
  let seq = 0
  for (const v of book.vols) {
    v.chs.forEach((c, i) => {
      if (c.no !== i + 1) { seq++; bad.push(`第${v.roman}卷 第 ${c.no} 章 号序断裂`) }
      c.secs.forEach((s, k) => {
        if (s.num !== `${c.no}.${k + 1}`) { seq++; bad.push(`第${v.roman}卷第 ${c.no} 节 ${s.num} 号序断裂`) }
      })
      let bibIdx = -1
      c.secs.forEach((s, k) => {
        if (/本章书目述评/.test(plain(s.title))) bibIdx = k
      })
      if (bibIdx >= 0 && bibIdx !== c.secs.length - 1) { seq++; bad.push(`第${v.roman}卷第 ${c.no} 章 述评节未列末位`) }
    })
  }
  // ③ 章题唯一：装配页按**卷内**统计同题
  let dupTitles = 0
  for (const v of book.vols) {
    const seen = new Set<string>()
    for (const c of v.chs) {
      const t = plain(c.title)
      if (seen.has(t)) dupTitles++
      seen.add(t)
    }
  }
  if (dupTitles) bad.push(`卷内章题重复 ${dupTitles} 处`)
  // ④ ref 可解析：注文里 `ref N` 的编号须在参考文献库中
  let refMiss = 0
  for (const v of book.vols) for (const c of v.chs) for (const s of c.secs) {
    for (const n of s.notes) {
      for (const m of n.t.matchAll(/\bref\s?(\d{1,5})/g)) if (!refMap[m[1]]) refMiss++
    }
  }
  if (refMiss) bad.push(`ref 未著录 ${refMiss} 处`)
  // ⑥ 年份：节名＋章题首个 1600—2049 年份的去重数（时间线面板同判据）
  const YEAR_RE = /(1[6-9]\d\d|20[0-4]\d)/
  const yearSet = new Set<string>()
  let secsN = 0
  for (const v of book.vols) for (const c of v.chs) for (const s of c.secs) {
    secsN++
    const m = `${plain(s.title)} ${plain(c.title)}`.match(YEAR_RE)
    if (m) yearSet.add(m[0])
  }
  return { seq, dupTitles, refMiss, years: yearSet.size, secsN, persons: personsN, bad, detail: bad.slice(0, 12) }
})

const scOpen = ref(false)
/** 六项判据的坏项数——公式与 doc.js 块 11 同：badCount＝(序列异常?1:0)＋(卷内章题重复?1:0)；
    ref 未著录只进明细行、不计入坏项（装配页 refMiss>0 时仍显 6/6）。 */
const badCount = computed(
  () => (selfcheck.value.seq > 0 ? 1 : 0) + (selfcheck.value.dupTitles > 0 ? 1 : 0),
)
const scSummary = computed(() =>
  `${6 - badCount.value}/6${badCount.value ? ' · ' + badCount.value + ' 项异常' : ' 通过'}`,
)

/* ---- 检索索引（首次输入时构建） ---- */
const q = ref('')
const index = shallowRef<Hit[] | null>(null)
function buildIndex(): Hit[] {
  if (index.value) return index.value
  const out: Hit[] = []
  for (const v of book.vols) {
    const vPath = `第${v.roman}卷`
    out.push({
      kind: '卷',
      num: `第${v.roman}卷`,
      text: plain(v.title),
      path: vPath,
      href: `${withBase(`/v${num(v.no)}/`)}#${volAnchor(v.no)}`,
    })
    for (const ch of v.chs) {
      const href = chHref(v.no, ch.no)
      const cPath = `${vPath}／第 ${ch.no} 章`
      out.push({ kind: '章', num: `第 ${ch.no} 章`, text: plain(ch.title), path: cPath, href: `${href}#${chAnchor(v.no, ch.no)}` })
      for (const s of ch.secs) {
        out.push({
          kind: '节',
          num: s.num,
          text: plain(s.title),
          path: cPath,
          href: `${href}#${secAnchor(v.no, ch.no, s.num)}`,
        })
        s.subs.forEach((u, ui) => {
          out.push({
            kind: '小节',
            num: u.num,
            text: plain(u.title),
            path: cPath,
            href: `${href}#${subAnchor(v.no, ch.no, s.num, ui + 1)}`,
          })
        })
      }
    }
  }
  index.value = out
  return out
}

const MAX_HITS = 200
const hits = computed<{ list: Hit[]; total: number }>(() => {
  const kw = q.value.trim().toLowerCase()
  if (!kw) return { list: [], total: 0 }
  const all = buildIndex().filter(
    (h) => h.text.toLowerCase().includes(kw) || h.num.toLowerCase().includes(kw),
  )
  return { list: all.slice(0, MAX_HITS), total: all.length }
})
const searching = computed(() => q.value.trim().length > 0)

const openVols = ref<Set<number>>(new Set())
const openChs = ref<Set<string>>(new Set())
const toggleVol = (n: number) => {
  const s = new Set(openVols.value)
  if (s.has(n)) s.delete(n)
  else s.add(n)
  openVols.value = s
}
const toggleCh = (key: string) => {
  const s = new Set(openChs.value)
  if (s.has(key)) s.delete(key)
  else s.add(key)
  openChs.value = s
}
const isChOpen = (key: string) => openChs.value.has(key) || searching.value
</script>

<template>
  <div class="cat-app">
    <!-- 书名区（B1）：logo＋书名＋版本号上标 -->
    <div class="doc-title">
      <h1>
        <img class="doc-logo" :src="withBase('/logo.svg')" width="40" height="40" alt="" decoding="async" />{{ book.ui.bookTitle }}<span
          v-if="book.version"
          class="page-version"
          title="页面版本（UTC+8，YYYY.MM.DD-HH:MM）"
        >{{ book.version }}</span>
      </h1>
    </div>

    <!-- 指标条（B2）：装配页 5 格口径 -->
    <div class="doc-metrics" role="list" aria-label="目录口径">
      <div v-for="m in metrics" :key="m.label" class="doc-metric" role="listitem">
        <span>{{ m.label }}</span><strong>{{ m.value }}</strong><small v-if="m.note">{{ m.note }}</small>
      </div>
    </div>

    <!-- 自校验胶囊（E7）：六项判据，与装配页 6/6 口径同 -->
    <div :class="['selfcheck', badCount ? 'bad' : '']">
      <button type="button" class="sc-sum" :aria-expanded="scOpen" @click="scOpen = !scOpen">
        目录自校验 {{ scSummary }}<template v-if="!badCount"> · 节号连续 · 章号连续 · 述评恒末</template>
        · 注 {{ book.legend.total }} · 人名 {{ selfcheck.persons }} · 年份 {{ selfcheck.years }} · 节 {{ selfcheck.secsN }}
      </button>
      <ul v-if="scOpen && selfcheck.detail.length">
        <li v-for="(d, i) in selfcheck.detail" :key="i">{{ d }}</li>
      </ul>
    </div>

    <!-- 注三色图例（E3） -->
    <div class="note-legend" role="list">
      <span v-for="l in legend" :key="l.cls" role="listitem"><i :class="l.cls"></i>{{ l.label }}{{ l.n }}</span>
      <span>{{ book.ui.legendTotal }}{{ book.legend.total }}{{ book.ui.legendUnit }}</span>
    </div>
    <p class="cat-hint">
      溯源注按注文判类（迁移 {{ book.legend.mig }} ／ 分工 {{ book.legend.xref }} ／ 史料 {{ book.legend.src }}），
      分布于 {{ book.counts.src }} 个小节。
    </p>

    <div class="cat-tools">
      <input
        v-model="q"
        type="search"
        :placeholder="`检索 ${book.counts.subs} 个小节题名或号（卷／章／节／小节）`"
        :aria-label="book.ui.searchTitle"
      />
      <span class="cat-hint">
        <template v-if="searching">命中 {{ hits.total }} 项（显示前 {{ Math.min(hits.total, MAX_HITS) }} 项）</template>
        <template v-else>点卷号展开；章页可深链到节与小节（跨页检索用 Ctrl/⌘+K）</template>
      </span>
    </div>

    <!-- 检索结果 -->
    <section v-if="searching" aria-label="检索结果">
      <a v-for="(h, i) in hits.list" :key="i" class="cat-hit" :href="h.href">
        <span class="cat-hit-no">{{ h.num }}</span>
        <span>{{ h.text }}</span>
        <span class="cat-hit-path">{{ h.kind }} · {{ h.path }}</span>
      </a>
      <p v-if="!hits.total" class="cat-hint">无命中。</p>
    </section>

    <!-- 四级树 -->
    <section v-else aria-label="目录树">
      <details
        v-for="v in book.vols"
        :key="v.no"
        class="cat-vol"
        :open="openVols.has(v.no)"
        @toggle="(e) => { const t = e.target as HTMLDetailsElement; if (t.open !== openVols.has(v.no)) toggleVol(v.no) }"
      >
        <summary>
          <span class="cat-vol-no">第{{ v.roman }}卷</span>
          <span class="cat-vol-title">
            <template v-for="(s, i) in v.title" :key="i">
              <span v-if="s.t === 'en'" lang="en">{{ s.s }}</span>
              <template v-else>{{ s.s }}</template>
            </template>
          </span>
          <span class="cat-vol-meta">{{ v.chs.length }} 章 · {{ v.chs.reduce((a, c) => a + c.secs.length, 0) }} 节</span>
        </summary>
        <div v-if="openVols.has(v.no)" class="cat-vol-body">
          <p v-if="v.intro.length" class="cat-intro">{{ v.intro.join(' ') }}</p>
          <p v-if="v.posnotes.length" class="cat-posnote">{{ v.posnotes.join(' ') }}</p>

          <details
            v-for="ch in v.chs"
            :key="ch.no"
            class="cat-ch"
            :open="isChOpen(`${v.no}:${ch.no}`)"
            @toggle="(e) => { const t = e.target as HTMLDetailsElement; if (t.open !== isChOpen(`${v.no}:${ch.no}`)) toggleCh(`${v.no}:${ch.no}`) }"
          >
            <summary>
              <!-- 章题＝就地折叠手势（与装配页一致），不作链接；深链走节/小节行与侧栏 -->
              <span class="cat-ch-title">
                第 {{ ch.no }} 章 <template v-for="(s, i) in ch.title" :key="i">
                  <span v-if="s.t === 'en'" lang="en">{{ s.s }}</span>
                  <template v-else>{{ s.s }}</template>
                </template>
              </span>
              <span class="cat-ch-meta">{{ ch.secs.length }} 节／{{ ch.secs.reduce((a, s) => a + s.subs.length, 0) }} 小节</span>
            </summary>
            <div v-if="isChOpen(`${v.no}:${ch.no}`)" class="cat-vol-body">
              <div v-for="s in ch.secs" :key="s.num" class="cat-sec">
                <div class="cat-sec-head">
                  <span class="cat-sec-title">
                    <span class="cat-sec-num">{{ s.num }}</span>
                    <span>
                      <template v-for="(x, i) in s.title" :key="i">
                        <span v-if="x.t === 'en'" lang="en">{{ x.s }}</span>
                        <template v-else>{{ x.s }}</template>
                      </template>
                    </span>
                  </span>
                </div>
                <p v-if="s.notes.length" class="cat-note">
                  <button
                    type="button"
                    class="note-badge"
                    aria-expanded="false"
                    :title="book.ui.notesTitle"
                  >注</button><span
                    :class="['src', 'note-x', `k-${s.notes[0].k}`]"
                  >{{ s.notes.map((n) => n.t).join(' ') }}</span>
                </p>
                <ul v-if="s.subs.length" class="cat-subs">
                  <li v-for="(u, ui) in s.subs" :key="u.num">
                    <span class="cat-sub-row">
                      <span class="cat-sub-num">{{ u.num }}</span>
                      <span>
                        <template v-for="(x, i) in u.title" :key="i">
                          <span v-if="x.t === 'en'" lang="en">{{ x.s }}</span>
                          <template v-else>{{ x.s }}</template>
                        </template>
                      </span>
                    </span>
                    <span v-if="u.notes.length" :class="['src', 'note-x', `k-${u.notes[0].k}`]">{{ u.notes.map((n) => n.t).join(' ') }}</span>
                  </li>
                </ul>
              </div>
            </div>
          </details>
        </div>
      </details>
    </section>
  </div>
</template>

<style scoped>
.sc-sum {
  font: inherit;
  border: 0;
  padding: 0;
  background: transparent;
  color: inherit;
  cursor: pointer;
}
.cat-posnote {
  margin: 4px 0 10px;
  color: var(--cat-faint);
  font-size: 13px;
  line-height: 1.65;
}
.cat-sec-title {
  display: flex;
  gap: 8px;
  align-items: baseline;
  color: inherit;
  text-decoration: none;
  min-width: 0;
  overflow-wrap: anywhere;
}
.cat-sec-title:hover {
  color: var(--cat-accent);
}
</style>
