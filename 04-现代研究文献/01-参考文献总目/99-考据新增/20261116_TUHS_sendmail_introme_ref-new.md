# 4.4BSD sendmail `doc/intro/intro.me`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/usr.sbin/sendmail/doc/intro/intro.me`（sendmail 导引文档，`.me` 宏格式），取自 TUHS utree（39,246 字节正文）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b019；source_url 四键查重：库内无该文档）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/usr.sbin/sendmail/doc/intro/intro.me>
- **quote（逐字，一处）**：
  1. delivermail only supported one gateway to any network, whereas sendmail can be sensitive to host names and reroute to different gateways.
- **考据注**：本句出自 “COMPARISON WITH OTHER MAILERS / Delivermail” 一节，是**起点差异的自述**：delivermail 对任一网络只支持一个网关，sendmail 则能依主机名改道——8.1.1 的“网关起点”即以此为本。同节首句 “Sendmail is an outgrowth of delivermail.” 可作同一关系的简式表述。**roff／.me 披露**：原文以 `.i delivermail` 等宏逐句分行排版，引文为宏解析并句后的文本，分词空白照录；未改字。**年代披露**：本件为 4.4BSD 树内 sendmail 文档（随 sendmail 8 发行），所述 delivermail 属更早世代，引文只证“后代自述其与前辈的差异”，不在本卷 8.1.1 内另断 delivermail 的年份。
- **本批落点**：V31.8.1.1 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b019；official_doc／L3）
