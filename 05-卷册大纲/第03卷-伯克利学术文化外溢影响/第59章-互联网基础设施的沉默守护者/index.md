---
chapter: 第 59 章
id: CH59
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 59 章 互联网基础设施的沉默守护者

## 要点

- BIND（Berkeley Internet Name Domain，伯克利 CSRG 四名研究生 Terry/Painter/Riggle/Zhou 1984 年开发，DNS 协议 RFC 882/883 1983 年 11 月标准化）与 Sendmail（1983 年随 4.2BSD 正式发布）长期主导互联网 DNS 与邮件传输市场，但 1990 年代后期两者均面临严重安全挑战——BIND 4
- BSD 作为互联网沉默支柱的辨析：（1）BSD 的 BIND/Sendmail/TCP/IP 在 1980-1990 年代是互联网基础设施核心，但 BSD 系统的市场份额在 1990 年代后期被 Linux 超越；（2）BSD 的 “沉默” 源于其许可证宽松（无需署名）与基础设施性质（用户不直接接触）；（3）BSD 作为沉默支柱的具体辨析基于实际部署数据——BIND 1990 年代约 90% DN
- 互联网基础设施边缘贡献者的史料辨析：（1）BSD 源码贡献者记录（CHANGELOG、SCCS 日志）是辨识边缘贡献者的主要史料，但 CSRG 时期（1978-1992）记录不完整，4.4BSD-Lite 之后的 CVS/SVN/Git 记录较完整；（2）邮件列表存档（如 IETF 邮件列表、CSRG 内部邮件）可补充源码记录，但存档可能存在截取、邮件丢失、事后编辑，须通过多个独立存档交叉验证；（

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_1548] 卷“第03卷-伯克利学术文化外溢影响”第 59 章，匹配置信度 0.9，原因：关键词搜索下载文献，标题含章节主题

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- BIND/Sendmail 被 “淘汰” 指主导地位被多元替代方案挑战，而非完全弃用——BIND 9 与 Sendmail 在 BSD 与 Linux 中仍保留一定份额，须区分 “主导地位退场” 与 “完全弃用”；Dan Kaminsky 2008 年漏洞（CERT VU#800113）是 DNS 协议设计层缺陷（事务 ID 仅 16 位 + 源端口固定），影响所有未实现源端口随机化的 DNS 实
- BSD/Linux 市场份额演变——Netcraft 统计显示 1990 年代后期起 Linux Web 服务器部署份额逐步超越 BSD 系统的部署份额（定性趋势确认，定量数据保留 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]）；Linux 借鉴 BSD 代码的具体案例——Linux NET-2 借鉴 BSD 网络代码（含 BSD 版权声明，与 23.
- 源码贡献者记录的完整性——BSD 源码 CHANGELOG 与 SCCS 日志为辨识边缘贡献者的主要史料，但早期（CSRG 时期 1978-1992）记录不完整，4.4BSD-Lite 之后的 CVS/SVN/Git 记录较完整；邮件列表存档的截取情况——IETF 邮件列表与 CSRG 内部邮件存档可能存在截取、邮件丢失、事后编辑，须通过多个独立存档（如 marc.info、ietf.org 邮件

## 文献

