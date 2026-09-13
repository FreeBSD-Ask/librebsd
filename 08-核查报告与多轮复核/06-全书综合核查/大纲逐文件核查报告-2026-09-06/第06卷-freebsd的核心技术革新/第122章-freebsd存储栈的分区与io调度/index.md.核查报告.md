# 核查报告：第06卷-freebsd的核心技术革新/第122章-freebsd存储栈的分区与io调度/index.md

- 源文件：d:\librebsd\05-卷册大纲\第06卷-freebsd的核心技术革新\第122章-freebsd存储栈的分区与io调度\index.md
- 批次：C338；检查日期：2026-09-13；检查方式：逐文件完整阅读人工核查（全文 107 行读毕）
- SUMMARY.md 收录：未收录（UNLISTED 实测确认：SUMMARY 第 1226 行章头指向概述.md、第 1227 行起收录 122.5；本 index.md 未收录；批次 JSON 记 null）
- A 占位符：发现 2 处显式占位（行 12“〔待核：原文截断，后文待回源〕”＋行 23 史观字段“(待人工回填)”）
- B 内容完整性：发现 8 处戛然截断（行 11“同期主流操”、行 13“**nfsv4(4)*”、行 14“实现极端复杂”、行 15“（统计结论 C-29）；非”、行 28“最终都收敛到”、行 29“网络块设备”、行 30“文件系统”、行 31“(2) 非”）
- C 编号与标题：通过（双头结构见清单 2）
- D 格式规范：发现 2 处（行 35/51 巨行塌陷；“*统计局限性标注**”星号错配）
- E 学术规范：发现 3 处（旧章号链接块；DB_REF 五组重复＋空心消解；散文跨文件重复）
- F SUMMARY 一致性：未收录（双头结构组成部分）
- 机械旗标复核：SECTION_GAP 实测确认（122.1-122.4 无文件、122.5-122.10 在盘）；UNLISTED_NOT_IN_SUMMARY 实测确认
- 问题清单：
  1. P2 | 行 12、23 | 显式占位两处（〔待核：原文截断〕＋史观“待人工回填”） | index 占位族（75index/171index/133index 同族） | 回源补全
  2. P2 | 行 11-15、28-31 | 戛然截断八处 | index 类截断损坏族重症（133index 同档）：设备命名演进、网络存储生态、Aurora 批评、统计印证四段均不完整 | 逐处回源补全
  3. P2 | 行 35 | “## 第 56.12 不同时期人员的采访录”“## 第 56.13 节 媒体反响与社区舆论” | 旧章号链接块（56 系旧章号，本文件 122 章；171index 68B 族第五例）＋巨行塌陷（文献＋综述＋DB_REF 连排） | 按 122.x 重挂并恢复换行
  4. P3 | 行 19 | chmatch“置信度 folder，原因：folder 第120章” | folder 噪声族（65/211/57/75index 同族） | 关闭 folder 兜底
  5. P3 | 行 37-58 | DB_REF 块重复五组（2010-2020 488,947×4＋2008-2018 455,206×1）＋行 55 doubt-resolved-649“待验证”空心消解＋全角“］”残缺 | 模板重复注入＋消解体例矛盾（326.5 同族） | 去重并清理
  6. P3 | 行 51 | 史观映射散文（phk“发呆”/Aurora/McKusick 执念段）与 122.8（C324）行 73 全量重复＋“Hibsd Project”×3＋“01-数据库本体”路径断链 | 散文跨文件复制＋机构名疑讹＋路径断链 | 定归属并订正
- 结论：存在问题 6 项（P0 0、P1 0、P2 3、P3 3）

## 补充说明（正样本与复核留痕）

- PODCAST_REVIEW 三期史观五条全对（总纲 10×2/22/4/13 权威全称）；EP109（Losh）为存储栈工程史金块：Netflix I/O 调度器（SSD trim 触发日志结构垃圾回收侵占带宽→读取优先写限 20-25MB/s→4ms 读延迟动态约束，Perforce projects.io.sked）、GEOM 内存耗尽回退“改进放大旧缺陷”案例（10 IOPS 病态退避→Motin direct dispatch 放大→1000 IOPS 权宜＋预分配 I/O 事务根本方案）、kld 自动加载（Selasky 原型→KLD 内标准化即插即用编码→devd.conf 动态生成→Minimal 内核模块目标）、NanoBSD→公共工具层抽取（总纲 4 落点精当，Netflix 双分区镜像六周滚动固件）、“部落知识足够支撑一整天教程”的动手者史料观；2.11BSD 复原与早期 Unix 分区史（分区表曾编译进驱动）。
- EP361 Firecracker NetBSD 微虚拟机/OpenBSD 首个 powerpc64 快照；BSDTalk EP61（lighttpd Jan Kneschke）C10K 概念验证起源、kqueue/epoll/dev-poll 事件分层、无 C 字符串库的安全设计、YouTube/Wikipedia 采用证词、mod_proxy_core 故障转移重写。
- Aurora LWN 原文（“too hard to understand, implement, and maintain”）带语境还原；Seltzer USENIX 2000 与 McKusick SUJ pdf 文献对口；辨析四条存疑标注（multiboot 仅 i386、GRUB 依赖树、转写讹误清单 Maffod/WellGriant/CycloN 等）。
- 实测留痕：SUMMARY 第 1226-1227 行；122.8（C324）报告所引“第 1085 行”为重构前值——本报告按检查时点实测记录。
