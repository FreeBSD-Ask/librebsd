<script setup lang="ts">
/**
 * 折叠手势（全局单实例）：卷页 section.doc-block 的卷题 h1 与章 h3.chapter 点击折叠，
 * 手势判据复刻装配页 doc.js「卷/章折叠」块——
 * ①纯点题才折叠：拖选（位移 >4px）或点击落点时选中区非空一律不折；
 * ②250ms 确认窗：单击不当场折，第二击（双击/三击，detail>1）到达即撤单；
 * ③双击兜底折回：手速慢于确认窗者由 dblclick 将已折的块折回。
 * 题面文字可选（箭头 user-select:none），与装配页 2026-09-27 修正一致。
 */
import { onBeforeUnmount, onMounted } from 'vue'

let down: { x: number; y: number } | null = null
let timer = 0
let last: { box: HTMLElement; t: number } | null = null

function foldBox(el: HTMLElement | null): HTMLElement | null {
  if (!el || !el.closest) return null
  const h1 = el.closest('.doc-block > h1')
  if (h1) return h1.parentElement
  return el.closest('h3.chapter')
}

function selectGesture(e: MouseEvent): boolean {
  if (down && (Math.abs(e.clientX - down.x) > 4 || Math.abs(e.clientY - down.y) > 4)) return true
  const sel = window.getSelection
    ? window.getSelection()
    : null
  return !!(sel && sel.rangeCount && !sel.isCollapsed)
}

function onClick(e: MouseEvent) {
  const t = e.target as HTMLElement | null
  if (!t) return
  const box = foldBox(t)
  if (!box) return
  if (t.closest('a, button, input, select, textarea, label, [role="button"]')) return
  if ((e as MouseEvent).detail > 1) {
    clearTimeout(timer)
    timer = 0
    return
  }
  if (selectGesture(e)) return
  clearTimeout(timer)
  timer = window.setTimeout(() => {
    timer = 0
    box.classList.toggle('folded')
    last = { box, t: Date.now() }
  }, 250)
}

function onDblClick(e: MouseEvent) {
  const prev = last
  last = null
  if (!prev || Date.now() - prev.t > 400) return
  const t = e.target as HTMLElement | null
  if (foldBox(t) !== prev.box) return
  prev.box.classList.toggle('folded')
}

function onDown(e: MouseEvent) {
  down = { x: e.clientX, y: e.clientY }
}

onMounted(() => {
  document.addEventListener('mousedown', onDown)
  document.addEventListener('click', onClick)
  document.addEventListener('dblclick', onDblClick)
})
onBeforeUnmount(() => {
  clearTimeout(timer)
  document.removeEventListener('mousedown', onDown)
  document.removeEventListener('click', onClick)
  document.removeEventListener('dblclick', onDblClick)
})
</script>

<template>
  <span hidden aria-hidden="true" />
</template>