- BIND/Sendmail 漏洞公告；BIND 9 发布记录；PowerDNS/Unbound/Postfix/qmail 发布记录；Dan Kaminsky 2008 DNS 漏洞披露；CVE 数据库[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]
- BSD/Linux 市场份额数据（Netcraft）；Linux 代码档案；Apache 档案；McKusick (1999) "Twenty Years of Berkeley Unix" ［A］### 史观映射> 互联网不是从硅谷的车库里诞生的，而是从伯克利的终端室里长出来的。BIND 让全球的域名得以解析，Sendmail 让全球的邮件得以送达，BSD TCP/IP 栈让全球的数据包得以路由——这些技术构成了互联网的神经系统，但写下它们的人从未出现在任何互联网创业的封面上。ARPANET 到 NSFNET 的二十年是互联网从军事实验到学术骨干再到公共基础设施的转型期，而 BSD 系统恰好站在了每一个转折点上——不是作为主角，而是作为那个沉默的、在后台运转的操作系统。当 IETF 说 "rough consensus and running code" 时，他们说的其实就是 BSD 的工程哲学：先跑起来，再谈标准。当万维网从 CERN 传遍全球时，跑着 Apache 的 BSD 服务器已经在为第一批网站提供服务——但它们从未被看见，因为真正的互联网基础设施本就不该被看见---## 第 23.12 不同时期人员的采访录（详见 [采访录.md](采访录.md)）## 第 23.13 节 媒体反响与社区舆论（详见 [媒体反响与社区舆论.md](媒体反响与社区舆论.md)）
- BSD 源码 CHANGELOG/SCCS 日志；IETF/CSRG 邮件列表存档；Allman/Vixie 回忆录；0 信任原则方法论 ［A］

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP378、BSD Now EP323、BSD Now EP165、BSD Now EP56、BSD Now EP1（共 5 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- Michael W. Lucas 访谈综述：SNMP 新书以克苏鲁恐怖为主题做特别版《Networknomicon》，含虚构的 Miskatonic University 图书馆印章（“勿从金库取出”“勿实现”“勿读”）与 Grimoire 书衣，并把定价刻意设为 66.66 美元，作为赞助者的赠书而非普通商品；TLS 书则改用《公主新娘》主题为枯燥内容增色，因为“结合 TLS、恐怖与 2020 年的美国”过于沉重。（BSD Now EP378，[337.1-424.24]，L1）
- SNMP 史与技术观：SNMP 取代了更早的 Gateway Management Protocol，且诞生于“字节总是 8 位”尚未成为共识的年代；Lucas 回忆 1997 年遇到一台完全靠 SNMP 配置、没有命令行的 Bay Networks 路由器，感叹这是“美好的想法未能经受现实考验”；他当初学 SNMP 时以为只是只读监控，得知可写以配置交换机、路由器时感到“邪恶”，但也承认线路拥塞无法 SSH 时可用单个 SNMP 包关闭接口来争取时间。（BSD Now EP378，[272.06-771.48]，L1）
- 监控的方法论难点在选择：一个小的 BSD 虚拟机经一次 SNMP walk 就能拉出上千项特性，直觉是“因为能画图就全部画图”，但决定监控什么才是真正的困难；Alan 补充 FreeBSD 12.2 从新版 ZFS 引入 per-dataset 读写字节与 IOPS 统计（经 sysctl），可用脚本暴露给 SNMP，用于定位哪个客户或虚拟机在制造磁盘负载，但数百个 dataset 会爆炸成上千维计数器，必须选择性采集。（BSD Now EP378，[787.2-1001.24]，L1）
- TLS 史的僵尸化案例：证书 subject 中的 common name（CN）在 1995 至 2000 年间有效五年后即被判定为问题并应于 2011 年停用，却以“mostly dead”状态继续存续约四倍于其正式寿命，说明互联网上废弃特性的惯性远大于预期；SSL3 可追溯到 1999 年，浏览器已基本弃用旧版本，只应运行 TLS 1.2 与 1.3。（BSD Now EP378，[1087.84-1239.08]，L1）
- 证书生命周期与 ACME：长寿命证书使旧技术难以下线（需提前数年停止签发），短寿命证书则缩短密钥泄露窗口并强迫自动化续期；Let's Encrypt/ACME 以极短有效期“逼迫你做正确的事”，有银行甚至签发不足 24 小时的证书并每几小时续期推送；证书撤销受制于 CRL 体积与 OCSP 的拒绝服务风险，故证书越短、对证书的控制力越强。（BSD Now EP378，[1800.52-1974.68]，L1）
- TLS 拦截与安全语义批判：Lucas 详述以 Squid 等代理做 TLS 拦截时，代理用自签或受托证书把过期、自签的“坏”证书伪装成有效证书呈现给用户；他认识的一位 appliance 厂商故意保留自签警告，拒绝隐藏拦截事实；TLS 1.3 伪装成 TLS 1.2 以穿透中间盒，恰说明拦截设备中存在大量营销式“安全”话术。（BSD Now EP378，[1396.34-1547.64]，L1）
- Lucas 在 TLS 书开头抨击“security”一词已失去意义：它像“人人每天吃热巧克力圣代还永不长胖”的空洞承诺；他承诺除引言外全书不使用该词，只用机密性、认证等具体术语，并把自己的写作责任定义为解释 x509 为何如此、TLS 1.3 为何如此行事，而非诉诸“标准机构腐败”或“计算机都是错误”的默认解释。（BSD Now EP378，[1514.52-1701.54]，L1）
- Cashflow for Creators 的创作者经济：Lucas 写书公开其小企业现金流运营法，指出市面商业书面向开加盟店或雇百人的读者，而创意小企业无书可依；该书恰在疫情初期发布，他因早已备好灾难预案、立即压缩开支而挺过疫情，反观大企业（如达美航空）疫情首周即向政府索要百亿美元；小企业只能靠现金流预案自救，这本质上是把系统运维的灾难恢复思维移植到商业。（BSD Now EP378，[2087.66-2447.58]，L1）
- 疫情与未来计划：因会议取消、无法赴会售书签名，Lucas 改做一次性直接邮件售书并清理库存；他预计 2022 年才可能再见，且不愿仅为见面而旅行；未来计划包括 TLS 书、科幻小说 Drinking Heavy Water、DNS 书修订、小型 OpenBSD 书，以及把文件系统传入 bhyve 的 9PFS 及其“邪恶”。（BSD Now EP378，[2472.78-3157.94]，L1）
- 计算机历史博物馆发布“最早 Unix 代码”周年源码版，收录 PDP-7 汇编清单（Space Travel、moo、井字棋等），经 Warren Toomey 与 John Mashey 等鉴定可溯至 1970 至 1971 年初。（BSD Now EP323，[167.90-193.82]，L2）
- Leonard Kleinrock 受访回顾 1969 年 10 月 29 日 UCLA 发出的“LO”消息：他预见网络“始终在线、无处不在、不可见”，但未预见其社交化与国家安全化，并拒绝为创造互联网而后悔。（BSD Now EP323，[486.68-671.22]，L1）
- OpenBSD 自 1995 年 10 月 18 日起跨过 40 万提交，Theo de Raadt 提醒计数口径不一；主持人补充 FreeBSD 约 92.5 万、NetBSD 加 pkgsrc 约 60 万，强调跨项目比较不可靠。（BSD Now EP323，[1095.24-1167.46]，L2）
- Blacklistd 作为 fail2ban 替代，通过 libexec helper 与 NPF 联动按失败认证次数封锁 IP；教程演示 securelevel=1 下需把模块编入内核或经 modules.conf 预载。（BSD Now EP323，[685.00-1027.92]，L2）
- “OSI 七层墨西哥卷饼”作者自建 DoH 服务器与私有 CA，把 Firefox 的 TRR 指向本地，以对抗浏览器厂商对 DNS 的集中收编，而非简单禁用。（BSD Now EP323，[1862.22-2002.76]，L2）
- 节目号召 BSD 社区在 ARIN 咨询委员会选举中投票，候选人 Ike 参选以代表 BSD 社区，在负责 IP 地址分配与管理的机构中发声。（BSD Now EP165，[99.14-175.64]，L2）
- ARIN 候选人页面提供每位候选人的背景、简历与对特定问题的回答；选举于本周早些时候开始、周五截止，持有 ARIN netblock 或 AS 号的联系人可投票。（BSD Now EP165，[190.58-250.16]，L2）
- OpenBGPD 新增对 draft RFC Large Communities 的支持，以三个 32 位值表达命名空间所有者与两个不透明值，解决 16 位 AS 号时代 communities 字段编码能力不足的问题。（BSD Now EP165，[1396.16-1609.12]，L2）
- 节目回顾早期互联网以 16 位 AS 号与 32 位“us+them”社区字段编码路由信息，32 位 AS 号普及后无法在单一 32 位值中表达两个 32 位 AS 号，遂需 Large Communities。（BSD Now EP165，[1406.5-1504.98]，L2）
- OpenBSD-current 已支持 Large Communities，预计随 OpenBSD 6.1 发布，部分基于 Job Snijders 的补丁。　[存疑脚注] 补丁作者姓名转写须核验。（BSD Now EP165，[1577.06-1615.68]，L2）
- CTL HA 由 Alexander Motin 与 iXsystems 完成并于约一年前提交，实现 ALUA，使主机可同时经两个控制器访问同一 LUN；Mikhail Zakharov 正将 Beast 存储设备从自定义仲裁器切换到 CTL HA。（BSD Now EP165，[1929.08-2090.68]，L2）
- CTL HA 提供 active/standby 与 active/active 模式，可按 LUN 指定主控节点，使多个 LUN 在两个控制器间分摊流量以获取更高带宽。（BSD Now EP165，[2121.16-2170.54]，L2）
- GSoC 学生 Abdali Kaltai 撰写首个 FreeBSD 内核模块教程，讲解模块事件处理、DECLARE_MODULE 宏与 bsd.kmod.mk 构建流程。（BSD Now EP165，[623.7-912.64]，L2）
- FreeBSD.org 集群由约一百三十台机器分布于全球六个地理位置，并运行一百一十多个 jail，广泛使用 ZFS、PF、VLAN 与 GeoDNS。（BSD Now EP56，[574.76-657.04]，L1）
- 集群长期在开发分支 head 上运行以对最新代码进行真实负载压力测试，并已转向统一二进制构建以替代逐机 make world。（BSD Now EP56，[1126.38-1225.00]，L1）
- 2012 年安全事件源于开发者经被攻破的大学网络跳板泄露 SSH 密钥，攻击者抓取连接关系并回连个人主机；David Wolfskill 因发现异常登录而触发追踪。（BSD Now EP56，[2102.38-2305.54]，L1）
- 事件后集群改为机器间互不信任、拉取而非推送、审计记录入密封存储，并尽量以 JBOD 取代不可靠的硬件 RAID 控制器。（BSD Now EP56，[2022.30-2423.84]，L1）
- 该期头条报道 FreeBSD 10-CURRENT 合入 Radeon KMS 内核图形驱动，标志 FreeBSD 桌面图形栈由传统驱动模式向内核模式设置过渡，并为 10.0 发布前的驱动测试提供基础。（BSD Now EP1，[70.30-125.02]，L2）
- VeriSign 公开拥抱 FreeBSD，以之支撑 .com、.net 等顶级域名的 DNS 根服务器；主持人归纳其选择理由为平台稳定、高并发查询处理能力与社区可回馈性。（BSD Now EP1，[281.60-311.04]，L2）
- Peter Hessler 的 BGP SpamD 以 BGP 协议实时分发垃圾邮件黑名单与白名单：黑名单社区属性为 666、白名单为 42，运营于私有自治系统 AS65066，并以 OpenBGPD 为基础。（BSD Now EP1，[4554.19-4919.96]，L1）
- FreeBSD 基金会 2013 年春季筹款募集 219806 美元，来自 12 家企业与 365 名个人捐赠者；为维持 501(c)(3) 免税地位，个体小额捐赠被视为关键支撑。（BSD Now EP1，[1879.13-1939.54]，L2）

