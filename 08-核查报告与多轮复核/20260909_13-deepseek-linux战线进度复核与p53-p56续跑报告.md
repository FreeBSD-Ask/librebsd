# 13-deepseek-linux 战线进度复核与 p53-p56 续跑报告

**复核时点**：2026-09-09 21:00–23:40
**复核对象**：`script/_db_row_mining/dslinux/01-战线spec`（spec.md、交接报告）、`02-遍历留痕/traversal_trail.duckdb`、`03-候选/candidates.jsonl`
**权威依据**：留痕库 `review_logs` 表（唯一真相）；源库 `03-原始史料库/11-邮件列表史料/05-linux-kernel/db/ksummit-discuss.duckdb`
**方法论**：逐封完整审读（不抽样、不跳页）；修改前后各复核一次；三方对账（留痕 / 候选库 / 源库）

---

## 一、复核结论：交接文档已过期，实况以留痕库为准

| 项目 | 交接报告（2026-09-07）记载 | 本次实测 | 判定 |
| --- | --- | --- | --- |
| ksummit-discuss 已读 | 18 页 / 900 封 | **52 页 / 2,600 封** | 过期 |
| ksummit-discuss 断点 | 第 19 页 `--after 345155` | 第 53 页 `--after 346855` | 过期 |
| 总进度 | 27.7% | **46.6%**（4,407/9,770） | 过期 |
| candidates.jsonl | 1,636 行 | **3,145 行** | 过期 |
| 末编号 | DSLXC-1637 | **DSLXC-3146** | 过期 |
| linux-smp 状态 | “第 20 页起”待续 | 19 页为**裁决三终态**（09-06 已终止逐封） | 表述误导 |

实测三库分布（对账一致，无重复 src、唯一缺口 98）：

| 库 | 页数 | 已读 | 候选 | 无值 | 末 pk |
| --- | --- | --- | --- | --- | --- |
| ksummit-discuss | 52 | 2,600 | 2,007 | 593 | 346855 |
| linux-smp | 19 | 950 | 557 | 393 | 1572287 |
| tech-board-discuss | 18 | 857 | 581 | 276 | 9363448 |

上述差异成因已登记于 `02-遍历留痕/03-战线口径对照清单.md` C-9，本次一并修复。

---

## 二、本轮续跑：ksummit-discuss 第 53–56 页（200 封）

### 2.1 逐页登记

| 页 | pk 区间 | 日期跨度 | 候选 | 无值 | 候选编号 |
| --- | --- | --- | --- | --- | --- |
| 53 | 346856–346905 | 2016-08-03～04（含 5 封 KS2014 混档） | 48 | 2 | DSLXC-3147..3194 |
| 54 | 346906–346955 | 2016-08-04（含 6 封 KS2014 混档） | 46 | 4 | DSLXC-3195..3240 |
| 55 | 346956–347005 | 2016-08-04～09（含 4 封 KS2014 混档） | 49 | 1 | DSLXC-3241..3289 |
| 56 | 347006–347055 | 2016-08-09～15（含 3 封 KS2014 混档） | 48 | 2 | DSLXC-3290..3337 |

合计 191 候选 / 9 无值 = 200 封，三态守恒成立。

### 2.2 no_value 判定标准（本次据 p50-p52 已登记样本校准）

纯礼节、纯流程协调、纯引用无新增论点者判 no_value，共 9 封：346868（邮件地址更正）、346894（行程说明）、346929/346952/346955（致谢与一句戏谑）、346932（链接 404 更正）、346957（他人邮箱变更转告）、347016（会议征稿通知）、347033（“啊，我明白了，谢谢”）。

### 2.3 内容脉络（p53-p56 增量）

