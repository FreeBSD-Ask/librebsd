## 282.7 BSD 许可证全系逐版本考据

本节叙述建立于 dslinux_claims 归属 282.7 的 94 条 claim，跨度 2004-01-26 至 2026-08-17，来源含 netdev、linux-fsdevel、linux-mm、linux-scsi 与 ksummit

广告条款移除构成 BSD 简化史第一刀：2004-01-26 Patrick McHardy 移植 altq HFSC 时转述原作者 "they removed the advertising clause, but they did not want to release the code under the GPL"，最终定为 GPL 单许可，四至三条款过渡由此成为内核侧兼容性判据；2005-01-31 OpenBSD 随机化移植中 Adrian Bunk 认定 "At least the three clause BSD license is GPL compatible"，Valdis Kletnieks 手中却是 "the problematic 4-clause version"，须 Shalayeff、Tso、Provos 三方同意重许可，最终改用 Arjan 实现；存量清理迟至 2012-03-04，Paul Mackerras 指出 if_ppp.h 仍挂 "the old BSD-style license with advertising clause"，David Miller 次日合入，距伯克利 1999 年废除公告近十五年

三条款以无线驱动谱系承载，2008-08 Jiri Slaby 说明 ath5k 的 base.c 进入公有领域后 "dual-licensed under 3-clause-BSD and GPL"，此前 Johannes Berg 曾要求恢复 BSD 声明

SPDX 化把 BSD 转为标识符治理：2018-03-14 Greg KH 反向劝退 "Remember, BSD is not the license you want/need for GPL header files that are exposed to userspace..."；2018-10-08 Alexei Starovoitov 完成 libbpf 首次双许可，"Hence let's relicense libbpf as dual license LGPL-2.1 or BSD-2-Clause, since BSD-2 is compatible with Apache2"，二条款由此获得 bcc、bpftrace 等 Apache2 项目接入理由，三条款则以厂商网卡与交换机驱动为承载

治理侧收紧并反向收敛：2020-04-07 checkpatch 补丁写定 "the Devicetree binding documents are preferrably licensed (GPL-2.0-only OR BSD-2-Clause)"，Laurent Pinchart 认为措辞过弱；Microchip KSZ956x 在 2020-11-18 至 2020-12-03 连续执行 "dts: remove OR BSD-2-Clause from SPDX-License-Identifier"，把双许可收敛回单一 GPL

语料末端的家族细分难题：2023-05-22 UDF 转换因 fs/udf/ecma_167.h 无法归类被排除，Jan Kara 转述 "The latter file apparently looks like 2-clause BSD Source-Code license, yet the second clause is from third clause of 3-Clause BSD"，该非标混合体在标识符体系中不可表达；2026-08-17 的 selftests/exec 补丁中 "The license is OpenBSD, not ISC." 显示 ISC 与 OpenBSD 模板仍需人工区分

须说明本节覆盖止于四、三、二条款及其 BSD 家族变体，条款递减表现为广告条款与背书禁止条款两次移除，1-Clause 与 0BSD 在语料中无可考记录
