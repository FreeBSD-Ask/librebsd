# 127. stable CVE 系列与 25MB 大差异（ann p15）（ann p15）

> 来源：linux-kernel-announce 人工信 p15（10 封全读，2003-12 至 2007-11，stable 2.6.15.6/.1/18.6 三封（CVE-2006-0742/0035-0037/6106）、-mm 发布五封（补丁被无视之叹/25MB x86 大差异/NMI 疑损 nmi_watchdog=0 规避/bk-audit 首纳）、loop-AES v2.0d 安全洞修复、伪造 2.0.1 公告玩笑 NV）
> 判定：9 CAND / 1 NV。主题分布：2.6.22-rc4-mm2 1、Linux 2.6.15.6 1、Linux 2.6.15.1 1、2.6.24-rc3-mm2 1、Announce loop-AES-v2.0d file/swap crypto package 1、2.6.21-rc6-mm1 1、Linux 2.6.18.6 1、2.6.12-rc2-mm1 1、2.6.11-mm1 1。

## 127.1 2.6.22-rc4-mm2

- 【Linux社区】Andrew Morton 发布 -mm 补丁集；开篇评语“基本是 rc4-mm1 的修 bug 版”，未重拉子系统树，丢弃若干坏补丁并逐条附修复说明，共 1208 个补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.722841 -->`

## 127.2 Linux 2.6.15.6

- 【Linux社区】Chris Wright 发布 stable 版；附 5 文件 diffstat 与逐人修复摘要，含 IA64 die_if_kernel 修复（CVE-2006-0742），并预告回帖贴出完整补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.722899 -->`

## 127.3 Linux 2.6.15.1

- 【Linux社区】Chris Wright 发布 stable 版；16 文件 diffstat 加逐人修复摘要，含 netlink DoS（CVE-2006-0035）与 ip_nat_pptp 两处崩溃（CVE-2006-0036、CVE-2006-0037） `<!-- ROW_MINE: linux-kernel-announce.messages.722909 -->`

## 127.4 2.6.24-rc3-mm2

- 【Linux社区】Andrew Morton 发布 -mm 补丁集；直言子系统补丁多被维护者无视、s390 编译失败、丢弃 unprivileged mounts 与 revoke 系列，余下开发周期不再收特性补丁，共 3329 提交 `<!-- ROW_MINE: linux-kernel-announce.messages.722927 -->`

## 127.5 Announce loop-AES-v2.0d file/swap crypto package

- 【Linux社区】Jari Ruusu 发布加密工具 loop-AES 与 ciphers v2.0d；说明 v2.0c 的 SMP race 修复在 2.2/2.0 内核多密钥模式下引入新竞争与安全洞，本版已修复并附 md5 与签名地址 `<!-- ROW_MINE: linux-kernel-announce.messages.722930 -->`

## 127.6 2.6.21-rc6-mm1

- 【Linux社区】Andrew Morton 发布 -mm 补丁集；评语为大量 x86 更新、相对主线 25MB 的较大差异，附逐补丁分组评语（paravirt_ops、maps2 等），共 1405 个补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.722951 -->`

## 127.7 Linux 2.6.18.6

- 【Linux社区】Chris Wright 发布 stable 版；27 文件 diffstat 与逐人修复摘要，核心为蓝牙 CAPI 报文长度检查（CVE-2006-6106），并预告回帖贴出补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.722958 -->`

## 127.8 2.6.12-rc2-mm1

- 【Linux社区】Andrew Morton 发布 -mm 补丁集；提醒 x86 NMI 处理疑似损坏可用 nmi_watchdog=0 规避、定时器相关挂起可能已修复，附全量补丁列表，共 634 个补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.723032 -->`

## 127.9 2.6.11-mm1

- 【Linux社区】Andrew Morton 发布 -mm 补丁集；新增 David Woodhouse 维护的 bk-audit 树、Dell 键盘问题应已修复待验证、丢弃 bk-dtor-input 树，共 821 个补丁 `<!-- ROW_MINE: linux-kernel-announce.messages.723039 -->`
