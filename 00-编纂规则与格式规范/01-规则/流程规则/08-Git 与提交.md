# 流程规则·08-Git 与提交

> 本件为《流程规则》分册（2026-10-27 ykla 令按主题拆分；原文 2 574 行 62 节）。判据正文以下列各节为准；总索引见同目录 `00-索引.md`。

## Git 克隆目录与更新规则

本节为 git 仓库克隆的存放位置、更新流程与去重约束（因增量更新时在 `script/` 下重复克隆既有仓库而确立）。

**克隆存放位置**：所有 git 仓库克隆统一存放于 `03-原始史料库/01-代码仓库史料/<项目目录>/` 下，与对应 SQLite 数据库同目录层级（如 `09-Darwin/xnu/`、`02-FreeBSD/freebsd-src/`）。克隆目录名应与 `repos` 表的 `repo_name` 字段一致，以便脚本自动定位。

**强制使用 tree:0 过滤器（仅提交信息）**：所有 git 克隆操作**应**使用 `--filter=tree:0`（仅获取 commit 对象，不传输 tree/blob 对象）。`git log` 元数据（作者、日期、消息、父提交）完整可用，但 `--numstat`/`--name-status` 不可用——即 commit_files 表无法从此克隆填充，只有 commits 表可更新。此规则适用于全部仓库，无论大小，永不例外。理由：① 全量克隆（如 linux-kernel ~8.2 GB）在代理环境下持续 TLS 截断；② 提交信息是史料考据的核心需求，文件变更细节可从数据库已有存量 + 未来专项补抽获取；③ 磁盘占用与传输耗时最小化。

**已有克隆清单**：截至 2026-08-25，全部 66 仓库已通过 tree:0 方式克隆至对应项目目录下。Darwin 项目下 42 个 apple-oss-distributions 仓库为既有工作克隆（含 `.git` 子目录），其余 24 仓库为 bare tree:0 克隆（`<repo>.git` 目录）。

**不应重复克隆**：`script/` 目录不应存放任何 git 克隆（属临时文件区，非长期留存位置）；任何 git 克隆操作优先检查 `03-原始史料库/01-代码仓库史料/` 下是否已有同名克隆，已存在则直接复用，不应在 `script/` 或其他目录重复克隆。

**增量更新完整 8 步流程**（执行脚本 `00-编纂规则与格式规范/01-规则/脚本与命令/git_update_duckdb_20260818.py`，写入目标为 DuckDB 主库 `duckdb/<db_name>.duckdb`。**🟡 2026-10-17 路径订正**：本条原写作 `script/git_update_duckdb_20260818.py`；该脚本 2026-09-18 随规则目录整体入库，`script/` 下早已无此文件——属“活规则＋死路径”缺口，现订正。`AGENTS.md`“Git 克隆目录与更新规则”同条已同步订正）：

1. **克隆（tree:0）**：`git clone --bare --single-branch --filter=tree:0 <url> <目标目录>`——仅传输 commit 对象（约全量 5%），磁盘占用极小（linux-kernel 2.5 GB→~200 MB，netbsd-src 74 MB）。如已有克隆则跳过此步直接复用。**Darwin 例外**：42 个既有工作克隆不含 tree:0 过滤，直接 `git fetch --tags` 拉取增量。

2. **门禁（哈希可达性）**：`git cat-file -e <库内最新已知 commit_hash>^{commit}`——验证库内最新哈希在新克隆中。通过 → 进入步骤 3；失败 → 进入锚点降级。

3. **锚点降级**（门禁失败时）：从 DuckDB 查询 `SELECT commit_hash, committer_date FROM commits WHERE repo_name=? ORDER BY committer_date DESC LIMIT 300`，逐条 `git cat-file -e` 探测，找到第一个可达哈希作为增量边界。典型场景：上游镜像分支重写导致最新哈希不在克隆中（如 hardenedbsd-src 降级至 2026-04-20）。若 300 条均不可达且仓库不在白名单（`REINGEST_ALLOW`），则报错退出。

