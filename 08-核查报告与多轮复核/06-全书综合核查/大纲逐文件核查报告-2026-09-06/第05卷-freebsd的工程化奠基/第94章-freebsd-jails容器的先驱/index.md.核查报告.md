# 核查报告：第05卷-freebsd的工程化奠基/第94章-freebsd-jails容器的先驱/index.md

- 源文件：d:\librebsd\05-卷册大纲\第05卷-freebsd的工程化奠基\第94章-freebsd-jails容器的先驱\index.md（365 行，分次完整通读）
- 批次：C629；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（辅以 freebsd.duckdb commit 实测、权威总纲表比对与 SUMMARY 实测）
- SUMMARY.md 收录：实测第 944 行（本章索引条目），批次 UNLISTED 旗标失效
- A 占位符：〔待核：原文截断〕与〔待核·needs_fix〕为自标留痕（随条目 2/4 登记）
- B 内容完整性：多处句中截断（见清单条目 2）
- C 编号与标题：93.x 旧章号节八处且两节重复出现（见清单条目 1）
- D 格式规范：通过
- E 学术规范：发现 3 处（见清单条目 3/4/5）
- F SUMMARY 一致性：通过

## 问题清单

1. P2 | 行 29-107 | 节号混乱与重复节：93.1.2/93.10.2/93.11.2/93.2.2/93.3.2/93.4.2/93.5.2 七个 93.x 旧章号节插入章索引体例（本章为 94），且 93.2.2 jail(2) 的系统调用设计 与 93.3.2 与 Docker 的时间差 各出现两次、两版本内容详略不一——章索引与残段混杂、结构无序 | 逐节比对 | 统一节号为 94.x、去重、或明确拆分归属
2. P2 | 行 37/47/53/71/76/81 等 | 多处句中截断：比 Solaris Zones(2〔待核：原文截断〕、辨析 后文待回源、jail 结构 增加网络绑定、进程可见（断）、ph（断）、jail(2) 聚合文件/网（断）、chroot→jail(2)→Solaris Zon（断）等，部分自标〔待核〕部分无标记 | 逐行可见 | 回源补全
3. P3 | 行 17-28/48/89/103 | 史观伪标签五处：总纲第 1 条——偶然性改写历史（两处，权威第 1 条为一切真历史都是古代史）、第 25 条——终结与延续（权威第 25 条为逻辑是形式主义而非世界本身的结构）、第 3 条——形式主义膨胀（权威第 3 条为不存在进步只有权力再分配）、第 22 条——开源运动（名目非权威）；第 4 条——分离与聚合（近名目，缺 永恒规律 尾） | 比对权威表 | 去号或统一名目
4. P3 | 行 62-64 | dangan-20260908 消解回写块含 ［待核·needs_fix］未决标记（FP-2016-015 Jail Networking，DKC-1873→fulltext:5997）——消解未完成即回写 | 块判读 | 完成 needs_fix 或移出正式文本
5. P3 | PODCAST 区 | EP223（bhyve Dexter）与 94.4、EP616（Goodkin/Gibbs）与 97index、EP7（PHK）与 137.5 重复注入——跨章重复注入族 | 与已核文件互证 | 按首发章分工

- 结论：存在问题 5 项（P0 0、P1 0、P2 2、P3 3）

## 补充说明（正样本与复核留痕）

- 要点首条的 commit 级修正为章级标杆：经 bsd_commits.duckdb commits 表与 commit_files 表交叉验证，Jails 确切诞生日为 1999-04-28（commit 02daf150a4434305b9181b0ac9150762afb4c8ce）——经主线 duckdb 实测逐字段吻合（freebsd-src，Poul-Henning Kamp，1999-04-28T11:28:49Z，Add the jail system call.），且要点明确指出旧叙事 2000.3.14 与 2000.3 两种说法均不准——以代码级证据终结日期两说并存。
- 要点第五条（再回应四点）为跨文件辩证的高质量延伸：VMware 2018.2.27 博客引文（a jail could only have one IPv4 address...）确证批评针对设计层限制而非旧版本；被动跟进（In response to the emergence...）的时间线对照（VNET 8.0/IPv6 更晚 vs Zones 2004/LXC 2008）；以版本更新否定批评的形式主义识别；以及 phk 本人 jails saga 标题直书 Jails – High value but shitty Virtualization 的作者自评与外部批评交叉印证——反批评因此失去效力 的结论由作者自我认知支撑，论证完整。
- 辨析审慎：Georgiev 博客定性为员工署名技术博客而非 VMware 公司正式立场；phk 行文惯用自嘲、shitty Virtualization 是否构成劣币自我承认须结合行文风格判断；Docker 劣币判定以生态完整性为标准则 Docker 非劣币——反劣币修辞的边界自觉。
- PODCAST 20 期正扣 jails 生态：EP499 Dan Langille FreshPorts 迁移史（IAC Systems 捐赠主机失效→AWS、三 jail 拆分、40 jail 家庭实验室、Syncoid 迁移省电 25%）与 BSDCan 二十年；EP513 新主持人 Jason Tubner 与生产使用反馈循环；EP406 Michael Lucas 进入 BSD 的第一手动因；文献 20 条著录规范（含 EuroBSDcon 2024 Dan Langille stupid things with jails 视频）。
- 史观部分名目正确者用得精准：总纲 11 商品是形式主义两次（版本更新话语的市场形式主义、容器市场选择）均为权威名目直用；自反性声明齐备。
