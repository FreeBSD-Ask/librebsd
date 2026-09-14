---
chapter: 第 182 章
id: CH182
volume: 第09卷-netbsd的历史
---

# 第 182 章 netbsd-9.0的发布与zfs集成

## 要点

- NetBSD 9.0（**2020.2.14**）引入实验性 ZFS 支持，源于 OpenZFS 移植；工程挑战包括 SPL（Solaris Porting Layer）适配、内存管理（NetBSD UVM vs Solaris VM）、并发原语转换；ZFS 在 NetBSD 上的稳定性与性能不及 FreeBSD OpenZFS
- NetBSD 9.0 Release Notes 与 CVS commit log 是研究 9.0 开发的核心史料；9.0 发布周期约 1 年 7 个月（8.0 于 2018.7.17 发布，9.0 于 2020.2.14 发布，后续 9.1/9.2/9.3/9.4 持续维护）；commit 记录反映 ZFS、GPU、网络协议栈的开发节奏
- NetBSD 9.0（**2020.2.14**）改进文件系统支持，ext2fs 的进一步改进支持更多 ext4 特性；旧 FFS 作为默认文件系统延续，新文件系统作为可选；此改进让 NetBSD 在现代 Linux 文件系统互操作上获得能力。~~原叙事中“NetBSD 9.0 引入对 F2FS（Flash-Friendly File System）〔待核：原文截断，后文待回源〕
- 2020 年 CoW 文件系统格局：FreeBSD 12/13 与 NetBSD 9.0 深度整合 OpenZFS，Linux 经 ZoL 树外提供，illumos/Solaris 持 ZFS 原创，OpenBSD 坚持 FFS/softraid，Windows 用 ReFS；NetBSD 9.0 的 ZFS 补齐使其存储能力与 FreeBSD 对齐。
- 9.x 周期 NetBSD Security Officer Team 的 18 个 SA 在数量、节奏、覆盖面三个维度均显著低于 FreeBSD 14.x 周期同时段——9.x 周期约 5 年（2020.2 至 2024+）18 个 SA，FreeBSD 14.x 周期不足 3 年（2023.11 至 2026.7）80 个 SA，年化速率 NetBSD 约 3.6 SA/年、FreeBSD 约

## 史料

- [DB:references_fulltext:chapter_matches:chmatch_4090] 卷“第09卷-netbsd的历史”第 182 章，匹配置信度 1.0，原因：任务4第二批 缺口章补充

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- NetBSD ZFS 与 FreeBSD OpenZFS 的关系存在叙事分歧——部分资料称 NetBSD 直接移植 FreeBSD OpenZFS，部分称通过 OpenZFS 仓库共享代码，需对照源码核验。经 netbsd.duckdb netbsd-src 仓库 commits 表验证：NetBSD ZFS 代码由 chs（Chuck Silvers）于 2018-05-28 从 FreeBSD SVN
- 先前叙事中称“9.0 发布日期 2020.5”系误传——NetBSD 官方发布页面（netbsd.org/releases/formal-9/NetBSD-9.0.html）明确为 2020.2.14；9.0 发布周期实际约 1 年 7 个月而非 2.5 年；9.0 的实际功能完整性需对照 release tarball 核验 ［考据注：2026-07-28 联网考据留痕，模板句式已按考据审慎原则精简（WO-004）；语义以正文与所引来源为准］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2020-2020 年间：34,930 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD 9.0 Release Notes；tech-file-system 邮件列表；ext2fs/ext4 设计文档 ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- McKusick M K, Neville-Neil G. The Design and Implementation of the FreeBSD Operating System [M]. 2nd ed. Addison-Wesley, 2015. ［B］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 2020-2020 年间：34,930 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。
- NetBSD Project. NetBSD Security Advisories Archive [EB/OL]. (2020-2024)[2026-07-22]. <https://www.netbsd.org/support/security/advisory.html>; NetBSD Project. NetBSD Security Officer Team — SA Release Process [EB/OL]. [2026-07-22]. <https://www.netbsd.org/support/security/>; FreeBSD Security Team. FreeBSD Security Advisories Archive [EB/OL]. (2023-2026)[2026-07-22]. <https://www.freebsd.org/security/advisories/>; OpenBSD Project. OpenBSD Errata Patches [EB/OL]. [2026-07-22]. <https://www.openbsd.org/errata.html>; NetBSD Project. netbsd.duckdb — netbsd-src SA pull-up commits [DB/OL]. 2026-07-22. `SQL: SELECT commit_hash, author_date, author_name, message_subject FROM commits WHERE repo_name='netbsd-src' AND author_date>='2020-02-14' AND author_date<'2024-12-31' AND (message_subject LIKE '%SA%' OR message_subject LIKE '%pull-up%' OR message_subject LIKE '%ticket%') ORDER BY author_date ASC` ［A］

