# 卡片草稿：OpenBSD signify(1) 签名工具

- 题名：signify(1) — cryptographically sign and verify files
- 作者／机构：Ted Unangst、Marc Espie（The OpenBSD Project）
- 出版者／站点：man.openbsd.org（OpenBSD Manual Pages）
- 出版年：2014（页无页脚日期；HISTORY 载 first appeared in OpenBSD 5.5，2014-05-01 发布，著录年按此记）
- URL：https://man.openbsd.org/signify.1
- 引用格式（GB/T 7714-2015）：OpenBSD Project. signify(1) — cryptographically sign and verify files[EB/OL]. OpenBSD-current. https://man.openbsd.org/signify.1 [2026-11-28].
- 引文摘录："Verify a signed checksum list, and then verify the checksum for each file. If no files are specified, all of them are checked. sigfile should be the signed output of sha256(1)."
- 引文摘录二："Verify a release directory containing SHA256.sig and a full set of release files:"
- 引文摘录三："When deducing the correct key to check a signature, make sure the actual key matches /etc/signify/\-keytype.pub."
- 备注：本批 2.12.1／2.12.2／2.12.4 三题引文出自该页；-t 引文含 \ 转义（快照原形照录）。
