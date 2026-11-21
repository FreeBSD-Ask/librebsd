<script setup lang="ts">
/**
 * 注徽标事件委托（全局单实例）：点“注”开合本节溯源注。
 * 装配页由 doc.js 逐元素绑定；站点改为 document 级委托，避免 19 363 个节的重复监听，
 * 也保证 SPA 路由切换后新页面无需重新绑定。
 */
import { onBeforeUnmount, onMounted } from 'vue'

function onClick(e: MouseEvent) {
  const t = e.target as HTMLElement | null
  const badge = t?.closest<HTMLElement>('.note-badge')
  if (!badge) return
  // 两种宿主形态：章页 .sec-note／首页 .cat-note（p 包裹）；卷页 li 形（装配页同构，折 li.note-open）
  const host = badge.closest('.sec-note, .cat-note')
  if (host) {
    e.preventDefault()
    const open = host.classList.toggle('open')
    badge.setAttribute('aria-expanded', open ? 'true' : 'false')
    return
  }
  const li = badge.closest('li')
  if (li) {
    e.preventDefault()
    const open = li.classList.toggle('note-open')
    badge.setAttribute('aria-expanded', open ? 'true' : 'false')
  }
}

onMounted(() => document.addEventListener('click', onClick))
onBeforeUnmount(() => document.removeEventListener('click', onClick))
</script>

<template>
  <span hidden aria-hidden="true" />
</template>
