# The Open Group Base Specifications `<sys/socket.h>`（新 ref）引用卡

- **性质**：The Open Group Base Specifications Issue 7（2018 年版，IEEE Std 1003.1-2017）中 `<sys/socket.h>` 一页，取自 pubs.opengroup.org（去标签后正文 13,546 字节）
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b002；source_url 四键查重＋规范化 URL：库内无该页）
- **source_url**：<https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_socket.h.html>
- **quote（逐字，三处，分落四块）**：
  1. The `<sys/socket.h>` header shall define the `socklen_t` type, which is an integer type of width of at least 32 bits; see APPLICATION USAGE.
  2. First released in Issue 6. Derived from the XNS, Issue 5.2 specification.
  3. UNIX ® is a registered Trademark of The Open Group.
- **考据注**：第 1 句是**规范化的形式**：socket 不再是某实现的接口，而是“头文件须定义……、函数原型须提供”的标准义务（页面同段列出 accept／bind／connect／socket 等 17 个原型），1.3.2 的“泛化”据此。第 2 句是**渊源注记的形态**：CHANGE HISTORY 明记“源自 XNS Issue 5.2 规范”，**不含 BSD**。第 3 句是**商标收窄的证据**：UNIX 在此是 Open Group 的注册商标（同页并注 “POSIX ™ is a Trademark of The IEEE”），1.4.1 的“把 UNIX 收窄为可认证资格”据此。**量化披露（要紧）**：本批实测该页全文 `BSD` 出现 0 次、`Berkeley` 0 次、`4.2BSD` 0 次——1.3.4 的“渊源注记密度”以此为样本（样本仅此一页，不外推为标准全貌）。**载体披露**：HTML 去标签后为纯文本，第 1 句原文在 “32” 与 “bits” 间断行，本卡并句未改字；®／™ 为原文实体转写。
- **本批落点**：V35.1.3.2 第 1 块（第 1 句）、V35.1.3.4 第 1 块（第 2 句）、V35.3.3.2 第 1 块（第 2 句）、V35.1.4.1 第 1 块（第 3 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b002；official_doc／L3）
