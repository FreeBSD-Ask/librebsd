<script setup lang="ts">
/**
 * 工具面（顶栏 nav 下拉＋弹层）：导出六格式、阅读版／研究版、节级时间线、结构修订史、跨卷关联图谱。
 * 另含全局溯源注开关（装配页工具列“注”钮的等价物）。
 *
 * 放置：theme/index.ts 的 Layout 挂到 nav-bar-content-after 与 nav-screen-content-after 两个槽位；
 * 每个实例各自持有面板状态，互不干扰（同一时刻只有可见实例会被点击）。数据惰性取用并全局缓存。
 */
import { computed, onBeforeUnmount, onMounted, ref, shallowRef } from 'vue'
import {
  buildGraph,
  buildTimeline,
  download,
  exportCsvText,
  exportFileName,
  exportHtmlSelf,
  exportJsonText,
  exportSummaryText,
  exportTxtText,
  loadCatalog,
  printPdf,
  type CatalogT,
  type GraphData,
  type TimelineRow,
} from '../lib/tools'
// 模式与注开关是全局单份状态（双实例共享；挂载仅首实例初始化，见 lib/ui-state.ts）
import { initState, notesAll, readMode, toggleNotes, toggleRead } from '../lib/ui-state'

// top＝顶栏实例（<960px 隐藏，工具收进汉堡抽屉的 screen 实例）；缺省＝screen 实例
const props = defineProps<{ top?: boolean }>()

const cat = shallowRef<CatalogT | null>(null)
const loading = ref(false)
const err = ref('')
const exportOpen = ref(false)
const panel = ref<'' | 'tl' | 'rv' | 'gp'>('')
const tl = shallowRef<{ years: number; total: number; rows: TimelineRow[] } | null>(null)
const gp = shallowRef<GraphData | null>(null)

async function ensure(): Promise<CatalogT | null> {
  if (cat.value) return cat.value
  loading.value = true
  err.value = ''
  try {
    cat.value = await loadCatalog()
    return cat.value
  } catch (e) {
    err.value = e instanceof Error ? e.message : String(e)
    return null
  } finally {
    loading.value = false
  }
}

const U = (k: string, d = '') => cat.value?.ui[k] ?? d

/** 模式钮字形＝当前态（装配页 doc.js 同语义：read 态显 ui.mode.read“阅”）。其余 nav 项文案
    在 ui-strings 无对应键（装配页为图标），取字面常量。 */
const modeRead = computed(() => U('ui.mode.read', '阅'))
const modeStudy = computed(() => U('ui.mode.study', '研'))

async function toggleExport() {
  exportOpen.value = !exportOpen.value
  if (exportOpen.value) await ensure()
}

async function doExport(kind: string) {
  const c = await ensure()
  if (!c) return
  exportOpen.value = false
  if (kind === 'summary') download(exportFileName(c, 'md'), exportSummaryText(c), 'text/markdown')
  else if (kind === 'json') download(exportFileName(c, 'json'), exportJsonText(c), 'application/json')
  else if (kind === 'csv') download(exportFileName(c, 'csv'), exportCsvText(c), 'text/csv')
  else if (kind === 'txt') download(exportFileName(c, 'txt'), exportTxtText(c), 'text/plain')
  else if (kind === 'pdf') printPdf()
  else if (kind === 'html') exportHtmlSelf(c)
}

async function openPanel(kind: 'tl' | 'rv' | 'gp') {
  panel.value = kind
  const c = await ensure()
  if (!c) return
  if (kind === 'tl' && !tl.value) tl.value = buildTimeline(c)
  if (kind === 'gp' && !gp.value) gp.value = buildGraph(c)
}

function closePanel() {
  panel.value = ''
}

/** 点空白处收起导出菜单（注徽标的事件委托在 NoteLayer.vue，单实例，避免双实例互抵）。 */
function onDocClick(e: MouseEvent) {
  const t = e.target as HTMLElement | null
  if (!t) return
  if (!t.closest('.opt-wrap, .opt-panel')) exportOpen.value = false
}
function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') {
    exportOpen.value = false
    panel.value = ''
  }
}

