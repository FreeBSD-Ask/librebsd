---
chapter: 第 301 章
id: CH301
volume: "第16卷-开源运动与合规治理"
---

# 第301章 开源运动与bsd-apache谱系

## 史料

- [DB:research_notes:blocks:432] 关键词「开源运动」命中：参见 三、开源运动与许可证 下 ESR 相关条目。本次俚语考证（KISS、DRY、YAGNI 原则）与习俗考证（Unix…
- [DB:research_notes:blocks:1227] 关键词「开源运动」命中：参见 五、开源运动与许可证 下 Lucas Absolute FreeBSD 3rd Edition 同条目（ISBN …
- [DB:research_notes:blocks:1595] 关键词「开源运动」命中：以下文献为第 64-71 章（FreeBSD 6.x 到 8.x 版本、jemalloc、PF 防火墙、CVS→SVN …

## 要点

- Apache 软件基金会（ASF）于 1999 年 3 月成立，前身是 1995 年的 Apache Group（Brian Behlendorf（布莱恩·贝伦多夫）、Cliff Skolnick 等维护 NCSA HTTPd 衍生的 Apache 服务器）；ASF 组织模式借鉴 BSD 精英评审模式（committer、PMC、member 三层）；ASF 是除 FSF 与 OSI 外最具影响力的开源组织
- Apache 许可证 1.0（2000 年）基于 BSD 许可证修改，1.1（2001 年）去除 advertising 条款，2.0（2004 年）加入专利授权条款；Apache 2.0 与 BSD 三条款在精神上同属宽松许可证阵营，但 Apache 2.0 加入专利保护；二者在 OSI 认证中并列
- Apache 对 BSD 开源传统的继承：(1) 宽松许可证哲学；(2) 精英评审模式（committer/PMC/member）；(3) 基金会治理（轻治理）；Apache 对传统的发展：(1) 加入专利授权；(2) 项目孵化器（Incubator）；(3) 项目独立治理（每个顶级项目独立 PMC）；Apache 模式成为现代开源基金会的主流范式
- Apache 项目生态与 BSD 系统的交织：(1) Apache HTTP Server 长期是 FreeBSD 默认 Web 服务器；(2) Yahoo! 早期 FreeBSD + Apache 是典型组合；(3) FreeBSD Ports 中 Apache 项目占重要位置；(4) Apache 项目大量在 BSD 系统上开发与测试
- Netscape 1998 年 1 月开源 Navigator 的背景：(1) Microsoft IE 通过 Windows 捆绑抢占浏览器市场；(2) Netscape 市场份额从 80% 跌至 50%；(3) CEO Jim Barksdale 阅读 Raymond CatB 后决定开源；(4) 开源是商业策略而非哲学选择；1998 年 3 月 31 日 Mozilla 代码正式发布（mozilla.org）

## 史观

- 总纲第 7 条——BSD 与 UNIX 谱系的连续性，Apache 继承 BSD 开源传统
  - 辨析：ASF 是否真借鉴 BSD 模式，需查早期组织文档
  - 文献：ASF 官方历史；Apache Group 早期文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 30

