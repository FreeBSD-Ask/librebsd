/**
 * 产物净化：Vite 的内容哈希是随机 Base64 片段，偶会发生 `v16_c06.md.BaK6epHY.js` 这类
 * 含 `.bak`／`.bak-*` 中缀的名字，触发第三十六件“旁路备份副本”判据误报。
 * 本模块把撞名的产物片段重命名，并在 dist 内全部文本文件中回写引用（哈希片段唯一，替换安全）。
 */
import { readdirSync, readFileSync, renameSync, writeFileSync } from 'node:fs'
import path from 'node:path'

const SUSPECT = /\.bak([A-Za-z0-9_-]*)\.(?:(lean)\.)?(js|mjs|css|json|woff2|map)$/i

export function sanitizeDist(distDir: string): { renamed: string[]; touched: number } {
  const renamed: string[] = []
  const pairs: Array<[string, string]> = []
  const hashPairs: Array<[string, string]> = []

  function walk(dir: string) {
    // withFileTypes：dirent 类型直接来自 readdir，不做 statSync 检查后再访问（消除 TOCTOU 形状）。
    for (const dirent of readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, dirent.name)
      if (dirent.isDirectory()) {
        walk(full)
        continue
      }
      const name = dirent.name
      const m = name.match(SUSPECT)
      if (!m) continue
      // 变形但保持唯一：bak → kbk（不与既有片段冲突的固定替换）
      const next = name.replace(/\.bak([A-Za-z0-9_-]*)\.(?:(lean)\.)?(js|mjs|css|json|woff2|map)$/i, (_, h, lean, ext) => `.kbk${h}.${lean ? 'lean.' : ''}${ext}`)
      renameSync(full, path.join(dir, next))
      renamed.push(path.relative(distDir, path.join(dir, next)).replace(/\\/g, '/'))
      pairs.push([name, next])
      // 页面数据文件名由 hashmap.json 的裸哈希值在运行时拼出，故必须同时改哈希本身
      const oldHash = m[0].slice(1, -`.${m[2] ? 'lean.' : ''}${m[3]}`.length)
      const newHash = oldHash.replace(/^bak/i, 'kbk')
      if (oldHash !== newHash) hashPairs.push([oldHash, newHash])
    }
  }
  walk(distDir)
  if (!pairs.length) return { renamed, touched: 0 }

  // 两阶段：先遍历收集待写清单（读＋内存替换，不落盘），再统一写盘。
  // 写阶段不再与任何文件读取交织，readFileSync→writeFileSync 的同路径检查—写入窗口不成立。
  function rewrite(dir: string, rows: Array<{ full: string; text: string }>) {
    // withFileTypes：同 walk，消除 statSync 检查后再访问的 TOCTOU 形状。
    for (const dirent of readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, dirent.name)
      if (dirent.isDirectory()) {
        rewrite(full, rows)
        continue
      }
      if (!/\.(html|js|mjs|css|json|xml)$/i.test(dirent.name)) continue
      let text = readFileSync(full, 'utf8')
      const before = text
      for (const [from, to] of pairs) if (text.includes(from)) text = text.split(from).join(to)
      for (const [from, to] of hashPairs) if (text.includes(from)) text = text.split(from).join(to)
      if (text !== before) rows.push({ full, text })
    }
  }
  const rows: Array<{ full: string; text: string }> = []
  rewrite(distDir, rows)
  for (const r of rows) writeFileSync(r.full, r.text, 'utf8')
  const touched = rows.length
  return { renamed, touched }
}
