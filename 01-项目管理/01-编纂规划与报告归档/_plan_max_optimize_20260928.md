> ⚠️ 2026-10-04 主理人令：本文件内所有“git add -f”声明一律作废——script/ 下一律不入库、保留磁盘文件，禁止 git add -f（除非主理人显式声明）。

# 重构2026 最大化优化方案（不计成本版）

- 日期：2026-09-28
- 对象：`08-核查报告与多轮复核/重构2026/`（`index.html` ＋ 目录树 ＋ 服务器层）
- 性质：**方案书**（本轮不执行改动；执行须逐波走“装配 → 九件门禁 → 三套浏览器回归 → 路径限定提交”）
- 红线（不变）：**① 字体不变**（`@font-face`、`font-family` 栈、字体交付方式）；**② 单体文件不变**（零外链、零 `@import`、数据内嵌、品牌件 data URI）

---

## 〇 前提：如何理解“不计成本”

**“不计成本”＝ 允许投入任意工程量去消除结构性缺陷，但不允许投入任何无法验证的改动。**

这两条并不矛盾，而是本项目用代价换来的纪律：

1. **可验证性是硬门槛**。任何性能类改动必须先做交错 A/B × N≥10 测噪声带；效应量小于噪声带即判“不可验证”，回滚，**不得宣称收益**。本页基线自身波动曾达 ±50%（Layout 1.5 s ↔ 2.3 s），滚动长任务两轮结论符号相反——这些都是噪声。
2. **“归因”≠“有效”**。火焰图能可靠指出“瓶颈在渲染管线”（本页布局 vs 脚本 8–20 倍），但不能证明微调有可测收益。
3. **负结果照报**。本轮就有两条负结果（见勘误 2、F 面 F1），照报不隐。

因此本方案把所有条目分成两类：**“确凿类”**（判据可机检、不依赖性能测量，直接做）与**“待测类”**（必须先建测量装置，再决定做不做）。

### 勘误（对 2026-09-28 上一轮审计报告的更正与补充）

| # | 上一轮表述 | 更正后的事实 |
| --- | --- | --- |
| 勘误 1 | “62 号文记录的 `serve_https.py` 已无实现” | `serve_https.py` **确实不存在**；但**存在两份**服务器实现——`00-编纂规则与格式规范/01-规则/脚本与命令/serve_refactor2026.py`（`0.0.0.0:8090`，`ThreadingTCPServer`，`allow_reuse_address=True`）与 `08-核查报告与多轮复核/重构2026/server/serve_index.py`（`0.0.0.0:80`，单线程，`allow_reuse_address=False`，幂等）。**两份均不发任何安全响应头**。上一轮只报了后者，检索模式过窄（`serve_https*`／`serve_index*` 匹配不到 `serve_refactor2026.py`）。 |
| 勘误 2 | “疑似死规则 65 条” | **误报，实际 0 条**。首版判据只收集了 `classList.add/className=` 等窄模式，把 `#exportMenu`／`#fontMenu`／`#tlView`／`#revView`／`.chart-*`／`.diagram-*` 等**运行时生成**的节点误判为死规则。改用“令牌是否在 页面 HTML ∪ `doc.js` ∪ `modern.css` 任一处出现”的宽松判据后 → **0 条**。**负结果：`doc.css` 无可识别的死规则**（272 个去重选择器全部有对应宿主）。 |
| 勘误 3 | 未提及 | `serve_refactor2026.py` 标称“固定脚本，规则引用资源”，但**未登记**进 `00-编纂规则与格式规范/01-规则/脚本与命令/README.md`，也**无任何规则文件引用**（全库仅一处提及，在 `.workbuddy/memory/2026-09-11.md`）→ **违反 CLAUDE.md“固定脚本须由规则文件引用并在 README 索引登记”**。 |

---

## 一 目标与不变量

### 1.1 不变量（任何改动都不得破坏；每条对应既有门禁或新增门禁）

| # | 不变量 | 现有守卫 | 缺口 |
| --- | --- | --- | --- |
| I1 | 产物 = 四层源件的确定性装配结果（逐字节） | 第八件 `assemble_index.py --check` | 无 |
| I2 | 零外链 / 零 `@import` / 数据内嵌 / 品牌件 data URI | 第九件 D1 | 无 |
| I3 | 内嵌字体子集覆盖页面全部字符 | 第九件 B1–B4 | 无 |
| I4 | 口径（卷/章/节/溯源注）由内容源派生，五处一致 | 第七件 F 组 | 无 |
| I5 | 结构自洽（卷/章/节编号、述评恒末、三级结构、不设附录、比较节位次） | 第七件 A–O 组 | 无 |
| I6 | 页面 class ↔ CSS 选择器双向有定义 | 第七件 J 组 | 无 |
| I7 | 目录列表不可枚举、docroot 白名单 | **无** | **新增** |
| I8 | 夹具数值随内容源自动新鲜 | **无** | **新增** |

### 1.2 成功判据（全部可机检，不看主观感受）

1. `assemble_index.py --check` → 无漂移；
2. 九件门禁全绿；三套浏览器回归全绿；
3. `git ls-tree -r -l HEAD -- 重构2026` 体积 **≤ 10 MB**（现 32.12 MB）；
4. `curl -I http://127.0.0.1:<port>/` → 有 `Content-Encoding: gzip|br`、有 `X-Content-Type-Options`、无 `no-store`；
5. `curl http://127.0.0.1:<port>/data/` → **非 200**；
6. `curl http://127.0.0.1:<port>/index.html.bak-20260917` → **404**；
7. 新增门禁 `audit_fixture_freshness.py` 对“内容源改、夹具未改”注入缺陷**报 FAIL**（判据非空自检通过）；
8. 二次刷新 `index.html` → **304**；
9. 单次传输体积 ≤ 0.90 MiB（现 1.51 MiB）。

---

## 二 总览矩阵

| 面 | 条目数 | 确凿类 | 待测类 | 需裁定 |
| --- | ---: | ---: | ---: | ---: |
| A 版本控制与仓库治理 | 7 | 7 | 0 | 0 |
| B 目录组织重构 | 6 | 6 | 0 | 0 |
| C 服务器与传输层 | 9 | 9 | 0 | 0 |
| D 元数据与资源引用 | 7 | 5 | 0 | 2 |
| E 无障碍 | 6 | 5 | 1 | 0 |
| F 性能工程 | 7 | 0 | 7 | 0 |
| G CSS 架构 | 6 | 6 | 0 | 0 |
| H JS 架构 | 5 | 5 | 0 | 0 |
| I 测试与门禁体系 | 7 | 7 | 0 | 0 |
| J 文档与口径治理 | 5 | 5 | 0 | 0 |
| **合计** | **65** | **55** | **8** | **2** |

