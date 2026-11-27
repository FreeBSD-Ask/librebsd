# Donenfeld《WireGuard: Next Generation Kernel Network Tunnel》（新 ref）引用卡

- **性质**：Jason A. Donenfeld 在 NDSS 2017 发表的 WireGuard 论文（同行评议会议论文）
- **数据库**：新建 ref（2026-11-28 G4 全责线 V37 批 b031；库内无该论文条目）
- **source_url**：<https://www.ndss-symposium.org/wp-content/uploads/2017/09/ndss2017_04A-3_Donenfeld_paper.pdf>
- **quote（逐字，PDF 提取后仅将连字 ﬀ 还原为 ff）**：

  > Since a public key uniquely identifies a peer, the outer external source IP of an encrypted WireGuard packet is used to identify the remote endpoint of a peer, enabling peers to roam freely between different external IPs, between mobile networks for example, similar to what is allowed by Mosh [24].

- **考据注**：用于**移动场景的漫游支持**（V37.2.9.4）。论文“Endpoints & Roaming”节说明：公钥唯一标识 peer，接收方以加密包的外层源 IP 识别对端端点，因而 peer 可在不同外部 IP 与移动网络之间自由漫游；端点可预配置也可由认证包学习，地址变化不打断会话。
- **限度**：①论文为设计自述与评估，具体实现行为须以 wireguard-freebsd 源码复核；②“roam freely”以 NAT 可达与认证包为前提，不保证所有网络环境；③PDF 连字 ﬀ 已还原为 ff，其余逐字照录。
- **本批落点**：V37.2.9.4
- **考据日期**：2026-11-28（Task 8.2 G4 全责线 V37 批 b031；academic_work／L3）
