# KAME 项目主页（复用卡，ref2145，含批量导入行订正）

- **性质**：复用既有 ref2145（批量导入件，`https://www.kame.net/`；curl 直取 2,642 B 逐字可靠）。原行状态：source_tier=NULL、raw_source 表定 academic_work／layer 5（“51.9% 待核”批量导入遗留）、sha256=NULL、**claim 使用面为 0**——按 J90 订正复用路径处理，不另立同 URL 新 ref
- **订正内容（事务内，写前断言使用面＝0）**：references.bibliography_entry 改规范著录（补 URL 与引用日期）、source_tier=NULL→primary；raw_source.source_type=academic_work→official_doc、source_layer=5→3、tier_basis 改“source_tier=primary（2026-11-18 逐字取证）”、reliability_grade=A
- **source_url**：<https://www.kame.net/>
- **quote（逐字，两段，段间以省略号连接）**：

  > The KAME project was a joint effort of six companies in Japan to provide a free stack of IPv6, IPsec, and Mobile IPv6 for BSD variants. … Almost all of our implemented code has been merged to FreeBSD and NetBSD.

- **考据注**：用于**测试床积累的互操作经验转为工程规范，遗产见于后续实现**（2.2.5）。两句分别承载：①联合工程身份（六公司、为 BSD 各系提供自由 IPv6/IPsec/Mobile IPv6 栈）；②遗产去向（项目 2006 年 3 月收官，“几乎全部实现代码已合并入 FreeBSD 与 NetBSD”——承接由合并句自证）。互操作测试面（TAHI 一致性测试等）本页未载，披露为限度，另有出处面。
- **订正披露**：表定改动由 academic_work→official_doc——KAME 官方页为项目当事人组织的自述页面，归官方文档类；原行 tier_basis 的“51.9% 待核”为批量导入统计遗留，订正后以逐字取证为准。原卡 file_path（操作系统官方文档/The-KAME-project-ref2145.md）保留不动，本复用卡独立存放。
- **限度**：①页为收官后的总结页，“测试床互操作→规范”的过程面本页未展开；②“几乎全部”为自述量词，不载逐文件清单。
- **本批落点**：V37.2.2.5
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b027；复用 ref2145，订正后 official_doc／L3）
