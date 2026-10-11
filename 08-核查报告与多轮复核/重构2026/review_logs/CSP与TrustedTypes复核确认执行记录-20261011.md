# CSP 与 Trusted Types 复核确认执行记录（2026-10-11）

> 缘起：《主理人批准登记-全部遗留项-20261011》A2 按序施工＋主理人令（排序第四批）。
> 性质：**复核确认批（零改动）**——75 号文 §89／§90 对 P2-4 TT 强制与 P2-5 style-src 哈希化已有负结果裁定，本批以当日代码现态重验其前提，逐条确认或推翻。

## 一、现态盘点（2026-10-11 15:59 产物）

| 项 | 现态 |
| -- | ---- |
| CSP meta | `default-src 'none'; script-src 'self' 'nonce-…'; worker-src blob:（O-3 增）; style-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data: blob:; connect-src 'none'; object-src 'none'; base-uri 'self'; form-action 'none'` |
| trustedTypes | 已建非强制 policy `librebsd`（`ttt()`：Sanitizer 优先、DOMParser 兜底净化）；CSP **未**启用 `require-trusted-types-for 'script'` |
| innerHTML 写入面 | 25 处（doc.js）；其中 **6 处**数据派生 HTML 经 `__LB.ttt()` 净化，其余为自有静态模板串（无外部输入） |
| 违规实况 | 复核探针全交互扫（四 dialog 面板开合×4＋主题×2＋研/阅×2＋plink 浮层）：**securitypolicyviolation = 0**；console error/warning = **0** |

## 二、负结果前提重验（逐条确认，无一推翻）

| 75 号文裁定 | 前提 | 当日重验 |
| ----------- | ---- | -------- |
| §89 P2-4 TT 强制 → **不做**（已回滚） | 强制后净化器自身被拦（Chromium 128+ `DOMParser.parseFromString` 即 TT sink——policy 内调 DOMParser 亦违规，鸡生蛋） | **前提不变**：`ttt()` 仍以 DOMParser 为兜底净化路径（doc.js L22）；6 处数据派生 innerHTML 依赖它。启用强制＝关闭真正的 DOM 净化，1,104 处违规的实测结论继续成立 |
| §90 P2-5 style-src 哈希化 → **不做** | ①去 `'unsafe-inline'` 不可行——12+ 处运行时内联样式写入（字号 zoom/宽度、进度条 width、浮层与菜单定位）会被拦，核心交互失效；②哈希须与 `<style>` 块逐字节一致，CSS 一变哈希未同步即全页无样式；③静态单体＋零网络＋无用户输入，**无注入面**，收益≈0 | **前提不变**：dialog 化与 VT 两批均未新增内联样式写入路径（openDialog/viewTransition 走类切换与原生 API）；无注入面结论继续成立 |
| O-3 已增 `worker-src blob:` | Blob Worker 白名单化 | 在场（见 §一） |

## 三、裁定

1. **维持 75 号文 §89／§90 不做裁定**——TT 强制与 style-src 哈希化在“单体文件＋静态内容＋无注入面”架构下收益≈0 且各引入一处新失效模式；本批零改动。
2. CSP 现态（含 O-3 worker-src）为**该架构下可达的合理最强配置**；`frame-ancestors` 等仅 HTTP 头可用的指令属服务器线（`serve_refactor2026.py`，第十一件已断言三项安全响应头），不在页面批范围。
3. 唯一残余面＝25 处 innerHTML 中 19 处自有静态模板串——其安全性由“字符串全部为本文件字面量＋无外部输入”保证，登记不改动（若未来引入用户输入，须一律过 `ttt()`）。

## 四、验证与落账

- 复核探针 `script/_csp_reconfirm_probe_20261011.mjs`（保留）：0 违规／0 报错／面板全关。
- 本批**零产物改动**：不装配、不递增版本（15:59 维持）、不触碰 prebak。
- changelog **id=2356**（复核确认类，循 2349 只读盘查先例）；92 号文 §十一 顶插一行；《11 项缓办评估与施工序登记》第四批回写。

*编制：WorkBuddy，2026-10-11。*
