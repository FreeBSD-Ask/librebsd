---
chapter: 第 47 章
id: CH47
volume: 第03卷-伯克利学术文化外溢影响
---

# 第 47 章 被遮蔽史实与csrg管理制度

## 要点

- CSRG 档案公开化涉及多重法律问题——其一，BSD 源码受加州大学董事会版权（The Regents of the University of California），1999 年 7 月 22 日 BSD 许可证最终条款移除 “广告条款” 后，源码公开化的法律障碍大幅降低；其二，CSRG 档案中含 AT&T UNIX 残留代码（USL 诉讼和解后 4.4BSD-Lite 已清除大部分，但 Ba
- CSRG 的经费主要来自 DARPA 联邦合同（1980 年 4 月生效的 18 个月长约及后续续签合同），经费分配遵循联邦合同研究的标准模式——直接成本（研究人员工资、研究生 RAship 津贴、设备采购、差旅）与间接成本（伯克利收取的 F&A 费用，通常为直接成本的 50-60%），此分配模式引发若干争议——其一，间接成本比例过高：伯克利收取的间接成本率（F&A rate）在 1980 年代约
- CSRG 机构化前 BSD 的商业化路径主要通过 AT&T UNIX 商业许可证——商业公司使用 BSD 代码须购买 AT&T UNIX 源代码许可证（1984 年反垄断分拆前 AT&T 垄断 UNIX 商业化），BSD 代码本身无独立商业授权模式；CSRG 机构化后（1980 起）BSD 商业化路径分化为多元模式——其一，CSRG 成员毕业后创办或加入 BSD 衍生公司，Bill Joy 198

## 史料

- [DB:bsdnow_podcast:outline_mappings:om_11803] BSD Now 第 487 期，匹配 CH47 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12016] BSD Now 第 465 期，匹配 CH47 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_12607] BSD Now 第 404 期，匹配 CH47 章，关联度 1.0

## 史观

（章级史观/辨析按子节字段聚合回填——本卷 47 章；2026-09-11 整改将占位改为编排说明，完整聚合随正文阶段逐章完成。子节级映射详见各节史观字段。）

## 辨析

- Bancroft CU-551 物理档案中是否仍含 USL 诉讼前材料（如 Net/2 时期含 USL 代码的版本）保留 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］ 待 Bancroft 实地核验与法律专家评估；USL 诉讼和解协议中关于 “诉讼前档案” 的保密条款是否仍约束 Bancroft 访问保留 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］. 美国新泽西联邦地区法院。<https://law.justia.com/cases/federal/district-courts/FSupp/832/790/1428569/> [2026-07-22]；Open Source Initiative BSD License 历史版本；McKusick 关于 CSRG 档案公开化的公开陈述 ［B］
- DARPA 合同档案；伯克利科研管理档案；CSRG 预算文件（Bancroft CU-551）；McKusick (1999)；Leslie, S. W. (1993) “The Cold War and American Science” ［A］
- AT&T UNIX 商业许可证档案；Sun Microsystems 注册文件（1982.2.24）；BSDi 公司档案；伯克利 OTL 档案；Walnut Creek CDROM 档案；McKusick (1999) “Twenty Years of Berkeley Unix” ［B］### 史观映射> 没有人能被 “教会” 写操作系统——McKusick 可以让研究生坐在终端前，但不能替他们的手指找到键盘上的路径。CSRG 的学徒制不是教育制度，而是一种在承认启蒙不可能之后仍然选择把工具递到别人手上的姿态。man pages 不是教材，而是一群人把自己摸索出来的东西写下来，让后来者少走弯路——写文档的人度不了别人，但写文档这件事本身就是在修行。伯克利的地理给了这一切一个容器：Evans Hall 四楼东翼的办公室、Sproul Plaza 上尚未散去的抗议标语、隔湾相望的硅谷——自由言论运动的遗产与 hacker 伦理在此渗透而非因果，反战一代的 “质疑权威” 与源代码分发的 “信息自由” 只在气质上共鸣，而非逻辑上衔接。而 Reagan 的 SDI 经费与 NSFNET 骨干、80386 的普及与 RISC 的兴起、Heyman 与 Tien 两任校长的治下——这些力量从外部挤压，使 CSRG 在学术自治的缝隙中走完了从研究小组到开源先驱的全部路程> 本章新增 22.21 节专述 CSRG 档案的去向与公开化：显而易见却罕有人知道的是，CSRG 1995 年解散后档案物理去向长期模糊——伯克利 Bancroft 图书馆 CU-551 全宗（1974-2005，12.5 线性英尺，10 罐档案盒）保存了纸质手册、9 磁道磁带、QIC 磁带等载体，而 McKusick 个人整理的 CSRG Archive CD-ROM 套装（4 CD 集，$99，CD-ROM #4 含 “ Final /usr/src including SCCS files ”）则是另一条平行的史料保存路径。CSRG 档案的公开化与 BSD 许可证的演化（1999.7.22 移除广告条款）以及 USL 诉讼前档案的法律状态紧密关联，史家研究 CSRG 时期事件需同时检索 Bancroft 图书馆全宗目录、McKusick CD-ROM 套装、SCCS 元数据、纸质手册与邮件列表归档五类载体——这是 CSRG 解散后留下的隐性遗产，也是 BSD 史学不可回避的考据挑战---

<!-- dangan-20260908 消解回写 -->
- Leslie. The Cold War and American Science[Z]. 1993. ［DKC-1304→fulltext:5860］
<!-- /dangan-20260908 -->
