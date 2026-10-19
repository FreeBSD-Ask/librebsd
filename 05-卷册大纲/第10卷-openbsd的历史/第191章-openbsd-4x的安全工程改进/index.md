---
chapter: 第 191 章
id: CH191
volume: 第10卷-openbsd的历史
---

# 第 191 章 openbsd-4x的安全工程改进

## 要点

- OpenBSD 4.0-4.4 的 Release Notes 与 CVS commit log 是研究此时期安全与工程改进的核心史料；openbsd.duckdb openbsd-src 仓库 2005-2010 年间贡献者以 deraadt@（5416 条）、jmc@（3921 条）、miod@（3760 条）、brad@（2728 条）、kettenis@（2271 条）为主；OpenBSD 4.0
- pf 2005-2012 年间的 commit 记录与设计文档是研究 pf 演进的核心史料；openbsd.duckdb openbsd-src 仓库显示 2005-2010 年间 pf 相关 commit 主要贡献者为 claudio@（198 条，ospfd/route 协议与 pf 集成）、henning@（169 条，ospfd 与 pf 接口组匹配）等 ［考据注：原采集行至此截断，余项待库侧重跑回源］
- 2005-2012 年间 OpenBSD 加密相关 commit 记录是研究此时期加密演进的核心史料——softraid 加密（2007-2008 tedu@、hshoexer@、jsing@）、IPSec 改进、TLS 库更新等；openbsd.duckdb openbsd-src 仓库保留完整 CVS 历史；交叉验证须对照 Release Notes、man page 与 commit log
- OpenBSD 4.x-5.x 时期 Release Notes 与 CVS commit log 是研究 6 个月周期工程实践的核心史料；release tags、release engineering 邮件、hackathons 报告共同构成考据链；OpenBSD 4.0 release 周期起点以 2006-09-17 steven commit e8d7e8373d3b “4.0-curr” 标记为起点 ［考据注：原采集行至此截断，后文待库侧重跑回源］
- OpenBSD Foundation 的注册文件、bylaws、董事会决议是研究其治理结构的核心史料；bylaws 详细规定捐赠接收、资金使用、董事会选举等流程

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4026] Theo de Raadt. That whole “Linux stealing our code” thing[EB/OL]. 2007. <https://lkml.org/lkml/2007/8/31/157>（库内文献 ref2216）；匹配第 191 章，置信度 1.0
- [DB:references_fulltext:chapter_matches:chmatch_4027] Theo de Raadt. OpenBSD bcw: Possible GPL license violation issues[EB/OL]. 2007. <https://marc.info/?l=openbsd-misc>（库内文献 ref2217）；匹配第 191 章，置信度 1.0

## 史观

- 总纲第 10 条——动手者创造历史：malloc 替代、synproxy、softraid 加密等 4.x 安全工程改进由具体开发者响应安全研究与运维需求逐项实现，动手者的局部方案经社区需求放大进入官方系统，而非自上而下规划的结果（详见 191.1-191.3）
- 总纲第 18 条——时间是一种形式主义：6 个月固定发布周期作为形式化时间规则塑造开发节奏——5 月与 11 月的 release 约束使特性须在周期内完成与稳定化，未完成者推迟至下个周期（详见 191.4）
- 总纲第 13 条——法律与道德是利益分配：OpenBSD Foundation 以加拿大非营利公司形式承接项目资金与法律责任，法人治理要求与社区既有治理形成双层结构（详见 191.5）
- 总纲第 3 条——不存在进步，只有权力再分配：Foundation 成立后企业赞助的引入改变贡献者构成与资金结构；BSD 许可证下 pf 被 FreeBSD 移植、OpenSSH 被产业采纳，均非单向的组织进步而是权力与资源的再配置（详见 191.6）

## 辨析

- Release Notes 的完整性以 plus.html 页面为准——该页面仅记录用户可见变更，内部代码重构需以 commit log 补充；OpenBSD 仓库无 release tag（OpenBSD 使用 CVS 而非 git tag 标记 release），故 release 日期以 OpenBSD 官方网站公告为准 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. <https://www.openbsd.org/40.html>；OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/>；openbsd.duckdb 查询 L1.1.1 与 L1.1.2（来源：原材料/研究/bsd 仓库分析/数据分析/宏观趋势统计.md §L1.1.1、§L1.1.2）；统计分析报告：描述性统计.md SubTask 2.1 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/描述性统计.md**；统计分析报告：推断性统计.md Task 6 [R/OL]. 2026-07-27. 文件路径：**03-原始史料库/01-代码仓库史料/01-数据库本体/统计分析/推断性统计.md**；SQL 查询：`SELECT COUNT(*) FROM commits WHERE repo_name='openbsd-src'`. openbsd.duckdb [DB/OL]. 查询日期：2026-07-27；Python 统计脚本：`script/phase2_inferential.py`. Task 6 Pettitt + BUISHAND 变点检测。执行日期：2026-07-27 ［A］

