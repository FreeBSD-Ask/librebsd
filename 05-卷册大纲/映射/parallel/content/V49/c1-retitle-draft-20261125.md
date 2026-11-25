# V49 第 1 章改题拟稿（retitle-V49-c1，G5 线研究子代理，2026-11-25）

> **性质**：改题拟稿（162 号文 v4.1 §15.4.2——拟定面免批；本件只作 spec，不写台账、不改树、不落块）。章题与六节节题不动，仅重拟 30 条小节题；卷／章／节三级题名未触碰。
> **范围**：第 1 章“LWKT 与内核架构重构：从 FreeBSD 分叉到消息传递模型”6 节 30 题（filled 12／skeleton 18）。
> **依从面**：六规则（冒号 0；设问 ≤3；题长有意拉开 8—19，同节极差 ≥6；“的”题同节 ≤半数；禁默认三件套；抽象动名词尾 0；构式族每节 ≥3）＋《小节建制与题名规则》§4.1—§4.4（T6 题长、C1—C6 术语与官方拉丁形、§4.4 人物名双层规则“Matt Dillon 保留拉丁，避‘狄龙’”）＋参照件 §二（实义锚作中心语、版本锚定、题长不齐、平行须递进）。
> **形态纪律（承 V50 已验收批）**：完整主谓句优先、主语入题、独立可读；不以机判紧凑替代可读性。

## 一、逐题对照（30 题）

| subsection_id | 旧题 | 判定 | 新题 | 实锚依据 | 题长 | 句式族 |
| ------------- | ---- | ---- | ---- | -------- | ---: | ------ |
| V49.1.1.1 | FreeBSD 4.x 内核的调度与锁基础 | 改 | 4.x 内核共用一把 Giant 锁 | Baldwin BSDCon 2002“one giant spin lock for the entire kernel”；FreeBSD smp(4)“reliance on a Giant kernel lock” | 15 | 主谓宾 |
| V49.1.1.2 | 分叉前夜的 SMP 扩展压力 | 保留 | （原题） | 实义锚 SMP；年代语感；无抽象动名词尾；12 字，合乎带宽容差 | 12 | 名词短语 |
| V49.1.1.3 | Matt Dillon 对内核路线的公开批评 | 改 | Dillon 批评 5.x 的互斥锁路线 | OSNews 2004 访谈自述“compartmentalized threading model … rather then the mutex model”；人物名依 §4.4 保留拉丁 | 17 | 主谓宾（兼介词框架） |
| V49.1.1.4 | 分叉决策的技术理由与人事摩擦 | 改 | 分叉源于不认同 5.x 内核路线 | Handbook 第 1 章（对 release 5 方向日益不满）＋OSNews 2004 访谈（核心部件要与 FreeBSD 5 走不同路线） | 14 | 因果主谓 |
| V49.1.1.5 | 4.x 代码库作为分叉的物质起点 | 改 | 分叉起点取自 FreeBSD 4.8 代码库 | Handbook“code base was taken from the 4.8 release”；官方 History 页同年同版表述 | 19 | 主谓宾 |
| V49.1.2.1 | LWKT 的设计目标与取舍原则 | 改 | LWKT 把内核拆成消息驱动的线程 | Hsu AsiaBSDCon 2004 论文（LWKT 与消息传递为两条主线）；节题 | 16 | 主谓（把字句） |
| V49.1.2.2 | 轻量级线程对内核栈的压缩 | 改 | 线程结构与内核栈成对缓存复用 | lwkt_thread.c“Nominally cache up to 32 thread + kstack structures”；thread.h“TDF_ALLOCATED_STACK … objcache allocated stack” | 14 | 主谓 |
| V49.1.2.3 | 消息传递优于共享内存的论证 | 改 | 以消息传递取代共享内存争用 | Hsu 论文摘要（partitioning and replication layered on top of a message passing system） | 13 | 介词框架 |
| V49.1.2.4 | 单核可扩展性与响应延迟 | 改 | 每颗 CPU 各有调度器 | lwkt_thread.c 头注“Each cpu … has its own self-contained light weight kernel thread scheduler”；Hsu“fast per-cpu fixed-priority roundrobin scheme” | 10 | 主谓 |
| V49.1.2.5 | LWKT 与 FreeBSD 线程模型的差异 | 保留 | （原题） | 双锚对照（LWKT／FreeBSD），“的”仅 1 个，无抽象动名词尾 | 19 | 并列对照 |
| V49.1.3.1 | 内核线程的轻量化实现路径 | 改 | 内核线程由创建接口按 CPU 派生 | msgport(9) 示例 lwkt_create(…, i, "myservice_cpu %d")；Hsu Table I lwkt_create | 15 | 主谓（被动义） |
| V49.1.3.2 | 消息队列与投递约定 | 改 | 线程自带消息端口 | msgport(9)“All light weight kernel threads have a built-in message port” | 8 | 主谓 |
| V49.1.3.3 | 线程间消息的分派与回收 | 改 | 消息取用与回复都经端口 | msgport(9) 三类端口与取用／回复路径；Hsu Table II（lwkt_getport／lwkt_replymsg） | 11 | 主谓（介词补足） |
| V49.1.3.4 | 阻塞与唤醒的消息驱动形态 | 改 | 无消息可取时线程睡在端口上 | msgport(9) lwkt_waitport“the caller thread will sleep until a message arrives” | 13 | 条件句 |
| V49.1.3.5 | 消息传递机制的性能边界 | 改 | 跨处理器消息经无锁环形缓冲投递 | Hsu“software crossbar switch and a lock-free ring buffer” | 15 | 介词框架 |
| V49.1.4.1 | token 作为串行化单位的引入 | 改 | token 自 1.0 起充当内核串行化单位 | token(9) HISTORY“LWKT tokens first appeared in DragonFly 1.0”；locking(9)“Tokens are not owned by a thread, but by the CPU” | 19 | 时点＋主谓 |
| V49.1.4.2 | 软 token 与共享模式并置 | 改 | 软 token 允许共享与排他并存 | token(9) 共享／排他两模式与 lwkt_gettoken_shared() 说明 | 15 | 主谓 |
| V49.1.4.3 | 自旋锁与 token 的分层配合 | 改 | token 内有自旋锁兜底 | spinlock(9)“Both the token code and the lockmgr(9) code use exclusive spinlocks internally” | 12 | 主谓（方位） |
| V49.1.4.4 | 锁粒度的细化与争用缓解 | 改 | 各子系统逐个拆锁减轻全局争用 | 官方首页“virtually no bottlenecks or lock contention in-kernel”；History 页“Major kernel subsystems were also scaled one after another” | 14 | 主谓（连动） |
| V49.1.4.5 | 同步模型在 SMP 下的验证负担 | 改 | token 须按取得逆序释放以免死锁 | token(9)“tokens must be released in the reverse order they were acquired”；spinlock(9)“mindful of ordering deadlocks” | 17 | 情态＋主谓 |
| V49.1.5.1 | LWKT 与用户线程调度的接缝 | 改 | 调度分作内核与用户两层 | Hsu“A lot of work went into separating the LWKT scheduler from the user process scheduler” | 11 | 主谓（被动义） |
| V49.1.5.2 | 内核子系统对 LWKT 的依赖方式 | 改 | 各子系统按调用面依赖 LWKT | thesis（依赖强度按调用面估算）＋msgport(9) 端口类型分层 | 14 | 介词框架 |
| V49.1.5.3 | 中断处理与线程调度的衔接 | 改 | 中断以线程身份参与内核调度 | Hsu（fast／threaded interrupts 由 LWKT 调度切换）；spinlock(9) 持锁期禁止中断线程抢占 | 13 | 介词框架 |
| V49.1.5.4 | 架构分层中的调度中心位置 | 改 | 重调度前先凑齐所需 token | locking(9)“The scheduler takes care of acquiring a token before rescheduling” | 14 | 时点＋主谓 |
| V49.1.5.5 | LWKT 在后续版本中的延续 | 改 | LWKT 一路沿用至 6.x 全系列内核 | token(9)／msgport(9) 起于 1.0 且现行手册仍在；History 页分期叙述 | 17 | 主谓 |
| V49.1.6.1 | 重构范围与兼容性代价 | 改 | 重写几乎全部内核而留存驱动接口 | 官方首页“rewriting of nearly all the original codebase”；OSNews 2004“maintaining a FreeBSD-5 compatible … device driver API” | 15 | 转折主谓 |
| V49.1.6.2 | 驱动适配成本的转嫁方式 | 改 | 驱动移植成本归驱动作者 | locking(9)“Lockmgr locks should be used for FreeBSD compatibility when porting drivers” | 11 | 主谓 |
| V49.1.6.3 | 增量重构与整体重写的权衡 | 改 | 在稳定旧库上逐步换掉核心 | Handbook“possible to make these radical changes as part of an incremental process” | 12 | 介词框架 |
| V49.1.6.4 | 上游同步与本地改动的两难 | 改 | 4.x 已停止更新只能择取 5.x 驱动 | OSNews 2004“FreeBSD-4 codebase is of strictly limited utility as a source of new code and maintainance updates”（单一来源，见证据稿） | 17 | 因果主谓 |
| V49.1.6.5 | 重构节奏与小团队人力的匹配 | 改 | 十六名提交者撑不起全线并行 | Hsu“16 committers with write privileges”；OSNews 2004“we don't have the manpower” | 13 | 主谓 |

