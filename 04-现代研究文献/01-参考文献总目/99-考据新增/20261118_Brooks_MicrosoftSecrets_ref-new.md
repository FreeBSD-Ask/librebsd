# 《Microsoft Secrets》（David Brooks 白皮书，新 ref）引用卡

- **性质**：微软 Windows 2000 Server Product Group 成员 David Brooks 撰写的 Hotmail 迁移内部白皮书（Version History：Draft 1 2000-08-08／修订 2000-08-22）；原为微软内部文档，经第三方自微软防护不善服务器披露后公开流传，现以 steve-parker.org 转载页实取（exa web_fetch 2026-11-18）。官方文档本体＋当事人执笔，归 official_doc／L3；泄露与转载渠道如实披露
- **数据库**：新建 ref（2026-11-18 Task 8.2 V71—V75 线 supp-V71-b034；source_url 四键查重无重合）
- **source_url**：https://steve-parker.org/articles/others/hotmail/
- **quote（逐字）**：其一：Microsoft acquired Hotmail at the end of 1997 as a going concern. The service’s creators had defined a two-layer architecture built around various UNIX systems: Front end web servers, built with dual Pentium systems on racked motherboards, running Apache on FreeBSD (a configuration with no need to install licensed software)／Back end file stores, built with Sun Enterprise 4500 servers, running Solaris 2.6 (Sun’s UNIX) and with all user data stored on RAID arrays, accessed using very simple filing semantics（原文弯撇号照录；列表符号 n 转写不取）。其二（Abstract）：There is potential, not yet realized, for stability of individual systems to be equal to that of UNIX.／while the core features of Windows 2000 are able to run the service, its administrative model is not well suited to the conversion.
- **考据注**：其一支撑 V71.3.12.1（分层硬件构成细节）与 V71.3.12.2（收购时点 1997 年末＋“service’s creators had defined”——收购方事后追记收购前架构，正是回溯材料样本）；其二支撑 V71.3.12.5（工程代价评价：管理模型不适＋单机稳定性潜力未兑现——与官方战略口径对置，正好承题面“评价口径不能被宣传材料替代”）
- **本批落点**：V71.3.12.1 第 2 块／V71.3.12.2 第 1 块／V71.3.12.5 第 1 块
- **考据日期**：2026-11-18（Task 8.2 V71—V75 线 supp-V71-b034；official_doc／L3）