---

## 史料登记与辩证校准（2026-08-08 追加）

> **本卷命题**：24.3 长期主义（详见本卷 00-总览“编纂指导思想叙事参照”）

### 史料文献

- openbsd.duckdb openbsd-src 仓库 pf 相关 commit；OpenBSD **pf.conf(5)** 手册页 [EB/OL]. <https://man.openbsd.org/pf.conf.5>；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；openbsd.duckdb 查询 L2.2.1.sys_net_pf（来源：原材料/研究/bsd 仓库分析/数据分析/中观模式挖掘.md §L2.2.1，数据缺口） ［A］
- openbsd.duckdb openbsd-src 仓库加密相关 commit；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD man pages ［A］
- openbsd.duckdb openbsd-src 仓库 commit e8d7e8373d3b；OpenBSD Release Notes [EB/OL]. <https://www.openbsd.org/plus.html>；OpenBSD CVS 仓库 [EB/OL]. <https://cvsweb.openbsd.org/> ［A］
- OpenBSD Foundation bylaws [EB/OL]. <https://www.openbsdfoundation.org/>；加拿大政府注册记录；OpenBSD Foundation 年报 ［B］
- OpenBSD 提交/文档/ports 贡献记录；OpenBSD Foundation 年报 ［A］

<!-- DB_REF:openbsd.duckdb -->
> **数据库引用（openbsd.duckdb）**：本子节对应 openbsd 代码仓库。> 1995-2026 年间：491,195 次提交。> 仓库总览：491,195 次提交，1,031 位贡献者（contributors 表实测），1995-10-18 至 2026-08-25。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSDTalk EP97（共 1 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- 受访者自述 hoststated（Host State Demon）源于一个快速的临时实现：OpenBSD 当时没有任何监控主机状态并把存活主机放入 PF 表的工具，他写了一个执行 TCP 连接检查、将存活主机置于 PF 表中、使重定向规则永不指向宕机主机的程序。与 round-robin DNS 相比，DNS 负载均衡无从得知主机死活、依赖客户端自行切换到下一主机（多数浏览器会如此、并非全部）；hoststated 则借 PF 的三层目的地址重写对客户端完全透明。典型部署为服务器池置于负载均衡器之后，DNS 将连接指向均衡器，PF 以 RDR 规则把连接分发到池内机器。（BSDTalk EP97，[62.86-198.28]，L1）
- hoststated 实为围绕 PF 的包装器，以非阻塞方式检查主机响应是否足够快；他仿照 OSPFD 实现了配套的 hoststated ctl，管理员可借此查看在线主机、并在维护或升级时禁用某台。检查方法包括 ICMP（对 IPv6 主机用 ping6）、TCP 连接检查、HTTP 检查（校验指定 URL 的返回码与页面内容的 SHA1 摘要），以及通用的 send/expect 方法——向连接发送一段数据并期待特定回应（如 SMTP banner 可只期待不发送），初以正则实现后改用 fnmatch；SSL 代码可用，所有 TCP 类检查方法均可包裹于 SSL。（BSDTalk EP97，[198.28-365.8]，L1）
- 关于演进方向：按服务器负载加权的均衡是计划中的目标——但加权所需的代码在内核中与 PF 绑定，须在 PF 侧实现方可让某些主机被查询得更少；团队的长期目标是功能完整的负载均衡器。初始可用版本的目标已然达成，他希望 hoststated 能赶在 4.1 之前链入 build（否则将于 4.1 打标签后的早期 snapshot 提供）。测试环境为笔记本电脑加上家与单位各一组负载均衡测试机器，另有一台由他自管、带真实均衡器与专用主机的准生产部署用于大改动验证，并尽量实现每种场景以测试回归。（BSDTalk EP97，[365.8-498.68]，L1）
- 受访者澄清负载均衡的一个常见误解：PF 式的基本负载均衡只重写目的地址、不重写源地址，因此 Web 服务器日志中记录的是真实的客户端信息，站点统计仍然准确；只有当均衡器与 Web 主机不在同一网段时才须同时重写源地址——此场景下若无七层负载均衡介入则丢失客户端信息（服务器只见来自均衡器的连接），做七层时通常附加 X-Forwarded 头。多数部署不采用该场景，源地址得以保留。（BSDTalk EP97，[517.96-600.4]，L1）
- 与 CARP 冗余防火墙的配合及可移植性：两台防火墙各自运行 hoststated、分别维护 PF 表，CARP 切换时备份机上的表处于良好状态；代价是须在 CARP 设备与底层接口上共预留三个 IP、双机都要运行，略显过度。hoststated ctl 暂只支持本地连接。依赖方面只要操作系统支持 PF 与 C 库即可——有人尝试在 FreeBSD 上编译且据称顺利（需要 3.5 之后版本的 PF ioctl 及 strlcpy 等函数），虽此后未再收到回音，据他所见可以运行。（BSDTalk EP97，[600.4-716.24]，L1）

