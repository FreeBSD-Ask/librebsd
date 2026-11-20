<script setup lang="ts">
/**
 * 目录应用：四级树浏览（卷→章→节→小节）＋注文＋检索＋口径指标条。
 * 数据来自构建期 loader（data/book.data.ts），不硬编码任何口径数字。
 */
import { computed, ref, shallowRef } from 'vue'
import { withBase } from 'vitepress'
import { data as book } from '../../../data/book.data'

type Hit = {
  kind: '卷' | '章' | '节' | '小节'
  num: string
  text: string
  path: string
  href: string
}

const c = book.counts
const metrics = computed(() => [
  { label: book.ui.metricVol || '总卷数', value: c.vols },
  { label: book.ui.metricCh || '总章数', value: c.chs },
  { label: book.ui.metricSec || '总节数', value: c.secs },
  { label: book.ui.metricSub || '总小节数', value: c.subs },
  { label: book.ui.metricNote || '溯源注', value: c.notes },
])

const num = (n: number, w = 2) => String(n).padStart(w, '0')
const chHref = (v: number, ch: number) => withBase(`/v${num(v)}/c${num(ch)}`)
const plainSegs = (segs: Array<{ t: string; s: string }>) => segs.map((s) => s.s).join('')

const q = ref('')
const openVols = ref<Set<number>>(new Set())
const openChs = ref<Set<string>>(new Set())
const toggleVol = (n: number) => {
  const s = new Set(openVols.value)
  s.has(n) ? s.delete(n) : s.add(n)
  openVols.value = s
}
const toggleCh = (key: string) => {
  const s = new Set(openChs.value)
  s.has(key) ? s.delete(key) : s.add(key)
  openChs.value = s
}
const isChOpen = (key: string) => openChs.value.has(key) || q.value.trim().length > 0

// ---- 检索索引（首次输入时构建）
const index = shallowRef<Hit[] | null>(null)
function buildIndex(): Hit[] {
  if (index.value) return index.value
  const out: Hit[] = []
  for (const v of book.vols) {
    const vPath = `第${v.roman}卷`
    out.push({ kind: '卷', num: `第${v.roman}卷`, text: plainSegs(v.title), path: vPath, href: withBase(`/v${num(v.no)}/`) })
    for (const ch of v.chs) {
      const href = chHref(v.no, ch.no)
      const cPath = `${vPath}／第 ${ch.no} 章`
      out.push({ kind: '章', num: `第 ${ch.no} 章`, text: plainSegs(ch.title), path: cPath, href })
      for (const s of ch.secs) {
        out.push({
          kind: '节', num: s.num, text: plainSegs(s.title), path: cPath,
          href: `${href}#_${s.num.replace(/\./g, '-')}`,
        })
        for (const u of s.subs) {
          out.push({
            kind: '小节', num: u.num, text: plainSegs(u.title), path: cPath,
            href: `${href}#_${u.num.replace(/\./g, '-')}`,
          })
        }
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
</script>

<template>
  <div class="cat-app">
    <div class="cat-metrics" role="list" aria-label="目录口径">
      <div v-for="m in metrics" :key="m.label" class="cat-metric" role="listitem">
        <span>{{ m.label }}</span>
        <strong>{{ m.value.toLocaleString('zh-CN') }}</strong>
      </div>
    </div>

    <div class="cat-tools">
      <input
        v-model="q"
        type="search"
        :placeholder="`检索 ${book.counts.subs.toLocaleString('zh-CN')} 个小节题名或号（卷／章／节／小节）`"
        :aria-label="book.ui.searchTitle || '检索'"
      />
      <span class="cat-hint">
        <template v-if="searching">命中 {{ hits.total.toLocaleString('zh-CN') }} 项（显示前 {{ Math.min(hits.total, MAX_HITS) }} 项）</template>
        <template v-else>点卷号展开；章页可深链到节与小节（注文共 {{ book.counts.notes }} 组，分布于 {{ book.counts.sectionsWithNotes }} 个小节）</template>
      </span>
    </div>

    <!-- 检索结果 -->
    <section v-if="searching" aria-label="检索结果">
      <a v-for="(h, i) in hits.list" :key="i" class="cat-hit" :href="h.href">
        <span class="cat-hit-no">{{ h.num }}</span>
        <span>{{ h.text }}</span>
        <span class="cat-hit-path">{{ h.kind }}　{{ h.path }}</span>
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
          <span class="cat-vol-meta">{{ v.chs.length }} 章</span>
        </summary>
        <div v-if="openVols.has(v.no)" class="cat-vol-body">
          <p v-if="v.intro.length" class="cat-intro">
            {{ v.intro.join(' ') }}
          </p>

          <details
            v-for="ch in v.chs"
            :key="ch.no"
            class="cat-ch"
            :open="isChOpen(`${v.no}:${ch.no}`)"
            @toggle="(e) => { const t = e.target as HTMLDetailsElement; if (t.open !== isChOpen(`${v.no}:${ch.no}`)) toggleCh(`${v.no}:${ch.no}`) }"
          >
            <summary>
              <a class="cat-ch-title" :href="chHref(v.no, ch.no)" @click.stop>
                第 {{ ch.no }} 章　<template v-for="(s, i) in ch.title" :key="i">
                  <span v-if="s.t === 'en'" lang="en">{{ s.s }}</span>
                  <template v-else>{{ s.s }}</template>
                </template>
              </a>
              <span class="cat-ch-meta">{{ ch.secs.length }} 节／{{ ch.secs.reduce((a, s) => a + s.subs.length, 0) }} 小节</span>
            </summary>
            <div v-if="isChOpen(`${v.no}:${ch.no}`)" class="cat-vol-body">
              <div v-for="s in ch.secs" :key="s.num" class="cat-sec">
                <div class="cat-sec-head">
                  <span class="cat-sec-num">{{ s.num }}</span>
                  <span>
                    <template v-for="(x, i) in s.title" :key="i">
                      <span v-if="x.t === 'en'" lang="en">{{ x.s }}</span>
                      <template v-else>{{ x.s }}</template>
                    </template>
                  </span>
                </div>
                <div v-if="s.notes.length" class="cat-note">
                  <div v-for="(n, i) in s.notes" :key="i">{{ n }}</div>
                </div>
                <ul v-if="s.subs.length" class="cat-subs">
                  <li v-for="u in s.subs" :key="u.num">
                    <a :href="`${chHref(v.no, ch.no)}#_${u.num.replace(/\./g, '-')}`">
                      <span class="cat-sub-num">{{ u.num }}</span>
                      <span>
                        <template v-for="(x, i) in u.title" :key="i">
                          <span v-if="x.t === 'en'" lang="en">{{ x.s }}</span>
                          <template v-else>{{ x.s }}</template>
                        </template>
                      </span>
                    </a>
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