<!-- DB_REF:netbsd.duckdb -->
> **数据库引用（netbsd.duckdb）**：本子节对应 netbsd 代码仓库。> 1993-2026 年间：1,999,408 次提交。> 仓库总览：1,999,412 次提交，1,545 位贡献者（contributors 表行数，1992-07-13 至 2026-08-24）。

<!-- PODCAST_REVIEW v20260829 -->
<!-- 语义复核范围：BSD Now EP376、BSD Now EP374、BSD Now EP352、BSD Now EP330（共 4 期）；逐期通读转写全文后重写，非关键词或实体评分提取 -->

**要点**：

- FreeBSD 12.2 引入 special VDEV（metadata classes）：可把元数据（目录内容、时间戳、文件大小等）与可选的小数据块存入专用 SSD VDEV，数据块留在机械盘，从而加速 find、rsync 等元数据密集操作；使用时须镜像元数据 VDEV（丢失元数据则数据近乎无用），且加入既有池后仅新写入文件的元数据迁移过去，需以 send/receive 或等待数据自然修改来迁移。（BSD Now EP376，[569.22-679.88]，L2）
- 12.2 的已知问题：IPFW forward 规则向同一接口多 IP 转发时存在栈损坏导致的随机端口问题，修复将随 12.2-p1 发布；zfs receive 在期待删除旧快照时也有问题并将修复；BeagleBone 因 SD 卡 IO 异常缓慢而暂未提供 12.2 镜像；DVD 安装器内附带的 GDM 版本损坏，需在安装后从上游镜像升级。（BSD Now EP376，[686.3-800.7]，L2）
- 用户空间与基础设施改进：rc.conf 新增 linux_mounts_enable（依赖 linux_enable 挂载 Linux 专用文件系统）；cron 新增 -n 与 -q（成功时不发邮件、不记日志）；dd 新增 conv=fsync/fdatasync/sync 与 iflag=fullblock 等选项；fsck 支持 ms-dosfs；showmount 支持长选项；mountd 修正 map root/map all 的根目录列出；sesutil 新增面向人读的 show 子命令；jail 工具支持在 jail 内运行 Linux 程序；read 系统调用默认禁止读目录，可用 security.bsd.allow_readdir 恢复。（BSD Now EP376，[84.16-477.1]，L2）
- certctl 项目由 Alan Jude 发起：把 Mozilla CA 根证书包拆分为单个证书随系统分发，并允许管理员额外信任自签证书或显式不信任某些证书，满足企业在 SSL 拦截设备、管理系统中信任自有证书的需求，由 Kyle Evans 完成落地；virtio 块驱动新增 trim 支持，使 FreeBSD 作为 guest 删除数据时能向 hypervisor 释放空间，bhyve 侧 zvol 也能相应释放。（BSD Now EP376，[234.84-295.3]，L1）
- ZFS per-dataset kstats：kstat.zfs.<pool>.dataset 下按 object ID 为每个数据集提供读写次数与字节数，计数自重启或导入后从零累计，可定位哪个客户或虚拟机在制造磁盘负载；升级时还须更新池与池的 boot 部分。（BSD Now EP376，[485.72-554.12]，L1）
- Klara Systems 的 ZFS 最佳实践研讨会于 11 月 18 日举行，由 Alan Jude 主持，内容覆盖存储阵列硬件选择、RAID-Z 与镜像取舍、special metadata VDEV、随数据增长的规划与池扩展/收缩（device evacuation），以及 dataset 与属性，强调建池早期的决策决定日后能否扩展或收缩。（BSD Now EP376，[822.68-947.34]，L1）
- NetBSD 的 GSoC 2020 最终报告：Ayush Sharma 开发 sys2z 工具链，用 extractor、bear.py、c2xml.py、description.py 四个步骤从 C 设备驱动源码自动提取 ioctl 命令及参数并生成 syscaller 描述文件，以减少手工错误、扩大 syscaller 覆盖；未来工作包括宏检测自动化与函数类型描述，导师为 William Caldwell、Siddharth Muralee、Santosh Raju 与 Kamil Rytarowski。（BSD Now EP376，[958.04-1225.66]，L2）
- OpenBSD stable 包构建基础设施（dataswamp.org）：2019 年夏获 Theo de Raadt 提供硬件后搭建，仅约 110 行 shell；各架构机器每日三次以 cron 更新 CVS ports 树，用 CVS rdiff 求自 release 以来变更的 port 列表，查 SQL ports 数据库展开 flavor/subpackage/multipackage，清理环境后用 dpb 编译，送交签名团队人工签名（自动构建者不接触签名密钥），再以 rsync 输出与邮件通知；新设计由一台机器汇总各架构输出、并在构建前统一下载 distfiles 以避免 NFS 并发抓取失败。（BSD Now EP376，[1233.08-1588.12]，L2）
- OPNsense 20.7.4 发布：完成近期的 netmap 内核改动与测试、更新 Realtek 厂商驱动及 kernel、libxml、openssl、php、suricata、syslog-ng、unbound 等第三方组件，并感谢 Sunny Valley Networks 持续把 netmap 修复送入 FreeBSD；WebGUI 支持地址选择、网关组件 API 化、接口 MTU 上限升至 65535（依 RFC 791），防火墙部分新增网络排除/别名类型与 pfInfo 页面。（BSD Now EP376，[1591.02-1720.44]，L2）
- 其他项目动态：DragonFly BSD 把 binutils 回退至 2.34 并暂时改回 ld.bfd，以解决 ld.gold 不尊重 section merge 链接脚本导致 boot1.efi/loader.efi 构建失败的问题（可设 WORLD_LDVER=ld.gold 恢复默认）；NetBSD 的 GitHub 贡献图自 1992 年延续 28 年、1996 年才明显繁忙；OpenBSD 无蓝牙支持，可用 Creative Labs BT-W2 这类把自己呈现为 USB 音频设备的桥接器；社区有基于 FreeBSD/bhyve、CBSD 与 netmap VALE 的 Kubernetes 集群方案，约一分钟 bootstrap，支持 PV/PVC 快照。（BSD Now EP376，[1720.44-2013.24]，L2）
- 反馈环节：Sean 询问 Poudriere 能否全局给 C/C++ 编译器传 -fsanitize 参数，Alan 说明可在 /usr/local/etc/poudriere.d/ 下按 make.conf 层级（全局、包集、ports 树及组合）设置 CFLAGS/CXXFLAGS，从最不特定到最特定拼接，个别必须用 GCC 的 port 可用条件判断排除；Thierry 询问树莓派 loop 挂载镜像的延迟问题，Alan 解释 ZFS 默认 128K record 在 4K 小改时产生读-改-写放大，建议把存放镜像的数据集 record size 调小（如 8K）。（BSD Now EP376，[2189.46-2722.88]，L1）
- OpenBSD 于 2020 年 10 月 18 日发布 6.8 版，正值项目创立二十五周年；该版引入由引导装载器向内核传递的随机种子置信度标记、在支持的 arm64 处理器上启用 PAN，并改进 FFS、安装镜像与多架构安装引导。（BSD Now EP374，[0.0-10.72]，L2）
- NetBSD 于 2020 年 10 月 18 日发布 9.1，新增并行磁盘加密、C.UTF-8 区域设置、ZFS 支持增强、NVMM 虚拟机监控器更新以及 PowerPC64 PowerNV 支持。（BSD Now EP374，[590.42-796.96]，L2）
- OpenZFS 开发者峰会 2020 因疫情改以 Zoom 举办，采用 webinar 演讲与虚拟走廊并行的组织方式；峰会自 2013 年起规模持续扩大，本年取消人数上限后允许更多人参加。（BSD Now EP374，[847.32-970.56]，L1）
- BastilleBSD 相关文章将容器技术谱系上溯至 1979 年 Unix 第七版 chroot，指出 jail 术语最早见于 1991 年 4.3BSD，FreeBSD 4.0 于 2000 年提供 jail 命令，Linux 迟至 2008 年才有 LXC、2013 年才有 Docker。（BSD Now EP374，[1848.72-2116.32]，L2）
- 本期主话题是 NetBSD 内核对随机数生成机制的重写，目标是把熵池升级到满足 256 位不可预测性等新期望。（BSD Now EP352，[182.96-190.12]，L2）
- 主持人的核心判断是：随机数在操作系统中多处不可或缺，现代系统通常把 RD-RAND、RD-SEED 等硬件输出与哈希混合，单一熵源失效不应击穿整个系统。（BSD Now EP352，[159.08-178.48]，L2）
- 新闻部分记载 NetBSD core team 人事变动：Matt Thomas 在服务十余年后卸任，Robert Elz 受邀加入；同期 FreeBSD core team 进行两年一度的民主选举。（BSD Now EP352，[764.8-901.42]，L2）
- OpenBSD 的 BSD Authentication 认证绕过漏洞源于 login_passwd 对 challenge 协议的处理缺陷，用户名形如 -schallenge 时会被自动判定成功；该漏洞远程可利用于 smtpd、ldapd、radiusd 等应用，但 sshd 因纵深防御机制不受影响。（BSD Now EP330，[185.76-193.66]，L2）
- OpenBSD 在初次联系后约 40 小时内修复该漏洞，主持人以此与其它项目耗时数月乃至数年的修复形成对照，凸显其把安全响应置于优先位置的组织惯性。（BSD Now EP330，[562.80-584.46]，L3）
- NetBSD 9.0 RC1 在四个月发布流程中处理逾 500 次 pull-up，新增 aarch64（含 Arm ServerReady）、NVMM 硬件虚拟化、更新版 ZFS、内核 ASLR、KLEAK/KASAN 等 sanitizer、NPF 改进与 SATA NCQ 支持。（BSD Now EP330，[724.00-802.99]，L2）
- FreeNAS 在 DigitalOcean 的部署教程通过第二块设备安装后再以 dd 重灌引导区完成，主持人补充 ZFS 的校验与校验和使消费级磁盘配合 RAID-Z1 冗余在家庭 NAS 场景可用，并强调以独立备份兜底。（BSD Now EP330，[1084.88-1299.54]，L2）
- NomadBSD 1.3 是基于 FreeBSD 12.1 的 USB 持久化 Live 系统，通过 SMBIOS 检测自动适配 VirtualBox，新增 ZFS 安装支持，并因 Lenovo 兼容问题从 GPT 改回 MBR。（BSD Now EP330，[1790.46-1892.38]，L2）
- e2k19 黑客松重写 RPKI 客户端的 X.509 验证，将证书与 CRL 表改为红黑树查找、以 rename 原子替换输出文件，使 VRP 验证从 20 余分钟降至约 1 分钟。（BSD Now EP330，[2281.90-2516.12]，L2）