4. **全量重灌**（白名单仓库锚点全不可达时）：情况 A——克隆 ≤2000 提交且 ≥ 存量一半（Apple 小库重写/清理引用，如 darwin 42 仓库）；情况 B——白名单仓库（上游镜像整体重建，如 trueos-src、netbsd-src）。执行 `DELETE FROM commits WHERE repo_name=?` 清空该 repo 存量后，按 `--all` 全量重灌。

5. **增量候选计算**：`git rev-list --all --since=<boundary-7天>` 获取候选哈希集合，减去 DuckDB 已有哈希（`SELECT commit_hash FROM commits WHERE repo_name=?`）得到真正新增。

6. **解析提交元数据**：`git -c core.quotepath=false log --all --since=<boundary> --date=iso-strict --pretty=format:<分隔符模板>` 一次遍历提取 12 字段：commit_hash、author_name/email/date、committer_name/email/date、message_subject、message_body、parent_hashes、signed_off_by（多签以 `,` 加空格连接）。分隔符：`\x01` 切 block，`\x02` 切字段。

7. **去重写入 DuckDB**：`rows = [r for r in rows if r[0] not in existing]`（用步骤 5 的已有哈希集合过滤），`BEGIN TRANSACTION` → `INSERT INTO commits (...) VALUES (...)` → `COMMIT`。**2.0.0 能力前提（2026-10-24 实测）**：`ALTER TABLE … ADD UNIQUE` 已支持，`INSERT OR IGNORE` 仅在目标表具备 UNIQUE／PRIMARY KEY 约束时可用；`commits` 表现状无唯一约束，故去重仍走应用层反连接。“1.5.5 不支持”的旧表述已废止。要改成约束式写入，应先测存量重复、补约束并走 ADR，不应直接改代码。最后 `UPDATE repos SET commit_count=?, latest_commit_date=? WHERE repo_name=?`。

8. **优化**：该库全部仓库更新完成后，执行 `sqlite2duckdb.py --optimize --db <name>`（刷新 ART 索引 + CHECKPOINT + ANALYZE + manifest），确保后续查询走索引加速。

**状态与断点续跑**：`script/_git_update_duckdb_state.jsonl` 记录每条 (db, repo) 的执行状态（ok/uptodate/error/skip），脚本重启时自动跳过已完成项，仅重试 error 项。

**镜像重建白名单**（`REINGEST_ALLOW`，需人工研判后添加）：`trueos-src`（上游镜像整体重建，0/100 抽样不可达）、`netbsd-src`（GitHub 镜像 2025 年重建，316k vs 774k 提交）、`openssh-apple/openssh`（Apple 清理历史引用，13 860 vs 35 提交）。

**数据库更新后清理**：增量更新直接写入 DuckDB，不经过 SQLite 中转。`--optimize` 已包含 manifest 刷新与索引重建，无需额外步骤。

## Git 暂存规则（.gitignore 与体积门槛；2026-10-17 立）

**规则**：除非 ykla 显式批准，不应将下列两类内容 `git add` 进暂存区：

1. **被 `.gitignore` 排除的条目**——包括以 `-f`／`--force` 强制添加的路径。项目内存在定向例外（如 `!00-编纂规则与格式规范/01-规则/脚本与命令/*.py`），**例外清单以 `.gitignore` 实际内容为准**，不应凭记忆判断。
2. **单个文件大于 5 MB（5 242 880 字节）**——数据库、字体、PDF、归档包、日志等大件一律不入库；确需入库者先经 ykla 批准。

**暂存前自查（三项，逐项实测）**：

```bash
git status --ignored --short <path>      # 被忽略项是否混入暂存（!! 标记）
git diff --cached --name-only            # 逐件确认路径
git diff --cached --numstat              # 体积与改动量
```

- 被忽略项显示 `!!` 者不应进入暂存区；已误加者用 `git rm --cached <path>` 撤回（保留工作树文件）。
- 体积以工作树实际字节为准（`wc -c` 或 `git ls-files -s` 取 blob 后核），不依赖文件名或扩展名推断。
- 提交前以 `git ls-tree HEAD -- <path>` 核定落定；`partial-commit` 按工作树态记录。

