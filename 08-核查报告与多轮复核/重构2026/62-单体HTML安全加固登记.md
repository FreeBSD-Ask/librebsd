# 62-单体 HTML 现代化安全加固登记

> 日期：2026-09-16
> 对象：`08-核查报告与多轮复核/重构2026/index.html`（26 卷 243 章 1760 节单体文件）
> 目标：现代化全面安全手段，同时保持 320–3440px 全分辨率自适应与全功能。

## 一、已落地措施

### 1. CSP（Content-Security-Policy，meta 送达）

```http
default-src 'none';
script-src 'self' 'nonce-Zk8rN2fT9qPm5vLx1wJh';
style-src 'self' 'unsafe-inline';
font-src 'self' data:;
img-src 'self' data: blob:;
connect-src 'self';
object-src 'none';
base-uri 'self';
form-action 'none'
```

- 4 个内联 `<script>` 全部加 `nonce`（头预载 + 行为层必带；ld+json 与数据块非执行脚本）。
- `default-src 'none'` 默认拒绝一切未白名单资源；`object-src 'none'`、`form-action 'none'`、`base-uri 'self'` 防插件/表单/基准 URL 劫持。
- `frame-ancestors` 经 meta 无效，已改由服务器 `X-Frame-Options: DENY` 承担（见 §7）。

### 2. SRI（Subresource Integrity）

- 字面 SRI 需外部 `<script src>`/`<link>` 挂 `integrity`；本单体外资源为 0，无法直接使用标准 SRI。
- **已实现等价校验**：给内嵌数据块 `#opt-data-blob` 加 `data-integrity="sha256-…"`；加载器用 Web Crypto `crypto.subtle.digest` 对数据块文本做 SHA-256 比对。相符→加载；不符→拒绝并 `data-opt-ready=0`、persons/refs 降级，静态 DOM 目录与 DOM 检索不受影响。
- 实测：正常页 ready=1、检索可用；篡改数据块一字符→完整性警告、DATA 拒绝加载（`DATAdefined=false`）、目录本体仍渲染。

### 3. rel="noopener"

- **不适用**：全文件 0 处 `<a target="_blank">`。仅 PDF 导出的 `window.open` 为同源新窗，无 opener 反向引用风险。

### 4. iframe sandbox

- **不适用**：0 处 `<iframe>`（静态或动态）。

### 5. Trusted Types

- 显式净化策略 `tt`（名 `librebsd`，DOMParser 基）+ 助手 `ttt()`。
- 已包裹数据驱动的 innerHTML 槽：**检索结果、时间线、注弹层、注复用、节重建**。
- 净化器剥离 `<script>/<iframe>/<object>/<embed>/<link>/<meta>/<style>/<form>/<base>/<template>`、`on*` 事件属性、`javascript:` 伪协议 URL；保留正文标记。
- 实测：`ttt('<b>ok</b><script>alert(1)</script><img onerror=…><a href="javascript:…">')` → `<b>ok</b><img src="x"><a>x</a>`，XSS 载荷被剥离、正文保留。
- 说明：`require-trusted-types-for 'script'` 会令 DOMParser/`createContextualFragment` 把字符串当作文本，且与"净化器需解析"构成死循环；故采用显式策略包裹数据槽（等价于将不信任数据流经净化器），CSP 主防线保持不变。

### 6. 安全 DOM / XSS 加固

- 用户检索词仅进 `input.value`（属性，安全），**从不注入 innerHTML**；检索结果标题转义 `&lt;` 且经 `tt` 净化。
- 数据槽（标题/注/年份）统一经净化器；图谱 SVG（跨卷指向）为目录受控数据，未包裹以避免 SVG 命名空间被 DOMParser 破坏。

### 7. HTTP 安全响应头（服务器层，serve_https.py）

```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=(), payment=(), usb=()
Cache-Control: no-store
```

（`X-Frame-Options: DENY` 补齐 meta-CSP 无法表达的点击劫持防护。）

〔注（2026-10-12 补记·r66 #15 复核）：本§所述 `serve_https.py` **已退役**——2026-09-28 服务器层归一（r66 wave1），现行唯一实现＝`serve_refactor2026.py`；缓存语义已由 `no-store` 更新为 `no-cache`（启用 304 再验证），并以 gzip 传输压缩。〕

### 8. 跨源隔离与传输层标准

服务器 `serve_https.py` 已增加：

- `Strict-Transport-Security: max-age=31536000; includeSubDomains`（HSTS，防 HTTPS 降级）；
- `Cross-Origin-Opener-Policy: same-origin`（COOP，隔离跨源窗口与 opener）；
- `Cross-Origin-Resource-Policy: same-origin`（CORP，限制跨源读取）；
- `Cross-Origin-Embedder-Policy: require-corp`（COEP，启用跨源隔离；单体文件无跨源子资源，天然满足）；
- `X-Frame-Options: DENY`、`nosniff`、`Referrer-Policy`、`Permissions-Policy`。

〔注（2026-10-12 补记）：`serve_https.py` 已退役（同上）；现行 `serve_refactor2026.py` 发送六项响应头——nosniff／Referrer-Policy／X-Frame-Options／Permissions-Policy／COOP／CORP。**HSTS 与 COEP 不再发送**（HSTS＝HTTP 场景刻意不发；COEP＝未纳入归一实现）——与本节原述之差异以本注为准。〕

〔注（2026-10-12 补记·r66 wave3/D7 复核）：CSP `nonce="Zk8rN2fT9qPm5vLx1wJh"` 为**固定字面量**（源件 `page.template.html` 内 5 处）——规范要求每响应不可预测。**维持现状的裁定理由**：本页威胁模型为“本地单文件、CSP `default-src 'none'`、零网络请求、零外链、零用户输入、内容全作者受控”，固定 nonce 无实际可乘之隙；改为每响应随机将破坏“产物＝源件装配结果”的逐字节可核验性（第八件门禁与 embed.py SHA-256 摘要的判据基础）。此为**有意识的决定**（非遗忘）；后续如引入服务端动态渲染再议。〕

### 9. 原生 Sanitizer API

`tt` 策略优先使用 `Sanitizer().sanitizeToString()`，不支持时回退 DOMParser 净化器；两条路径均剥离危险元素、事件属性与 `javascript:` 伪协议。

### 10. 不适用/不建议标准

- `crossorigin`：无跨源资源；
- CSP `sandbox`：本页需要脚本与本地存储，启用会误伤核心功能，暂不采用；
- `X-XSS-Protection`：已废弃，不启用；
- `Clear-Site-Data`：无登录态/会话态，不适用。

## 二、回归验证

- 320–3440px 全分辨率：jsErr 0、无横向溢出、26 卷 243 章 1760 节。
- 功能：检索、时间线（开/关）、图谱、注开关、导出（SUMMARY/JSON/CSV/PDF/纯 TXT）全部可用；`ttt` 净化器对数据槽生效且不破坏渲染。

## 三、待办/说明

- `frame-ancestors` 依赖 HTTP 头；若换非 serve_https.py 部署，需在服务器另设 `X-Frame-Options` 或 CSP 头。
- 单体文件直接 file:// 打开时，服务器层安全头不生效；meta-CSP 仍生效（除 frame-ancestors）。

*（完）已提交。*