**史料**：

- Michael W. Lucas 关于 SNMP 书、TLS 书与 Cashflow for Creators 的写作动机、出版机制与销售方式的当事人自述。（BSD Now EP378，[337.1-2294.02]，L1）
- Lucas 亲历的 1997 年 Bay Networks 纯 SNMP 路由器与 SNMP 可写配置交换机/路由器的运维经验，属网络管理史的一手口述。（BSD Now EP378，[726.36-771.48]，L1）
- FreeBSD 12.2 引入 per-dataset ZFS 读写统计的 sysctl（Alan Jude 所述），属 ZFS 观测性的一手工程线索。（BSD Now EP378，[840.34-950.58]，L1）
- 计算机历史博物馆“Earliest Unix Code”目录与 PDF，含 PDP-7 汇编、Space Travel 1970 源码页。（BSD Now EP323，[214.28-234.20]，L2）
- CBC《The Current》对 Leonard Kleinrock 的半小时访谈节选（首条消息“LO”及网络阴暗面）。（BSD Now EP323，[387.08-402.72]，L1）
- Theo de Raadt 致 tech@ 的“OpenBSD 跨 40 万提交”邮件，说明计数困难与仓库历史歧义。（BSD Now EP323，[1100.92-1113.56]，L2）
- unitedbsd.com 的 Blacklistd 与 NPF 教程，及 NetBSD securelevel 与 bpf-jit 配置说明。（BSD Now EP323，[693.04-812.78]，L2）
- ARIN 咨询委员会选举候选人页面与投票说明。（BSD Now EP165，[190.58-250.16]，L2）
- OpenBGPD 对 Large Communities draft RFC 的支持公告。（BSD Now EP165，[1396.16-1615.68]，L2）
- Alexander Motin 的 CTL HA 提交与 Mikhail Zakharov 的 Beast 存储设备设计文档。（BSD Now EP165，[1929.08-2090.68]，L2）
- Peter Wemm 访谈（FreeBSD.org 集群管理员当事人自述）。（BSD Now EP56，[226.16-2846.68]，L1）
- 当事人 Peter Hessler 自述其为 OpenBSD 用户与开发者：2000 年起使用、2008 年起成为开发者，早期从事 ports 移植，后加入 Vantronics 从事 OpenBSD 防火墙与路由器相关工作，并曾运行约 50 个路由域。（BSD Now EP1，[2946.18-3109.14]，L1）
- 当事人自述其 BGP SpamD 聚合阿尔伯塔大学与《The Book of PF》作者 Peter Hanstein 的 SpamD 黑名单，并以 24 小时内命中蜜罐邮箱地址作为黑名单收录口径。（BSD Now EP1，[3984.50-4100.90]，L1）