---

## 三 详案

## A 版本控制与仓库治理（7 条，全部确凿类）

### A1 `.gitignore` 增补备份/临时模式（P0）

现状：备份后缀**三套并存**（`.bak-` / `.prebak-` / `.bak_`），日期两种（`YYYYMMDD` / `YYYYMMDDHHMM`），扩展名三态（无 / `.html` / **双重扩展名 `.md.prebak-…`**），另有 `outline.txt.bak83`（**无日期**）→ **无单条 glob 能覆盖**，这正是 59 件 23.39 MB 混入索引的直接原因。

建议模式（覆盖全部现存形态，且不误伤源件）：

```gitignore
# 备份（统一前缀 + 无日期遗留）
*.prebak-*
*.bak-*
*.bak_*
*.bak[0-9]*
# 临时件
/08-核查报告与多轮复核/重构2026/_tmp_*
/08-核查报告与多轮复核/重构2026/script/_snapshot_*
# 例外：现行源件不在上列模式内（doc.css / doc.js / modern.css / page.template.html / outline.txt / index.html）
```

**验证**：`git check-ignore -v` 逐件抽样；并加**反向用例**——确认 `assets/doc.css`、`data/outline.txt`、`index.html` **未**被忽略。

### A2 已入库备份件出索引（P0）

`git rm --cached` 移除 59 件（**保留磁盘文件；不重写历史；不 rebase**）。
**前置**：确认无他会话在途改动（多会话共享工作树）；**提交路径限定**。
**预期**：HEAD 树 32.12 MB → 约 8.7 MB（−73%）。

### A3 备份命名规范化为单一形制（P1）

目标形制：`<原名>.<YYYYMMDDTHHMMSS>.bak`（ISO 8601 基本型；单一分隔符；**不重复扩展名**——`outline.txt.20260928T163500.bak` 而非 `outline.txt.prebak-…`）。
配套：备份统一落 `script/_bak/<YYYYMMDD>/`，不进交付树、不进 docroot。
**纪律**：改名不改内容；改名前后逐件 `sha256sum` 对照；改名清单留痕。
**注**：项目禁止自动化，故轮换为**脚本化、人工触发**（如 `script/_r66/_bak_rotate.py --keep 5 --dry-run`）。

### A4 `serve_refactor2026.py` 登记或退役（P0）

二选一（**须主理人择一，见 §六 裁定项 R3**）：
- **(a) 登记**：在 `脚本与命令/README.md` 索引表加一行（脚本 / 用途 / 引用规则），并在 `流程规则.md` 相应小节引用；
- **(b) 退役**：删除该脚本，改由统一的一份服务器承担（推荐，见 C1）。

### A5 单一服务器实现（P0，与 C1 合并执行）

现状：两份实现并存且**语义分叉**——端口 80 vs 8090、单线程 vs `ThreadingTCPServer`、`allow_reuse_address` False vs True、幂等守卫 vs 无。
**这正是项目自己警告过的“同一功能的第二份实现，且常缺后加的安全防护”**。保留一份，另一份删除并在留痕中写明理由。

### A6 仓库卫生：`.gitattributes` 加固（P1）

对 `08-核查报告与多轮复核/重构2026/**` 声明 `text eol=lf`，把“UTF-8 无 BOM、LF”从纪律升格为**版本控制层强制**（现仅靠脚本与门禁事后检查）。

### A7 `git log` 可读性（P2）

备份出索引后，`git log --name-only` 的判据面恢复清晰。补一条约定：**重构2026 目录内任何提交的 message 必须含 `[r2026]` 前缀**，便于 `git log --grep` 过滤（非强制钩子，属约定）。

---

## B 目录组织重构（6 条，全部确凿类）

### B1 三层分离：交付物 / 装配源 / 构建期数据（P1）

目标布局（**分五批迁移，每批单独全绿后提交**）：

```text
重构2026/
├─ deliverable/            # 服务器 docroot（白名单，仅此目录可被访问）
│   └─ index.html
├─ src/                    # 装配源（四层）
│   ├─ outline.txt                    # 内容层
│   ├─ doc.css  modern.css            # 格式层 / 现代化层
│   ├─ doc.js   theme-preset.js       # 行为层
│   ├─ page.template.html             # 页壳
│   └─ brand/logo.svg  favicon.ico    # 品牌派生件
├─ build/                  # 构建期数据（不进 docroot）
│   ├─ catalog.json  catalog.schema.json  schema.jsonld
│   ├─ font-source-cmap.txt  domains-skeleton.json
│   └─ tools/  → 软链或说明指向 脚本与命令/
├─ server/                 # 服务器（含 README）
├─ tests/                  # 正式套件
│   └─ _scratch/           # _probe_* / _*.log / _*.txt 中间件
├─ records/                # 0–83 号文、映射表、说明类 .md
└─ archive/                # 备份、快照、_prep_*（不进 docroot）
```

**耦合面实测（决定迁移成本）**：
- `重构2026/assets` → 3 个外部文件引用
- `重构2026/data` → 44 个（**其中绝大多数是历史 `.md` 快照，按“历史快照豁免”不改**）
- `重构2026/tests` → 12 个
- **活件耦合面**：`脚本与命令/` 内 **17 个脚本**提及 `重构2026`（其中装配/门禁/回归相关约 10 个需改路径常量）＋ `流程规则.md`（10 处）＋ `脚本与命令/README.md`（2 处）＋ `tests/README.md`。

**纪律**：每批迁移只动一类；**同批必须同步**：`assemble_index.py` 的 `BASE` 派生常量 → 九件门禁路径 → `tests/*.mjs` 的 `URL` 常量 → `tests/README.md` 夹具 → `流程规则.md` → `.gitignore` → 本目录 README。任一批未全绿即回滚该批。

### B2 构建期数据移出 docroot（P0，可先于 B1 单独做）

最小动作：`server` 的 docroot 收窄为**白名单只服务 `index.html`**（见 C4）。这样即使不做 B1，`catalog.json`（1.35 MB）、37 个 `outline.txt.bak_*`、`_prep_20260915/mapping_unresolved.duckdb`（536 KB）、102 个规划文档也**立即不可被局域网获取**。

