# 《FreeBSD/EC2: Community vs. Marketplace AMIs》（新 ref）引用卡

- **性质**：Colin Percival 个人博客（daemonology.net）技术博文；web_reader 实取 2026-11-18。作者为 FreeBSD EC2 AMI 官方维护者、release engineering 团队成员，博文系当事人对其所司发布机制的事后书面追述（talk_interview 抬头／L4 当事人一手记载）
- **数据库**：新建 ref（2026-11-18 Task 8.2 V71—V75 线 supp-V71-b032；source_url 四键查重无重合）
- **source_url**：https://www.daemonology.net/blog/2017-10-21-FreeBSD-EC2-community-vs-marketplace-AMIs.html
- **quote（逐字）**：其一：FreeBSD has been available in Amazon EC2 since FreeBSD 9.0 (January 2012), and from FreeBSD 10.2 (August 2015) AMIs have been built by the FreeBSD release enginering team as part of the regular release process.（原文 enginering 拼写照录，逐字保真）。其二：The AWS Marketplace is designed as a sales channel for products based on AWS, replacing a previous mechanism called "paid AMIs".／Amazon provides me with statistics about the "sales" of FreeBSD AMIs.（如 yesterday there were 1000 AWS accounts which collectively had a total of over 10,000 FreeBSD instances running）。其三：Because adding images to the AWS Marketplace is a manual process, we only do this for FreeBSD releases — not for the weekly snapshots or the beta and release candidate images in the months leading up to the release.／The AWS Marketplace often lags behind EC2 in adding support for new regions and instance types.
- **考据注**：三句分别支撑 V71.3.10.1（EC2 双渠道：release 公告列各区域 AMI 号的社区渠道＋第三方验证后上架 Marketplace 的渠道）、V71.3.10.3（Marketplace 条目化：产品页、销售渠道机制、维护者可得“销售”统计）、V71.3.10.5（上架为手动流程、仅覆盖正式 release、新区域与实例类型滞后于 EC2 本体）。博文原含 11.1 发布公告逐区域 AMI 号清单转引（ami-…），佐证社区渠道形态；release 公告原文另有签名字面背书（signed release announcement）
- **本批落点**：V71.3.10.1 第 2 块／V71.3.10.3 第 1 块／V71.3.10.5 第 2 块
- **考据日期**：2026-11-18（Task 8.2 V71—V75 线 supp-V71-b032；talk_interview／L4）
