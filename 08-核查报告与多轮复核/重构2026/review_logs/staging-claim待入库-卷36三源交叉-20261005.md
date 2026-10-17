# staging｜claim 待入库 4 条（卷 36 阶段二三源交叉·2026-10-05）

> **性质**：**待执行清单**（staging）。`historical_claims.duckdb` 被 System PID 4 持续持有（本日多次重试 3×2 秒均失败），4 条已核证结论暂存于此，**待锁释放后按本件参数执行**。
> **放位说明**：本件置于 `review_logs/`（持久目录）而非 `script/`（随时清理），避免丢失。
> **执行方式**：`claim_id` 须在写入时回核 `max(claim_id)` 后取值（本件号段为 2026-10-05 17:45 时点推算，仅供参照）；逐条 INSERT 后 `CHECKPOINT` 并断言。

## 待入库 4 条（evidence_level 统一 L2／claim_type FACT／wording_gate attribution_allowed／status supported）

| # | 参照号段 | claim_text | time_start | time_end |
| - | -------- | ---------- | ---------- | -------- |
| 1 | CL-RM-388972（参照） | Debian GNU/kFreeBSD 系 Debian 官方推出的系统形态，以 FreeBSD 内核替代 Linux 内核（官方定义原文：an operating system from Debian, but which uses the kernel of FreeBSD instead of the Linux kernel）；来源＝Debian Wiki Debian_GNU/kFreeBSD 页 2008-05-01 Internet Archive 快照；这一内核—用户空间组合的本体史（官方移植至终止）载于本书第四十二卷 2.2–2.6 | 2008-05-01 | 2008-05-01 |
| 2 | CL-RM-388973（参照） | Gentoo/BSD（Gentoo /*BSD 子项目，含 FreeBSD/NetBSD/OpenBSD 移植）的 Gentoo Wiki 项目页 Project:BSD 正文已清空，页面末编辑时间为 2019-12-21——子项目停止活动的官方 wiki 侧一手佐证 | 2019-12-21 | 2019-12-21 |
| 3 | CL-RM-388974（参照） | TrustedBSD 为 Watson 等创立的 FreeBSD 安全框架项目，其成果（MAC Framework、OpenBSM、Capsicum 等）已并入 FreeBSD 基本系统；本书参考文献库存 Watson 等 TrustedBSD 论文两篇（ref 502、ref 1628）；本体集成史见第二十二卷第 5 章 5.3、第二十卷 5.6 | NULL | NULL |
| 4 | CL-RM-388975（参照） | smolBSD 有专门技术文献存于本书参考文献库（ref 1312：SMOLBSD: Making NetBSD a fast(er) booting microvm），与 GitHub 官方仓库（NetBSDfr/smolBSD，2024-12-29 建仓）互证——NetBSD 基微 VM 工具 | 2024-12-29 | NULL |

**created_by**：`llm:agent（卷36阶段二·三源交叉核证）`

## 本次交叉核证的其余结论（已落大纲注，无需入库）

1. **分工注互设**（5 处，已落 outline）：卷 42 2.2／2.7 ↔ 卷 36 5.2；卷 22 5.3（TrustedBSD）→ 卷 36 5.2；卷 36 3.1／5.2 注升级。
2. **大纲交叉发现**：卷 42 ch2“内核、用户空间与发行版的重新组合”（12 节）已系统承载 kFreeBSD（2.2–2.6）＋Gentoo/FreeBSD（2.7）＋Chimera Linux（2.9）——**该卷此前与卷 36 无互设分工注，本批已补**。
3. **ref 库交叉**：smolBSD（ref 1312）、TrustedBSD（ref 502／1628）、MirOS（ref 5253，bsdtalk081 Thorsten Glaser 访谈）——为核证提供本地文献支撑。
4. **待核项（下批）**：irBSD／Jibbed／PolyBSD／pocketSAN／OliveBSD／Anonym.OS 的官网或 IA 原件（本批 GitHub／CDX 检索未获主仓库；jibbed.org 与 microbsd.org 有 IA 快照可取）；Anonym.OS 域名形制待定。

*编制：二旺（WorkBuddy），2026-10-05。锁释放后执行并回报。*