- 总纲第 1 条——偶然性改写历史，商业困境催生开源决策
  - 辨析：【双库核查 2026-08-15】邮件列表库 freebsd 1997-1999 年查询 'Netscape Mozilla' 命中 5 条，参考文献库 'Netscape' 命中 5 条（Meeker 2008、bsdcan2019 等）——双库间接验证；Netscape 1998-01-22 精确日期双库无法直接确证 [存疑
- 总纲第 13 条——边缘者的作用
  - 辨析：freebsd.db freebsd-src 仓库的 Mozilla 主题 commit 显示 Mozilla 与 FreeBSD 的交集主要是 FreeBSD 为 Mozilla 提供兼容性修复——Jordan K. Hubbard、John Polstra、Brian Feldman、Scott Long 等核心 committer 均参与过 M
- 总纲第 1 条——偶然性改写历史，GitHub 普及改变开源协作
  - 辨析：PR 模式是否真优于补丁，需独立判断；Microsoft 收购是否影响开源
  - 文献：GitHub 官方历史[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.7.2 PR 模式对 BSD

- 总纲第 1 条——偶然性改写历史，2020 年迁移是 FreeBSD 工具链关键转折
  - 辨析：FreeBSD 是否完全接受 GitHub PR，须查当前文档；freebsd.db freebsd-doc 仓库的 Git 迁移主题 commit 显示原大纲 “2021 年 1 月正式完成” 叙事在 doc 仓库层面需修正——doc 仓库的 Git 迁移文档更新集中在 2021-03-16 至

## 辨析

- ASF 是否真借鉴 BSD 模式，需查早期组织文档
  - 文献：ASF 官方历史；Apache Group 早期文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.5.2 Apache 许可证与 BSD 许可证的谱系关系

- 要点：Apache 许可证 1.0（
- 【双库核查 2026-08-15】邮件列表库 freebsd 1997-1999 年查询 'Netscape Mozilla' 命中 5 条，参考文献库 'Netscape' 命中 5 条（Meeker 2008、bsdcan2019 等）——双库间接验证；Netscape 1998-01-22 精确日期双库无法直接确证 [存疑脚注]；Barksdale 是否真读 CatB，须查自述
  - 文献
- freebsd.db freebsd-src 仓库的 Mozilla 主题 commit 显示 Mozilla 与 FreeBSD 的交集主要是 FreeBSD 为 Mozilla 提供兼容性修复——Jordan K. Hubbard、John Polstra、Brian Feldman、Scott Long 等核心 committer 均参与过 Mozilla 兼容性修复，Mozilla 是 F
- PR 模式是否真优于补丁，需独立判断；Microsoft 收购是否影响开源
  - 文献：GitHub 官方历史[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.7.2 PR 模式对 BSD 补丁文化的冲击

- 要点：PR 模式对 BSD 补丁文化的冲击：(1) G
- FreeBSD 是否完全接受 GitHub PR，须查当前文档；freebsd.db freebsd-doc 仓库的 Git 迁移主题 commit 显示原大纲 “2021 年 1 月正式完成” 叙事在 doc 仓库层面需修正——doc 仓库的 Git 迁移文档更新集中在 2021-03-16 至 2021-06-16，说明 doc 仓库的实际迁移完成时间在 2021 年 3 月中旬而非 1 月；

## 文献

- ASF 官方历史；Apache Group 早期文档[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.5.2 Apache 许可证与 BSD 许可证的谱系关系

- 要点：Apache 许可证 1.0（2000 年）基于 BSD 许可证修改，1.1（2001 年）去除 advertising 条款，2.0（2004 年）加入专利授权条款；Apache 2.0 与 BSD 三条款在精神上同属宽松许可证阵营，但 Apache 2.0 加入专利保护；二者在 OSI 认证
- mozilla.org 历史[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.6.2 Mozilla MPL 许可证与 BSD 许可证的关系

- 要点：Mozilla 公共许可证（MPL）由 Mitchell Baker 主导设计，1998 年初版，1.1（1999 年）成熟；MPL 是 “弱 copyleft”（文件级 copyleft），介于 BSDL 与 GPL 之间；MPL 允许与闭源代码链接但要求修改的 MPL 文件开源；BSDL 不要求修改文件开源而
- freebsd-hackers mailing list archives；FreeBSD Quarterly Status Reports；The FreeBSD Foundation Annual Reports；bsd_commits.db commits 表 freebsd-src Jordan K. Hubbard commit `e14abeefac54`（1999-12-17T01:47:15Z，"MFC: fixes for dlopen() which allow mozilla to actually work in -stable"）；bsd_commits.db com
- GitHub 官方历史[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.7.2 PR 模式对 BSD 补丁文化的冲击

- 要点：PR 模式对 BSD 补丁文化的冲击：(1) GitHub PR 简化贡献门槛；(2) BSD 传统补丁文化（diff/patch 邮件提交）显得过时；(3) GitHub fork 模式降低贡献门槛但增加质量风险；(4) BSD 社区面临 “是否迁移 GitHub” 的长期争论；冲击持续至 2021 年 FreeBSD 迁移 GitH
- FreeBSD Git 迁移公告；bsd_commits.db commits 表 freebsd-doc Warner Losh commit `86836673be10`（2021-03-16T18:43:35-06:00，"Fix more typos from the original github docs"）；bsd_commits.db commits 表 freebsd-doc Warner Losh commit `abff932fe818`（2021-03-16T22:23:19-06:00，"Merge in the migration from subversion /
- ASF 文档； Jagielski 2008 ［A］
- Weber《The Success of Open Source》；开源会议议程[考据完成：2026-07-28 经穷尽联网考据，上述文献清单为已知公开来源汇总，部分原始档案未公开数字化或须付费访问，属史料缺口，须待原始档案公开后方可补充确证]

## 301.9.2 Open Source 去政治化对 BSD 的消解

- 要点：Open Source 一词去政治化对 BSD 哲学的消解：(1) BSD 哲学强调 “代码在那里，拿走就好” 的低调；(2) Open Source 运动强调 “开放作为商业策略”；(3) BSD 低调哲学被 Open Source 话语淹没；(4) BSD 社区
- DiBona, C., Ockman, S., Stone, M. (eds.) Open Sources: Voices from the Open Source Revolution [M]. Sebastopol: O'Reilly Media, 1999. ISBN 1-56592-582-3（McKusick 章节"From AT&T-Owned to Freely Redistributable"）[Z/OL]. <http://www.oreilly.com/catalog/opensources/book/toc.html> [2026-07-22]；McKusick, M.

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
