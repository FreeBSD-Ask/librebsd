/**
 * 小节树件索引（2026-11-22 ykla 令“每个小节独立成页”）：
 * 扫描 `05-卷册大纲/第NN卷-…/第M章-…/A.B-…/A.B.C-….md`，取 YAML 的 thesis／status 与
 * 树内证据块（DOC_MINE／ROW_MINE／MAIL_INSIGHT），供 gen-pages 生成 19 363 个小节页。
 *
 * 只读消费树件，不改装配源；块文本按行内最小 Markdown（`code`／**bold**）渲染，其余一律转义。
 */
import { readFileSync, readdirSync, statSync } from 'node:fs'
import path from 'node:path'
import { SITE_ROOT } from './source'

/** 05-卷册大纲（站点根的上两级）。 */
const OUTLINE_ROOT = path.resolve(SITE_ROOT, '..', '..')

export interface SubBlock {
  kind: 'DOC_MINE' | 'ROW_MINE' | 'MAIL_INSIGHT'
  ref: string
  head: string
  body: string[]
}

export interface SubTree {
  status: string
  thesis: string
  blocks: SubBlock[]
  /** frontmatter 之后的原文（含 H1 与全部正文／块），站点小节页原样渲染。 */
  body: string
}

const BLOCK_RE = /^<!--\s*(DOC_MINE|ROW_MINE|MAIL_INSIGHT):\s*(.*?)\s*-->$/

/** 极简行内 Markdown → HTML（先整体转义，再还原 `code` 与 **bold**；不做链接与 HTML 透传）。 */
export function mdInline(s: string): string {
  const esc = s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
  return esc.replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
}

function parseFrontmatter(text: string): { fm: Record<string, string>; body: string } {
  const lines = text.split('\n')
  if (lines[0]?.trim() !== '---') return { fm: {}, body: text }
  let i = 1
  const fm: Record<string, string> = {}
  while (i < lines.length && lines[i].trim() !== '---') {
    const m = lines[i].match(/^([A-Za-z_]+):\s*(.*)$/)
    if (m) {
      const key = m[1]
      let val = m[2]
      if (val === '|' || val === '|-' || val === '>' || val === '>-') {
        const buf: string[] = []
        i++
        while (i < lines.length && (lines[i].startsWith('  ') || lines[i].trim() === '')) {
          if (lines[i].trim() === '') {
            if (buf.length && buf[buf.length - 1] !== '') buf.push('')
          } else buf.push(lines[i].trim())
          i++
        }
        val = buf.join('\n').trim()
        fm[key] = val
        continue
      }
      fm[key] = val.trim()
    }
    i++
  }
  return { fm, body: lines.slice(i + 1).join('\n') }
}

function parseBlocks(body: string): SubBlock[] {
  const lines = body.split('\n')
  const out: SubBlock[] = []
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].trim().match(BLOCK_RE)
    if (!m) continue
    const kind = m[1] as SubBlock['kind']
    const ref = m[2]
    const chunk: string[] = []
    let j = i + 1
    while (j < lines.length && !BLOCK_RE.test(lines[j].trim())) {
      chunk.push(lines[j])
      if (lines[j].trim() === '' && lines[j + 1]?.trim() === '') break
      j++
    }
    const text = chunk.join('\n').trim()
    const parts = text.split(/\n\s*\n/)
    const head = (parts.shift() ?? '').trim()
    const paras = parts.map((p) => p.trim()).filter(Boolean)
    out.push({ kind, ref, head, body: paras })
    i = j - 1
  }
  return out
}

/**
 * 正文里的“尖括号”处理：树件正文含 `<lib>`／`<sys/socket.h>`／`<no-id-…>` 这类**非标签**尖括号，
 * 原样进 Vue SFC 会被当成未闭合标签而编译失败。规则：只放行 HTML 注释（`<!--`）、URL 自动链接
 * 与邮箱自动链接；其余 `<` 转义为 `&lt;`——页面仍原样显示 `<…>`。
 */
export function escapeStrayAngles(s: string): string {
  // 行内代码与围栏代码块逐字保真（消息 ID 常以 `<…>` 形式写在反引号里），只在普通文本段处理尖括号
  return s
    .split(/(```[\s\S]*?```|`[^`\n]*`)/g)
    .map((seg, i) => (i % 2 === 1 ? seg : neutralizeSchemeRelative(escapeAnglesInText(seg))))
    .join('')
}

/**
 * `//word` 在 markdown-linkify 下会被当成协议相对 URL（实测树件 `socket(2)[EB/OL]//4.4BSD source tree` 渲染成
 * `href="//4.4BSD"`，指向错误主机）。把“非 `scheme://` 的 `//`”转成实体，读者仍看到 `//` 原文。
 */
function neutralizeSchemeRelative(s: string): string {
  return s.replace(/(?<!:)\/\//g, '&#47;&#47;')
}

function escapeAnglesInText(s: string): string {
  let out = ''
  for (let i = 0; i < s.length; i++) {
    const ch = s[i]
    if (ch !== '<') {
      out += ch
      continue
    }
    const rest = s.slice(i)
    if (rest.startsWith('<!--')) {
      out += '<'
      continue
    }
    const m = /^<[^\s<>]*>/.exec(rest)
    if (m) {
      const inner = m[0].slice(1, -1)
      if (/^(https?:\/\/|mailto:)/i.test(inner) || /^[^\s<>]+@[^\s<>]+$/.test(inner)) {
        out += m[0]
        i += m[0].length - 1
        continue
      }
    }
    out += '&lt;'
  }
  return out
}

/** key＝`{vol}/{小节号}`（如 `1/1.1.1`）→ 树件解析结果。 */
export function loadTreeIndex(): Map<string, SubTree> {
  const idx = new Map<string, SubTree>()
  for (const volDir of readdirSync(OUTLINE_ROOT)) {
    const vm = volDir.match(/^第(\d+)卷-/)
    if (!vm) continue
    const volNo = Number(vm[1])
    const volPath = path.join(OUTLINE_ROOT, volDir)
    if (!statSync(volPath).isDirectory()) continue
    for (const chDir of readdirSync(volPath)) {
      if (!/^第\d+章-/.test(chDir)) continue
      const chPath = path.join(volPath, chDir)
      if (!statSync(chPath).isDirectory()) continue
      for (const secDir of readdirSync(chPath)) {
        if (!/^\d+\.\d+-/.test(secDir)) continue
        const secPath = path.join(chPath, secDir)
        if (!statSync(secPath).isDirectory()) continue
        for (const f of readdirSync(secPath)) {
          const fm2 = f.match(/^(\d+\.\d+\.\d+)-.*\.md$/)
          if (!fm2) continue
          const text = readFileSync(path.join(secPath, f), 'utf8')
          const { fm, body } = parseFrontmatter(text)
          idx.set(`${volNo}/${fm2[1]}`, {
            status: fm.status ?? '',
            thesis: fm.thesis ?? '',
            blocks: parseBlocks(body),
            body: body.replace(/^\s*\n+/, '').trimEnd(),
          })
        }
      }
    }
  }
  return idx
}