### B3 一次性产物归档（P1）

移入 `archive/`（**不删**）：
- `_prep_20260915/`（1.2 MB，含 `__pycache__/`）
- `_tmp_behavior.js`（97,289 B）、`_tmp_script1.js`、`_tmp_script4.js`、5 个 `_tmp_font*.woff2`（1.8 MB）
- `script/_snapshot_pre_o2_20260913.html`（4.5 MB）、`script/_snapshot_pre_r4_20260912.html`（4.4 MB）
- 三处 `.mimosa/`（根 147 KB、`script/.mimosa/`、`tests/.mimosa/`）

**纪律**：先出清单、再提议、等确认；**绝不删除**（SOUL 铁律：不删用户的文件来“整理”）。

### B4 `tests/` 中间件隔离（P1）

正式件仅 5 个（`visual_regression.mjs`、`full_matrix_regression.mjs`、`fullsize_regression.mjs`、`tri_structure_negtest.py`、`README.md`）；其余 40 余个 `_probe_*.mjs` / `_*.txt` / `_*_run_*.log` 移入 `tests/_scratch/`。
**收益**：`tests/` 从“套件 + 考古层”变为“套件”；第 9 件门禁 E3 的判据面更清晰。

### B5 根目录编号文档归档（P1）

102 个编号 `.md` ＋ 12 个无编号 `.md` 移入 `records/`。
**例外**：`00-v3-方法论增强-新版编纂总纲.md` 被 `CLAUDE.md` 作为编纂基准引用 → 移动须同步改 CLAUDE.md。
**跳号与变体登记**：`58`、`76` 缺失，`01b`/`06a`/`31a`/`33a`/`34a` 为变体 → 按“编号缺口登记”规则补登记，**不重编号**。

### B6 空件与语义不明件处置（P2）

`_toc_full.md`（**0 字节**）确认后删除或补内容；`_既有缺陷清单.json`（159,688 B）、`_vol_lines.json`、`_index_fingerprint.json` 加日期前缀或移入 `records/`。

---

## C 服务器与传输层（9 条，全部确凿类）—— **本方案收益最高的一面**

### C1 重写为单一、自包含、无依赖的增强服务器（P0）

约束：**不得引入第三方依赖、不得编译、不得打包**（延续现有“无编译无打包”定位）；单文件 Python 标准库实现。

规格（可直接落地）：

```python
# 1) docroot 白名单：只服务显式清单
ALLOW = {"/", "/index.html"}
def _allowed(self, path):
    return path in ALLOW          # 其余一律 404，不做目录列表、不做前缀匹配

# 2) 目录列表闸死（覆盖父类行为）
def list_directory(self, path):
    self.send_error(403, "Forbidden")
    return None

# 3) 传输压缩：内存内 gzip（或预压 .gz 旁挂）
#    index.html 实测 gzip -6 = 890,469 B（−43.8%）；brotli -q11 = 847,304 B（−46.5%）
def end_headers(self):
    if self._gz and "gzip" in self.headers.get("Accept-Encoding", ""):
        self.send_header("Content-Encoding", "gzip")
        self.send_header("Vary", "Accept-Encoding")
    ...  # 安全头

# 4) 缓存语义：允许存储 + 强制再验证（父类 send_head 已支持 If-Modified-Since → 304）
CACHE = (("Cache-Control", "no-cache"), ("Pragma", "no-cache"))   # 去掉 no-store 与 Expires: 0

# 5) 安全响应头（补 62 号文 §7/§8 声明而现已失效者；HTTP 下 HSTS 不适用，不补）
SEC = (
    ("X-Content-Type-Options", "nosniff"),
    ("Referrer-Policy", "no-referrer"),
    ("X-Frame-Options", "DENY"),
    ("Permissions-Policy", "geolocation=(), microphone=(), camera=(), payment=(), usb=()"),
    ("Cross-Origin-Opener-Policy", "same-origin"),
    ("Cross-Origin-Resource-Policy", "same-origin"),
)
```

**判据**（全部可机检，见 §一 成功判据 4/5/6/8/9）。

### C2 gzip 传输（P0）

单次 1,583,076 B → 890,469 B（**−43.8%**，省 0.66 MiB）。**压缩在响应层，不触碰单体产物 → 不违红线。**

### C3 `no-cache` 取代 `no-store`（P0）

已核验 Python 3.14 `SimpleHTTPRequestHandler.send_head` **支持 `If-Modified-Since` → `HTTPStatus.NOT_MODIFIED`**；`no-store` 禁止存储 → 条件请求无从发起。
改后：磁盘未变 → **304，正文 0 字节**；`assemble_index.py` 重装配后 mtime 变 → 自动回 200，**新鲜度语义不变**。

### C4 docroot 白名单（P0）

局域网可及面 **311 文件 / 44 MB → 1 文件 / 1.5 MB**。

### C5 目录列表闸死（P0）

现状已核验：未重写 `list_directory`，而 `send_head` 在目录无 index 页时**调用它** → `/data/`、`/tests/`、`/script/`、`/_prep_20260915/` 可枚举。**与 README“不给目录列表”的声明直接矛盾**。

### C6 安全响应头补齐（P0）

补 `X-Content-Type-Options`、`Referrer-Policy`、`X-Frame-Options`、`Permissions-Policy`、COOP、CORP。
**说明**：`frame-ancestors` 经 meta 无效（62 号文已述），故 `X-Frame-Options` 是必要补充；HSTS 仅 HTTPS 有效，本服务为 HTTP，**不补并在 README 注明原因**。

### C7 `serve_index.py` 纳入版本控制（P0）

归位到 `脚本与命令/`（固定脚本）并登记，或在 `.gitignore` 加例外。**不得只靠 `git add -f` 绕过**（绕过即下次仍会漏）。

### C8 服务器契约测试（P0，新增第十一件门禁，见 I1）

### C9 服务器 README 重写（P1）

改正三处失实：①“不给目录列表”→ 实际开启；②“在端口 80 上对外提供 index.html”→ 实际提供整棵树；③硬编码 IP `192.168.5.4` 与网卡名“以太网 2”→ 改占位符 ＋ 查询方法。
补：HTTP 下 HSTS 不适用的说明；压缩与缓存语义的说明；停止方式改为**按 PID 精确停止**（现 `taskkill /F /IM pythonw.exe` 会误杀所有 `pythonw`）。