**史料**：

- 本期为 OpenBSD 开发者 Pierre-Yves Ritschard 的口述访谈（bsdtalk097，2007-02-01），提供其履历与 commit 历程的一手陈述：自 OpenBSD 2.3 起（上大学前装于工作站）为其用户，此前用过 FreeBSD 与少量 Linux；视 OpenBSD 为开发平台、后用于网络架构；贡献自提交 ports 与小补丁起步，工作中深度使用后发现需要修复之处、渐多投入、尤以 OSPFD 为主；因工作常用 keepalived 而不喜其设计，遂以 OpenBSD 工具风格自写 hoststated——初始六成以上代码复用自 OSPFD（父进程架构与配置文件解析器几乎相同），先以 port 形式提交；Reyk Floeter 等开发者因同样需要而接洽、邀其维护，经邮件与代码往来后获得 commit 账号。访谈后 hoststated 被链入 build、随二月 snapshot 发布。（BSDTalk EP97，[725.8-895.88]，L1）

**史观**：

- 总纲10 动手者创造历史：hoststated 的进入路径是运维痛点驱动的个体劳动案例：作者在工作中对既有工具不满，以复用 OSPFD 代码与设计范式的方式为自身需求造轮，先以 port 交付、再经核心开发者因共同需要而接洽，最终获得 commit 权限并链入官方 build。工具的正规化不是自上而下规划的结果，而是动手者的局部方案被社区需求放大的过程。（BSDTalk EP97，[804.24-895.88]，L1）

**文献**：

- [BSDTalk EP97] Backman W. BSDTalk: 97: bsdtalk097 - OpenBSD Developer Pierre-Yves Ritschard[EB/OL]. (2007-02-01)[2026-08-27]. <https://archive.org/details/bsdtalk097>.

<!-- /PODCAST_REVIEW -->

<!-- GAP-A-YT:BEGIN 2026-10-20 缺口A 662 期战役注入 -->
<!-- ROW_MINE: youtube.episodes.CL-15-2898 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2898`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔MeetBSD 2008《Hardware Crypto Suport》讲者口述：FreeBSD 于 2002 年从 OpenBSD 借用 open_crypto 框架，由转写音作 Sam leer 者最初导入，用途是为密码系统提供一致的硬件与软件接口；讲者说明其原本主要面向 IPC，但 OpenBSD 的实现同时支持把该接口导出到用户态，并做成可插拔多算法的模块化结构。（YouTube EP2oV2ZGXO33o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2899 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2899`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔MeetBSD 2008《Hardware Crypto Suport》讲者口述：open_crypto 为会话式接口，使用者声明所需算法与密钥长度后把数据流持续送入同一会话；接口是异步的，调用方不在密码操作上阻塞，而是把操作发出去、等回一条完成消息后再取回加密或解密的块。（YouTube EP2oV2ZGXO33o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2900 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2900`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔MeetBSD 2008《Hardware Crypto Suport》讲者口述：多数内核子系统已改用 crypto 框架，但讲者发现 gbde 是个例外——它不使用该框架，因此即使硬件里插着加密加速器，用 gbde 做块设备加密也不会更快。（YouTube EP2oV2ZGXO33o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

<!-- ROW_MINE: youtube.episodes.CL-15-2901 -->
**存疑材料**（证据等级：L1，来源：`historical_claims.duckdb.claim.CL-15-2901`；2026-10-18 缺口A 662 期战役逐条判定采纳）

据〔MeetBSD 2008《Hardware Crypto Suport》讲者口述：在一台 3.8 GHz 的 AMD 系统上，开启硬件加速反而更慢——1K 块上数字约减半甚至慢到五倍，讲者据此说在这些快系统上不要开加速。（YouTube EP2oV2ZGXO33o，SUB）引用时按 L1 纪律：以上为存疑材料，采信前须另行考据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。
<!-- GAP-A-YT:END -->
