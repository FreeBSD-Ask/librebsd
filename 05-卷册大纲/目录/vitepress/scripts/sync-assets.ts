/**
 * 资产同步：从装配源 assets/ 抽取站点所需静态件到 public/（public 与 .vitepress 分离）。
 * - 字体：doc.css 内嵌的 LXGW WenKai Screen woff2 子集 → public/fonts/lxgw-wenkai-screen-subset.woff2
 * - 图标：assets/favicon.ico → public/favicon.ico；assets/apple-touch-icon.png → og:image／apple-touch-icon
 * - 书名标志：assets/logo.svg → public/logo.svg（首页书名区，装配页为内嵌同名 SVG）
 * 均为生成件（vitepress/.gitignore 排除），装配源零改动。
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import path from 'node:path'
import { SITE_ROOT, CATALOG_DIR, DOC_CSS_PATH, FAVICON_PATH } from './lib/source'

const PUB = path.join(SITE_ROOT, 'public')
mkdirSync(path.join(PUB, 'fonts'), { recursive: true })

const css = readFileSync(DOC_CSS_PATH, 'utf8')
const m = css.match(/data:font\/woff2;base64,([A-Za-z0-9+/=]+)/)
if (!m) {
  console.error('[sync] FAIL：doc.css 内未找到 woff2 子集')
  process.exit(1)
}
const buf = Buffer.from(m[1], 'base64')
const out = path.join(PUB, 'fonts', 'lxgw-wenkai-screen-subset.woff2')
writeFileSync(out, buf)

const ico = readFileSync(FAVICON_PATH)
writeFileSync(path.join(PUB, 'favicon.ico'), ico)

const touch = readFileSync(path.join(CATALOG_DIR, 'assets', 'apple-touch-icon.png'))
writeFileSync(path.join(PUB, 'apple-touch-icon.png'), touch)

const logoSvg = readFileSync(path.join(CATALOG_DIR, 'assets', 'logo.svg'))
writeFileSync(path.join(PUB, 'logo.svg'), logoSvg)

console.log(`[sync] PASS 字体 ${buf.length} B → public/fonts/lxgw-wenkai-screen-subset.woff2`)
console.log(`[sync] PASS 图标 ${ico.length} B → public/favicon.ico；触控图标 ${touch.length} B＋书名标志 ${logoSvg.length} B`)