---

## D 元数据与资源引用（7 条，5 确凿 + 2 需裁定）

### D1 `link rel="icon"` 属性补全（P1）

`<link rel="icon" type="image/x-icon" sizes="16x16 32x32 48x48" href="…">`（favicon 实测含 16/32/48 三帧）。

### D2 `apple-touch-icon`（P2）

iOS 加书签/主屏需要。会增字节（须评估是否可接受）；如不可接受，**只在发布态注入**（见 D6）。

### D3 结构化数据增强（P2）

现有 JSON-LD 仅 `Book` ＋ 三项 `additionalProperty`。可增 `author`／`publisher`／`dateModified`／`hasPart`（卷级 `CreativeWork`）。
**注意**：会显著增字节，且对本地单文件无消费者 → **建议只在发布态注入**。

### D4 OG 完整集（**需裁定 R1**）

缺 `og:image`／`og:image:width`／`og:image:height`／`og:image:alt`／`og:url`／`og:site_name`；Twitter 仅 `summary`（建议 `summary_large_image` ＋ `twitter:title/description/image`）。
**裁定点**：`og:image` 规范要求**绝对 HTTPS URL**（多数平台忽略相对路径与 HTTP）。本页为本地单文件 ＋ 局域网 HTTP，**不存在合规取值**；且新增图片引用会触碰零外链红线。

### D5 `canonical`（**需裁定 R1**，同 D4）

### D6 “发布态注入”机制（P2，**本方案的结构性建议**）

新增装配档：`assemble_index.py --release --origin=https://…`，在**不改单体源**的前提下，于产物中注入 `og:url`／`canonical`／`og:image` 等**仅发布态成立**的元数据。
好处：本地单文件交付物保持零外链；发布态获得完整社交卡片。**代价**：产物不再逐字节唯一 → 第八件门禁须支持 `--profile`（默认 `local`，与现行判据一致；`release` 档单独判）。
**须主理人裁定**：是否接受“产物分档”。

### D7 CSP nonce 处置（P2，**建议维持并记录理由**）

`nonce="Zk8rN2fT9qPm5vLx1wJh"` 固定字面量（产物 5 处，且写在源件 `page.template.html`）。规范要求每响应不可预测。
**判断**：本页威胁模型为“本地单文件、`default-src 'none'`、零网络、零外链、零用户输入、内容全作者受控”→ 固定 nonce 无实际风险；改为每响应随机**会破坏 I1“产物 = 源件装配结果”的逐字节可核验性**（第八件门禁的判据基础）。
**建议**：维持现状，并在 `流程规则.md` 记录理由（把“未改”从遗忘变成决定）。

---

## E 无障碍（6 条）

### E1 局部语言标记（P1，确凿类但触内容源语法）

现状：全页仅 1 处 `lang`（`<html lang="zh-Hans">`）；英文术语（BSD / FreeBSD / sendfile / POSIX / CSRG / DARPA…）未标 `lang="en"` → **WCAG 2.1 AA 3.1.2 不满足**（W3C WAI：与页面默认语言不同的语段**必须**标 `lang`）。

**两条路径**：
- **路径 A（完整）**：内容源引入语言标记语法（如 `@@en:…@@`）→ `parse_outline` 输出 `<span lang="en">`。
- **路径 B（最小）**：仅对**固定的英文缩写/术语**在渲染层包裹（须维护术语表）。
**推荐 A**：一次做对，且与既有 `@@` 定界语法同族。**代价**：触及内容源语法 → 属结构变动，须走完整流程并同步 `tests/README.md` 夹具纪律。

### E2 `aria-current` 补全（P2）

现 2 处。TOC 当前卷/章/节、面包屑当前项均宜标 `aria-current="true"`（或 `location`／`page`）。

### E3 `aria-live` 复核（P2）

现 1 处（检索结果）。复核“动态结果应有 live、静态导航不应有”的既有结论是否仍成立。

### E4 键盘契约扩展（P2）

`role="toolbar"` 未声明 `aria-orientation`；`#exportMenu`／`#fontMenu` 方向键契约已在 2026-09-19 审计中处置 → **复核回归是否仍在**（判据：聚焦首项后按 `ArrowDown` 焦点须移动）。

### E5 自动化无障碍门禁（P1，**本方案的重点新增**）

新增第十二件门禁：`axe-core` 静态/无头扫描（`@axe-core/playwright` 或 `axe-core` ＋ Playwright）。
- **对象**：桌面 1920×1080 / 手机 390×844 × light/dark 四组合；
- **判据**：`violations` 中 `impact ∈ {critical, serious}` 数 = 0；`moderate` 记 INFO 不 FAIL（避免噪声）；
- **判据非空自检**：构造注入缺陷页（去掉 `alt`、去掉 `lang`、加空按钮）须报 FAIL。
**注意**：本页零 `style=`、零 `on*=`、`img` 有 `alt`、静态按钮 `aria-label` 全覆盖，预期首轮即接近全绿——**正因如此才需要自动化**：人工审计已到收益递减点。

### E6 对照度与强制色复核（P2）

`modern.css` 已有 `forced-colors` 与 `prefers-contrast: more` 分支（各 1 处）。**休眠分支必须实测**——用 Playwright `emulateMedia({forcedColors:'active'})` / `{contrast:'more'}` 各跑一次，确认非空转。

---

## F 性能工程（7 条，**全部待测类**）

> **本面总纪律**：先建测量装置（已有 `_perf_bench.mjs`：交错 A/B × N=10 × 中位/IQR × `Tracing` 事件计数为主判据 × A-vs-A 自检），再逐条测。**任何一条效应量小于噪声带即回滚并判“不可验证”。**

### F1 `content-visibility: auto`（待测）

**现状**：`doc.js:293` 有探针（`CSS.supports('content-visibility: auto')` → 临时置 `visible` 测高 → 还原），但 `doc.css`／`modern.css` **零处声明该属性** → **该分支从未执行**。
**已知三根因**（历史记录）：跳过态子树 `offsetTop` 不可靠；须联动 `rebuildOffsets`／`j`·`k` 跳章／抽屉点击；`rebuildOffsets` 读 `offsetTop`／`getBoundingClientRect` 属**强制渲染 API**（会破坏跳过）。
**参考**：web.dev 对同类分块页面实测 232 ms → 30 ms（7×），但官方同时列出三坑：滚动条跳动（须配 `contain-intrinsic-size`，推荐 `auto` 关键字）、强制渲染 API、离屏地标元素需补 `aria-hidden`。
**必测项**：①首屏（冷启动）；②滚动遍历；③TOC 跟随正确性；④`j`/`k` 跳章落点；⑤抽屉点击落点；⑥`Layout`/`UpdateLayoutTree` 计数。

