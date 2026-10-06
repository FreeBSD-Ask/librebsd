---
chapter: 第 315 章
id: CH315
volume: 第17卷-政治制度与社区治理
---

# 第 315 章 基金会治理模式与治理范式演变

## 要点

- 两类基金会的 990 表数据比较须包括——收入规模、收入来源（捐赠/会员费/赞助/投资收益）、支出结构（项目支出/管理支出/筹款支出）、资产规模、董事会构成、员工规模、最高薪酬员工等；FreeBSD Foundation 与 Linux Foundation 的治理文件比较须包括——Articles of Incorporation、By-Laws、董事会选举程序、会员体系（如有）、项目托管协议；
- 批评方认为 BSD 三大项目（FreeBSD、NetBSD、OpenBSD）的治理模式在三个方面存在结构性缺陷——其一，核心团队制缺乏民主性：FreeBSD Core Team 由 active committer 选举产生（2000 年章程规定每 2 年改选全部 9 席、由 9 名当选 committer 组成 Core，2026 年 5 月 27 日通过的新章程改为每年选举、7 名投票成员并设任期限制〔注：句尾原文截断，按本文件辨析行“任期限制/2028 年生效”语境收束，细节待新章程原文核对〕）
- 反批评方认为，BSD 项目的治理模式选择不是“现代化不足”而是有意识的工程哲学选择——其一，核心团队制的精英主义优势：FreeBSD Core Team 由 active committer 选举产生而非全体用户普选，是工程合理性而非民主缺陷——只有 commit bit 持有者才具备判断技术决策的工程深度，将选举权限制在 active committer 群体内保证了技术决策的工程导向而非政治导向
- 再回应方指出，反批评的四个论点均存在结构性局限——其一，“精英主义优势”论证忽视了精英主义的代际传承危机：FreeBSD Core Team 的连任现象（参见 18.12.7“基金会-核心团队来回轮换”批评）显示精英主义在实践中可能退化为小圈子循环——Core.10（2018-2020）回顾显示 Hiroki Sato（佐藤広生）已任 7 届、John Baldwin（约翰·鲍德温）6 届、W〔原文截断，后续连任者名单待回 Core.10 回顾原文补全〕
- 综合三层辩证，BSD 治理模式的批评、反批评与再回应揭示了治理选择的多维张力——其一，“核心团队制缺乏民主性”批评在选举权封闭维度成立（active committer 群体筛选使选举权具有精英性），但在工程合理性维度不成立（反批评层的“技术决策应由具备技术能力的人做出”论证成立）；然而“精英主义优势”在代际传承维度存在代价（再回应层的“代际传承危机”论证成立），2026 年 FreeBSD 新章程的任期限制即为此代价的制度回应

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_10431] BSD Now 第 676 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10446] BSD Now 第 674 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10487] BSD Now 第 665 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10493] BSD Now 第 664 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10517] BSD Now 第 661 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10522] BSD Now 第 659 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10551] BSD Now 第 654 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10595] BSD Now 第 645 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10601] BSD Now 第 644 期，匹配 CH315 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10620] BSD Now 第 641 期，匹配 CH315 章，关联度 1.0

## 史观

- 总纲第 13 条——法律与道德是利益分配：基金会治理（990 表、会员费、董事席位）本质是资源与话语权的利益分配结构
- 总纲第 21 条——革命与改革：2026 年新章程以渐进改革回应代际传承批评，体现 FreeBSD 工程文化的改革式路径
- 总纲第 10 条——动手者创造历史：active committer 群体的持续技术劳动是治理与工程的实际基础
- 总纲第 8 条——本体论上各方平等：FreeBSD 与 Linux Foundation 两种治理模式同源不同途，不构成优劣单一线性
- 总纲第 23 条——一切历史写作都是基于哲学设定的历史小说：本章批评—反批评—再回应的三分辩证本身是哲学设定下的书写选择
- 专题语（不设条号）：“工程合理性”与“代际流动性”的张力为本章核心论旨；总纲第 1、4、5、9、14、19 条映射散见于本文件文献行，留待子节互证后归位

## 辨析

- 990 表的会计口径差异须明确（如会员费归类、项目支出定义）；用户文章的比较框架须考据；两类基金会的规模差异（百倍以上）使直接比较须控制规模变量
- 批评须区分“形式民主”与“实质民主”——FreeBSD Core Team 选举在形式上是民主的（active committer 一人一票），但 active committer 群体的筛选机制使选举权本身具有精英性；【0 信任原则·Linux Foundation 模式参照的限度】Linux Foundation 模式被作为“治理现代化”参照须考据——Linux Foundation 的会员制企业渗透机制须有具体决策记录支持（参见下条 0 信任限定）
- 反批评须避免简单反转——“精英主义优势”论证须对照精英主义可能带来的社区萎缩代价（参见 18.12b 再批评层）；“小团队效率高”论证须对照小团队模式在快速响应（如 CVE 披露）上的实际表现；【0 信任原则·Linux Foundation 商业渗透的实证】“Linux Foundation 模式企业渗透”论证须有具体案例支持——企业会员通过会费影响项目方向的具体决策记录须考据，不得仅以 501(c)(3)/(c)(6) 税务身份推断其治理优劣
- 再回应须避免单边批判——“代际传承危机”论证须对照 OpenBSD 实际传承规划（如有）与 FreeBSD 2026 新章程任期限制的实际效果（2028 年后须观察）；【0 信任原则·资源匮乏归因辨析】“BSD 治理资源匮乏”论证须区分“治理模式导致的资源匮乏”与“历史时机导致的资源匮乏”——Linux 因 1991 年诞生恰逢 BSD 诉讼真空期获得先发优势（参见相关章节 BSD 诉讼部分），此种资源差异的归因须区分治理模式与历史时机两层因素
- 合图是否过于中庸——是否有明确的改革建议；【0 信任原则·合图的非终结性】合图并非辩证链的终结而是阶段性综合，随 BSD 治理改革（如 2028 年 FreeBSD 新章程生效、OpenBSD 传承规划公开、NetBSD Foundation 治理调整）须重新展开；【0 信任原则·合图的非折中主义】合图不是“BSD 在工程上合理、在现代化上不合理”的简单分类，而是揭示“工程合理性”与“代际流动性”之间的张力