## 二、分布自检（30 题）

- **冒号**：0；**设问**：0（≤3）。
- **题长**：8—19（含拉丁字母逐字计数、不计空格）。逐节极差：1.1＝7（12—19）／1.2＝9（10—19）／1.3＝7（8—15）／1.4＝7（12—19）／1.5＝6（11—17）／1.6＝6（11—17）。
- **“的”题**：全章 4／30；逐节 1.1＝2／5、1.2＝2／5、1.3—1.6＝0（均 ≤ 半数）。
- **抽象动名词尾**：0（无“……的实现／引入／取舍／分析／探讨”式收尾）。
- **构式族**：主谓句／主谓宾／介词框架／条件句／时点＋主谓／情态＋主谓／并列对照——7 族；逐节 1.1＝4、1.2＝5、1.3＝4、1.4＝4、1.5＝4、1.6＝4（均 ≥3）。
- **保留题**：2 题（1.1.2、1.2.5），判定理由见 §一；其余 28 题重拟。

## 三、须主会话裁定的连带项

1. **1.2.2 论题与证据错位**：原 thesis 称“压缩内核栈”，本轮可落证据只支撑“线程结构与内核栈成对缓存复用”（代码层），故题面改为缓存复用；thesis 宜同批改写（改题三件套：题、thesis、证据行同步）。
2. **1.4.5 题旨收窄**：原题“SMP 下的验证负担”无公开一手支撑（压测与回归成本属过程数据），改锚“逆序释放与死锁约束”，依据 token(9)／spinlock(9) 明文；thesis 宜同步。
3. **1.6.4 证据偏弱**：仅 OSNews 2004 访谈一源（当事人自述），第二源检索见 `c1-closed-draft-20261125.tsv`；标题暂按单一来源表述拟，是否降级为 needs_more 由主会话定。