### F2 `updateCurrentChapter` 用缓存（待测）

既有实测 160 ms **未使用已缓存的 `chTops`** → 每步重新线性扫描。**对首屏无影响**，仅滚动期。

### F3 `scrollIntoView` + `findScrollParent`（待测）

既有实测占滚动场景 33%（458 ms）。改进方向：改用 `scrollTop` 直接计算（避免 `findScrollParent` 的逐级 `getBoundingClientRect`）。

### F4 首次几何采集延后（**已有负结果，勿重复**）

2026-09-19 曾实施“进度条 `max` 缓存 / `rebuildOffsets` 批量读写 / 首次几何采集延后双 rAF / 字号 margin 缓存”→ **A/B 实测无可信收益，已全部回滚**（提交 `040b5056f`）。**不得重复尝试同一批改动。**

### F5 数据层首屏（**已完成，留档**）

“DATA JSON script 化 ＋ Compression Streams 瘦身”已落地（现 blob 334,228 B）。留档以免重复立项。

### F6 字体字节（**红线，不做**）

字体 base64 609,648 B 占全页 38.5%；data URL 不可独立缓存、base64 膨胀约 33%（MDN）。**按红线只作事实记录。**

### F7 首屏渲染阻塞（**结论性事实**）

全部 CSS（646 KB）内联 `<head>` → 必须收完 1.51 MiB 才首绘。这是单体形态的**固有代价**；在红线内**唯一可动的杠杆是传输层**（已由 C2/C3 覆盖）。

---

## G CSS 架构（6 条，全部确凿类）

### G1 引入 `@layer` 显式化级联顺序（P1，**本面最高价值项**）

现状：`doc.css` 首行自述“按级联序合并自 **5 个历史 style 块**”，但段注释只剩 `1`、`5`、`10`–`13`（缺 2–4、6–9）→ **级联顺序成为隐性契约**；实测 **45 个选择器跨块重复**（`.doc-page` ×7、`.toc-left`/`.toc-right` 各 ×6、`:root` ×5、`.doc-metrics` ×5 …），`@layer` 计数 **0**。
**建议**：
1. 先从 `index.html` 的 git 历史（`git log -p --follow -- …/index.html`）**考古恢复 5 块原始边界**（现存的 Sep-12 快照已只剩 1 块，故须回 git 历史）；
2. 按块声明层序：`@layer base, layout, components, patches, theme;`（具体层名依考古结果定）；
3. 把 `doc.css` 各段包进对应层，`modern.css` 独立层（保证覆盖 `doc.css`）。
**收益**：把“靠声明顺序”的隐性契约变成“靠层序”的显性契约；后续新增补丁不再需要“必须在文件末尾”这种口耳相传的规则。
**风险**：`@layer` 会改变既有优先级语义（层内 vs 未分层）→ **必须**三套浏览器回归 ＋ 视觉回归全绿；建议**先做只读的层序模拟**（不改盘，用 `--path` 对备份件跑结构门禁）再落地。
**验证**：第 9 件门禁 J 组（class ↔ 选择器）+ 视觉回归几何断言。

### G2 断点接缝集中化（P1）

实测接缝重复次数：

| 接缝 | `doc.css` | `modern.css` | `doc.js` | `tests/` |
| --- | ---: | ---: | ---: | ---: |
| `820px` | 5 | 2 | 1 | 0 |
| `821px` | 4 | 1 | 0 | 0 |
| `1099px` | 2 | 0 | 0 | 0 |
| `1100px` | 4 | 0 | 0 | 1 |

共 **10 个断点**、**24 个 `@media` 块**。改一次抽屉断点要动 **8 处以上**（且 `tests/README.md` 已列明“改顶栏控件尺寸后须同步 T15/T16 判据”——即**还要动测试**）。
**建议**：在 `doc.css` 顶部单点声明（CSS 无自定义媒体查询，可用注释区块 ＋ 约定 `/* @breakpoint: drawer 820 */`），并写一个**静态门禁**核验“全树出现的断点值 ⊆ 声明集”。

### G3 `@media print` 合并（P2）

现 2 块（992 行、1211 行），规则有重叠（`.theme-toggle`／`.toc-toggle`／`.back-to-top` 在两块均出现）。合并为 1 块并去重。

### G4 自定义属性归并（P2）

46 处声明 / 23 个唯一名 → 每个约声明 2 次（light/dark 各一），结构合理。**建议**：把 dark 覆盖集中到单个 `html[data-theme="dark"]` 块，避免散落（实测 `html[data-theme="dark"]` 跨块出现 ×2）。

### G5 `color-mix` 层序兜底复核（P2）

`doc.css` 中 `color-mix` 仅 2 处，`@supports` 0 处；既有结论“关键属性有层序兜底（焦点环不会在旧浏览器消失）”→ **复核该结论在 `@layer` 化后仍成立**。

### G6 死规则（**负结果，不做**）

**实测 0 条**（272 个去重选择器全部有宿主）。**不做清理**——无对象可清。首版报告的 65 条为判据过窄所致，已勘误。

---

## H JS 架构（5 条，全部确凿类）

### H1 源件拆分（P1）

现状：`doc.js` **2,077 行 / 102,118 B**，**131 个 `(function` 分块**、274 个 `function` 声明、74 个 `addEventListener`、35 个 `querySelectorAll`、28 个 `innerHTML`。
**建议**：把 `doc.js` 拆为 `src/js/*.js`（按分块主题：toc / search / panels / graph / timeline / export / theme / a11y…），由 `assemble_index.py` **按固定顺序拼接**为 `assets/doc.js`（保持单一写者与逐字节可核验）。
**收益**：①单文件可读性从“2,077 行滚动”变为“按主题定位”；②分块函数作用域问题（Annex B 依赖、严格模式破坏点）在拆分后**自然消解**——跨块引用变成模块间引用，编译期即可发现。
**代价**：装配器新增一个合并步骤（`page.template.html` 的 `{{JS_BEHAVIOR}}` 由“读单文件”改为“按清单拼接”），须同步第八件门禁与第九件 A 层源件清单。

