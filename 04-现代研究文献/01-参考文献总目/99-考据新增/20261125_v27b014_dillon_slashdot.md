# Matthew Dillon Slashdot IRC 访谈（2003-10-03）引文卡

- **著录（GB/T 7714-2015）**：SLASHDOT. IRC Forum with Matthew Dillon of DragonFly BSD[EB/OL]. (2003-10-03)[2026-11-25]. https://bsd.slashdot.org/story/03/10/03/0158217/irc-forum-with-matthew-dillon-of-dragonfly-bsd.
- **来源 URL**：https://bsd.slashdot.org/story/03/10/03/0158217/irc-forum-with-matthew-dillon-of-dragonfly-bsd
- **访问日期**：2026-11-25（WebSearch 抓取页内正文；同时代访谈）
- **用途**：Task 8.2 G3 全责线 V27 b014（4.2.2A 既有锁模型批评面）
- **tier 依据**：source_type=talk_interview、source_tier=primary（当事人本人答问，2003-10-03，分叉当年）
- **披露**：原文含网络论坛口语与拼写（aggregious 等）一律照录；页面含第三方跟帖，仅取 Dillon 答问段

## 逐字引文

Q1（4.2.2A 源，对五版路线与锁／抢占复杂度的当事人批评）:
FreeBSD-5 has gone down a road that I believe will lead to a slow, cumbersome, and unmaintainable result. There are plenty of examples of this but the most aggregious is thread preemption in the kernel, preemptive thread movement between cpus (also while in the kernel), and a ridiculously complex API for various types of mutex operations.

Q2（4.2.2A 源，对四版稳定性维护态度的判断，作同题补充句）:
FreeBSD-4.x is nearing its end-of-life, and it is obvious that less care is being taken in preserving its vaunted stability then in the past.
