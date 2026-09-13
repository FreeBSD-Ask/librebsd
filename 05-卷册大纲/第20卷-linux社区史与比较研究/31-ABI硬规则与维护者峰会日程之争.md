# 31-ABI硬规则与维护者峰会日程之争.md

> 对应页面：ksummit-discuss p83（pk 348356-348405，2017-07-06/08 多线程并进 + 2014 档案信，348389 纯寒暄 1 封 NV）
> 判定：49 CAND / 1 NV
> 编号：DSLXC-5182..5230 | claim 已入库（50/50，dslinux_claims.duckdb）

## 31.1 sysfs 文档扫描与 checkpatch 半自动基建（7 例）

**要点（判定表逐字）**：Greg KH 提议在 linux-next 扫新增 sysfs 的 ATTR 宏并比对 Documentation/ABI，称半自动基建可作 GSoC 项目；Theodore Ts'o 建议把 sysfs 文档缺失检查直接加进 checkpatch；Greg KH 谓 checkpatch 易误报（文档常随系列后补），自嘲其正则曾令己落泪；Joe Perches 调侃 Greg 连 Linus 都适应 perl 正则了，劝其莫退缩；Geert Uytterhoeven 析 checkpatch 收发两端顺序差异致误报，可借其他 checkpatch 问题作深度审阅预警；Steven Rostedt 主张新 tracepoint 也须随文档加入，否则不应合入；Linus 指真正老大难是新增 ioctl 而非 sysfs 或 tracepoint，设备专属代码常有对齐与字宽问题

**史料**：`348357、`348358、`348359、`348360、`348363、`348374、`348375

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348357 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348358 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348359 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348360 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348363 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348374 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348375 -->` 

## 31.2 ABI 硬规则之争：Linus 拒绝任何放松（10 例）

**要点（判定表逐字）**：NeilBrown 视 ABI 稳定为社会与沟通问题，提出改为需 N 个连续发布版方稳定的折中（拟 N=2）；Laurent Pinchart 认为放松稳定承诺将削弱审阅，主张以教育加足够审阅者为主，并指 DRM/KMS 已要求新 API 落地真实用户态组件；Linus Torvalds 斩钉截铁拒绝放松无回归硬规则，称这是内核唯一真正硬性规则；NeilBrown 提改用 pre 与 rc 命名以多给两月烘焙期，谓可信 X.Y 内核者或比现在更多；Linus 重申不要用户信任 X.Y 版本号，版本号必须无关紧要，能随时升级才是信任之本；NeilBrown 追问 Linus 升级之义，质疑能否从 3.15 升到 3.16-rc1；Linus 答升级含 rc1 乃至随机内核，安全议题与极老硬件为仅有的两类可免责断裂；NeilBrown 提 no harm no foul 漏洞，问能否对新 API 协商宽限期以免实质回归；Linus 称绝无截止线，发布版中出现的特性即永久支持，此讨论无意义；Linus 补刀：回归只论实际断裂，语义可随意改只要无人察觉，否则必修

**史料**：`348361、`348362、`348364、`348365、`348366、`348369、`348370、`348371、`348372、`348373

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348361 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348362 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348364 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348365 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348366 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348369 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348370 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348371 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348372 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348373 -->` 

## 31.3 feature gate 设计与用户态 ABI 维护者（6 例）

**要点（判定表逐字）**：Rostedt 提议设 linux-api 类 linux-next 分支供 API 试炼，并加 CONFIG_TEST_ABI 类开关防误用；Andy Lutomirski 举 cgroup v2 cpu 控制器多年树外补丁为例，盼系统化 feature gate 使新特性仅 rc 可用；Linus 答 Andy：真实场景罕见，用户程序多建于厂商内核，纯属理论，但可用 expert 配置项；Julia Lawall 给出量化：约 2500 个 _IOW/_IOR/_IOWR 名仅约 500 见于 Documentation；Andy Lutomirski 举 iproute2 与 RDMA 灾难为例，称很多用户态程序本就建于开发内核；Michael Kerrisk 主张设带薪用户态 ABI 维护者把关文档与测试，并以 cgroup v1 失控为鉴

**史料**：`348376、`348377、`348378、`348380、`348381、`348382

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348376 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348377 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348378 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348380 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348381 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348382 -->` 

