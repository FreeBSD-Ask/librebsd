# 第14卷“商业生态与企业案例”双库事实核查

> **核查日期**：2026-08-15
> **核查工具**：邮件列表库（_mail_search.py）+ 参考文献全文数据库（_ref_search.py）
> **方法**：0 信任原则，所有检索结果均为真实检索所得。

## 核查范围

第14卷共11章（第270-280章），涵盖 Foundation 资助、商业使用案例、基金会争议、商业 Unix 谱系对比等。

## 邮件列表库检索说明

- FreeBSD 邮件列表：部分列表库（如 cu.db、hackers.db）具备 FTS5 全文索引，部分列表库（如 nnounce.db）缺失 messages_fts 表，导致遍历全部 *.db 时中断。本核查使用 --list cu 参数绕过此限制。
- NetBSD 邮件列表：FTS5 索引完整，检索正常。
- OpenBSD 邮件列表：FTS5 索引完整，检索正常。

---

## 逐条核查

### 已确认事实（双库检索验证通过）

#### F-001：Jan Koum 向 FreeBSD Foundation 捐赠 $1,000,000（2014年11月）
- **来源文件**：270.1.4 经济生态史料辨析
- **参考文献库**：✅ 通过。
ef_id=2108（FreeBSD Foundation Announces Generous Donation from Jan Koum，2014-11）、
ef_id=3987（2014-11-17 freebsdfoundation 博客全文 $1,000,000）、
ef_id=4438（FreeBSD Journal 2014.11/12 Foundation Letter）
- **邮件列表库**：两库无法验证（FreeBSD hackers 列表无精确命中）
- **判定**：✅ **通过**——参考文献库三处独立来源交叉验证。

#### F-002：Netflix Open Connect CDN 基于 FreeBSD
- **来源文件**：275.5 Netflix CDN
- **参考文献库**：✅ 通过。
ef_id=668（looney-netflix_and_freebsd，BSDCan 2019）、
ef_id=700（同 FOSDEM 2019）、
ef_id=1070（netflix-CASE-STUDY-1，FreeBSD Foundation 官方案例研究）
- **邮件列表库**：✅ 部分通过。reebsd cu 列表 Warner Losh 2021-07-17 提及 Netflix 使用 NVMe 驱动器
- **判定**：✅ **通过**

#### F-003：NetApp ONTAP 存储操作系统基于 FreeBSD
- **来源文件**：275.3 NetApp ONTAP
- **参考文献库**：✅ 通过。
ef_id=1069（NetApp-CASE-STUDY-1-1，FreeBSD Foundation 官方案例研究）
- **邮件列表库**：两库无法验证
- **判定**：✅ **通过**

#### F-004：Apple Darwin/XNU 内核整合 FreeBSD 代码
- **来源文件**：275.1 Apple macOS/iOS Darwin
- **参考文献库**：✅ 通过。
ef_id=1136（Amit Singh《Mac OS X Internals》，2006）、
ef_id=2458（Apple Releases Darwin 1.0，2000-04-05）、
ef_id=4345-4353（apple-oss-distributions/xnu GitHub 快照）
- **邮件列表库**：两库无法验证
- **判定**：✅ **通过**

#### F-005：FreeBSD Foundation 商标转让（2004年11月）
- **来源文件**：270.1.1 Foundation 成立
- **参考文献库**：✅ 通过。
ef_id=1049（FreeBSD Foundation Timeline PDF）
- **邮件列表库**：两库无法验证
- **判定**：✅ **通过**——commit 记录（def4307484a Murray Stokely 2004-11-27）已在大纲中援引。

#### F-006：Juniper 员工 Simon J. Gerraty 在 FreeBSD 邮件列表活跃
- **来源文件**：275.4 Juniper Junos
- **邮件列表库**：✅ 通过。reebsd cu 2022-02-08：sjg@juniper.net 关于 buildworld 讨论（4封邮件）
- **参考文献库**：✅ 部分通过。
ef_id=1810/1811（FreeBSD Journal 2022 含 Juniper 广告）
- **判定**：✅ **通过**

#### F-007：iXsystems/Matt Olander 在 BSD 社区活动
- **来源文件**：275.7 iXsystems TrueNAS
- **邮件列表库**：✅ 通过。
etbsd-advocacy 2008-09-22：matt@ixsystems.com 发布 meetBSD 通知；
etbsd-bugs 2012-05-05：dwhite@ixsystems.com 提交 NetBSD bug
- **参考文献库**：两库无法验证
- **判定**：✅ **通过**

### 部分确认事实（有线索但需进一步验证）

#### F-008：Sony PS4 运行修改版 FreeBSD 9.0（Orbis OS）
- **参考文献库**：⚠️ 弱线索。
ef_id=3989（The Register 2021-03-10 提及 FreeBSD 用于 PlayStation）
- **邮件列表库**：两库无法验证
- **判定**：⚠️ **存疑**——非 Sony 官方一手来源。建议补充 Sony 官方文档或逆向分析报告。

