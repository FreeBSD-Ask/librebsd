/**
 * 章页生成：按 outline.txt 内容源生成 75 个卷页＋539 个章页（站点根下 vNN/）。
 * 生成件（vitepress/.gitignore 的 v*\/ 排除），装配源零改动；侧边栏结构与 SUMMARY 由 verify 门禁锁定一致。
 */
import { mkdirSync, writeFileSync, rmSync } from 'node:fs'
import path from 'node:path'
import { SITE_ROOT, readOutline, segs } from './lib/source'

const OUT = SITE_ROOT

/** Markdown 转义：仅处理会改变结构的字符（题名内允许出现 * / _ [ ] < > | 等）。 */
function esc(s: string): string {
  return s.replace(/([\\`*_[\]<>|#])/g, '\\$1')
}
/** 题名 → 行内 HTML（⟦en:X⟧ 渲染为 <span lang="en">，其余转义）。 */
function inline(title: string): string {
  return segs(title)
    .map((x) => (x.t === 'en' ? `<span lang="en">${esc(x.s)}</span>` : esc(x.s)))
    .join('')
}
const pad = (n: number, w = 2) => String(n).padStart(w, '0')
/** 号锚：1.1 → _1-1；1.1.1 → _1-1-1（与 CatalogApp 生成的 href 同式）。 */
const anchor = (num: string) => `_${num.replace(/\./g, '-')}`

const tree = readOutline()
let chFiles = 0
let volFiles = 0

for (const v of tree.vols) {
  const vdir = path.join(OUT, `v${pad(v.no)}`)
  // 只清理本卷目录（生成件），绝不触碰站点其他文件
  rmSync(vdir, { recursive: true, force: true })
  mkdirSync(vdir, { recursive: true })

  // ---- 卷页
  const volLines: string[] = []
  volLines.push('---')
  volLines.push(`title: ${JSON.stringify(`第${v.roman}卷 ${v.title}`)}`)
  volLines.push('outline: false')
  volLines.push('---')
  volLines.push('')
  volLines.push(`# 第${v.roman}卷　${inline(v.title)}`)
  volLines.push('')
  if (v.intro.length) {
    for (const p of v.intro) volLines.push(`> ${esc(p)}`)
    volLines.push('')
  }
  if (v.posnotes.length) {
    volLines.push('::: details 卷级定位注')
    for (const p of v.posnotes) volLines.push(`${esc(p)}`)
    volLines.push('')
    volLines.push(':::')
    volLines.push('')
  }
  const chCount = v.chs.length
  const secCount = v.chs.reduce((a, c) => a + c.secs.length, 0)
  const subCount = v.chs.reduce((a, c) => a + c.secs.reduce((b, s) => b + s.subs.length, 0), 0)
  volLines.push(`本章卷含 **${chCount}** 章／**${secCount}** 节／**${subCount}** 小节。`)
  volLines.push('')
  volLines.push('| 章 | 题名 | 节数 | 小节数 |')
  volLines.push('| -- | ---- | ---- | ------ |')
  for (const c of v.chs) {
    const sc = c.secs.length
    const uc = c.secs.reduce((b, s) => b + s.subs.length, 0)
    volLines.push(`| 第 ${c.no} 章 | [${inline(c.title)}](./c${pad(c.no)}.md) | ${sc} | ${uc} |`)
  }
  volLines.push('')
  writeFileSync(path.join(vdir, 'index.md'), volLines.join('\n'), 'utf8')
  volFiles++

  // ---- 章页
  for (const c of v.chs) {
    const L: string[] = []
    L.push('---')
    L.push(`title: ${JSON.stringify(`第 ${c.no} 章 ${(c.title || '').replace(/⟦en:([^⟧]*)⟧/g, '$1')}`)}`)
    L.push('outline: [2, 3]')
    L.push('---')
    L.push('')
    L.push(`# 第 ${c.no} 章　${inline(c.title)}`)
    L.push('')
    L.push(`[← 返回第${v.roman}卷](./index.md)`)
    L.push('')
    for (const s of c.secs) {
      // 显式锚点：VitePress 默认 slug 会带整题（_1-1-题名），首页深链需稳定的号锚
      L.push(`## ${s.num} ${inline(s.title)} {#${anchor(s.num)}}`)
      L.push('')
      if (s.notes.length) {
        for (const n of s.notes) L.push(`> ${esc(n)}`)
        L.push('')
      }
      if (s.subs.length) {
        for (const x of s.subs) L.push(`### ${x.num} ${inline(x.title)} {#${anchor(x.num)}}`)
        L.push('')
      }
    }
    writeFileSync(path.join(vdir, `c${pad(c.no)}.md`), L.join('\n'), 'utf8')
    chFiles++
  }
}

console.log(`[gen] PASS 卷页 ${volFiles} ＋ 章页 ${chFiles} → vNN/（站点根）`)
