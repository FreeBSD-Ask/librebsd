# WireGuard《Protocol & Cryptography》（新 ref）引用卡

- **性质**：WireGuard 官方协议页（wireguard.com/protocol/，作者页署 Jason A. Donenfeld；本机 curl 直连超时，经 exa 渲染取得全文，只引全 ASCII 句）
- **数据库**：新建 ref（2026-11-18 G4-P2 批 b027；wireguard.com 域库内无条目）
- **source_url**：<https://www.wireguard.com/protocol/>
- **quote（逐字，两段，段间以省略号连接；exa 渲染层的行内代码反引号剥离后连读）**：

  > This handshake occurs every few minutes, in order to provide rotating keys for perfect forward secrecy. … WireGuard uses the Noise_IK handshake from Noise

- **考据注**：用于**密钥协商以静态公钥与临时密钥组合、会话模型决定前向保密**（2.9.3）。两句分别承载会话模型的两要素：①握手每数分钟一次、轮转密钥以提供完美前向保密（会话模型＝前向保密的机制）；②密钥协商协议为 Noise_IK（Noise 家族，含静态与临时密钥的合取结构）。基元面另有“Curve25519 for ECDH”等条目，本批未引。
- **改道披露**：wireguard.com 本机 curl 超时（exit 28），经 exa 渲染取证——两句全 ASCII、无撇号引号符，转换层无改写点；行内代码反引号（Noise_IK 原文在页面上为代码体）剥离披露。
- **限度**：①协议页是设计自述，实现面（wireguard-freebsd 移植）另有出处面；②“静态公钥＋临时密钥组合”的结构细节在 Noise_IK 握手分节，本批未整段引；③页随协议版本演进更新。
- **本批落点**：V37.2.9.3
- **考据日期**：2026-11-18（Task 8.2 G4-P2 批 b027；official_doc／L3）