onMounted(() => {
  initState()
  document.addEventListener('click', onDocClick)
  document.addEventListener('keydown', onKey)
})
onBeforeUnmount(() => {
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('keydown', onKey)
})

/* ---- 图谱几何：环形布局，节点＝卷，边宽＝注指向次数 ---- */
const GRAPH_W = 900
const GRAPH_H = 900
const RING = 350
const nodesPos = computed(() => {
  const g = gp.value
  if (!g) return []
  const n = g.nodes.length
  const deg = new Map<number, number>()
  for (const e of g.edges) {
    deg.set(e.a, (deg.get(e.a) ?? 0) + e.w)
    deg.set(e.b, (deg.get(e.b) ?? 0) + e.w)
  }
  return g.nodes.map((v, i) => {
    const a = (i / n) * Math.PI * 2 - Math.PI / 2
    return {
      ...v,
      x: GRAPH_W / 2 + RING * Math.cos(a),
      y: GRAPH_H / 2 + RING * Math.sin(a),
      deg: deg.get(v.no) ?? 0,
    }
  })
})
const edgeLines = computed(() => {
  const g = gp.value
  if (!g) return []
  const byNo = new Map(nodesPos.value.map((p) => [p.no, p]))
  return g.edges
    .map((e) => {
      const a = byNo.get(e.a)
      const b = byNo.get(e.b)
      if (!a || !b) return null
      return { ...e, x1: a.x, y1: a.y, x2: b.x, y2: b.y }
    })
    .filter((x): x is NonNullable<typeof x> => !!x)
})
</script>

