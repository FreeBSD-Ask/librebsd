# 功能库第二批行级遍历考据：research_notes

日期：2026-08-31
Spec：db-row-traversal-mining-2026-08-29（Phase 2A）

## 查证来源

- research_notes.duckdb blocks 486894 行（json_node/quote/paragraph/list_item/footnote 分层）与 files 表全量清单
- 自写漏洞群归档叙述层 53 行（_pg_rn_selfreports.jsonl）、五国判例取证报告 fid=1620 全部叙述行
- 联网核验（检索时间 2026-08-31）：
  - 罗盒诉玩友案：最高人民法院官网 court.gov.cn/zixun/xiangqing/355881.html（2021 年中国法院 10 大知识产权案件，2022-04-21 发布，"赔偿罗盒公司经济损失及维权合理支出共计50万元。一审宣判后，双方当事人均未上诉"）+ 最高法知产法庭官网 ipc.court.gov.cn/zh-cn/news/view-1823.html（（2019）粤73知民初207号判决书原文，2020-11-03 公开开庭）
  - 罗盒诉风灵案：ipc.court.gov.cn/zh-cn/news/view-3655.html（（2021）最高法知民终2063号判决书，2024-11-08 发布；原审为深圳中院（2019）粤03民初3928号，2021-04-30 判决）——补全源行"案号待补"存疑项
  - 北京隆诺律师事务所《中国知识产权审判动态跟踪》第 48 期（2022-01-04）交叉印证罗盒案 GPL V3 协议性质认定
- 产物：claims_to_write_research_notes.jsonl（6 条：CL-RM-001501~001506），已逐条写入 historical_claims.duckdb 并回读校验

## 交叉验证方法

1. 漏洞群归档主张（L5）：数据源为 bsd_commits.db 查询 + NVD 元数据 + 官方 Security Advisory 三方组合（归档文件自述），属代码层统计事实，直接采纳为 L5 data_query 证据；同源归档间互证（FreeBSD 各周期数据连续、OpenBSD 2.x 期 0 CVE 与 FreeBSD 1.x 期 0 CVE 互证"CVE 惯例晚于 CVE 制度普及"）。
2. 中国判例主张（L3）：源行三源核验（裁判文书网+最高法公告+法院官网）+ 本次联网复核最高法官网原文，案号、判决日期、赔偿金额、上诉状态逐项比对一致；风灵案案号以最高法知产法庭官网 2024-11 公开的二审判决书为准补全。
3. 分层判定：json_node 随机抽样 8 行 + 长度分布全量统计（88.9% 为 <100 字符键值）；quote 层标记统计（1956 行考据/63 行评级）；para/list 批次画像（file_id 集中度 + GB/T 标记/新闻/代码模式计数）+ 每批首行抽验，按批判定登记型/结论型。

## 存疑判定依据

- 不乱买诉闪亮案（pk=464461）与 NeoBit v. Daou 案（pk=464485）：源行明确标记 [存疑脚注]（案号/裁判要旨未取得），按宁缺毋滥不入主张，登记 needs_research_notes_recheck.md。
- 日本/英国判例稀少结论（pk=464469/464477）：属跨国比较学理综述而非单一原子事实，随五国比较框架留在大纲层，不入主张库。
- json_node >300 字符 2522 行：登记后续精读池，非存疑。
