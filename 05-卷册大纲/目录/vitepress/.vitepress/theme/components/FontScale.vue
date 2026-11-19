<script setup lang="ts">
/**
 * 字号档位（对应装配页的字号调节功能）：五档，写入 CSS 变量 --cat-font-scale 并持久化。
 * SSR 安全：只在 onMounted 后触碰 document／localStorage。
 */
import { onMounted, ref } from 'vue'

const STEPS = [0.9, 1, 1.1, 1.25, 1.4]
const KEY = 'librebsd-outline-font-scale'
const idx = ref(1)

function apply(i: number) {
  idx.value = Math.min(STEPS.length - 1, Math.max(0, i))
  document.documentElement.style.setProperty('--cat-font-scale', String(STEPS[idx.value]))
  try {
    localStorage.setItem(KEY, String(STEPS[idx.value]))
  } catch {
    /* 隐私模式下忽略 */
  }
}

onMounted(() => {
  let saved = 1
  try {
    const v = Number(localStorage.getItem(KEY))
    if (Number.isFinite(v) && v > 0) saved = v
  } catch {
    /* 忽略 */
  }
  const at = STEPS.findIndex((s) => Math.abs(s - saved) < 0.001)
  apply(at >= 0 ? at : 1)
})
</script>

<template>
  <div class="cat-fontscale" role="group" aria-label="字号">
    <button type="button" :disabled="idx === 0" aria-label="缩小字号" @click="apply(idx - 1)">A−</button>
    <button type="button" :disabled="idx === STEPS.length - 1" aria-label="放大字号" @click="apply(idx + 1)">A+</button>
    <button type="button" aria-label="恢复默认字号" @click="apply(1)">A</button>
  </div>
</template>