**stable workflow 大辩论收束**（p53-56 主体）
- Kosina 给出真实案例（`lkml.org/lkml/2013/4/22/259`，2013 年 VFS 补丁修一个 stable 里不存在的问题、导致系统立即损坏），Bottomley 以“stable review 比上游更不彻底”“上游没抓住凭什么 stable 能抓住”否定之，Kosina 反驳其前提错置。
- **Fixes/版本范围提案全弧**：Torokhov 提出裸 `cc:stable` 只指最新 stable → Kosina 成文规则草案 → Roeck 补全措辞（“未限定 stable 标注将只被应用到最新的 stable 发布”，并提议扩展到 longterm）→ Jan Kara 指出该方案的可行性在于**负担是每补丁一次而非每补丁每树一次** → **Greg KH 三次否决**（“那会施加比我想强制的更多负担”“我甚至不想为我维护的树做那份额外工作”“维护者是我们眼下最有限的资源”“我们仍*有整个整个的子系统从不给 stable 标注任何东西，请把注意力放在它们身上”）。
- **Rostedt 把 Fixes 门槛具体化**：完整给出 `git blame broken-file.c` → `git show SHA1` → 遇空白改动则 `git blame SHA1~1` → `git describe --contains SHA1-OF-BROKEN-COMMIT` 得 `v3.14-rc1~82^2~40` → 加 `Cc: stable@vger.kernel.org # v3.14+` 的可复制流程；并以 tracing 子系统“上千选项、bug 可能多年无人察觉”论证为何坚持回溯。
- **定量化**：LWN 692866 的 0.6–1.4%（4.6）/2.2–9.6%（3.14）→ Greg KH 指出 Jon 口径缺陷（“只看补丁是否声称修复了先前 stable 里恰好存在的补丁”，有时“修复”并未真修好）→ **Roeck 的 chromeos-4.4 实证：1,044 补丁中 1 个坏 = 0.1%**（`dea2cf7c0c6e` ecryptfs），并指出这是**感知问题**（1,043 个修复因一个回归就不算数）。
- **Bottomley 的 Fixes 超越 stable 论**：任何修正先前提交的修复本身就是回归，而 Fixes 的用途远超 stable（含回归追踪），“是我们本来就该在做的事，不是专为此发明的”。
- **命名与文档之争**：Brown 主张“好实践而非打勾”，Rostedt 主张“指南而非硬要求”，Uytterhoeven 提议名人堂/耻辱堂，Rostedt 以 20 美元奖金寓言与 Dilbert 漫画（1995-11-13）反驳激励机制。
- 补充材料：Chris Mason“内核工程师日记”（第 1/68/157 天）、Takashi Iwai 的 PCI ID 属“增强而非修复”例外、Rafael 的“可接受数字取决于服务哪一群人”。

**secure/verified boot 与信任根**（p53-56 续）
- Lutomirski 的 `trusted_policy_header` ELF 段跨架构提案 + Garrett 的打包侧集成路径（公钥入包、签名步骤一并签密钥、bootloader 验证后传递）。
- Jason Cooper 的“验证 vs 信任”严格区分 + **Eviltel 攻击模型**（恶意厂商 blob 借他人签名载入竞品设备）→ 提出以 PCI/USB id 或 devicetree compatible 串作为鉴别符，并把**真实性（Intel 造了它）与策略（我们只允许它进这些设备）分开**。
- Walleij 的“我信 Dirk Hohndel 胜过信他所在的公司”与 Monkeysphere/web-of-trust 之辩。
- **固件签名生态实况**：Vinod Koul 披露部分 Intel 提交至 linux-firmware 的固件已签名（坏/未签名密钥将加载失败）→ Woodhouse“任何方案必须能*使用*现有签名”→ **主张（捏着鼻子）支持 Authenticode**。

**设备探测顺序与复杂依赖**（p53-56）
- deferred probe 功过并存：Brown“内核错误处理质量史上最好的事”vs Nikula“对 i915 复杂度效率极低”；Greg KH 否决“模块主动请求延后”。
- **Bergmann 的 probe/remove/probe 编译期选项** → Hajda 指出已有 unbind/bind sysfs 属性 → **Rob Herring 实机验证**：x86 VM 上输入设备重复注册，随后在 virtio-gpu 上炸出 `drm_mm_takedown` 警告与 `slub.c:3657` BUG（报告附完整内核日志）。
- **Rödel 的 AMD-KFD/IOMMUv2 实证**：作为模块时靠符号依赖定序、内置时顺序错即崩溃；当前“解法”是确保 iommu 驱动先被链接。
- **Bottomley 的 ATA/SCSI transport class 方案**（subsystem_init 管独占资源 → module_init 启动探测 → 依赖初始化推迟到消费者实例化），并提出**可分离性定理**（“任何极其复杂的相互依赖，也许只要换一种方式看问题就可以变得不必要”）；Rodriguez 追问扩散性，Woodhouse 答“大多数子系统都在用”。
- Walleij 以 Android 全内置反驳“启动变慢不重要”。