**史料**：

- FreeBSD 12.2 发布说明、errata 列表与已知问题 PR 链接，一手发布工程文献。（BSD Now EP376，[686.3-800.7]，L1）
- dataswamp.org 关于 OpenBSD stable 包构建的博客（含脚本步骤、签名团队与各架构差异），一手基础设施记录。（BSD Now EP376，[1233.08-1588.12]，L1）
- NetBSD GSoC 2020 最终报告（sys2z 工具链与导师名单），一手项目文献。（BSD Now EP376，[958.04-1225.66]，L1）
- OPNsense 20.7.4 发布说明与 Sunny Valley Networks 的 netmap 上游化贡献记录。（BSD Now EP376，[1591.02-1720.44]，L1）
- OpenBSD 6.8 官方变更日志与发行公告，涵盖 OpenSSH 8.4、LibreSSL 3.2.2、OpenSMTPD 与 VMM/VMD 更新，由主持人转述。（BSD Now EP374，[357.24-391.04]，L2）
- NetBSD 9.1 官方发布公告，涵盖 cgd 并行磁盘加密、ZFS、NVMM、NPF、X11 默认窗口管理器切换等内容，由主持人转述。（BSD Now EP374，[590.42-823.44]，L2）
- OpenZFS 开发者峰会 2020 议题，包括 Matt Ahrens 论 OpenZFS 状态与版本化、George Wilson 论 ARC 与操作系统内存协作、持久 L2ARC、ZIL 并行化、顺序重建与 send/recv 性能提升，由 Alan Jude 亲历转述。（BSD Now EP374，[974.72-1777.74]，L1）
- NetBSD rnd(4) 手册页及其引用的随机性论文，节目提示可阅读 rnd(4) 了解熵源设计。（BSD Now EP352，[448.56-454.56]，L2）
- NetBSD 公告邮件列表中 Alistair Crooks 发布的 core team 变更公告，记载 Matt Thomas 的 ELF、VAX 维护与 GCC 贡献。（BSD Now EP352，[764.8-788.16]，L2）
- Bill Joy 1999 年 Linux Magazine 采访与 2003 年离任 Sun 时的报道，提及 BSD Unix、NFS、UltraSPARC、Java 与 1976 年创作的 vi。（BSD Now EP352，[1860.4-1891.92]，L3）
- OpenBSD 官方安全公告与 CVE 记录（认证绕过，涉及 smtpd/ldapd/radiusd，sshd 因纵深防御免责），经主持人转述并引其代码分析。（BSD Now EP330，[256.84-267.32]，L2）
- NetBSD releng 团队发布的 9.0 RC1 公告，列明 pull-up 数量、硬件支持与安全特性清单。（BSD Now EP330，[734.06-745.10]，L2）
- Claudio Jeker 的 e2k19 黑客松报告《Nobody Can Hear You Scream》，当事人自述 RPKI 客户端 X.509 重写过程。（BSD Now EP330，[2288.98-2299.82]，L1）

