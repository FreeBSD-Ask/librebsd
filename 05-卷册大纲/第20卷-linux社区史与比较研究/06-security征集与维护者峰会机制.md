# 06-security-TODO征集与维护者峰会入选机制

> 来源页：ksummit-discuss p71（pk 347756-347805，50 封）
> 主题：security-related TODO 大线程（2017-01/03）+ Maintainer summit 邀请讨论（2017-04-18）+ Sphinx 收尾 + UAPI 策略 + KS2014 混档 5 封
> 判定：CAND 44 / NV 6（347759-762 XML 折叠微循环、347788 纯确认、347804 重复确认）

## 6.1 【Linux社区】Sphinx 图像之争收尾：构建失败门禁与规程化

**要点**：p70 的 9 连 PATCH 应用后，Corbet 实测 `pdfdocs` 构建失败（xelatex media.pdf，无更详细日志）；Mauro 定位根因为 field-order.rst 一处 figure include 漏改扩展名（`.svg` → `.*`），附修复补丁并折叠进新版本。同期 PATCH v2 2/2 正式新建 `Documentation/doc-guide/images.rst`——Graphviz（`*.dot`）与 SVG 两类型、`.*` 通配、`Makefile.sphinx` 集成与 LaTeX/PDF 转换链的**文档图像插入规程**定型。ASCII art 保护共识：Mauro 同意一般原则，但复杂图（pxa_camera.rst）可用 Graphviz 重写。

- **要点**：文档工具链质量门禁（构建失败实证）；images.rst 规程成文化；ASCII art 一般保护 vs 复杂图 Graphviz 化的边界共识。
- **史料**：`347763`（Corbet 构建失败实证）、`347764`（Mauro 修复+补丁）、`347756`（images.rst v2）、`347758`（ASCII art 共识）
- **史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347763 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347764 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347756 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347758 -->`

## 6.2 【Linux社区】security TODO 征集：Google 赏金化与 KSPP 主线索

- **要点**：Kees 借 Google Patch Reward 程序扩展之机，向 ksummit 维护者征集 security wishlist（KSPP TODO 已有列表）；明言 LKML 只是公共存档、ksummit-discuss 才是维护者触达渠道——**赏金化安全 TODO 的机制起点**。
- **史料**：`347765`（Kees 开帖）、`347767`（Kees 回应 vsyscall/PCID）、`347771`（Dobriyan：unmap 模块加载器）、`347778`（Hellwig：应发 linux-kernel，列表职能定位）、`347783`（Lutomirski：/proc 拆分总纲）
- **史料锚点**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347765 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347767 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347771 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347778 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347783 -->`

## 6.3 【Linux社区】execve 用户态化论证链（安全架构史）

- **要点**：Lutomirski 提出「binfmt 解析器移用户态」——重写 execve 使实际二进制格式解析在用户模式运行，缩小内核攻击面（setuid 安全挑战、预加载器、映射地址/ASLR/无栈启动/NOMMU 双模等 7 点难点由 Howells 全面论证）；Triplett 扩展为除 execve 过渡全部外移（compat/x32/废弃 syscall 用户态化可隔离单进程妥协）；Wilcox 提出内核地址用户态执行能力（仅访问自身栈+用户内存+可发 syscall），Lutomirski 称已开始原型（k 核代码用户态执行部分，用户地址观察为务实选择、s390 分裂地址空间或不可行）。
- **要点**：内核攻击面消减思想的**论述群**——怎么把高危解析移到低特权域，核心设计约束（preloader、地址规划、ASLR、栈、NOMMU 双模、脚本循环安全重算）。
- **史料**：`347766`（原提案）、`347770`（Triplett 扩展）、`347769`（Wilcox 用户态执行）、`347772/347777`（Howells 难点与追问）、`347776`（设计澄清）、`347781`（原型已开始）、`347782`（FLAT 双模）、`347771`（unmap 模块加载器）
- **史料锚点**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347766 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347770 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347769 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347772 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347777 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347780 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347776 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347781 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347782 -->`

## 6.4 【Linux社区】/proc 现代拆分之辩（procfs 架构演进）

- **要点**：Lutomirski 总纲——sysctlfs（scope=global/net 挂载）、proc 真 per-superblock 挂载选项、hidepid per 挂载、cmdline 仅 argv[0]、mini-proc（无非 PID 内容）；Biederman 否决 fs_fully_visible 绕过（根策略；cgroupfs 特例因用户空间兼容），bind 已够，并提议更好答案替代 hidepid；Dobriyan 支持（mount -t sysctl/proc-pid/proc-kitchen-sink）；Howe 警示 /proc 是用户 API（open/read/write/close 的 syscall），不可破坏；同 pidns 同 st_dev 设计回应 Djalal 的 device-id 兼容顾虑。**proc 挂载架构演进关键史料——为后来 sysctlfs/hidepid 相关工作的前期论证**。

- **史料**：`347784`（Biederman 否决）、`347786`/`347787`（Lutomirski sysctlfs scope 澄清）、`347789`（/proc 用户 API）、`347791`（同 st_dev）、`347785`（Dobriyan 支持）
- **史料锚点**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347784 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347786 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347787 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347789 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347791 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347785 -->`

