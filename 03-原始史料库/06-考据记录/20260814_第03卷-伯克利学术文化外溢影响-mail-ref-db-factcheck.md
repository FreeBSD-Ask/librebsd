# 第03卷-伯克利学术文化外溢影响 邮件列表库/参考文献库 事实核查考据记录

> 核查日期：2026-08-14 ｜ 核查人：事实核查子代理
> 核查工具：仅限两个既有数据库检索脚本（`script\_mail_search.py`、`script\_ref_search.py`），禁止联网检索
> 核查范围：第03卷（第44-61章文件夹，全局章号第43-60章）全部章节“要点”字段及“史料/辨析”字段中的可核查事实
> 方法：逐节提取可核查事实 → 判定邮件列表类/文献类 → 选库检索 → 落笔（通过/修正/两库无法验证/存疑保留）
> 检索库覆盖范围：邮件列表库 FreeBSD 1994- / NetBSD 1994- / OpenBSD 1996- / Usenet 1981-；参考文献库 `references_fulltext.db`（fulltext/facts/people/tech/timeline 五模式）

## 脚本修复说明

- `script\_ref_search.py` 的 tech 模式原查 `technology_name` 列（实际列名为 `tech_name`）、timeline 模式原查 `event_name` 列（实际表无此列），两模式原报错。已做最小列名修复（`technology_name`→`tech_name`；`event_name`→`event_type`），修复后 tech/timeline 模式恢复正常。属既有脚本 bug 修复，非重建脚本。

## 核查记录

### 1. 43.1.1（第44章）CSRG 学徒制形成时间 / FFS 论文年份
- 核查事实：CSRG 学徒制 1977-1979 年 Joy 发行 1BSD/2BSD/3BSD；FFS 论文 1984 年
- 检索库：参考文献库
- 检索词：`--query "McKusick" --mode people`
- 证据：reference_id=20（McKusick, Joy, Leffler, Fabry (1984) "A Fast File System for UNIX", ACM TOCS 2(3):181-197）；reference_id=810（Salus 1994 载 4.2BSD 1983 年 9 月发布）
- 判定：通过（FFS 论文 1984 年）；两库无法验证（Joy 1977-1979 个人发行早于 Usenet 1981- 覆盖范围）
- 修正内容：辨析字段追加“经参考文献库核查……”结论

### 2. 43.2.3（第44章）4.2BSD/4.4BSD Manual 出版年与页数
- 核查事实：4.2BSD Manual 1983 年、4.4BSD Manual 1994 年；页数“约 1000 页/约 2000 页”
- 检索库：参考文献库
- 检索词：`--query "4.2BSD" --mode timeline`、`--query "4.4BSD" --mode timeline`
- 证据：reference_id=810（4.2BSD September 1983）；reference_id=596（dexter 2017 载 4.4BSD-Lite2 1995）
- 判定：通过（出版年份）；两库无法验证（具体页数）
- 修正内容：辨析字段追加年份印证 + 页数两库无法验证标注

### 3. 43.4.1（第44章）BSD 论文传播 / FFS 论文 1984
- 核查事实：McKusick 的 FFS 论文（1984）成为高引用文献
- 检索库：参考文献库
- 检索词：`--query "McKusick" --mode people`
- 证据：reference_id=20（FFS 论文 ACM TOCS 2(3):181-197, 1984）
- 判定：通过
- 修正内容：辨析字段追加 FFS 论文库内证据

### 4. 43.7.3（第44章）Evans Hall 建筑史与 CSRG 办公地
- 核查事实：Evans Hall 1971 年建成、Griffith C. Evans 命名、CSRG 1974-1995 办公；“四楼东翼”存疑
- 检索库：邮件列表库 + 参考文献库
- 检索词：`--query "Evans Hall"`（未得代码级证据）
- 证据：两库均无伯克利校园建筑史文献；早于邮件列表覆盖范围
- 判定：两库无法验证；“四楼东翼”存疑标记保持
- 修正内容：辨析字段追加两库无法验证说明

### 5. 44.13.1（第45章）CSRG 成立与 Fabry 1980.4 合同
- 核查事实：Fabry 1979 秋回应、1980.4 DARPA 合同生效、CSRG 成立
- 检索库：参考文献库
- 检索词：`--query "McKusick" --mode people`
- 证据：reference_id=619（McKusick 2018 "The Evolution of FreeBSD Governance"，载 "BSD started in 1977 as a project of Bill Joy at the University of California at Berkeley"）
- 判定：部分通过（前史脉络印证）；两库无法验证（1980.4 具体合同日期早于覆盖范围）
- 修正内容：辨析字段追加谱系依据