**例外审批留痕**：经批准入库的大文件或忽略项，应在 `changelog` 记明“批准人／批准时间／用途／体积／sha256”，并在提交说明首行标注 `APPROVED-BIGFILE:` 或 `APPROVED-IGNORED:`。

**阻断类（commit-msg 阶段核对批准标记；2026-10-17 ykla 批准扩展）**：除上述 G1（忽略条目）/G2（>5 MB）外，另设下列阻断：

- **B2 根目录新增一级条目不在白名单**——白名单＝`.autocorrectrc`／`.gitattributes`／`.gitignore`／`.zcodeignore`／`.markdownlint.json`／`.textlintrc`／`.textlintrc.json`／`LICENSE`／`AGENTS.md`／`favicon.ico`／`logo.svg`／`README.md`／`bsd-family-tree.txt`／`bsd-family-tree-zh.txt`（末三组 2026-10-29 补登记：家族树两件为第三方参照件，已在库且被 `01-项目管理/03-架构与技术文档/07-附录-谱系与术语.md` 引用；`.zcodeignore` 为已入库的根级忽略配置，补登以免误判）；编号目录与 `script/` 等既有目录的新增文件不受限（只拦**根目录一级**新条目）。
- **B3 暂存区删除 `12-数据库备份/**`**——备份归档不应经 git 删除。
- **B4 文档类文件含全角空格 U+3000**（禁 AI 不可见字符）。
- **B5 暂存区含旁路备份副本**（2026-10-23 用户令，**无放行标记**）：路径名命中 `.prebak*`／`.bak`／`.bak-*`／`.bak_*`／`.bak.<数字>`／`.orig`／`.rej`／`~` 结尾，或任一路径段含 `prebak`——一律拒收。缘由：2026-10-23 实测清除 783 件 prebak（17.7 GB）与 1 064 件 bak 类旁路件；留痕与回滚唯一靠 Git，数据库快照唯一走 `12-数据库备份/` 正式槽。
- **H1 提交说明质量**（2026-10-17 ykla 批准批，无放行标记）：首行非空、≥8 字符、非纯数字／标点占位、消息不以 BOM 起始——违者拒（改写消息零成本，不设 bypass；缘由＝当日“1／2／！”式整索引提交 ≥7 件、69ee8a32a6d8 消息首字符带 BOM）。
- **H3 暂存 `.md` 含直角引号六码位**（U+300C／U+300D／U+300E／U+300F／U+FF62／U+FF63；2026-10-17 直角引号转写批补设）——对象面＝**全部暂存 .md**（含内容层/逐字保真档案与代码上下文），与第二十四件 `audit_md_quote_glyphs.py` 全库 T1 同一口径；F1 不自动改正代码上下文与内容层（逐字保真），此两类面残留由本判据兜底阻断——pre-commit 自动改正＋commit-msg 阻断闭环。
- 放行标记：G1 用 `APPROVED-IGNORED:`、G2 用 `APPROVED-BIGFILE:`、B2/B3/B4 共用 `APPROVED-BY-OWNER:`（均在提交说明全文检索，规范要求标注于首行）；**B5 不设放行标记**。

**自动改正类（pre-commit 阶段，改后重新暂存并提示，永不拒收；2026-10-17 ykla 批准）**：对暂存区文档类文件（`.md`／`.txt`；**排除内容层与逐字保真档案**——`05-卷册大纲/`、`02-sacred源材料/`、`03-原始史料库/`、`12-数据库备份/`、`05-卷册大纲/目录/data/`、`12-重构大纲书目述评/`）：