**回归追踪**（p55-56）
- Leemhuis 的 bugzilla 失效论（测试者得出“报 bug 不值得”的结论）→ Roedel“多种上报渠道本身是问题，应确定单一方式”→ **Nikula 提议 MAINTAINERS 增 `B:` 条目** → Vetter +1（gfx 侧更糟：用户分不清内核/X/mesa）→ Bottomley 的 bugzilla 邮件等价配置（**bugzilla v3 后回复捕获失效**）→ Laura Abbott 评 ABRT（噪声大，唯一有用是一键建 bug 与去重）→ Iwai 提 regression flag 自动通知 → **Rafael 反驳“bugzilla 无人照看”：PM/ACPI 回归由 Intel 团队跟踪**。

**KS2014 混档议题**（p53-56 内）
- 运行时检查（Marinas：lockdep/RCU 调试/投毒/kmemcheck/kmemleak，三条讨论目标，点名各工具维护者）
- 爱好者招募（Cooper：不主动外联、单独邮箱与规则集、Eudyptula Challenge 首次贡献者现象）
- QR 编码 oops（Cooper：oops 编码 QR → 手机扫码即上报，三步流程，作者 Kurusa/Băluţă）
- ARM 遗留板级 DT 转换收尾（Cooper 的逐子架构汇报 + 三分类清单；Corbet 判断属 ARM 迷你峰会；Olof 交代今年不办与沿革）
- 能耗偏置三档 profile（Murthy：powersave/performance/balanced）
- 静态检查工作流（Sang：sparse/smatch/coccicheck/cppcheck）
- 2038 与 32 位微控制器（hpa：0.25 美元 32 位 MCU 将大量跑 Linux，Rafael 补“其中一些到 2038 年还在做着某种事”）
- secure boot 下的 root 分类（Jones：`[*] 哦天，ioctl`）

**工具链与其他**
- git-series：Tsirkin 的 am/cherry-pick 导入接口与 `-x` 溯源元数据；Hogan 的依赖系列分叉需求 + 完整命令草案；Triplett 的分离头指针设计意图、系列依赖机制与引导式 status 交互示例。
- more useful types：Wilcox 的返回值类型清单（`errno_t`/`count_t`/…）→ Tsirkin 的“来自用户空间的索引”标注与 `force_range` 方案 → NeilBrown 的 sparse `__attribute__((bitwise))` 现成解法 → Dobriyan“名字最容易，问题是清除错误后变量不变回普通类型”→ Carpenter 的 Smatch 实践与“75%/25% 未注释返回零”统计。
- StGit 元数据格式（Marinas 说明 `stgit/lib/log.py`、`<branch>.stgit` 结构与多人协作计划）。

---

## 三、口径缺陷修复（对照清单 C-8 / C-9）

### C-8：`progress.py` 缺三列入参（已修复）
- 现象：`review_logs` 的 `themes`/`cand_no`/`no_val_examples` 三列，09-08 起登记的 24 页全空，仅 09-06 迁移的 13 行有值，页级主题与候选编号追溯链断裂。
- 处置：`progress.py` 补三个可选入参并透传至 `append()`（第 55-66、111-114 行）；本轮 p53-p56 四行已带参登记；历史空行暂不回填（原文需重读，成本高于收益，留待收尾阶段按需处理）。
- 复核：填充度由 13/93 升至 17/93，p53-p56 四行三列均非空。

### C-9：交接文档过期（已修复）
- 处置：交接报告重写第一、六、七、八节，断点更新为 ksummit-discuss 第 57 页 `--after 347055`；linux-smp 明确标注 19 页为裁决三终态（非未完成）；主题脉络备忘扩至 p1-56。
- 同步：`spec.md` 编号上限改 3337 并登记三列入参约定；`03-战线口径对照清单.md` 更新 read 4,607、候选 3,336，C-8/C-9 划闭合。

---

## 四、复核后实测状态

| 项目 | 数值 |
| --- | --- |
| 累计已读 | 4,607 / 9,770（**47.1%**） |
| ksummit-discuss | 56 / 147 页（2,800 / 7,323 封，38.2%） |
| candidates.jsonl | **3,336 行**，末编号 DSLXC-3337，重复 src 0，缺口 [98] |
| 留痕一致性 | review_logs 三库 cand 合计 2,198+557+581 = 3,336，与候选库逐条吻合 |
| 三态守恒 | 各库 candidate + no_value + needs_recheck = 已读行；无 needs_recheck |
| 断点 | ksummit-discuss 第 57 页 `--after 347055` |

---

## 五、遗留事项

