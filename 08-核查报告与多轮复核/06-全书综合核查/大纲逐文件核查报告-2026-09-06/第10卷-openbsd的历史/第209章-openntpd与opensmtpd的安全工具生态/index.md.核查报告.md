# 核查报告：第10卷-openbsd的历史/第209章-openntpd与opensmtpd的安全工具生态/index.md

- 源文件：d:\librebsd\05-卷册大纲\第10卷-openbsd的历史\第209章-openntpd与opensmtpd的安全工具生态\index.md（117 行，一次完整通读）
- 批次：C345；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以 openbsd.duckdb 只读实查、SUMMARY 实测）
- SUMMARY.md 收录：实测第 2031 行“本章索引”条目收录本文件（批次 JSON 旗标 UNLISTED_NOT_IN_SUMMARY 已失效——57/75/320/100.15 同款；第 209 章块起于第 2024 行）；章块简题“OpenNTPD 与 OpenSMTPD 的安全工具生态”为正体，源文件 H1 为 slug 连写体（openntpd与opensmtpd），二者并存
- A 占位符：发现 1 处（行 25 史观字段“(待人工回填)”显式占位，见清单 3）
- B 内容完整性：发现 2 处（要点五条截断、两表内容错配，见清单 1/2）
- C 编号与标题：通过——H1 与 frontmatter 相符
- D 格式规范：发现 1 处（文献区结构损坏，见清单 6）
- E 学术规范：发现 5 处（见清单）
- F SUMMARY 一致性：通过
- 机械旗标复核：UNLISTED_NOT_IN_SUMMARY 旗标经实测失效

## 问题清单

1. P2 | 行 11-15 | 要点五条全部句中截断（“……系统反”“……系统回应 Sen”“……三次演讲与项目目标页面”“……LibreSSL 采用 OpenSSL/IS”“……OpenBSD fork 决”） | 字节截断族重症：5/5 断尾，无一条完整 | 按 209.1-209.5 子节内容补全五条要点
2. P2 | 行 45-60 | “OpenSMTPD 四层辩证链结构”与“OpenNTPD 四层辩证链结构”两表 | 表内容系 LibreSSL 表（行 39-44）逐行复制（OpenSSL 阵营/Marquess 反思、FIONBIO/socklen_t、SRP timeline、BoringSSL fork 等 2014 行），与表题项目完全不符 | 以 209.2/209.3 实际辩证链内容重写两表
3. P3 | 行 25 | “(待人工回填——详见子节文件史观/辨析字段)” | 史观字段显式占位空置（章级 index 未回填） | 回填或改为子节史观映射的摘要引用
4. P3 | 行 74 | “仓库总览：491,195 次提交，3,352 位贡献者” | 贡献者数三口径均不合：openbsd.duckdb author_name 与 author_email 全库去重实测均为 427、contributors 表 1,031 行——3,352 无出处（2014 年 20,651 次提交实测逐字吻合）；且总览三行折叠为两行（“>”续行断裂） | 按实测口径改写并修复换行
5. P3 | 行 61 | “c:\Users\ykla\Documents\hibsd\原材料\哲学\项目统摄史观\第 25 章.md” | 私有绝对路径入库且指向库外目录（本项目统摄史观在库内为 02-sacred源材料/sacred_sources.duckdb 第 25 章） | 改为库内规范路径
6. P3 | 行 19、37-45、61-71 | 文献条目与表格粘连（“［A］**LibreSSL fork 四层辩证链结构**：”后直接接表，三处同款）＋行 71 十条 FreeBSD 社区论文无换行连排＋全半角括号混用（行 71 ［EB/OL］）＋行 19 chmatch_3906“匹配置信度 folder，原因：folder 第207章”元数据异常 | 结构与元数据损坏：列表被表格劫持、置信度字段值非数值 | 分行重排并清理机械匹配残留
7. P3 | 行 71 | FreeBSD 社区论文 10 条（Baldwin 内核 crypto、smart(8)、pfSense/FreeNAS、澳洲医疗 BSD、mandoc、家用路由 Homenet、内核 RNG 等） | 与 OpenNTPD/OpenSMTPD/LibreSSL 章弱相关（仅内核 crypto 与 RNG 两条擦边） | 复核相关性后删除或重配
8. P3 | 行 101-103 | “总纲10 动手者创造历史：总纲10 动手者创造历史：”等 | PODCAST 标签前缀双写三处（282.11 同族） | 去重

- 结论：存在问题 8 项（P0 0、P1 0、P2 2、P3 6）

## 补充说明（正样本与复核留痕）

- 五条要点与 SUMMARY 收录的 209.1-209.5 子节一一对应（LibreSSL 反批评链/OpenSMTPD/OpenNTPD/总纲 13/19/21 审视/Heartbleed 时间线），章级框架完整——问题仅在要点文本截断。
- 辨析考据留痕质量高：三处项目官方页面（openbsd.org/papers/eurobsdcon2014-libressl.html、opensmtpd.org/goals.html、openntpd.org/goals.html）一手核验留痕并摘录原文（"Not the worst bug ever"、"We gutted the junk"、"apply the brakes"、"revolution to evolution"、"Reach a reasonable accuracy…"）；“据原文第25章.md”引注体例正确（第 25 章＝总纲章本体，C343 勘误确立的双轨体例）；一处自标“〔待核：原文截断〕”。
- LibreSSL 时间线三阶段框架正确：2014-04-07 Heartbleed（CVE-2014-0160）→ fork 决议 → portable 首发分流，与 209.5 题目对应。
- 行 63-70“三大 fork 许可证与利益分配对比”表内容相关且结构正确（LibreSSL/OpenNTPD/OpenSMTPD/OpenSSL/NTP Classic/Chrony 六行的许可证、资金机制、市场结果），与前两张复制错误表形成对照——表格素材本身在档，修复清单 2 有据可依。
- PODCAST 双期契合：BSDTalk EP23 系 OpenNTPD 主导者 Henning Brauer 一手访谈（2006，OpenBGPD 九天会话引擎、随机化哲学与 Paul Watson 2004 攻击研究的先后印证、blob 批评、PF 取代 IPF 始末），与本章 OpenNTPD 主题直接相关；BSD Now EP648 的 spamd 灰陷阱/PF→nftables 评估亦属 OpenBSD 安全工具生态；转写讹误（Brower→Brauer、iSarKMPD→isakmpd）逐条自标存疑；史观标注总纲 10/4/9/13 名目（去重后）经权威表核验正确。
- 复核留痕：DB_REF 三个数字经 duckdb 只读实查（2014=20,651 吻合、贡献者 427/427/1,031 三口径均非 3,352）；SUMMARY 收录与章块结构实测第 2024-2031 行；旗标失效判定以实测为准。
