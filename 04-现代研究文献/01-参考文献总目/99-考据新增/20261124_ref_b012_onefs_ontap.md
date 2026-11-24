# OneFS／Data ONTAP／基金会案例引用卡（ref 新建三件）

- **性质**：Dell InfoHub OneFS 技术概览与高可用页、IBM Redpaper、FreeBSD 基金会 NetApp 案例研究——5.1 节商用系统 BSD 成分面的一手与官方表述
- **取件**（curl 直取 2026-11-24）：https://infohub.delltechnologies.com/en-us/l/dell-powerscale-onefs-technical-overview/overview-3166/（587 132 B）＋https://www.dell.com/en-us/infohub/articles/high-availability-and-data-protection-with-dell-powerscale-scale-out-nas（590 851 B）＋https://freebsdfoundation.org/netapp-case-study/（63 122 B）＋https://www.redbooks.ibm.com/redpapers/pdfs/redp4671.pdf（IBM Redpaper PDF 文本层经 exa 抓取，卡式 D2 引用）
- **Dell 概览句（V57.5.1.3 A 块）**：OneFS is built on a BSD-based UNIX operating system foundation. It supports both Linux/UNIX and Windows semantics natively, including hard links, delete-on-close, atomic rename, ACLs, and extended attributes. It uses BSD as its base operating system because it is a mature and proven operating system, and the open-source community can be leveraged for innovation.
- **Dell HA 句（V57.5.1.3 B 块；弯撇号照录）**：Built atop FreeBSD’s UNIX implementation, availability and resilience are integral to OneFS from the lowest level on up.
- **IBM Redpaper 句（V57.5.1.4 B 块）**：Data ONTAP GX was created as a combination of the WAFL file system and SpinFS running in a FreeBSD environment. Data ONTAP 8.0 brings Data ONTAP 7G and Data ONTAP GX together into a single storage operating system, also running on FreeBSD.
- **基金会案例句（V57.5.1.4 A 块）**：In 2004, NetApp leadership decided to base NetApp ONTAP, the underlying data management software across their entire product range, on a more performance-driven system: FreeBSD. A huge factor in that decision was the BSD licensing model, and from version 6.0 in 2004 to version 14.0 today, FreeBSD has remained a constant and up-to-date component in NetApp.
- **口径**：Dell InfoHub 两页为 PowerScale/OneFS 厂商官方技术概览（BSD 基座官方自述——5.1.3“不公开内部构成”的替代线索面：基座与版本线官方公开）；IBM Redpaper 为官方合作出版物的 ONTAP 演进记载（7G 网络栈 BSD→GX FreeBSD 环境→8.0 全系统基座）；基金会案例研究为一手官方记载（BSD 许可模型为选择动因——5.1.5 面佐证）。
- **考据日期**：2026-11-24

## supp-V57-b012 追加引文（G6 全责线，2026-11-24）

- IBM Redpaper 句（ref10461 复用卡；V57.5.1.4 D 块）：Data ONTAP GX was created as a combination of the WAFL file system and SpinFS running in a FreeBSD environment. Data ONTAP 8.0 brings Data ONTAP 7G and Data ONTAP GX together into a single storage operating system, also running on FreeBSD.