**史观**：

- 总纲9 经验优先：纯 SNMP 配置路由器的“美好想法”败于真实世界，说明协议的命运由运维现场的经验决定，而非设计愿景：一个想让它成立的愿望并不足以让它成立。（BSD Now EP378，[742.38-760.7]，L1）
- 总纲22 知识注定过时：CN 字段“僵尸化”存续四倍于正式寿命，展示技术知识的过时并非即刻退场：废弃标准在解释学惯性与互操作压力中被反复续命。（BSD Now EP378，[1095.58-1152.4]，L1）
- 总纲18 时间是一种形式主义：证书寿命的短长之争本质是时间形式的治理：寿命越短，对旧技术与密钥泄露的控制力越强，安全能力被转化为证书有效期这一时间参数。（BSD Now EP378，[1816.7-1947.38]，L1）
- 总纲15 文化即形式主义：Lucas 拒绝使用“security”这个被掏空的词，坚持只谈机密性与认证，是对行业话术形式化的自觉抵制：概念的泛化使它失去指涉能力。（BSD Now EP378，[1514.52-1602.9]，L1）
- 总纲3 不存在进步，只有权力再分配：大企业疫情首周向政府要钱，小作者靠既有现金流预案自救：同一次外部冲击下，规模差异决定了谁能把风险转嫁给公共财政、谁只能自我承担。（BSD Now EP378，[2320.76-2350.52]，L1）
- 总纲1 一切真历史都是古代史：总纲1 一切真历史都是古代史：50 年前的“LO”消息与 PDP-7 汇编被当作当下仍须考据的古代对象。（BSD Now EP323，[120.92-125.14]，L2）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：ARPANET 首条消息因机器崩溃停在“LO”而非“LOGIN”，是偶然事件。（BSD Now EP323，[421.34-425.12]，L1）
- 总纲19 解释学循环是历史认识的根本条件：总纲19 解释学循环是历史认识的根本条件：源码断代依赖 Toomey、Mashey 等当事人回忆与目录残迹的循环解释。（BSD Now EP323，[167.90-193.82]，L2）
- 总纲8 本体论上各方平等：总纲8 本体论上各方平等：OpenBSD、FreeBSD、NetBSD 提交数被并置比较时，主持人强调口径差异，避免以数量定高下。（BSD Now EP323，[1161.86-1189.66]，L2）
- 总纲6 和解优于斗争：总纲6 和解优于斗争：DoH 作者不以禁用对抗，而以自建本地 DoH 把集中化化解为自托管。（BSD Now EP323，[1972.26-1999.44]，L2）
- 总纲14 苦难不值得被提倡：总纲14 苦难不值得被提倡：Kleinrock 对网络阴暗面的回顾不美化早期“全员良善”的叙事，也不为创造互联网而后悔。（BSD Now EP323，[587.28-671.22]，L1）
- 总纲3 不存在进步，只有权力再分配：BSD 社区通过在 ARIN 咨询委员会争取代表席位，试图在互联网号码治理中获得话语权，是治理权力的再分配。（BSD Now EP165，[99.14-250.16]，L3）
- 总纲22 知识注定过时：16 位 AS 号与 communities 编码曾足够使用，随网络增长而失效，既有技术知识注定过时并需新形式替代。（BSD Now EP165，[1406.5-1504.98]，L3）
- 总纲9 经验优先：Beast 存储设备从自定义仲裁器转向 CTL HA 内置能力，工程实践沉淀为通用组件。（BSD Now EP165，[1959.6-2090.68]，L3）
- 总纲10 动手者创造历史：CTL HA 与 Beast 的高可用由 Alexander Motin、Mikhail Zakharov 等具体动手者推进。（BSD Now EP165，[1929.08-2090.68]，L3）
- 总纲7 理论必须自反：总纲7 理论必须自反：Peter Wemm 反复以事故教训反观并修正基础设施设计，而非固守既有运维惯例。（BSD Now EP56，[1982.06-2022.30]，L1）
- 总纲5 没有必然性，只有偶然性：总纲5 没有必然性，只有偶然性：2012 年事件由跳板主机、共享 NFS home 与可写 authorized_keys 等偶然叠加而成，并非必然发生。（BSD Now EP56，[2102.38-2192.90]，L1）
- 总纲10 动手者创造历史：总纲10 动手者创造历史：集群由 Peter Wemm、Glen Barber、Sean Bruno 等动手维护者在长周期中持续改造。（BSD Now EP56，[666.00-748.68]，L1）
- 总纲4 分离聚合是永恒规律：BGP SpamD 将阿尔伯塔大学与 Peter Hanstein 各自维护的黑名单聚合为统一的 BGP 分发列表，以本地复制取代中心网站下载与实时 DNS 查询，是分散源向聚合结构流转的具体实践。（BSD Now EP1，[4411.69-4474.51]，L1）
- 总纲8 本体论上各方平等：该期将 FreeBSD 图形驱动、OpenBSD BGP SpamD、NetBSD 6.1.1 等并列报道，未以单一分支为中心，呈现多方平等的叙事格局。（BSD Now EP1，[0.00-125.02]，L2）
- 总纲10 动手者创造历史：BGP SpamD 由 Peter Hessler 个人搭建并维护，访谈记录的是具体动手者对垃圾邮件防御工具的工程选择，而非抽象的项目叙事。（BSD Now EP1，[2946.18-3109.14]，L1）