### H2 跨块函数可见性门禁（P1）

现状：既有教训——严格模式使块内函数声明变块级作用域，曾致“人物卡浮层／时间线视图／修订差异视图”**三个功能同时失效**；检测工具 `_scan_blockfn_scope.py` 已存在但**未入门禁**。
**建议**：把该扫描器升格为第十三件门禁（判据：块内 `function` 声明若被块外引用即 FAIL）。**收益**：把一次性教训变成常备护栏。

### H3 `innerHTML` 审计面固化（P2）

28 处 `innerHTML`（均经 `ttt()` 净化）。**建议**：新增门禁断言“产物中 `innerHTML` 赋值必须出现在 `ttt(`／`__LB.ttt(` 上下文内”，把“都净化过”从人工结论变成机检不变量。
**注意**：Trusted Types 强制已实测为**负结果**（DOMParser 本身是 TT sink，强制会连净化器一起拦下 → 1,104 处 CSP 违规），**不得重复尝试**。

### H4 `var` → 现代化（P2，**建议保守**）

实测 `var` 423 / `let` 12 / `const` 64。既有结论：“`var`→`const` 全量改写属纯风格，TDZ 风险不在现有测试覆盖面内，收益有限”→ **不做全量改写**。
**替代**：只对 H1 拆分后**新模块的顶层**使用 `const`，存量不动。

### H5 死代码清理（P2）

`doc.js:1293` `var LABEL_W_UNUSED = 0;`（注释自称预留，布局不依赖）；`content-visibility` 探针（见 F1，**在 F1 定案前不得删**——它是 F1 的载体）。

---

## I 测试与门禁体系（7 条，全部确凿类）

> **本面是本方案的“复利面”**：每加一件门禁，都会在未来每一次改动上持续收费。

### I1 第十一件：服务器契约门禁（P0）

`audit_server_contract.py`：
- 启动临时服务器（**绑定 127.0.0.1 ＋ 高位端口**，不得绑 `0.0.0.0`、不得用 80）→ 逐项断言：
  1. `/` 200 且 `Content-Encoding` ∈ {gzip, br}（当 `Accept-Encoding` 提供时）；
  2. `Cache-Control` **不含** `no-store`；
  3. 二次请求带 `If-Modified-Since` → **304**；
  4. `/data/`、`/tests/`、`/script/` → **非 200**；
  5. `index.html.bak-20260917`、`data/outline.txt.bak83` → **404**；
  6. 响应头含 `X-Content-Type-Options`、`Referrer-Policy`、`X-Frame-Options`；
  7. `../` 与 `%2e%2e%2f` → 404。
- **判据非空自检**：对**修复前**的 `server/serve_index.py` 跑同一套断言 → 至少 4 项 FAIL。
- **依赖缺失**（无可用端口）→ exit 2。

### I2 第十二件：无障碍门禁（P1）

见 E5（axe-core，四组合，critical/serious = 0）。

### I3 第十三件：跨块作用域门禁（P1）

见 H2（`_scan_blockfn_scope.py` 升格；**必须同时匹配“调用”与“以值引用”两种形态**——`.map(fn)`／`forEach(fn)`／`addEventListener(…, fn)`，本页 `personCard` 曾因此漏检）。

### I4 第十四件：夹具新鲜度门禁（P1，**补 I8 缺口**）

`audit_fixture_freshness.py`：
- 从 `data/outline.txt` **派生**真值：口径串（卷/章/节）、溯源注计数、卷题分隔符形态、节题最长值；
- 与 `tests/*.mjs` 内写死值逐项比对；不一致即 FAIL。
- 实测耦合点：口径串 `43 卷 412 章 3435 节` 写死在 **4 处**（`full_matrix_regression.mjs:87/215`、`visual_regression.mjs:447`、另 1 处），溯源注 `注 537` 写死在 **1 处**。
- **收益**：把“人记”变“机检”。现状是第 9 件门禁 E3 只验**编号集**吻合，**不验数值新鲜度** → 内容源一变即静默陈旧。
- **判据非空自检**：对一份“改了内容源但未改夹具”的副本须报 FAIL。

### I5 第十五件：断点声明集门禁（P2）

见 G2（全树断点值 ⊆ 声明集）。

### I6 门禁元门禁（P1，**本方案的结构性建议**）

现状：门禁已达 **12 件**（九件命令行 ＋ 三套浏览器），且“工具已文档化 ≠ 工具已生效”的教训已发生过两次（`markdownlint-cli2` 长期未接入；`_scan_blockfn_scope.py` 未升格）。
**建议**：新增 `audit_gate_registry.py`——
- 维护**门禁登记表**（`脚本与命令/README.md` 或专表）：门禁名 / 触发条件 / 对象面 / 判据非空自检命令 / 上次实测日期；
- 断言：①登记表内每件门禁脚本**存在**；②每件门禁**可执行且自检通过**；③`流程规则.md`／`CLAUDE.md` 中声明的门禁件数与登记表**一致**；④**任何 `脚本与命令/*.py` 若名字匹配 `audit_*` 但不在登记表内 → WARN**（防“写了门禁却忘了接线”）。
- **判据非空自检**：注入一个假门禁条目（不存在的脚本）须报 FAIL。

### I7 判据非空纪律固化（P1）

既有教训已多次：“判据存在 ≠ 判据有效”“报 0 前须证明分支执行过”“判据真值不得取被测对象自身”（T7a 假绿实例）。
**建议**：把三条写成 `脚本与命令/README.md` 的**门禁开发必读**小节，并要求**每件新门禁必须附 `--selftest`**（本方案 I1–I6 均已含自检规格）。

---

## J 文档与口径治理（5 条，全部确凿类）

### J1 `52-重构2026迁移规格书.md` 口径统一（P1）

实测**同一文件内并存三套口径**：头部与 §一“37 卷 352 章 3023 节”、§一任务定义“43 卷 412 章 3435 节”、§3.2 目标表“26 卷 242 章 1730 节”。
**处置**：现行口径统一为 `index.html` doc-metrics（**唯一权威**）；历史口径加“历史”标注并按“历史记录不追改”保留。

### J2 `62-单体HTML安全加固登记.md` §7/§8 修正（P1）