<template>
  <div class="opt-toolsbar" :class="props.top ? 'opt-toolsbar--top' : 'opt-toolsbar--screen'">
  <div class="opt-wrap">
    <button
      type="button"
      class="opt-item"
      :class="{ on: exportOpen }"
      aria-haspopup="menu"
      :aria-expanded="exportOpen"
      @click.stop="toggleExport"
    >导出 ▾</button>
    <div class="opt-menu" :class="{ open: exportOpen }" role="menu">
      <template v-if="loading"><button type="button" disabled>载入中…</button></template>
      <template v-else-if="err"><button type="button" disabled>数据载入失败：{{ err }}</button></template>
      <template v-else>
        <button type="button" role="menuitem" @click="doExport('summary')">{{ U('ui.export.summary', 'SUMMARY（Markdown）') }}</button>
        <button type="button" role="menuitem" @click="doExport('json')">{{ U('ui.export.json', '目录数据（JSON）') }}</button>
        <button type="button" role="menuitem" @click="doExport('csv')">{{ U('ui.export.csv', '节级表（CSV）') }}</button>
        <button type="button" role="menuitem" @click="doExport('txt')">{{ U('ui.export.txt', '纯 TXT') }}</button>
        <button type="button" role="menuitem" @click="doExport('pdf')">{{ U('ui.export.pdf', '输出 PDF（打印）') }}</button>
        <button type="button" role="menuitem" @click="doExport('html')">{{ U('ui.export.html', 'HTML 本体') }}</button>
      </template>
    </div>
  </div>
  <button type="button" class="opt-item" :class="{ on: readMode }" :aria-pressed="readMode" :title="readMode ? modeRead : modeStudy" @click="toggleRead">
    {{ readMode ? modeRead : modeStudy }}
  </button>
  <button type="button" class="opt-item" :class="{ on: panel === 'tl' }" @click="openPanel('tl')">时间线</button>
  <button type="button" class="opt-item" :class="{ on: panel === 'rv' }" @click="openPanel('rv')">修订史</button>
  <button type="button" class="opt-item" :class="{ on: panel === 'gp' }" @click="openPanel('gp')">图谱</button>
  <button type="button" class="opt-item" :class="{ on: notesAll }" :aria-pressed="notesAll" @click="toggleNotes">注</button>

  <Teleport to="body">
    <div v-if="panel" class="opt-panel" role="dialog" aria-modal="false">
      <button type="button" class="opt-close" aria-label="关闭" @click="closePanel">×</button>

      <template v-if="loading"><p class="hint">载入中…</p></template>
      <template v-else-if="err"><p class="hint">数据载入失败：{{ err }}</p></template>

      <template v-else-if="panel === 'tl' && tl">
        <h3>{{ U('ui.tl.h3', '时间线视图（依节名与章题年份抽取）') }}</h3>
        <p class="hint">
          {{ U('ui.tl.pre', '共 ') }}<b>{{ tl.years }}</b>{{ U('ui.tl.mid', ' 个年份、') }}<b>{{ tl.total }}</b>{{ U('ui.tl.post', ' 节已归年；点击条目跳转。') }}
        </p>
        <div class="tl-scroll">
          <div v-for="r in tl.rows" :key="`${r.href}-${r.year}`" class="tl-row">
            <span class="tl-year">{{ r.year }}</span>
            <a :href="r.href"><span class="hint">{{ r.vol }} / {{ r.num }}</span> {{ r.title }}</a>
          </div>
          <p v-if="!tl.rows.length" class="hint">{{ U('ui.tl.empty', '无可归年条目。') }}</p>
        </div>
      </template>

      <template v-else-if="panel === 'rv' && cat">
        <h3>{{ U('ui.rv.h3', '结构修订史（现行大纲目录）') }}</h3>
        <div class="rev-scroll">
          <table>
            <thead>
              <tr>
                <th>{{ U('ui.rv.th1', '序') }}</th>
                <th>{{ U('ui.rv.th2', '日期') }}</th>
                <th>{{ U('ui.rv.th3', '变更') }}</th>
                <th>{{ U('ui.rv.th4', '口径') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(r, i) in cat.revs" :key="i">
                <td>{{ r[0] }}</td>
                <td>{{ r[1] }}</td>
                <td>{{ r[2] }}</td>
                <td>{{ r[3] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="hint">{{ U('ui.rv.hint', '') }}</p>
        <p class="hint">{{ U('ui.rv.cur', '当前页面版本：') }} {{ cat.version }}</p>
      </template>

      <template v-else-if="panel === 'gp' && gp">
        <h3>{{ U('ui.graph.h3', '跨卷关联图谱（依溯源注中的跨卷指向生成）') }}</h3>
        <p class="hint">{{ U('ui.graph.hint', '节点＝卷；连线＝分工/交叉引用注数量（线越粗越密）。') }}
          合计 {{ gp.total }} 处指向、{{ gp.edges.length }} 条连线。</p>
        <div class="opt-graph">
          <svg :viewBox="`0 0 ${GRAPH_W} ${GRAPH_H}`" role="img" :aria-label="U('ui.graph.svg_aria', '跨卷关联图谱')">
            <line
              v-for="(e, i) in edgeLines"
              :key="`e${i}`"
              class="edge"
              :x1="e.x1"
              :y1="e.y1"
              :x2="e.x2"
              :y2="e.y2"
              :stroke-width="0.4 + (e.w / gp.maxW) * 2.6"
            />
            <a v-for="p in nodesPos" :key="p.no" :href="p.href" class="node">
              <title>{{ p.label }} {{ p.title }}（{{ p.ch }} 章／{{ p.secs }} 节；关联 {{ p.deg }} 处）</title>
              <circle :cx="p.x" :cy="p.y" :r="4 + (p.deg / Math.max(1, gp.maxW)) * 6" fill="var(--cat-accent)" fill-opacity="0.75" />
              <text :x="p.x" :y="p.y - 9" text-anchor="middle">{{ p.no }}</text>
            </a>
          </svg>
        </div>
        <p class="hint">{{ U('ui.graph.note', '点击卷名可放大 · 完整卷名在悬停提示与点击放大中可见') }}</p>
      </template>
    </div>
  </Teleport>
  </div>
</template>

<style scoped>
.tl-scroll {
  max-height: 60vh;
  overflow: auto;
}
.opt-panel table th,
.opt-panel table td {
  padding: 4px 8px;
  border-bottom: 1px solid color-mix(in srgb, var(--cat-line) 60%, transparent);
  text-align: left;
  vertical-align: top;
}
</style>
