<script setup lang="ts">
/**
 * 数据视图：catalog.json 的 persons／refs／revs 三视图（检索式浏览，限前 200 条）。
 * 数据来自构建期 loader（data/catalog.data.ts）。
 */
import { computed, ref } from 'vue'
import { data } from '../../../data/catalog.data'

type Tab = 'persons' | 'refs' | 'revs'
const tab = ref<Tab>('persons')
const q = ref('')
const MAX = 200

const tabs: Array<{ key: Tab; label: string; n: number }> = [
  { key: 'persons', label: '人物', n: data.persons.length },
  { key: 'refs', label: '文献', n: data.refs.length },
  { key: 'revs', label: '修订', n: data.revs.length },
]

const kw = computed(() => q.value.trim().toLowerCase())

const persons = computed(() => {
  if (!kw.value) return data.persons
  return data.persons.filter(
    (p) =>
      p.zh.toLowerCase().includes(kw.value) ||
      p.en.some((e) => e.toLowerCase().includes(kw.value)) ||
      p.role.toLowerCase().includes(kw.value),
  )
})
const refs = computed(() => {
  if (!kw.value) return data.refs
  return data.refs.filter(([id, t]) => id.includes(kw.value) || t.toLowerCase().includes(kw.value))
})
const revs = computed(() => {
  if (!kw.value) return data.revs
  return data.revs.filter((r) => `${r.id} ${r.date} ${r.desc} ${r.status}`.toLowerCase().includes(kw.value))
})

const shown = computed(() => ({
  persons: persons.value.slice(0, MAX),
  refs: refs.value.slice(0, MAX),
  revs: revs.value.slice(0, MAX),
}))
const totals = computed(() => ({ persons: persons.value.length, refs: refs.value.length, revs: revs.value.length }))
</script>

<template>
  <div class="cat-app" id="data">
    <h2>数据视图</h2>
    <p class="cat-hint">
      DATA 段三视图（人物／文献／修订），源 <code v-pre>data/catalog.json</code>；每视图最多显示 {{ MAX }} 条。
    </p>

    <div class="cat-tabs" role="tablist">
      <button
        v-for="t in tabs"
        :key="t.key"
        class="cat-tab"
        role="tab"
        :aria-selected="tab === t.key"
        @click="tab = t.key"
      >
        {{ t.label }} {{ t.n.toLocaleString('zh-CN') }}
      </button>
      <input v-model="q" type="search" placeholder="在本视图内检索" aria-label="检索" style="flex: 1 1 200px" />
    </div>

    <p class="cat-hint">
      命中 {{ totals[tab].toLocaleString('zh-CN') }} 条<template v-if="totals[tab] > MAX">，显示前 {{ MAX }} 条</template>
    </p>

    <div v-if="tab === 'persons'">
      <div v-for="p in shown.persons" :key="p.id" class="cat-row">
        <div>
          <div class="cat-row-id">{{ p.zh || p.id }}</div>
          <div class="cat-row-sub">{{ p.priority }}<template v-if="p.volume">　卷 {{ p.volume }}</template></div>
        </div>
        <div>
          <div>{{ p.role || '—' }}</div>
          <div class="cat-row-sub">
            <span v-if="p.en.length">{{ p.en.join('／') }}</span>
            <template v-if="p.life">　{{ p.life }}</template>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="tab === 'refs'">
      <div v-for="[id, text] in shown.refs" :key="id" class="cat-row">
        <div class="cat-row-id">[{{ id }}]</div>
        <div>{{ text }}</div>
      </div>
    </div>

    <div v-else>
      <div v-for="r in shown.revs" :key="r.id" class="cat-row">
        <div>
          <div class="cat-row-id">#{{ r.id }}</div>
          <div class="cat-row-sub">{{ r.date }}</div>
        </div>
        <div>
          <div>{{ r.desc || '—' }}</div>
          <div class="cat-row-sub">{{ r.status }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