## 6.5 【Linux社区】UAPI 头文件策略（对外接口治理）

- **要点**：Howells 以 include/uapi/linux/cec.h 违规为引，提议 UAPI 头文件禁止清单：inline 函数/函数声明、匿名内嵌结构体/联合、CONFIG_*/*_ARCH_*/__KERNEL__ 条件（除重新包含/C++ guard）、extern（除 C++ guard）；愿望是无需过滤可原样拷贝 /usr/include。内核侧 cec 与 lustre 的「单源双用」（内核+用户）与 UAPI 纯净性冲突浮现，本地维护者能力同步定位问题。编译器兼容性与保留词（new 作参数名）也在考量。

- **史料**：`347773`（禁令清单）、`347774`（Greg：单源双副本问题）、`347775`（Howells 编译器/保留词）
- **史料锚点**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347773 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347774 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347775 -->`

## 6.6 【Linux社区】Maintainer summit 倡议（维护者峰会机制史）

- **要点**：Linus 以 pull 请求「累计 files changed」12 个月统计 top50 维护者名单（贴全文），目标 30-35 人、以流程/过程问题为议题（非技术），并首次牵涉五行：架构（x86/arm/powerpc）、驱动（drm/rdma 最大）、文件系统（Al/XFS/ext4）、核心（Andrew/Tejun）、安全（Lutomirski/Kees）——然后用发行方参与（Android/Fedora/SUSE/Ubuntu）作为下游听众；David Miller 缺席是显眼漏洞（要他推子维护者）；稳定树维护量（Ben Hutchings 的 3.2/3.16）统计不可见，Greg 举出。sx 音商细节也标志性：Airlie 的 top50 用列读梗「I am not a number」、Dave 推荐 Vetter（drm）、SUSE 分支维护者分权（Iwai/Marek/Kosina/Jeff Mahoney + Slaby 的 Tumbleweed 3.12）、Fedora 双人团队（Abbott+Forbes）、Android tech lead=Rom Lemarchand、Vetter 推 Sean Paul/Jani 的 drm-misc 视角。**KS 与维护者峰会关系的形成史料**。
- **史料**：`347792`（Linus 发起+ top50）、`347793`（Takashi sound）、`347794`（Dave）、`347795`（Hallyn security）、`347796`（Greg 稳定树）、`347797/347798`（Linus ~35人/发行方）、`347799`（Kosina SUSE 分支）、`347800`（Takashi 补充）、`347802`（Lau Abbot Fedora/Android）、`347803`（Pinchart DRM 附议）、`347805`（Vetter 推荐）
- 【Linux社区】**史料锚点**：`<!-- ROW_MINE: ksummit-discuss.messages.347792 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347793 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347794 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347795 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347796 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347797 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347798 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347799 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347800 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347802 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347803 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347805 -->`

## 6.7 【Linux社区】KS2014 混档档案信（2014-05-12，归历史卷另处）

- **要点**：5 封 2014 年 ksummit 会前 Tech/Core topic 档案信混入本页：Kurusa（QR oops cookie 去重）、hpa（QR 价值判据——信息量+解码优于文本屏照）、Pinchart（IOMMU 忽略故障源头 vs 只关报告）、Berg（QR 全 URL 与应用 TWO 楼 Android intent）、Vetter（IOMMU 风暴隔离 IO 重新开启）——与 2016/2017 线程无关，已读入 claim，按「KS2014 档案」归卷处理。
- **史料**：`347757`、`347768`、`347779`、`347790`、`347801`（均 2014-05-12）
- 【Linux社区】**史料锚点**：`<!-- ROW_MINE: ksummit-discuss.messages.347757 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347768 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347779 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347790 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347801 -->`