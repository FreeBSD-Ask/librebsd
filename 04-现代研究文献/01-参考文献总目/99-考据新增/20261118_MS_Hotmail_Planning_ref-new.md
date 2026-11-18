# 《Microsoft Hotmail Migration Technical Case Study: Planning Guide》（新 ref）引用卡

- **性质**：Microsoft Learn tn-archive 归档的 Hotmail 迁移技术案例研究规划章；exa web_fetch 实取 2026-11-18（official_doc／L3）
- **数据库**：新建 ref（2026-11-18 Task 8.2 V71—V75 线 supp-V71-b034；source_url 四键查重无重合）
- **source_url**：https://learn.microsoft.com/en-us/previous-versions/tn-archive/bb496990(v=technet.10)
- **quote（逐字）**：其一（Business Drivers）：Performance (and therefore cost). The cgi "one-process-per-socket" model, under FreeBSD, is very inefficient.／FreeBSD lacked the necessary Unicode support. 其二（Pre-Windows 2000 环境）：The Hotmail configuration consisted of clusters of servers—each cluster consisting of approximately 300 Web servers and 8 storage machines. Each cluster supported between 2 million and 20 million users. 其三（End-State）：this included migrating approximately 3,600 servers within a two-month period. The process used for the migration was able to scale to as many as 400 servers per 24-hour period.
- **考据注**：三句分别支撑 V71.3.12.3（迁移决策的业务动因三条：性能成本／全球化 Unicode 缺失／开发周期——技术理由与商业理由并置）、V71.3.12.1（集群构成补充：约 300 Web 机＋8 存储机／200 万—2,000 万用户每集群）、V71.3.12.4（分期实施规模：约 3,600 台两月完成、峰值 400 台每 24 小时）
- **本批落点**：V71.3.12.3 第 1 块／V71.3.12.1 未落（集群句留卡）／V71.3.12.4 第 2 块
- **考据日期**：2026-11-18（Task 8.2 V71—V75 线 supp-V71-b034；official_doc／L3）