1. ~~**C-10（lkml 是否纳入本战线）仍待第四次裁决**~~ **已于 2026-09-09 21:31 裁定并落地：lkml 不纳入本战线**。执行记录见本报告第七节。
2. **C-11（双轨与旧索引库去重基线）未定**：`dslinux_persons.duckdb`（1,044）与 `linux-mail-core-figures.duckdb` 同构，需 `src` 坐标 + 原文 SHA-256 建去重基线。
3. **C-7（`exempt_counts.audited` 15 库全 False）**、C-6（`exempt_rules` 第 17 条脏数据）待复核回填。
4. **P2 主题层（candidates_p2_theme.jsonl 剔除 lkml 后 36,448 封）尚未启动**，P3a 小库逐封在 ksummit-discuss 读完后接 ksummit、linux-kernel-announce。
5. 历史 76 行 `review_logs` 三列仍空（C-8 修复前登记），如需追溯须回读原文，建议收尾阶段统一评估。

---

## 六、相关文件

- 规范：`script/_db_row_mining/dslinux/01-战线spec/spec.md`、`交接报告_逐封审读_20260907.md`
- 留痕：`script/_db_row_mining/dslinux/02-遍历留痕/traversal_trail.duckdb`、`03-战线口径对照清单.md`
- 候选：`script/_db_row_mining/dslinux/03-候选/candidates.jsonl`
- 脚本：`script/_db_row_mining/dslinux/{read_page,view_page,progress,append_claims}.py`
- 本轮材料：`script/_db_row_mining/dslinux/{gen,review,view}/`（ksd53-56 全套）
- 回填脚本：`script/_dslinux_backfill_c8_20260909.py`
- C-10 剔除脚本：`script/_db_row_mining/dslinux/c10_exclude_lkml.py`（样本 `script/_staging/c10_20260909/`，备份 `*.bak_c10_20260909*`）

---

## 七、C-10 裁定与落地执行（2026-09-09 21:31–22:00）

### 7.1 裁定

主理人 2026-09-09 21:31 裁定：**lkml 不包含在本战线内**（C-10 闭合）。

### 7.2 影响面实测

| 资产 | lkml 行数 | 处置 |
| --- | --- | --- |
| `candidates_p1.jsonl` | 8,141（全部 keyword 轨） | **剔除**，48,240 → 40,099 |
| `candidates_p2_theme.jsonl` | 8,141（全部 L1 层） | **剔除**，44,589 → 36,448 |
| `candidates.jsonl`（审读成果） | 0（实测） | 无需处理 |
| `dslinux_persons.duckdb` | 无 list 维度（1044 人语料级） | **保留**（维持 C-11 去重基线） |
| `dslinux_keywords.duckdb` | hit 8,686 / 13,363 | **保留**（语料级抽取资产，与源索引库同构） |

补充实测：lkml 在 L2/L3 层**零命中**（L2 11,465 / L3 20,523 均不含 lkml），故主题池剔除仅影响 L1 层。

### 7.3 执行与复核（按脚本安全规程）

1. **备份**：`candidates_p1/p2_theme.jsonl.bak_c10_20260909`、`dslinux_keywords.duckdb.bak_c10_20260909`（script/_db_row_mining/dslinux/）。
2. **脚本**：`script/_db_row_mining/dslinux/c10_exclude_lkml.py`（DRY 默认，`--apply` 才写入；自动备份 + 写入后双向复核）。
3. **最小样本验证**（script/_staging/c10_20260909/）：5 行样本（3 非 lkml + 2 lkml）→ 剔除后 3 行，lkml 残留 0、逐行内容一致、CRLF 保持。**首次验证发现 CRLF 行尾 `\r` 未剥离导致二次叠加的缺陷，已修正 `read_lines()` 后复验通过**。
4. **正式执行**：p1 48,240 → 40,099、p2 44,589 → 36,448；两文件复核均为“行数符合、lkml 残留 0、内容逐行一致、换行符保持”。

### 7.4 文档同步

- `01-战线spec/spec.md`：新增裁决四（§1）、主题审读集口径改 36,448（§2）、Token 预算第四次修订（§4）、铁律增“审读池不得含 lkml”校验项（§5）、资产索引更新（§6）。
- `02-遍历留痕/00-编目.md`：第一节范围注 + 库清单第 15 项划除 + 关键数据表 14 库 + 执行顺序移除 lkml。
- `02-遍历留痕/02-豁免计数.md`：lkml 行划除 + 范围注 + 执行顺序更新。
- `02-遍历留痕/03-战线口径对照清单.md`：C-10 划闭合 + 主题池计数更新 + 建议动作 6 标记完成。
- `01-战线spec/交接报告_逐封审读_20260907.md`：范围声明 + 审读池计数更新。
