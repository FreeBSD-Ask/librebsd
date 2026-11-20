/**
 * 工具面全局状态（单 store）：阅读版／研究版与全局溯源注开关。
 * ToolsMenu 挂在 nav-bar 与 nav-screen 两个槽位＝两个实例，状态必须模块级共享，
 * 否则切态只在一份生效（另一份按钮态失真，再点需两次才能退出当前模式）；
 * 移动端菜单（v-if 重挂）也不得重复执行初始化——否则挂载即回放 sme-mode，
 * 会把用户已打开的全局注静默抹掉（独立复核 RV-20261120 P1-2）。
 * 持久化键与装配页同：sme-mode（仅在用户点击时写）、sme-notes（装配页 doc.js 同名）。
 */
import { ref } from 'vue'

export const readMode = ref(false)
export const notesAll = ref(false)

let initialized = false

/** 应用阅读版／研究版；persist＝用户主动点击（才写 localStorage）。 */
export function applyMode(read: boolean, persist: boolean): void {
  readMode.value = read
  document.body.classList.toggle('read-mode', read)
  if (read) {
    // 阅读版隐注：与装配页同——仅在切入 read 时清 notes-all
    notesAll.value = false
    document.body.classList.remove('notes-all')
  }
  if (persist) {
    try {
      localStorage.setItem('sme-mode', read ? 'read' : 'research')
    } catch {
      /* 隐私模式忽略 */
    }
  }
}

export function toggleRead(): void {
  applyMode(!readMode.value, true)
}

export function toggleNotes(): void {
  notesAll.value = !notesAll.value
  document.body.classList.toggle('notes-all', notesAll.value)
  try {
    localStorage.setItem('sme-notes', notesAll.value ? '1' : '0')
  } catch {
    /* 隐私模式忽略 */
  }
}

/** 首次挂载时执行一次：回放持久化的模式与注开关（≤820px 默认阅读版，与装配页同）。 */
export function initState(): void {
  if (initialized) return
  initialized = true
  let saved = ''
  try {
    saved = localStorage.getItem('sme-mode') || ''
  } catch {
    /* 忽略 */
  }
  const wantRead = saved ? saved === 'read' : window.innerWidth <= 820
  applyMode(wantRead, false)
  try {
    if (localStorage.getItem('sme-notes') === '1') {
      notesAll.value = true
      document.body.classList.add('notes-all')
    }
  } catch {
    /* 忽略 */
  }
}