**史观**：

- 总纲4 分离聚合是永恒规律：special VDEV 把元数据与数据块分离存放、再以池聚合，用布局的分离换取元数据路径的加速，体现存储系统以分离-聚合应对硬件差异的设计。（BSD Now EP376，[579.08-641.7]，L2）
- 总纲13 法律与道德是利益分配：OpenBSD 把签名权留给人工、自动构建者不接触密钥，信任被刻意分配在人与机器之间：安全不是技术自动化的结果，而是权限结构的人为安排。（BSD Now EP376，[1467.38-1480.46]，L2）
- 总纲13 法律与道德是利益分配：certctl 的动机来自企业要信任自签证书以运行 SSL 拦截设备的实际需求：信任存储的设计由部署现场的利益格局反向塑造。（BSD Now EP376，[234.84-264.14]，L1）
- 总纲10 动手者创造历史：NetBSD 28 年贡献图自 1992 年起、1996 年才繁忙，个体贡献者有活跃期与干涸期、有人来去：社区史由无数动手者的断续劳动而非均匀的“进步”曲线构成。（BSD Now EP376，[1778.88-1849.42]，L2）
- 总纲5 没有必然性，只有偶然性：DragonFly 因 ld.gold 的链接脚本处理差异而回退 binutils，工具链“升级”被 EFI bootloader 的现实失败打断：所谓进步被具体硬件的偶然约束重新拉回。（BSD Now EP376，[1738.68-1771.74]，L2）
- 总纲10 动手者创造历史：OpenZFS 峰会的进展来自各平台维护者在 ARC 内存协作、持久 L2ARC、顺序重建等具体工程上的改进，而非单一权威的主导。（BSD Now EP374，[1024.98-1169.92]，L2）
- 总纲4 分离聚合是永恒规律：OpenZFS 代码在 FreeBSD、Linux、illumos、macOS、Windows 之间聚合，jail 则在 chroot 基础上分离出独立的隔离模型，两者皆呈现分离聚合的循环。（BSD Now EP374，[1848.72-2116.32]，L2）
- 总纲10 动手者创造历史：Matt Thomas、Robert Elz 等长期维护 ELF、VAX、shell 与 POSIX 的动手者构成社区治理的实质基础。（BSD Now EP352，[764.8-810.32]，L2）
- 总纲9 经验优先：开发者对 Allwinner ARM 真随机数设备实测统计测试，发现输出高度偏置，遂以经验判定不能仅依赖该硬件熵源。（BSD Now EP352，[366.88-377.24]，L2）
- 总纲10 动手者创造历史：OpenBSD 开发者与黑客松参与者在雪山小屋中直接动手重写 X.509 代码，把验证时间压缩 20 倍，历史由动手者而非口号推进。（BSD Now EP330，[2505.66-2516.12]，L2）
- 总纲9 经验优先：主持人从自身 24×7 使用廉价盘与 ZFS 的实际经验回答磁盘选型问题，实践知识优先于厂商宣传。（BSD Now EP330，[3813.36-3853.76]，L1）
- 总纲8 本体论上各方平等：本期同时呈现 OpenBSD、NetBSD、FreeBSD/FreeNAS、NomadBSD，各分支被平等对待，不以规模论高下。（BSD Now EP330，[1790.46-1814.48]，L2）
- 总纲5 没有必然性，只有偶然性：OpenBSD 罕见的远程认证漏洞出现与 40 小时修复并非必然，而是具体代码缺陷与具体响应条件的偶然叠加。　[存疑脚注] 漏洞为偶发事件这一判断系史学概括，非节目明言（BSD Now EP330，[245.98-255.10]，L4）
- 总纲3 不存在进步，只有权力再分配：NomadBSD 从 GPT 改回 MBR、UnionFS 换为 FUSE 等变化并非线性进步，而是兼容性与约束在不同硬件间的重新分配。（BSD Now EP330，[1872.70-1888.38]，L2）
- 总纲22 知识注定过时：本期多则教程与工具（如云主机装 FreeNAS 的旧法）提醒知识会随平台与版本过期，需持续核验。（BSD Now EP330，[1482.36-1494.88]，L2）