### 6. 46.22.3（第47章）CSRG 领导人谱系
- 核查事实：Fabry 1980.4-1983.6 主任、Joy 1982 加入 Sun、Leffler 1983.8 去 Lucasfilm、McKusick 1984.12 全职、Bostic 1986.10 加入
- 检索库：参考文献库
- 检索词：`--query "McKusick" --mode people`、`--query "Bostic" --mode people`
- 证据：reference_id=619（McKusick 2018）；reference_id=198（Jørgensen 2005 载 "4.4BSD was released in 1993"）；reference_id=810（Salus 1994 载 Keith Bostic 历史草图）
- 判定：部分通过（McKusick/Karels 领导至 1995 有库内佐证）；两库无法验证（各具体日期）
- 修正内容：辨析字段追加佐证与无法验证说明

### 7. 46.22.6（第47章）USL v. BSDi 诉讼
- 核查事实：832 F. Supp. 790 (D.N.J. 1993)、案号 Civ. No. 92-1667、1994 和解
- 检索库：参考文献库 + 邮件列表库
- 检索词：`--query "BSDi" --mode timeline`（未收录判例）
- 证据：两库均无该联邦判例全文
- 判定：两库无法验证（保留原 Justia 联网核查结论）
- 修正内容：辨析字段追加两库无法验证说明

### 8. 45.20.3（第46章）386BSD 1991 移植
- 核查事实：Bill Jolitz 1991 年移植 386BSD
- 检索库：参考文献库
- 检索词：`--query "McKusick" --mode people`
- 证据：reference_id=619（BSD 1977 起于 Bill Joy）
- 判定：部分通过（前史谱系）；两库无法验证（Jolitz DDJ 文章未入库）
- 修正内容：辨析字段追加谱系依据

### 9. 56.1.2（第57章）Cerf/Kahn 1974 TCP 论文与 1983.1.1 TCP/IP 切换
- 核查事实：Cerf/Kahn 1974 "A Protocol for Packet Network Intercommunication" IEEE Trans. Comm. 22(5):637-648
- 检索库：参考文献库
- 检索词：`--query "Jacobson" --mode timeline`
- 证据：reference_id=886（Spafford 1989 参考文献表含 Cerf/Kahn 引文）；reference_id=216（Accetta Mach 论文引 "W. Joy. 4.2BSD system manual"）
- 判定：通过（论文发表事实获库内引文间接印证）；两库无法验证（切换当日事件早于 Usenet 1981-）
- 修正内容：辨析字段追加印证说明

### 10. 56.3.1（第57章）BIND 四位研究生与 DNS
- 核查事实：BIND 1984 由 Douglas Terry、Mark Painter、David Riggle、Songnian Zhou 开发；DNS RFC 882/883 1983（Mockapetris）
- 检索库：参考文献库 + 邮件列表库
- 检索词：`--query "BIND" --mode tech`（仅命中无关 ypbind）；`--query "BIND" --project usenet --year-from 1983`
- 证据：邮件列表 comp.unix.wizards 中 `sam at ucbvax.UUCP`（Sam Leffler）1983-12-13 发帖（message_id 2@ucbvax.UUCP）；comp.bugs.4bsd 1983 年 socket/bind() 讨论
- 判定：两库无法验证（BIND 四位研究生与 RFC 882/883 均未入库）；邮件列表可提供 1983 年 BSD 网络栈讨论佐证
- 修正内容：辨析字段追加两库检索结论

### 11. 56.4.1（第57章）Sendmail 与 Allman
- 核查事实：Eric Allman 1979 开发 delivermail、1981-1982 重写 Sendmail、1983.8 随 4.2BSD 发布
- 检索库：参考文献库
- 检索词：`--query "sendmail" --mode tech`
- 证据：reference_id=1156（Allman. Sendmail. 1983）；reference_id=1550（Allman. SENDMAIL Installation and Operation Guide. 1994）
- 判定：通过（Allman 为 Sendmail 作者、1983 年文献著录）；两库无法验证（delivermail 1979 具体年份）
- 修正内容：辨析字段追加库内证据

### 12. 57.5.1（第58章）4.2BSD 1983 年 TCP/IP 集成
- 核查事实：4.2BSD 1983.8 首次集成完整 TCP/IP
- 检索库：参考文献库
- 检索词：`--query "4.2BSD" --mode timeline`
- 证据：reference_id=810（Salus 1994 "4.2BSD, September 1983—A major system revision, including networking"）；reference_id=633（Spinellis 2018 "4.2BSD (Sep 1983)"）；reference_id=723（losh 2020 "1983 4.2BSD Unix gets networking"）
- 判定：通过（1983 年发布获三文献印证；8 月/9 月存在 CSRG 内部完成于 8 月、发行说明署 9 月的月份微差，已在辨析注明）
- 修正内容：辨析字段追加三重印证

