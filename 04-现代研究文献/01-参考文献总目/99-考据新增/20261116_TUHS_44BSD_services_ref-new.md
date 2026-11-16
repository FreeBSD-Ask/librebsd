# 4.4BSD `etc/services`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/etc/services`（服务名与端口号表）全文，取自 TUHS utree（2,127 字节正文；文件头 `@(#)services	8.1 (Berkeley) 6/9/93`，日期 1993-06-09）
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b020；source_url 四键查重：库内 TUHS 条目无 `etc/services`；另按规范化 URL 复查无同页）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/etc/services>
- **quote（逐字，两处，分落两块）**：
  1. `smtp		25/tcp		mail` 与 `domain		53/tcp		nameserver	# name-domain server`（第 21、27 行，制表符原样）
  2. `# Network services, Internet style` / `# UNIX specific services` / `# Kerberos (Project Athena/MIT) services`（第 3、53、77 行的三处分节标题）
- **考据注**：第 1 处是**并置的实物**：同一张表里邮件（smtp 25）与域名（domain 53）相邻而立，属同一套“服务名—端口”秩序，8.4.4 的“并置”不必论证，指表即可。第 2 处是**分类的实物**：文件自分三段（Internet 风格网络服务／UNIX 特有服务／Kerberos 服务），另有 Bootp 实验段，8.4.5 的“分类盘点”以此为据。**缺项披露（要紧）**：该表**没有 www／http 条目**（1993 年 6 月的 IANA 风格清单未收 Web 服务），故 8.4.x 不得据本表推称“BSD 当时已在服务层收编 Web”；缺项只证本表所列。**载体披露**：引文为 `<pre>` 纯文本原样，制表符保留，未统一空白。
- **本批落点**：V31.8.4.4 第 1 块（第 1 处）、V31.8.4.5 第 1 块（第 2 处）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b020；official_doc／L3）
