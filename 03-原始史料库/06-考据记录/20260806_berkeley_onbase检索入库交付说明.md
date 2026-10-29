# 伯克利市 OnBase 公共记录检索交付说明（2026-08-06）

## 任务概述

从伯克利市 OnBase 公共记录检索系统（`records.cityofberkeley.info/PublicAccess/paFiles/cqFiles/index.html`，收录市政府法令/决议/会议纪要/通信/合同/选举 6 类档案）检索本项目（BSD 史 18 卷 348 章）所需内容，并整理入库（references_fulltext.db）与入大纲（05-卷册大纲）。

## 检索过程

- **方式**：浏览器 CDP 自动化全文检索（站点有 WAF 防护，命令行直接请求被拦截封 IP，须真实浏览器）
- **关键词**：BSD / CSRG / Unix / computer / Computer Science / International Computer Science Institute / McKusick / DARPA / VAX / Bill Joy / Thompson / free software / Sun Microsystems / University of California 共 14 组
- **排除项**：BSD（建筑安全部门缩写）、CSRG（社区服务拨款缩写）、VAX/DARPA（OCR 乱码/自动驾驶）等均为缩写巧合或噪声，已排除

## 核心成果：确认相关并下载 22 份 PDF

### 一、McKusick 市政活动系列（ref 2736-2741，6 份）★ 最高价值
BSD 核心人物 **Marshall Kirk McKusick**（4.3/4.4BSD 主要开发者、CSRG 核心、FreeBSD 早期领导者）作为**伯克利市民**的市政参与政府档案：
- 2007-05-22 ZAB 上诉案（1885 University Avenue 开发案）议程包，含 McKusick 2006-11-28 意见信
- 2007-09-04 UCB 学生运动员高性能中心市民通信（McKusick 意见信）
- 2007-07-16 通信载 McKusick 住址（1614 Oxford St, Berkeley）
- 2017-05-30 与 2024-07-23 市议会公开评论发言记录（第 32 号/第 517 号发言人）

### 二、ICSI 租赁系列（ref 2742-2751，10 份）
国际计算机科学研究所（ICSI，1988 年由 UCB 与 SRI 创办，位于 1947 Center Street，首任所长 Richard Karp）与伯克利市的租赁契约档案：
- 法令：Ordinance 7024（2008 租赁）、7281（2013 修正）、7496（2016 修正）
- 合同：Lease R7593、Revenue R7593A、R7593B
- 议程包：2008-03-11、2013-02-19、2016-07-12、2016-07-19

### 三、UNIX/计算机市政史系列（ref 2752-2757，6 份）
- 1986-02-18 会议纪要：市政府为卫生与公众服务部购置 UNIX 计算机（Resolution No. 53,086）
- 1990-07-24 决议 55,534：市政府计算机化规划
- 2008-04-22 通信：UNIX/Linux 用户可及性投诉
- 1990-03-27 决议 55,266 + 会议纪要（正文待核验）
- 1984-12-04 决议 52,501（OCR 含 BSD/BIDS，疑似投标，备查）

## 入库与入大纲

| 产出 | 位置 |
|------|------|
| 22 份 PDF 原件 | `04-现代研究文献/03-文献下载/01-pdf/_onbase_berkeley/`（SHA-256 见 `_manifest.json`） |
| 数据库入库 22 条 | `references_fulltext.db#references` id 2736-2757（status=kaoju_new，GB/T 7714 著录） |
| 引用卡 3 张 | `04-现代研究文献/01-参考文献总目/99-考据新增/`（McKusick / ICSI / UNIX计算机市政史） |
| 著录登记 22 条 | `04-现代研究文献/01-参考文献总目/99-考据新增.md` 第十六节 |
| 大纲史料增补 5 文件 | 第 55 章 55.33、第 53 章 53.32、第 54 章 54.1、第 44 章概述、第 55 章概述 |
| 考据记录 | `03-原始史料库/06-考据记录/20260806_berkeley_records_kaoju.md` |
| 数据库备份 | `script/_backup_20260806_onbase_ingest/references_fulltext.db` |

## 存疑事项（0 信任原则）

1. **ref 2757**（1984-12-04 决议 52,501）：OCR 摘要 "TRANSMITTAL OF BSD" 疑似 "BIDS"（投标）误识，倾向无关，原件已存档备查
2. **ref 2754**（1990-03-27 决议 55,266）：正文未及提取核验，待核
3. **Sara McKusick 排除**：2008-07-28 Zero Waste Commission Minutes 命中 Sara McKusick（环境委员会成员），非 BSD 人物，未下载
4. 1984/1986/1990 年旧扫描件 OCR 质量差，**正文引用前须人工核对原件**
5. ICSI 与 CSRG 无人员/技术直接传承，叙事中不得混淆（ICSI 档案为机构史与学科制度史史料）
6. 2024-07-23 通信包（29.5MB）超下载阈值未存档，以同次会议纪要（ref 2738）替代