## 31.4 维护者峰会日程公布与办会确认（17 例）

**要点（判定表逐字）**：Jiri Kosina 反对对子系统维护者强加统一工作风格，举 patchwork 与 git 可由维护者自选为例，称任何强制尝试注定失败；Grant Likely 询问 Kernel Summit 工作坊日程何时公布，关乎 Devicetree 工作坊成行；Sergey Senozhatsky 追问 Grant 工作坊日程有无更新；Grant Likely 答 Devicetree 工作坊已定 10-26 下午，附 linuxplumbersconf 的 wiki 页；Sergey 谢 Grant 并告知，另问有无总体 KSummit 工作坊日程；Vlastimil Babka 给 Sergey 一个 Kernel Summit 议程页链接；Laurent Pinchart 宣 ELCE 2017 Bash the kernel maintainers BoF 入选，拟向 LWN 投稿汇集 occasional 开发者反馈；Linus 称维护者确应听取该 BoF 反馈；Doug Ledford 问维护者峰会是否确办，以便提旅行申请；James Bottomley 答已收赞助付款订场，维护者峰会附于 Prague 内核峰会；Doug Ledford 仍疑维护者峰会是否成行；James Bottomley 澄清内核峰会与维护者峰会皆办，前者需 OSS 加 ELCE 证、后者需邀；Doug Ledford 申明因未收邀故不知维护者峰会是否已定；Theodore Ts'o 述遴选机制：Linus 给程序委员会名单与标准，邀函已发，将公布草案议程；Takashi Iwai 答 Jiri：无意强制策略，只用 guidance 一词，指各子系统报 bug 方式与补丁无回应成社区障碍；James Morris 问公开内核峰会形式何在，仅见 OSS Europe 内核峰会轨道提及；Leon Romanovsky 请 Ted 能否公开最终受邀名单

**史料**：`348356、`348383、`348385、`348386、`348387、`348388、`348391、`348392、`348394、`348395、`348397、`348398、`348399、`348400、`348401、`348402、`348403

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348356 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348383 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348385 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348386 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348387 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348388 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348391 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348392 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348394 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348395 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348397 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348398 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348399 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348400 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348401 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348402 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348403 -->` 

## 31.5 tracing、kselftest 与安全议题征集（5 例）

**要点（判定表逐字）**：Shuah Khan 提议 Kselftest 议题，述 TAP13 转换已在 4.13 大部完成、4.14-rc1 续推；Rostedt 提 tracepoints without user space interfaces：FB 以手写 kprobes 加 BPF 顶替，建议加未导出 tracepoint 供模块分析；Rostedt 答 Josef Bacik：加模块让 eBPF 访问这些 tracepoint 亦轻而易举，启动时可加载；Sergey Senozhatsky 指 Josef Bacik 回复未达 ksummit 列表，自陈关注该 tracepoint 话题；James Morris 提 Kernel security 技术议题：KSPP（Kees Cook）、TPM（Jarkko）、容器安全读out

**史料**：`348384、`348393、`348396、`348404、`348405

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348384 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348393 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348396 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348404 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348405 -->` 

## 31.6 oops 报告与 2014 档案（4 例）

**要点（判定表逐字）**：Sarah Sharp 问 QR oops 是否除 kerneloops.org 外还应可选建 bugzilla 报告；David Woodhouse 玩笑：智能联网电视可直接嵌 app 上传 oops，何必用相机扫 QR；H. Peter Anvin 论内核精简：子集系统调用利于 seccomp 沙箱，超低端嵌入式可只编入固定应用所需功能；David Woodhouse 论设备错误隔离：除开 IOMMU 外可函数级复位或断电，部分平台能电气隔离顽劣设备 DMA

**史料**：`348379、`348390、`348367、`348368

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348379 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348390 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348367 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348368 -->` 

---
注：本文件由判定表程序化生成（6 块，覆盖 49/49 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