按勘误 1：`serve_https.py` 不存在；现有两份服务器**均未实现**所述头。
**处置**：改注“本节所述头随 `serve_https.py` 退役而失效；现行实现见 C1，待补”，或**先补实现（C6）再回填本节**。推荐后者（先做后写，避免二次漂移）。

### J3 `CLAUDE.md` 正文段口径（P2）

正文段仍写“37 卷 352 章 3023 节”，与自动维护的口径基准块（43 卷 412 章 3435 节）不一致。
**处置**：正文段的现行声明改为指向基准块（避免手写数字），历史沿革保留。

### J4 `server/README.md` 重写（P1）

见 C9（三处失实 ＋ 停止方式 ＋ 环境事实）。

### J5 周边文件联动清单化（P1）

“目录页更新总则”已要求“联动更新周边文件”，但**未列清单** → 靠人记。
**建议**：在 `流程规则.md` 该条下补**显式清单**（本次实测的完整联动面）：`CLAUDE.md`／`流程规则.md`／`脚本与命令/README.md`／`tests/README.md`／`tests/*.mjs` 夹具／`重构2026/*.md` 口径声明／`server/README.md`／`12-重构大纲书目述评/index.md`。
并纳入 I4（夹具新鲜度）与 I6（门禁登记）的机检范围。

---

## 四 波次编排

> **纪律**：每波结束必须“装配 → 九件门禁 → 三套浏览器回归 → **路径限定提交**”全绿；**多轮迭代批次在首轮可交付状态即提交**（防兜底提交裹挟）。项目**禁止自动化**，全部人工触发。

| 波 | 主题 | 条目 | 触及产物 | 风险 |
| --- | --- | --- | --- | --- |
| **Wave 0** | 只建测量与护栏（**不改行为**） | I1／I3／I4／I6／I7 骨架 ＋ A1/A2 的 dry-run | 否 | 极低 |
| **Wave 1** | 服务器层（收益最高、与产物解耦） | C1–C9 ＋ A4/A5 ＋ J4 | **否** | 低（可逐项回滚） |
| **Wave 2** | 版本控制与仓库治理 | A1–A3 ＋ A6/A7 | 否（仅索引） | 低 |
| **Wave 3** | 元数据与无障碍 | D1／D2 ＋ E1–E6 ＋ I2 | **是** | 中（须完整门禁链） |
| **Wave 4** | CSS 架构 | G1–G6 | **是** | 中高（级联语义） |
| **Wave 5** | JS 架构 | H1–H5 | **是** | 中高（拆分改动面大） |
| **Wave 6** | 目录重组 | B1–B6 | 否（路径） | 高（耦合面 ~59 文件） |
| **待定** | 性能 | F1–F3（须先测噪声带） | **是** | 视实测 |

**说明**：把 Wave 1／2 放在最前，因为它们**收益确定、不触碰产物、可逐项回滚**；Wave 6（目录重组）放最后，因为它的价值（可读性/边界）不如前几波紧迫，而耦合面最大。

---

## 五 新增护栏规格汇总

| 件 | 脚本 | 对象面 | 核心判据 | 自检 |
| --- | --- | --- | --- | --- |
| 第十一件 | `audit_server_contract.py` | 服务器响应 | 压缩／缓存／白名单／目录列表／安全头 7 项 | 对修复前实现 ≥4 项 FAIL |
| 第十二件 | `audit_a11y_axe.py` | 产物（浏览器） | critical/serious 违规 = 0（4 组合） | 注入缺陷页须 FAIL |
| 第十三件 | `audit_blockfn_scope.py` | `doc.js` 源 | 块内函数被块外引用即 FAIL | 对历史缺陷版须 FAIL |
| 第十四件 | `audit_fixture_freshness.py` | `tests/*.mjs` | 夹具值 vs 内容源派生值 | 改源未改夹具须 FAIL |
| 第十五件 | `audit_breakpoint_registry.py` | CSS 全树 | 断点值 ⊆ 声明集 | 注入野断点须 FAIL |
| 第十六件 | `audit_gate_registry.py` | 门禁体系自身 | 登记 ↔ 实况 ↔ 文档三方一致 | 注入假条目须 FAIL |

**注**：新增 6 件后，常备门禁从 **12 件 → 18 件**。须同步更新 `tests/README.md`“配套门禁”节与 `流程规则.md`／`CLAUDE.md` 的件数声明（**这正是 I6 要机检的项**）。

---

## 六 需主理人裁定（红线相关，3 项）

| # | 裁定项 | 选项 | 影响 |
| --- | --- | --- | --- |
| **R1** | 是否引入“发布态”元数据（OG 完整集 ＋ canonical ＋ `og:image`） | (a) 不做（本地单文件无合规 `og:image`）｜(b) 加 `--release` 档，发布态注入（产物分档） | 选 (b) 则第八件门禁须支持 `--profile`，且“产物逐字节唯一”不再成立 |
| **R2** | 局部语言标记的实现路径（E1） | (a) 内容源语法扩展（完整、一次性）｜(b) 渲染层术语表包裹（最小、不触语法） | 选 (a) 触 `parse_outline`，属结构变动 |
| **R3** | 服务器脚本归一（A4/A5） | (a) 保留 `serve_refactor2026.py`（8090，多线程）｜(b) 保留 `server/serve_index.py`（80，单线程幂等）｜(c) 新写 C1 版并退役两者 | 建议 (c)：现有两者**均缺压缩、均缺安全头、均开目录列表**，改造量与新写相当 |

**〔注（2026-10-12，140 批修订）：R1 经 139 批注销、140 批部分修订**（主理人指正“新增图片引用会触碰零外链红线，但是图片可以 base64 离线”）。修订后分态：①**og:image（base64 data URI 形态）＋ og:image:width/height/alt ＋ og:site_name ＋ twitter:card/twitter:image（均 inline meta）＝复活为可执行项**——meta content 属性不触第九件 D1 四正则（src=／href=／url()／@import；合成用例实证 0 命中），data URI 内联不违零外链红线（功能注记：多数社交平台爬虫忽略 data URI，社交卡片实效有限；offline／归档消费者可读）；②**canonical 维持注销**（link href 直触 D1，实证 FAIL）；③**og:url 维持不做**（origin 依赖，本地单文件无合规取值——与红线无关的功能性理由）；④**--release 分档（D6）维持注销**（破坏“产物逐字节唯一”）；⑤**D3 维持注销**（价值裁定，与红线无关）。og:image 施工待点名（实施门槛见 140 批执行记录）。**〕**

