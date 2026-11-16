# 《Open Sources》第 3 章 McKusick “Twenty Years of Berkeley Unix”（新 ref）引用卡

- **性质**：McKusick 所撰《Open Sources》（O'Reilly 1999）第 3 章全文，取自贝尔格莱德大学 afrodita.rcub.bg.ac.rs 的纯文本镜像（49,265 字节，含 O'Reilly 版权页与书名信息）；**O'Reilly 官方 openbook 页本机与 exa 均不可直取**（exa 报 CRAWL_NOT_FOUND），故用镜像全文
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b008；source_url 四键查重：库内 `openbook/opensources/book/`（ref10730）为目录页、`book/intro.html`（ref10732）与 `book/young.html`（ref10731）为他章，本章镜像路径无重合）
- **source_url**：<http://afrodita.rcub.bg.ac.rs/~ggajic/pub/4.4BSD/kirkmck.txt>
- **quote（逐字，三处）**：
  1. They complained to DARPA that Berkeley was to implement the interface while BBN was supposed to implement the protocol, so Berkeley should replace the TCP/IP code in 4.3BSD with the BBN implementation.
  2. To decide which code base to use, they gave both to Mike Muuse of the Ballistics Research Laboratory, who was viewed by both Berkeley and BBN as an independent third party.
  3. within eighteen months more than 1,000 site licenses had been issued
- **考据注**：第 1 句是**合同分工的书面痕迹**（接口归柏克莱、协议归 BBN，BBN 据此要求换实现），用于 7.2.1；第 2 句是**仲裁安排**（两方都认的第三方 Mike Muuse 评测两套代码），用于 7.3.2；第 3 句是**扩散规模**（4.2BSD 发行十八个月内逾千份站点许可），用于 7.6.1。**异体字披露（要紧）**：本镜像把 Myers／Muuss 写作 “Mike Muuse”，而卷内小节题名与通行写法为 Muuss；引文按镜像原文照录，不作“顺手改正”，并在此标明差异。**体裁披露**：作者是 CSRG 当事人，属事后追述（L4、retro=1），其数字与分工叙述均带当事人视角，不作独立核账之用。**载体披露**：镜像文本与 O'Reilly 版可能有排印差异（如连字符与断行），本批只取整句，遇断行已并句**未改字**
- **本批落点**：V31.7.2.1 第 1 块（第 1 句）、V31.7.3.2 第 1 块（第 2 句）、V31.7.6.1 第 1 块（第 3 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b008；academic_work／L4）
