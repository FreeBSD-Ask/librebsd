# Ubuntu `openssh-server`（noble 24.04 LTS）包页（新 ref）引用卡

- **性质**：Ubuntu 官方软件包页 `packages.ubuntu.com/noble/openssh-server`（20,629 字节；包版本 `1:9.6p1-3ubuntu20.4` 系列），含一句式说明、维护者与来源包链接
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b015；`packages.ubuntu.com` 库内无条目）
- **source_url**：<https://packages.ubuntu.com/noble/openssh-server>
- **quote（逐字，两处，本批用第 1 处）**：
  1. secure shell (SSH) server, for secure access from remote machines
  2. External Resources: Homepage [www.openssh.com]
- **考据注**：用于**血统可见度的层级差异**（1.13.4）的**消费端下限**样本。计数实测（抓取文本）：`OpenBSD` **0 次**、`OpenSSH` 1 次（仅出现在包名与相关包列表中）、说明句本身不含项目名。与 Debian 同一说明文本（`portable version of OpenSSH, a free implementation of the Secure Shell protocol as specified by the IETF secsh working group`）相比，Ubuntu 页面把说明进一步压成一句功能描述，**可见度更低一层**；但页内仍留“Homepage [www.openssh.com]”链接与“Original Maintainers (usually from Debian): Debian OpenSSH Maintainers”一行，即**线索以链接与来源包形式存续**。**限度**：本页只是一件（noble 一个发行版一个包），不可外推为“Ubuntu 一贯不署 OpenBSD”；跨版本（jammy／resolute）与跨组件（openssh-client、libssh）抽样列待补。缺载不等于反证。
- **本批落点**：V35.1.13.4（第 1 块）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b015；official_doc／L3）