**另需注意（非裁定，属告知）**：Wave 6 目录重组会改动 `assemble_index.py` 等约 10 个活件脚本的路径常量与 `流程规则.md` 10 处引用；若主理人认为收益不足，可只做 **B2（docroot 白名单）＋ B3（一次性产物归档）**，跳过 B1。

---

## 七 明确不做（红线与既有负结果）

| 项 | 理由 |
| --- | --- |
| `@font-face`／`font-family` 栈／字体交付方式／`unicode-range` 分片 | **红线**（主理人明令不允许修改既有字体） |
| base64 膨胀 33%、不可跨页缓存 | **红线**内只作事实记录 |
| 零外链／零 `@import`／零 CDN／数据内嵌／品牌件 data URI | **红线** |
| 压缩 `doc.js`／折叠正文 HTML／产物 minify | 破坏按行解析门禁与 A2 空格形制判据 |
| 固定 nonce 改随机（D7） | 破坏 I1 逐字节可核验性 |
| Trusted Types 强制 | **实测负结果**（DOMParser 本身是 TT sink → 1,104 处 CSP 违规） |
| F4 那批几何/缓存微优化 | **实测负结果，已回滚**（提交 `040b5056f`） |
| `var` → `const` 全量改写 | 纯风格，TDZ 风险不在测试覆盖面内 |
| CSS 死规则清理 | **实测 0 条**，无对象 |
| 创建定时任务/自动化 | **项目明令禁止** |

---

## 八 度量与验收

### 8.1 可机检的量化目标

| 指标 | 现状 | 目标 | 判据来源 |
| --- | ---: | ---: | --- |
| HEAD 树体积 | 32.12 MB / 223 文件 | **≤ 10 MB** | `git ls-tree -r -l HEAD` |
| 工作树备份/临时占比 | 75%（33.2 MB / 44 MB） | **≤ 25%** | `du -sh` 分项 |
| 局域网可及文件数 | 311 | **1** | `curl` 逐路径 |
| 单次传输字节 | 1,583,076 | **≤ 943,718（0.90 MiB）** | `curl -w '%{size_download}'` |
| 二次加载字节 | 1,583,076 | **0（304）** | `curl -H 'If-Modified-Since: …'` |
| 门禁件数 | 12 | 18（含 6 件新增） | `audit_gate_registry.py` |
| 夹具写死值处数 | 5（口径 4 ＋ 注 1） | **0（全部派生）** | `audit_fixture_freshness.py` |
| 目录列表可枚举 | 是 | **否** | `curl /data/` |
| 安全响应头 | 0 项 | 6 项 | `curl -I` |
| WCAG 3.1.2 | 不满足 | 满足 | axe-core ＋ 人工抽检 |

### 8.2 性能类验收（F 面）

- 装置：`_perf_bench.mjs`（交错 A/B × N=10 × 中位/IQR × `Tracing` `Layout`/`UpdateLayoutTree` 计数 × **A-vs-A 自检**）；
- **符号检验须剔除并列对**（`LayoutCount` 常大量并列；把 `b==a` 计入会令同一文件对自身也报“显著更优”）；`eff<8` 报“样本不足”，改用中位差的分位数区间；
- 结论只能是三种之一：**B 优**／**A 优**／**不可判定**。**“不可判定”即为最终结论，不得改写为“略有改善”。**

---

## 九 风险登记

| # | 风险 | 触发条件 | 缓解 |
| --- | --- | --- | --- |
| 1 | **兜底提交裹挟** | 多轮迭代暴露窗口过长，他会话兜底提交裹挟 | 每波**首轮可交付状态即路径限定提交**；被裹挟后**不改写历史** |
| 2 | 路径迁移破坏门禁 | Wave 6 改路径未同步全部消费者 | 分批迁移；每批全绿才进下一批；`audit_gate_registry` 兜底 |
| 3 | `@layer` 改变级联语义 | Wave 4 落地 | 先只读模拟（`--path` 对备份件跑结构门禁）；三套浏览器 ＋ 视觉回归全绿 |
| 4 | `doc.js` 拆分引入跨模块引用错 | Wave 5 | 拆分后先跑 I3（跨块作用域门禁）＋ 三套回归 |
| 5 | 服务器改造引入回归 | Wave 1 | I1 契约门禁 7 项 ＋ 对旧实现负向自检 |
| 6 | `git rm --cached` 误伤 | Wave 2 | 只 `--cached`（不动磁盘）；逐件 `git check-ignore` 复核；反向确认源件未被忽略 |
| 7 | 内容源语法扩展（E1/R2a）破坏既有解析 | Wave 3 | 先在 `outline.txt` 副本上跑解析往返（回环检查），0 差异再落盘 |
| 8 | 文档口径二次漂移 | J 面 | J2 采“先做后写”；J5 把联动清单机检化（I4/I6） |

---

## 十 一页速览

**本方案 65 条：55 条确凿类（判据可机检，直接做）、8 条待测类（先建测量装置）、2 条需裁定。**

**优先级排序（按“收益 ÷ 风险”）**：

1. **服务器层**（C1–C9）：单次传输 −43.8%、二次加载 −100%、暴露面 311→1 文件、恢复 6 项安全头、关目录列表、消灭双实现。**与产物完全解耦，可逐项回滚。**
2. **版本控制治理**（A1–A2）：仓库 −73%（32.12 MB → 8.7 MB）。
3. **测试与门禁复利**（I1–I7）：6 件新门禁，把已有的一次性教训变成常备护栏；其中 I4（夹具新鲜度）与 I6（门禁登记）直接补两个已存在的结构性缺口。
4. **元数据与无障碍**（D/E）：WCAG 2.1 AA 3.1.2 合规；axe-core 门禁。
5. **CSS/JS 架构**（G/H）：`@layer` 显式化级联、断点集中化、`doc.js` 源件拆分——**长期可维护性的主投入**。
6. **性能**（F）：**只在建好测量装置后**逐条试；三条候选（`content-visibility`／`updateCurrentChapter` 缓存／滚动路径）任一“不可验证”即回滚。
7. **目录重组**（B）：收益是边界清晰，耦合面最大 → 放最后；可只做 B2/B3。

**三条勘误已并入正文**：① 服务器为**两份**实现（均无安全头）② CSS 死规则**实测 0 条**（上轮 65 条为误报）③ `serve_refactor2026.py` **未按固定脚本规则登记**。
