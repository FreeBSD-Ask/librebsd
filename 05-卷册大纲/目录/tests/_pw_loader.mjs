/* playwright 解析器（2026-11-10 立）：取代 tests/ 各脚本里硬编码的
 *   import { chromium } from 'file:///C:/Users/<用户名>/AppData/Roaming/npm/...
 * 用户名、npm 前缀、playwright 的嵌套位置一变就炸；此处按 Node 解析顺序动态定位。
 *
 * 查找顺序：
 *   1. 本文件向上冒泡的 node_modules（仓库内本地依赖，若有）
 *   2. %APPDATA%\npm\node_modules\playwright（npm 全局提升安装）
 *   3. %APPDATA%\npm\node_modules\<pkg>\node_modules\playwright 与
 *      %APPDATA%\npm\node_modules\@<scope>\<pkg>\node_modules\playwright
 *      （本项目现实形态：playwright 挂在 @executeautomation/playwright-mcp-server 之下）
 *
 * 用法：import { chromium } from './_pw_loader.mjs';
 */
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

function playwrightIndex(pkgDir) {
  const idx = path.join(pkgDir, 'index.mjs');
  return fs.existsSync(idx) ? idx : null;
}

function tryResolveFrom(baseDir) {
  if (!baseDir || !fs.existsSync(baseDir)) return null;
  const req = createRequire(path.join(baseDir, '_pw_resolve_stub.js'));
  try {
    const pkgJson = req.resolve('playwright/package.json');
    const hit = playwrightIndex(path.dirname(pkgJson));
    if (hit) return hit;
  } catch { /* 继续下一候选 */ }
  return null;
}

function nestedCandidates(npmModules) {
  const out = [];
  if (!fs.existsSync(npmModules)) return out;
  for (const entry of fs.readdirSync(npmModules, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name === '.bin') continue;
    const dir = path.join(npmModules, entry.name);
    if (entry.name.startsWith('@')) {
      for (const sub of fs.readdirSync(dir, { withFileTypes: true })) {
        if (sub.isDirectory()) out.push(path.join(dir, sub.name, 'node_modules'));
      }
    } else {
      out.push(path.join(dir, 'node_modules'));
    }
  }
  return out;
}

async function resolvePlaywright() {
  const here = import.meta.dirname;

  // 1. 本地（仓库内）解析
  const local = tryResolveFrom(here) || tryResolveFrom(path.resolve(here, '..'));
  if (local) return local;

  // 2/3. npm 全局前缀
  const npmRoot = process.env.APPDATA ? path.join(process.env.APPDATA, 'npm') : null;
  if (npmRoot) {
    const g = tryResolveFrom(npmRoot);
    if (g) return g;
    const gm = path.join(npmRoot, 'node_modules');
    for (const cand of nestedCandidates(gm)) {
      const direct = playwrightIndex(path.join(cand, 'playwright'));
      if (direct) return direct;
      const viaReq = tryResolveFrom(cand);
      if (viaReq) return viaReq;
    }
  }

  throw new Error(
    'playwright 未找到：仓库内无 node_modules，npm 全局前缀（%APPDATA%\\npm）下也没有。' +
    '先执行 `npm i -g @executeautomation/playwright-mcp-server` 或本地 `npm i playwright`。'
  );
}

const { chromium } = await import(pathToFileURL(await resolvePlaywright()).href);
export { chromium };