- **F1 直角引号（U+300C/300D/300E/300F）→ 弯引号**——开闭字符一一映射，无需配对判断；围栏代码块与行内代码段内**不动**（逐字保真）。
- **F2 不可见字符全口径清理（2026-10-17 清理批合入；裁定与细则见“AI 不可见字符清理规则”）**——①Unicode Cf 格式符／填充符（U+200B–200F、U+202A–202E、U+2060—206F、U+FEFF、U+00AD、U+0601、U+034F 等）一律删除；②Zs 空格类（U+3000、U+00A0、U+202F 等，除 U+0020）一律归一为 1 个半角空格，含此类字符的极大空白串合并为 1 个半角空格，行首／行尾整段删除；③U+FFFD 只披露不改正；④整文件范围、含围栏代码块与行内代码段（与 B4 对象面一致，防 pre-commit 漏改而 B4 拒收的矛盾）；⑤改写前后以 canon 内容指纹断言，不符即回退本件。算法单一来源＝`fix_md_invisible.py` 的 `norm_body`／`canon`，缺失时降级窄口径（仅删 U+200B/200C/200D/2060/FEFF）并在改动说明标注。
- **F3 CRLF/CR → LF；剥离 UTF-8 BOM**。
- 二进制文件（前 8 KB 含 NUL）跳过。

**自动执行（2026-10-17 ykla 批准安装）**：门禁由两个 hook 薄壳调用固定脚本 `00-编纂规则与格式规范/01-规则/脚本与命令/git_commit_gate.py`——`.git/hooks/pre-commit`（`--stage pre-commit`，自动改正）与 `.git/hooks/commit-msg`（`--stage commit-msg <msg>`，阻断核对）。阻断类放 commit-msg 而非 pre-commit 的原因：pre-commit 阶段提交说明尚未定稿，无法核对批准标记。hook 薄壳位于 `.git/` **不入版本库**，仓库重建（新 clone）后应重装两条薄壳：

```sh
# .git/hooks/pre-commit
exec python "00-编纂规则与格式规范/01-规则/脚本与命令/git_commit_gate.py" --stage pre-commit "$@"
# .git/hooks/commit-msg
exec python "00-编纂规则与格式规范/01-规则/脚本与命令/git_commit_gate.py" --stage commit-msg "$@"
```

**判据非空**：`--selftest` 隔离临时仓库 **30 用例**（含 H1 四例、H3 直角引号四例——散文拒／批准放行／内容层面拒／代码上下文拒——与 F1 半角形两例（U+FF62/FF63））（F 改正放行＋改正内容正确；F2 全口径放行＋内容钉死——Cf 全删／Zs 归一／行首行尾删除／围栏与行内代码一并清理／U+FFFD 保留；B4 链路改正后复检放行；FIX_EXCLUDE 边界三例——pre-commit 跳过／内容原样／提交放行〔内容层文件 fix 与 B4 均不涉，存量由批量工具覆盖〕；G1 忽略拒／撤回放行；G2 拒／批准放行；B2 拒／批准放行／白名单放行；B3 拒／批准放行；B4 拒／批准放行）。**三条假绿教训**：①`git check-ignore` 对暂存区中的路径默认不按 ignore 规则评估，应 `--no-index`；②`--` 终止选项解析，`--no-index` 应前置；③临时仓库应 `commit.gpgsign=false`——全局签名配置使 `git commit` 以 No secret key 失败（rc 128），后续 add 把 index 清空，夹具全空。夹具应 `git add -f` 构造忽略条目入库场景。

用 `--no-verify` 绕过应 ykla 显式指示并留痕 changelog。

**与既有规则的关系**：`script/` 不入库、`*.duckdb` 不入库、备份归档不入库等专项规定各自有效；本节为一般化条款，冲突时以更严者为准。

### 提交隔离与并发写者（2026-10-22 合入）

**背景**：本仓库为多会话共享工作树 ＋ 共享 git 索引的作业环境，实测反复出现“以为只提交本批、实际卷走他线在途改动”。下列四条为硬纪律。

**① 本环境无 GPG 密钥，提交一律显式免签**。`git commit` 默认签名必失败（`gpg: skipped ... No secret key` → `fatal: failed to write commit object`），且失败后索引可能被清空、表现为“看似没提交”。故：