## 文献

- FreeBSD Foundation 990 表；Linux Foundation 990 表；两类基金会章程；用户文章 ［A］
- FreeBSD Core Bylaws [EB/OL]. <https://www.freebsd.org/internal/bylaws/>；NetBSD Foundation bylaws [EB/OL]. <http://www.netbsd.org/foundation/bylaws.html>；OpenBSD Project Goals [EB/OL]. <https://www.openbsd.org/goals.html>；Linux Foundation Bylaws ARTICLE III §3.1；FreeBSD Committer's Guide [EB/OL]. <https://docs.freebsd.org/en/articles/committers-guide/#admin>；参见 18.12.1 与 18.12.7 子节史料〔旧结构节号，现行对应待结构映射核验〕 ［A］
- FreeBSD Core Bylaws；NetBSD Foundation bylaws；OpenBSD Project Goals；Linux Foundation Bylaws ARTICLE III §3.1；FSF 官方许可证列表 [EB/OL]. <https://www.gnu.org/licenses/license-list.en.html>；参见 16.7.3 与 17.10a 子节史料〔旧结构节号，现行对应待结构映射核验〕 ［A］
- FreeBSD Core Team Activity Reports；2026 年 FreeBSD 新章程；FreeBSD Foundation 年报；Linux Foundation 2023 年报；参见 17.10b 与 18.12b 子节史料〔旧结构节号，现行对应待结构映射核验〕 ［A］
- 上述 16.7a-c 节辩证链所有文献综合；FreeBSD Core Bylaws；Linux Foundation Bylaws ARTICLE III §3.1；参见 16.7.1-16.7.4、17.10、18.12 子节史料〔旧结构节号，现行对应待结构映射核验〕 ［A］
- 项目史观总纲第 13、19、21、23 条；IRC §501(c)(3) 与 §501(c)(6) 原文；FreeBSD Foundation IRS Determination Letter（2000-12-07）；FreeBSD Core Bylaws；Linux Foundation Bylaws ARTICLE III §3.1；OSDL 合并档案（2007-01-22）；FSF 官方许可证列表 [EB/OL]. <https://www.gnu.org/licenses/license-list.en.html>；freebsd-advocacy 邮件列表存档 [EB/OL]. <https://lists.freebsd.org/archives/freebsd-advocacy/>；第 16.7a-d 节辩证链补足〔旧结构节号，现行对应待结构映射核验〕；第 16.7.1-16.7.4、17.10、18.12 节史料〔旧结构节号，现行对应待结构映射核验〕；参见相关章节 BSD 治理改革与许可证哲学部分史料 ［A］〔注：行尾原有粘贴残片“---## 史料登记与辩证校准（2026-08-08 追加）> 本卷命题：24.1 少数与多数…### 史料文献”系模板残片（仅标题与指向 00-总览 的重复指针、无实质内容），已于 2026-09-12 整改清除〕
- 上述各子节文献综合；FreeBSD Foundation 年报；参见相关章节关于 FreeBSD Foundation 与 Linux Foundation 治理模式比较及公众认知的史料；项目史观总纲第 1、4、5、8、9、10、13、14、19、21、23 条（见 据原文第 25 章、据原文第 14 章 14.2 节、据原文第 21 章 21.1-21.2 节、据原文第 23 章 23.1 节） ［A］
- 媒体报道档案；公众认知调查；用户文章 ［C］

<!-- ROW_MINE: login-zazhi.articles.CL-1-128 -->
**一手刊文**（证据等级：L4，来源：`historical_claims.duckdb.claim.CL-1-128`；login 逐条遍历判定采纳）

Mary Ann Horton 作为原 BSD Unix 团队成员，在 Bill Joy 离开后长期维护 vi；她发明 uuencode/uudecode 以解决电子邮件仅能传输 7 位字符时二进制文件的发送问题；后在 Bell Labs 合著 RFC 976（UUCP 邮件格式）与 RFC 1036（Usenet 消息格式）。。引用时按 L4 纪律：以上为 ;login: 一手发表文本，属一手出版物证据，具体技术结论仍须以源码与提交记录复核为准，不得单独引为定论。