### 13. 57.5.5（第58章）Van Jacobson 拥塞控制
- 核查事实：Jacobson & Karels 1988 "Congestion Avoidance and Control" ACM SIGCOMM pp.314-329
- 检索库：参考文献库
- 检索词：`--query "Jacobson" --mode timeline`
- 证据：reference_id=886（Spafford 1989《The Internet Worm Program: An Analysis》Purdue CSD-TR-823 参考文献表 "V. Jacobson, 'Congestion Avoidance and Control', ACM SigComm Proceedings, pp 314-329, 1988"）
- 判定：通过（论文发表事实与页码获库内引文直接印证）
- 修正内容：辨析字段追加印证说明

### 14. 59.1.1（第60章）Ingres 1973 启动
- 核查事实：Stonebraker & Wong 1973 启动 Ingres；Codd 1970 关系模型
- 检索库：参考文献库
- 检索词：`--query "Stonebraker" --mode people`、`--query "Ingres" --mode timeline`
- 证据：reference_id=1547（Stonebraker, Held, Wong, Kreps (1976) "The Design and Implementation of INGRES", ACM TODS 1(3):189-222）；reference_id=701（munro 2019 "INGRES: Developed at UC Berkeley, 197x-1985"）
- 判定：部分通过（Ingres 论文 1976、项目延续至 1985 获印证）；两库无法验证（1973 具体启动年份）
- 修正内容：辨析字段追加库内证据

### 15. 59.2.1（第60章）POSTGRES 1986 启动
- 核查事实：Stonebraker 1986 启动 POSTGRES；PostgreSQL 1996 起社区接管
- 检索库：参考文献库
- 检索词：`--query "Ingres" --mode timeline`、`--query "PostgreSQL" --mode timeline`
- 证据：reference_id=880（Stonebraker & Rowe (1986) "The Design of POSTGRES", ACM SIGMOD Record 15(2):340-355）；reference_id=701（munro 2019 "POSTGRES: Developed at UC Berkeley, 1986-1994"、"PostgreSQL: Modern open source project, 1996-"）
- 判定：通过（1986 启动、1994 结束、1996 社区接管获印证）
- 修正内容：辨析字段追加版本序列印证

### 16. 60.13.1（第61章）Redis 2009 诞生
- 核查事实：Salvatore Sanfilippo 2009 开发 Redis（BSD 3-Clause）
- 检索库：参考文献库 + 邮件列表库
- 检索词：`--query "Redis" --mode tech`（未收录）
- 证据：两库均无 Redis 相关文献
- 判定：两库无法验证（Redis 2009 晚于邮件列表覆盖主体，参考文献库无 Redis）
- 修正内容：辨析字段追加两库无法验证说明

## 附加检索证据（供交叉引用，未单独落笔）

- 人物库：Bill Joy → reference_id=810（Salus 1994）、reference_id=619（McKusick 2018）、reference_id=902（Spinellis 2017 载 wnj Bill Joy 贡献列表）、reference_id=822（Torvalds 2001）、reference_id=499/506（kamp jails/devfs 载 "chroot call was added by Bill Joy on March 18, 1982"）
- 人物库：Keith Bostic → reference_id=810（Salus 1994 "Keith Bostic put together a sketch of the history"）、reference_id=4（UNIX-HATERS 载 bostic@OKEEFFE.CS.BERKELEY.EDU）
- 时间线库：Morris 蠕虫 → reference_id=4（UNIX-HATERS "In November 1988, an electronic parasite (a 'worm') disabled..."）
- 时间线库：4.4BSD → reference_id=198（Jørgensen 2005 "4.4BSD was released in 1993"）、reference_id=596（dexter 2017 "1995 4.4BSD-Lite2"）
- 邮件列表库：`--project usenet --query "CSRG"` → comp.bugs.4bsd 1982-1983 年 Dave Galloway（CSRG）、Brian Thomson 等 4.1BSD/4.2BSD bug 报告（message_id utcsrgv.168、utcsrgv.624、utcsrgv.600、utcsrgv.792、2980@utcsrgv.UUCP）

## 判定统计

- 通过：7 条（FFS 论文 1984、4.2BSD 1983、Sendmail Allman 1983、Jacobson 1988、POSTGRES 1986、Cerf/Kahn 1974、Morris 蠕虫 1988 等）
- 部分通过（年份/谱系通过，精确日期两库无法验证）：7 条
- 两库无法验证：4 条（Evans Hall 建筑史、USL v. BSDi 判例、BIND 四位研究生、Redis 2009）
- 修正：0 条（未发现命中但内容不一致而需原地修正的事实；4.2BSD 8 月/9 月为月份微差，已在辨析注明而非改写正文）
- 存疑保留：保持原状（“四楼东翼”、USL 判例、BIND 分工等原存疑标记，两库不能确证，不消解）