```bash
git commit --no-gpg-sign -F <消息文件>
```

> **🟢 2026-11-06 根治（ykla 裁定方案一）**：根因＝私钥在 gpg4win（`C:/Program Files/GnuPG/bin/gpg.exe`，keyboxd）而 Git Bash 侧 MSYS gpg 钥匙串为空，全局 `commit.gpgsign=true` 使无旗标提交必败。已全局 `gpg.program` 指向 gpg4win 并 unset `commit.gpgsign`（临时仓无旗标提交 rc=0 验证）——**提交默认免签，`--no-gpg-sign` 不再必需**（带之无害）；需签名时显式 `git commit -S`（交互输口令），无头会话签名挂死问题随自动签名关闭而消解。上方“一律显式免签”自即日起为历史口径。

`git commit-tree` **不读** `commit.gpgsign`，会静默产出无签名提交却 RC=0——用 `commit-tree` 建提交时应显式 `--gpg-sign`，或明确接受免签并在说明里写清。

**② 仓库存在自动暂存器与自动提交器，`git diff` 为空不代表无改动**。实测 `git diff` 空而 `git diff --cached` 有上万文件在索引；`.gitignore` 的 `/script` 一行会让 `git status` 对被忽略文件**完全沉默**（不算 untracked、不报错）。判“本批是否已在索引”的唯一办法：

```bash
git diff --cached --unified=0 -- <path>      # 或
git show :<path> | grep <本批标记>            # 判在索引
```

**③ `git commit -- <pathspec>` 与 `git commit --only -- <pathspec>` 提交的是这些路径的“工作树”内容，不是 hunk 级选择**。共享文件上他线的并发改动**照样被卷走**（实测：登记表 99 行 diff 中仅约 40 行属本批；另一次在途批次被整体吸收）。可用的隔离手段：

- 有他线件已在索引：`git reset -q -- <他线路径>` 拆回（只动索引、不动工作树、非破坏），再提交；
- 需严格 hunk 级隔离：先把工作树改成“HEAD ＋本批改动”→ 提交 → 再写回全量；走不通就**如实披露**“含他线并发改动”，不重写历史；
- 已用过四次的隔离通道：`git hash-object -w` ＋ `git update-index --cacheinfo`（提交 blob＝HEAD＋本批行，工作区另留他线行待其自提）。**`git update-index` 的路径应全用正斜杠**，否则 `core.quotePath` 会转义路径。

**④ 并发写者存在时禁用 `--amend`**——它会把当前暂存区一并收进被改的提交。宁可另起一次留痕提交。并行整索引清扫卷走本批记账提交属常态（内容无损）：**不补空提交、不 amend，只如实披露**。

**提交前固定四步自查**（与本节开头的“暂存前自查三项”合并使用）：

```bash
git diff --cached --name-only | wc -l        # 索引里还有谁
git show :<path> | grep <本批标记>            # 本批内容确已在索引
git add <显式路径>                            # 显式路径，不用 -A/-all/-f
git commit --no-gpg-sign -F <消息文件>        # 不带 pathspec
```

- 多段 `-m` 会被 commit-msg 质量判据误判 → 一律 `-F 消息文件`；
- 管道后接 `| head`／`| tee` 会吞退出码 → 取 `PIPESTATUS[0]`，或独立查 `git log -1 --format=%G?`；
- `git stash -- <pathspec>` 会 stash **全树**而非仅该 pathspec；单文件回退用 `git checkout HEAD -- <file>`；
- `git rm --cached` 之后若用 `git commit -- <path>`，会取工作区内容把文件重新写回历史——应用不带 pathspec 的提交，或 `GIT_INDEX_FILE` 临时索引 ＋ `commit-tree`。

**判据非空**：上述四条均可复现——②用 `git diff` 与 `git diff --cached` 双查即可见差异；③用一次含他线改动的共享文件提交即可复现卷走；④用 `--amend` 后 `git show --stat` 可见夹带。