#### F-009：Juniper Junos 路由器操作系统基于 FreeBSD
- **参考文献库**：⚠️ 弱线索。
ef_id=1810/1811（FreeBSD Journal 含 Juniper 广告）
- **邮件列表库**：✅ 间接证实。sjg@juniper.net 在 FreeBSD 列表活跃
- **判定**：⚠️ **存疑**——无官方技术白皮书。建议补充 Juniper 官方文档。

#### F-010：WhatsApp 早期服务器基于 FreeBSD
- **参考文献库**：⚠️ 弱线索。
ef_id=725（Deb Goodkin LCA 2020 演讲，未明确提及 WhatsApp）
- **邮件列表库**：两库无法验证
- **判定**：⚠️ **存疑**——建议补充 Jan Koum 公开演讲或采访。

### 两库无法验证（前期已标注存疑，已解决）

#### F-011：个人捐赠“平均一年才十七块三毛”
- **判定**：✅ **存疑已解决**（id 1737，2026-08-04）——确认为自媒体《FreeBSD 大败局》表述，大纲已加警示。

#### F-012：Linux 基金会“一年收六十多亿”
- **判定**：✅ **存疑已解决**（id 1738，2026-08-04）——夸大且未标货币单位，实际约 $2-3 亿量级。

### 引语存疑（两库无法验证，未标注原始出处）

#### F-013：John Baldwin 引语“我不会因此而责怪他们”
- **两库检索**：均无精确命中
- **判定**：⚠️ **存疑**——未标注原始出处（演讲/邮件/采访的具体日期与链接）。

#### F-014：McKusick 引语“BSD 许可证就是一个复制中心”
- **两库检索**：均无精确命中
- **判定**：⚠️ **存疑**——未标注原始出处。

#### F-015：Linus Torvalds 引语“BSD 许可证不一定是很好的许可证”
- **两库检索**：均无精确命中
- **判定**：⚠️ **存疑**——未标注原始出处。

### 商业 Unix 谱系日期（两库无法验证，属一般知识）

以下为第277章厂商成立/产品日期，属科技史一般知识，双库无法直接验证：

| 编号 | 事实 | 大纲声称 |
|------|------|---------|
| F-016 | IBM AIX 始于 | 1986 |
| F-017 | DEC OSF/1 基于 Mach 2.5 + 4.3BSD-Reno | 1992 |
| F-018 | SGI IRIX 基于 System V + BSD | 1988 |
| F-019 | SunOS 1.0 基于 4.1BSD | 1983 |
| F-020 | Oracle 收购 Sun | 2010-01 |
| F-021 | Windows NT 由 David Cutler 设计 | 1993 |
| F-022 | Cisco IOS 网络栈受 BSD TCP/IP 影响 | 1987 |
| F-023 | Novell 从 AT&T 购买 Unix | 1993 |
| F-024 | BSDi 由 Rick Adams 成立 | 1991 |
| F-025 | Walnut Creek CDROM 由 Bob Bruce 创立 | 1991-08 |
| F-026 | NeXT 由 Steve Jobs 成立 | 1985 |
| F-027 | Be Inc. 由 Jean-Louis Gassee 成立 | 1990 |
| F-028 | Minix 由 Andrew Tanenbaum 开发 | 1987 |
| F-029 | QNX 由 Quantum Software Systems 开发 | 1980s |
| F-030 | Wind River 成立 | 1981 |
| F-031 | AT&T 成立 USL | 1989 |
| F-032 | Red Hat IPO | 1999 |
| F-033 | Canonical 成立 Ubuntu | 2004 |

---

## 核查统计

| 类别 | 数量 |
|------|------|
| 通过（至少一库验证） | 7 |
| 部分确认/存疑 | 3 |
| 存疑已解决 | 2 |
| 引语存疑 | 3 |
| 两库无法验证（一般知识） | 18 |
| **合计** | **33** |

---

## 工具改进建议

1. **_mail_search.py FTS5 兼容性**：FreeBSD 部分列表库缺失 messages_fts 表，建议在 _search_one_db 中添加 	ry/except sqlite3.OperationalError 容错。
2. **邮件列表库时间窗口**：FreeBSD cu 列表 FTS5 索引覆盖到 2022 年，2025 年事件无法检索。
3. **参考文献库覆盖面**：商业 Unix 谱系官方技术文档未纳入。

## 下一步行动

1. 回写大纲文件：对 F-001~F-007 在对应子节辨析字段追加双库验证来源。
2. 补充文献：对 F-008~F-010 联网检索补充原始出处。
3. 引语出处：对 F-013~F-015 查找原始出处（邮件列表/演讲/采访）。