**辨析**：

- 转写把书名记作 Network-Nomecon、Networkonomicon 等多种形态，标准拼写应以 Lucas 本人发布为准；“Get Sank Murder”疑为转写噪声，可能指其 git 主题书，不宜据此引用。[考据脚注] 书名以 Lucas 官方书目为准　[考据脚注] Networknomicon 及 Get Sank Murder 书名拼写系转写噪声，须以作者官方书目核对（BSD Now EP378，[341.6-343.36]，L4）
- CN 字段“1995-2000 有效五年、2011 年停用”的时间线系 Lucas 口述概括，具体标准号（X.509/各 RFC）与废止过程须以标准文本核验。（BSD Now EP378，[1095.58-1148.44]，L2）
- “银行签发不足 24 小时的证书”为 Lucas 观察到的个案，未经系统统计，引用时不宜推广为行业普遍实践。（BSD Now EP378，[1948.22-1964.54]，L2）
- OpenBSD 的 40 万提交仅为一种测量口径，仓库历史久、有缺失 changelog 与不可转换分支，任何计数都可能高估或低估。　[考据脚注] Theo 本人与主持人双重提示计数不可靠（BSD Now EP323，[1131.88-1154.46]，L3）
- PDP-7 源码断代“1970 至 1971 初”依赖两位早期贡献者与馆方编目，属多源交叉但仍非绝对定年。　[存疑脚注] 定年证据链为多源交叉，非单一权威结论（BSD Now EP323，[167.90-193.82]，L3）
- [存疑脚注] 转写将选举机构记作“Aaron Advisory Council”，应为 ARIN Advisory Council 的误转；候选人“Ike”的全名须核验。　[存疑脚注] ARIN 与候选人姓名须核验。（BSD Now EP165，[99.14-250.16]，L4）
- [存疑脚注] 转写将补丁作者记作“job schneider”，应为 Job Snijders 的误转，须核验。　[存疑脚注] Job Snijders 姓名须核验。（BSD Now EP165，[1595.0-1609.12]，L4）
- 2012 年事件中患者零号的初始入侵路径仅存候选推断，Peter Wemm 自述只有短名单而无确定结论。　[存疑脚注] 初始入侵路径未获确证，属当事人事后推断（BSD Now EP56，[2224.94-2233.42]，L4）
- VeriSign 同时使用 BSD、Linux、Solaris 等操作系统作多样性冗余的说法为主持人转述，其根服务器内部各系统的具体比例未获官方资料核验。　[存疑脚注] VeriSign 各操作系统在根服务器中的具体占比属单一播客转述，须以官方资料交叉验证。（BSD Now EP1，[460.01-478.53]，L4）

**文献**：

- [BSD Now EP378] Pennington J. BSD Now: 378: Networknomicon[EB/OL]. (2020-11-26)[2026-08-15]. https://www.bsdnow.tv/378.
- [BSD Now EP323] Pennington J. BSD Now: 323: OSI Burrito Guy[EB/OL]. (2019-11-07)[2026-08-15]. https://www.bsdnow.tv/323.
- [BSD Now EP165] Pennington J. BSD Now: 165: Vote4BSD[EB/OL]. (2016-10-26)[2026-08-15]. https://www.bsdnow.tv/165.
- [BSD Now EP56] Pennington J. BSD Now: 56: Beastly Infrastructure[EB/OL]. (2014-09-24)[2026-08-15]. https://www.bsdnow.tv/56.
- [BSD Now EP1] Pennington J. BSD Now: 1: BGP & BSD[EB/OL]. (2013-09-04)[2026-08-15]. https://www.bsdnow.tv/1.

<!-- /PODCAST_REVIEW -->