**辨析**：

- 转写把人名误记（Theo Durant 应为 Theo de Raadt，Kamil Ritarovsky 应为 Kamil Rytarowski，Ayushu Sharma 应为 Ayush Sharma）；OpenBSD 包构建博文的作者在转写中未署名，dataswamp.org 系 OpenBSD 开发者个人站点，引用时须以原文署名核实。[考据脚注] 人名与博文作者须以原文为准　[考据脚注] Theo de Raadt、Kamil Rytarowski、Ayush Sharma 等人名及博文作者系转写误记或未署名，须以原文核对（BSD Now EP376，[1244.68-1260.16]，L4）
- sys2z 的“最小化手工错误”与覆盖扩大属项目目标陈述，实际自动化程度与产出质量须以其代码库与后续维护状态核验。（BSD Now EP376，[1014.64-1024.52]，L2）
- IPFW 转发“栈损坏导致随机端口”系主持人对 PR 的口头转述，具体根因与修复提交须回到 PR 与 12.2-p1 公告核对。（BSD Now EP376，[699.24-715.08]，L2）
- 转写中 OpenBSD 6.8 随机种子置信度标记被表述为“RB_GOODRANDOM”，其具体宏名与语义应以 OpenBSD 6.8 发布说明及源码为准。　[存疑脚注] 具体宏名待官方变更日志核对（BSD Now EP374，[397.32-447.44]，L4）
- 转写中‘Robert Ells’ 疑为 Robert Elz，写作时须以 cross_indexes.duckdb 译名表校正，不宜直接照搬语音转写。　[存疑脚注] 转写人名拼写存疑（BSD Now EP352，[764.8-800.48]，L4）
- 转写中‘Rastrad’ 等拼写疑指 NetBSD 开发者 Riastradh（Taylor R Campbell），其 Allwinner RNG 驱动与统计测试的准确姓名需另核。　[存疑脚注] 转写人名拼写存疑（BSD Now EP352，[366.88-377.24]，L4）
- OpenBSD 认证绕过漏洞的“远程可利用”与 sshd 免责边界需逐应用分析，实际影响应按个案评估，不能笼统宣称整个系统不安全。　[存疑脚注] 转写对漏洞细节的表述为口语转述，建议以官方 errata 与 CVE 原文核对（BSD Now EP330，[193.66-204.80]，L4）
- NetBSD 9.0 当时尚未正式发布，RC1 特性清单可能随正式版调整，所引安全与虚拟化特性宜以正式公告为准。　[考据脚注] RC1 为发布前状态，存在后续变更可能（BSD Now EP330，[971.00-979.36]，L4）

**文献**：

- [BSD Now EP376] Pennington J. BSD Now: 376: Build stable packages[EB/OL]. (2020-11-12)[2026-08-15]. <https://www.bsdnow.tv/376>.
- [BSD Now EP374] Pennington J. BSD Now: 374: OpenBSD’s 25th anniversary[EB/OL]. (2020-10-29)[2026-08-15]. <https://www.bsdnow.tv/374>.
- [BSD Now EP352] Pennington J. BSD Now: 352: Introducing Randomness[EB/OL]. (2020-05-28)[2026-08-15]. <https://www.bsdnow.tv/352>.
- [BSD Now EP330] Pennington J. BSD Now: 330: Happy Holidays, All(an)[EB/OL]. (2019-12-26)[2026-08-15]. <https://www.bsdnow.tv/330>.

<!-- /PODCAST_REVIEW -->
