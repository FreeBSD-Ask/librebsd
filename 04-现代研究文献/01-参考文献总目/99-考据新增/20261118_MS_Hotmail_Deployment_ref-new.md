# 《Microsoft Hotmail Migration Technical Case Study: Deployment and Migration Guide》（新 ref）引用卡

- **性质**：Microsoft Learn tn-archive 归档的 Hotmail 迁移技术案例研究部署章（ms.date 2007-12-05）；WebFetch 实取全文 2026-11-18（official_doc／L3）
- **数据库**：新建 ref（2026-11-18 Task 8.2 V71—V75 线 supp-V71-b034；source_url 四键查重无重合）
- **source_url**：https://learn.microsoft.com/en-us/previous-versions/tn-archive/bb496988(v=technet.10)
- **quote（逐字）**：其一（Application Migration）：The net result is that significantly better throughput was achieved on the same hardware without a drastic reengineering of the code-base with just a few months work. Almost all the application logic is the same as it was on the FreeBSD version of the code base. 其二：Under FreeBSD, bugs and memory leaks would often go undetected because of the lack of tools.（其一段落另载：Perl CGI 转 C++ 系微软收购后首项任务、Sysprep 镜像重装 60 分钟＋15 分钟定制、三测试环境 50/50 混跑等，本批未取）
- **考据注**：两句分别支撑 V71.3.12.5（官方成果口径：同硬件显著吞吐提升）与工程代价面（FreeBSD 缺工具致缺陷内存泄漏难察——官方文档自陈的反面观察，与 Brooks 白皮书 administrative model 句互证）
- **本批落点**：V71.3.12.5 第 2 块（throughput 成果口径句；与 Brooks 工程代价句对置）
- **考据日期**：2026-11-18（Task 8.2 V71—V75 线 supp-V71-b034；official_doc／L3）
