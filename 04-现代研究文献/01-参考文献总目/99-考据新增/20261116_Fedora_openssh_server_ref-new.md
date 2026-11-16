# Fedora `openssh-server` 包页（新 ref）引用卡

- **性质**：Fedora 官方包页 `packages.fedoraproject.org/pkgs/openssh/openssh-server/`（5,490 字节），含 Upstream 字段、SPDX 许可清单、维护者与各发行版版本表
- **数据库**：新建 ref（2026-11-16 V35 P2 联网补证批 b015；`packages.fedoraproject.org` 库内无条目）
- **source_url**：<https://packages.fedoraproject.org/pkgs/openssh/openssh-server/>
- **quote（逐字，一处）**：

  > Upstream: http://www.openssh.com/portable.html License(s): BSD-3-Clause AND BSD-2-Clause AND ISC AND SSH-OpenSSH AND ssh-keyscan AND snprintf AND LicenseRef-Fedora-Public-Domain AND X11-distribute-modifications-variant

- **考据注**：用于**血统可见度的层级差异**（1.13.4）的**元数据层**样本。可证者三：①`Upstream` 字段直指 `openssh.com/portable.html`，即**归名以 URL 形式进元数据**；②许可清单为 SPDX 表达式，其中 `BSD-3-Clause`、`BSD-2-Clause`、`ISC`、`SSH-OpenSSH` 四条目皆**许可标识符**，是许可层面的可见度而非来源层面的归名；③抓取文本中 `OpenBSD` **0 次**——即**许可名（BSD…）在场，项目名（OpenBSD）缺席**，二者不可混为一谈。这一区分正是 1.13.4 的判据所在。**限度**：许可标识符由打包者填制，其准确性须回核 spec 文件（本批未取，列待补）；`SSH-OpenSSH` 是 Fedora 自定义许可标签而非 SPDX 官方标识符，本卡照录其字面。
- **本批落点**：V35.1.13.4（第 2 块）
- **考据日期**：2026-11-16（Task 8.2 G4 V35 P2 批 b015；official_doc／L3）
