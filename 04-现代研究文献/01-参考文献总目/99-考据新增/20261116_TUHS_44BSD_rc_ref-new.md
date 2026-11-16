# 4.4BSD `etc/rc`（新 ref）引用卡

- **性质**：4.4BSD `usr/src/etc/rc`（系统启动脚本）全文，取自 TUHS utree（3,616 字节正文）
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b001；source_url 四键查重＋规范化 URL 比对：库内无该文件）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/etc/rc>
- **quote（逐字，三行连引）**：

  ```
  echo -n ' named';		named
  echo -n ' sendmail';		sendmail -bd -q30m
  echo -n ' inetd';		inetd
  ```

- **考据注**：这三行是**“默认件”的直接证据**：1993 年 4.4BSD 的开机脚本按序拉起 named、sendmail、inetd（另有 routed／rwhod／lpd／portmap 等），即这些 Internet 基础设施软件随系统默认安装并默认运行，V35 1.2.1 据此。**载体披露**：脚本原文为 `sh` 代码，制表符与单引号照录，未统一空白；三行在原文分处第 143、158、159 行，本卡按行序连引并标行号。**边界披露**：本件只证 4.4BSD 的开机行为，不外推其他站点或发行版；站点自改 `/etc/rc` 属常态。
- **本批落点**：V35.1.2.1 第 1 块
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b001；official_doc／L3）
