# 修复目录页遗留可访问性问题 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 修复重构2026目录页 Lighthouse 已确认的三类遗留问题，同时保持 242 章、1730 节结构和现有视觉行为不变。

**Architecture:** 只修改单体 `index.html` 的动态导航、动态人名链接和相关 CSS；不改变目录数据、章节结构或数据载荷。用现有 Playwright 回归套件、Chrome DevTools、Lighthouse 和四项项目门禁验证。

**Tech Stack:** 单体 HTML、CSS、原生 JavaScript、Playwright、Chrome DevTools Lighthouse。

---

### Task 1: 修复动态人名链接的可爬取性

**Files:**
- Modify: `08-核查报告与多轮复核/重构2026/index.html` 动态 `plink` 生成与绑定区域
- Test: `08-核查报告与多轮复核/重构2026/tests/visual_regression.mjs`

- [ ] **Step 1: 确认现状**

确认动态生成的人名节点当前为 `<a class="plink" data-nm="…">` 且没有 `href`，保留现有点击浮层逻辑。

- [ ] **Step 2: 添加页内无副作用 href**

将生成模板改为包含稳定页内目标：

```js
return '<a class="plink" href="#person-' + encodeURIComponent(nm) + '" data-nm="' + esc(nm) + '">' + m + '</a>';
```

若当前项目已有统一的 `esc`/编码函数，沿用现有函数；点击处理器必须继续 `preventDefault()`，避免页面跳转。

- [ ] **Step 3: 验证人名浮层行为**

运行：

```powershell
node tests/visual_regression.mjs --headless
```

Expected：17 项全部 PASS；人名浮层挂载数量仍大于 50，点击行为不改变。

---

### Task 2: 修复触控目标尺寸

**Files:**
- Modify: `08-核查报告与多轮复核/重构2026/index.html` `.toc-fold` CSS 规则

- [ ] **Step 1: 增大触控命中区而不改变视觉图标**

为 `.toc-fold` 及移动端规则设置至少 44×44 CSS px 的命中区域，保留现有图标居中和视觉层级：

```css
.toc-fold {
  width: 44px;
  min-width: 44px;
  height: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

如果已有 `padding`、`line-height` 或移动端覆盖规则，合并到同一套规则，避免后面的媒体查询重新缩小按钮。

- [ ] **Step 2: 验证布局与触控目标**

运行：

```powershell
node tests/full_matrix_regression.mjs --headless
```

Expected：36 组合、592 项断言全部 PASS，零横向溢出，目录开关和移动抽屉仍正常。

---

### Task 3: 修复 Lighthouse 颜色对比度

**Files:**
- Modify: `08-核查报告与多轮复核/重构2026/index.html` 被 Lighthouse 标记的文字/徽标颜色规则

- [ ] **Step 1: 只调整失败选择器**

通过 Lighthouse 失败节点确定具体选择器，优先将浅色主题中的弱文字颜色提升到与背景至少 4.5:1 的普通文字对比度、3:1 的大字号文字对比度；不要全局替换主题色。暗色主题同步检查，不破坏现有配色。

- [ ] **Step 2: 验证可访问性**

运行 Lighthouse navigation audit，Expected：Accessibility 分数不低于当前 92，且 `color-contrast` 不再失败；同时运行视觉和矩阵回归，确认无视觉/功能回归。

---

### Task 4: 全量门禁与交付记录

**Files:**
- Modify: `08-核查报告与多轮复核/重构2026/tests/README.md`（仅在测试口径或遗留问题说明变化时更新）
- Modify: `08-核查报告与多轮复核/重构2026/64-专门史章处置建议-批复整合版.md`（追加修复记录）

- [ ] **Step 1: 运行全部门禁**

```powershell
python "00-编纂规则与格式规范/01-规则/脚本与命令/sync_refactor2026_baseline.py" --check
python "00-编纂规则与格式规范/01-规则/脚本与命令/xref_audit.py"
python "00-编纂规则与格式规范/01-规则/脚本与命令/audit_data_integrity.py"
python "00-编纂规则与格式规范/01-规则/脚本与命令/audit_sequence_continuity.py"
python "00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py"
```

Expected：全部退出码 0。

- [ ] **Step 2: 运行 Markdown lint**

```powershell
npx markdownlint-cli2 "08-核查报告与多轮复核/重构2026/tests/README.md" "08-核查报告与多轮复核/重构2026/64-专门史章处置建议-批复整合版.md" --config .markdownlint.json
```

Expected：0 errors。

- [ ] **Step 3: 追加执行记录**

在 64 号文追加日期、修复项、回归结果和 Lighthouse 结果；不修改历史快照结论。

- [ ] **Step 4: 复核工作区改动**

确认 `index.html`、测试文件和执行记录为预期改动，未改动备份文件与无关用户变更。
