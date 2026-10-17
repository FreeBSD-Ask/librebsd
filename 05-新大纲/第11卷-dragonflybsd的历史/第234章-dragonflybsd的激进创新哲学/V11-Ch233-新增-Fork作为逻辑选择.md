# Fork 作为逻辑选择——Dillon 从 4.x 而非 5.x 分叉的不可通约论

## 要点

2003 年 Matthew Dillon（马修·狄龙） 宣布从 FreeBSD 4.x 分支创建 DragonFly BSD 时，外部观察者普遍质疑这一决策：FreeBSD 5.x 正在推进 SMPng 多核支持，为何不从 5.x 分叉？Dillon 在 dragonfly.kernel 邮件列表中的回应是：“FreeBSD 5 的架构方向是重写 SMP 以微内核化——这与我认为的 OS 内核并发设计是根本不同的两类范式。”Dillon 选择 4.x 作为起点，因为 4.x 的 Giant Lock 单核模型提供的是一个“可被重新设计的系统”，而 5.x 的 SMPng Fine-grained Locking 已经将特定的并发设计（mutex/rwlock/sx 锁层级）深嵌在内核结构中——这些结构在形式上自洽，但 Dillon 认为它们在逻辑上不可通约于（incommensurable）他想要的轻量级线程模型（LWKT）。

**02-sacred源材料/shigang.md** §4 逻辑学指出：“逻辑不是世界本身的结构，而是人类认知框架的结构。将逻辑与本体挂钩是一种形式主义的僭越。”（15.1）Dillon 的决策展示了这一点：5.x 的 Fine-grained Locking 在 FreeBSD 社群的认知框架中被视为“逻辑上必然的方向”——所有现代 OS 都这样做——但 Dillon 发现了这一“逻辑”的形式主义本质。Fine-grained Locking 之所以成为“逻辑必然”是因为 FreeBSD 的认知框架预设了用锁来解决并发——而这一预设本身可被挑战。Dillon 挑战的不是 5.x 的实现质量，而是 5.x 的认知框架本身——两个系统在基本前提上的不可通约使得 fork 成为唯一的逻辑路径。

## 史料

- Dillon M. “DragonFly BSD announcement”（2003-07-16）——DragonFly kernel@ 列表首帖，阐述选择 4.x 作为起点的技术原因。
- Dillon M. “Light Weight Kernel Threading vs Scheduler Activations”（2003-11-08）——DragonFly kernel@ 列表长文，系统语言对比 LWKT 与 FreeBSD 5.x KSE/SMPng 的范型差异。
- Kamp P-H. “FreeBSD 5.0 稳定性的批评”（中文译述，2003-07-22）——PHK 在 FreeBSD-current@ 列表中公开批评 5.x 的稳定性时说 “我们用两年时间把一个不稳定的系统替换成了另一个不稳定的系统”。
- FreeBSD Project. FreeBSD 5.0-RELEASE Announcement [EB/OL]. (2003-01-19)——FreeBSD 5.0 是首个启用 SMPng 的生产版本，其稳定性问题直至 5.3（2004-11-06）才基本解决。
- Lehey G. *The Complete FreeBSD* [M]. 4th ed. 2003——附录记载 5.x 的架构争议与 Dillon 的分歧。

## 史观

**总纲第 25 条（逻辑是形式主义而非世界本身的结构）**——**02-sacred源材料/shigang.md** §4 逻辑学 15.1 节：“逻辑不是世界本身的结构，而是人类认知框架的结构。将逻辑与本体挂钩是一种形式主义的僭越。”Dillon 对 FreeBSD 5.x 的拒绝就是拒绝“Fine-grained Locking 是唯一逻辑”。逻辑的有效性仅限于“形式主义化的非存在领域”（15.1），超出此范围便沦为独断论。5.x 的架构选择在 FreeBSD 的形式主义内部自洽，但 Dillon 站在了这个形式主义的外部——两种不同形式主义之间不可通约。

**总纲第 4 条（分离聚合是永恒规律）**——见 **02-sacred源材料/shigang.md** 4.1 节：“UNIX 分裂出各种 BSD，BSD 又分裂出 FreeBSD、NetBSD、OpenBSD、DragonFly BSD，此乃分离；而各分支间的代码共享、ports 互通、社区人员的流动，此乃聚合。”DragonFly 的 fork 是分离的典型案例，但 DragonFly 继而从 FreeBSD 的 CAM SCSI 子系统、NFS 服务器等组件中继续拉取代码——分离聚合循环从未停止。

**自反性声明**：本子节将 Dillon 描述为“跳出 FreeBSD 认知框架的人”——但这一描述本身设立了“框架内/框架外”的认知，即本子节预设了两个分立的形式主义空间。这与 **02-sacred源材料/shigang.md** §29 空间哲学 20.5 的“中心与边缘”同构——Dillon 的 DragonFly 站在 FreeBSD 的边缘，恰恰是边缘提供了看清中心的可能。

## 辨析

**Dillon 的 LWKT 是否真的超越了 Fine-grained Locking？**：Dillon 的轻量级内核线程模型在单核-双核时期（2003-2007）确实展示了更好的稳定性，但 DragonFly 在 2011-2019 年间反复改写调度器才能支持多核（Hammer2 等）。部分二手资料声称 “Dillon 证明了 Fine-grained Locking 是错的”——考据结论：Dillon 从未这样说；他的批评针对的是 “自始至终把 Fine-grained Locking 当作唯一正确的并发设计框架” 这一认知封闭。DragonFly 最终引入的混合锁机制实际上融合了两种并发的元素——不是 LWKT “战胜”了 SMPng，而是两种范式在时间中汇流。

**不可通约论与分离决策的关系辨析**：Dillon 在 2003 年的决策不能仅被理解为“技术范式不可通约”。他同时也是 FreeBSD Core Team 内部对 5.x 方向表达异议的 “少数人”。fork 是技术+政治的双重决策——不可通约论提供技术合法性给已经不可调和的政治分歧。

## 文献

[1] Dillon M. DragonFly BSD announcement [EB/OL]. dragonflybsd.org, 2003-07-16.

[2] Dillon M. LWKT vs Scheduler Activations [EB/OL]. dragonflybsd.org kernel@, 2003-11-08.

[3] Kamp P-H. FreeBSD-current@ critique of FreeBSD 5.0 stability [EB/OL]. freebsd.org, 2003-07-22.

[4] Lehey G. The Complete FreeBSD [M]. 4th ed. Walnut Creek: BSDi, 2003.

White H. Metahistory: The Historical Imagination in Nineteenth-Century Europe [M]. Baltimore: Johns Hopkins University Press, 1973.

