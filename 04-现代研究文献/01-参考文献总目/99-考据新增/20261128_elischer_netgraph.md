# Elischer《All About Netgraph》（新 ref）引用卡

- **性质**：Julian Elischer 在 Daemon News 2000 年 3 月号发表的文章《All About Netgraph》（作者主页转载）
- **数据库**：新建 ref（2026-11-28 G4 全责线 V37 批 b030；库内无该文条目）
- **source_url**：<https://people.freebsd.org/~julian/netgraph.html>
- **quote（逐字）**：

  > One of the main goals of netgraph is speed, which is why it runs entirely in the kernel. Another design decision is that netgraph is entirely functional. That is, no queuing is involved as packets traverse from node to node. Instead, direct function calls are used.

- **考据注**：用于**图遍历与消息传递的开销结构**（V37.2.3.5）。作者自述 netgraph 以速度为首要目标、全内核运行，节点间不经排队而用直接函数调用；该设计消除了队列延迟，但每次转发仍须逐边调用与 mbuf 传递，图规模与节点数因之成为吞吐评估的结构变量。
- **限度**：①文章为作者自述的设计说明（2000 年），具体性能数字须以基准测试复核；②“no queuing”指节点间直通，不等于零开销；③页面为作者主页转载，原刊版面另见 Daemon News 存档。
- **本批落点**：V37.2.3.5
- **考据日期**：2026-11-28（Task 8.2 G4 全责线 V37 批 b030；magazine-article／L3）
