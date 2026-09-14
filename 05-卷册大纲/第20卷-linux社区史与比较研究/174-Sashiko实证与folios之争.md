# 174 【Linux社区】Sashiko实证与folios之争

> 来源：ksummit 独有 p38（50 封全读，2021-04 至 2026-08：SeongJae Park 对 Sashiko AI 审阅一手用户叙述曾抓出其手工 stable 回移错误并逐条表态 LTS 审阅与提示词入 kernel.org；Kent Overstreet folios 之争长篇文化批评跨子系统重构文化已坏与 Chris Mason 回应构成 MM 治理史成对史料；Maintainer Summit 经费具体数字 30+7 人人均日 2500 美元对比 Pinchart 自办 100 欧元；Pinchart 披露大型 SoC 厂因直通空白支票临门放弃开放相机栈；加速器 UAPI 四封、设备直通三封、Rust 内核政策三封）
> 判定：40 CAND / 10 NV。主题分布：DRM樱桃派流程 1、隐藏提交 1、drm-misc权限 1、加速器UAPI 4、Rust链表疑虑 1、Link尾注之争 1、变量声明风格 2、设备直通 3、trivial补丁政策 2、Sashiko AI审阅 1、安全提交验证 1、峰会疫情形式 2、AI代码标注 3、MAINTAINERS列表迁移 1、信任之网 2、峰会经费成本 1、Rust内核政策 3、工具生成内容 2、stable回移回归 1、错误指针约定 1、峰会远程形式 1、AI审阅之辩 1、Folios文化争论 2、ACPI音频怪癖 1、文件系统维护 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p38 的逐封提取（2021-04 至 2026-08，40 CAND / 10 NV），全 25 块采用**精简块体例**（丙型）：每块一行，由【Linux社区】叙述句与 `<!-- ROW_MINE: … -->` 来源坐标构成，不逐块展开要点/史料/史观/辨析/文献五字段。取舍依据：本层为页面级逐封索引——叙述句承担“要点”职能、ROW_MINE 坐标承担“史料锚”职能（与 claim 库 `source_ref` 一致，可反查去重）；史观/辨析/文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 174.1 DRM樱桃派流程

- 【Linux社区】Airlie 称 cherry-pick 不加 -x 曾因引用尚未进入 Linus 树破坏脚本而遭抵制，将推动恢复 -x；并计划用 rerere 缓存构建合并 -fixes 的 next 树 `<!-- ROW_MINE: ksummit.messages.5878 -->`

## 174.2 隐藏提交

- 【Linux社区】Kosina 称自己总是维护多个 topic 分支汇入 for-next 供 linux-next 拉取，质疑经拉取请求收下的提交会错过 linux-next 这一前提 `<!-- ROW_MINE: ksummit.messages.5880 -->`

## 174.3 drm-misc权限

- 【Linux社区】Geert 称自己没有也不想要 drm-misc 提交权，“有无 drm-misc 提交权”是询问补丁延误时的标准答案，无人说得清权限在谁手里 `<!-- ROW_MINE: ksummit.messages.5903 -->`

## 174.4 加速器UAPI

- 【Linux社区】Arnd 主张 BLAS/GEMM 是 AI 加速器基础接口构件，PyTorch 等框架皆调 oneMKL/oneDNN；定死功能接口应禁厂商扩展与旁路；高通 misc 加速驱动定位错误 `<!-- ROW_MINE: ksummit.messages.5913 -->`
- 【Linux社区】Airlie 将加速器编程模型分 a-d 四级，由 MMIO 大锁到全抢占；GEMM 级接口仅适用 a 类且该类设备将消亡，AI 加速器须追平 GPU 编程模型才具竞争力 `<!-- ROW_MINE: ksummit.messages.5926 -->`
- 【Linux社区】Corbet 提出峰会议题：何种情况要求自由用户空间、是否需 EXPORT_SYMBOL_USERSPACE_GPL()、何为合格实现，并指 Habana 正自行化解但根本问题未解 `<!-- ROW_MINE: ksummit.messages.5933 -->`
- 【Linux社区】Pinchart 称文档先行假设高质量文档存在而开源实现常是更好文档；DRM 要求内核驱动须配主流图形栈（Mesa、AOSP 等）实现并经其维护者认可，以此保证质量 `<!-- ROW_MINE: ksummit.messages.6018 -->`

## 174.5 Rust链表疑虑

- 【Linux社区】Glisse 质疑 Rust 弱引用：双向链表僵尸元素会卡死遍历形同死锁，链表外置损缓存性能，RCU 链表跳过死节点难表达 `<!-- ROW_MINE: ksummit.messages.5916 -->`

## 174.6 Link尾注之争

- 【Linux社区】Brown 称 Link 主要用于二分定位提交对应邮件以报告测试失败，即补丁到邮件映射，对 message-ID 服务于补丁版本追踪的价值存疑 `<!-- ROW_MINE: ksummit.messages.5918 -->`

## 174.7 变量声明风格

- 【Linux社区】Viro 称 kzalloc 显式写 struct 类型利于代码审计找出全部分配点；抱怨缺可搜索的强制转换手段防指针乱转，结构体包装只解部分问题 `<!-- ROW_MINE: ksummit.messages.5920 -->`
- 【Linux社区】Nikula 观察到 const int foo = bar + 5 类非常量指针 const 局部变量明显增多，风格指南无规可循，此类 const 宜延后声明以获得初值 `<!-- ROW_MINE: ksummit.messages.5940 -->`

## 174.8 设备直通

- 【Linux社区】Gunthorpe 阐明 fwctl 边界：不得妨碍日后内核化；持续擦洗与 EDAC 属设备核心使命不宜入 fwctl，调试性 ECC 评估合适，单实例资源被占用将阻碍共享 `<!-- ROW_MINE: ksummit.messages.5923 -->`
- 【Linux社区】Pinchart 披露某大型 SoC 厂商临近开放相机栈却因可经他子系统直通合入而作罢的一手见闻；逆向难度渐增，DRM 开放用户空间门槛证明规则可分情况设定 `<!-- ROW_MINE: ksummit.messages.5983 -->`
- 【Linux社区】Bottomley 以 FIDO 令牌为旁路未酿灾的反例，指出内核 FIDO 驱动本可作加密密钥信任根用于加密设备树、模块签名等，旁路风潮使社区错失此方向 `<!-- ROW_MINE: ksummit.messages.5999 -->`

## 174.9 trivial补丁政策

- 【Linux社区】Bottomley 借明尼苏达大学事件提案： SCSI“维护驱动不收 trivial 补丁”推至全内核；trivial 修复须附真实 bug 报告或可信静态检查器（0day、Coverity）背书 `<!-- ROW_MINE: ksummit.messages.5930 -->`
- 【Linux社区】Pinchart 警告 Fixes: 标签若沦为负面评分工具，开发者会游说逃避被归咎，反而削弱 Fixes: 的价值 `<!-- ROW_MINE: ksummit.messages.5931 -->`

## 174.10 Sashiko AI审阅

- 【Linux社区】Park 记述 Sashiko 曾抓出他手工 stable 回移的错误，忧 LTS 审阅重复已知发现；支持既有 bug 数据库、提示词入 kernel.org、交互模式限签名树 `<!-- ROW_MINE: ksummit.messages.5941 -->`

## 174.11 安全提交验证

- 【Linux社区】Greg KH 评四道安全提交验证闸门：仅网络等可模拟子系统可行，DRM 依赖实硬件不适用；security@ 报告不得进第三方基础设施，只能各人自机运行 `<!-- ROW_MINE: ksummit.messages.5942 -->`

## 174.12 峰会疫情形式

- 【Linux社区】Pinchart 认为 2021 年恢复线下过早，提议分会场区域聚集加视频互联，强调参会者并非“怯懦/莽撞”两类所能划分 `<!-- ROW_MINE: ksummit.messages.5948 -->`
- 【Linux社区】Bottomley 断言远程参会将成常态但仍应线下为主，反对以恐惧者绑架意愿者造成“最小公分母”式平等，引疫情前轮换欧洲办会先例 `<!-- ROW_MINE: ksummit.messages.5996 -->`

## 174.13 AI代码标注

- 【Linux社区】Wysocki 认同 AI 标注可作维护者提示，但质疑缺失标注能否可靠识别，若可疑改动本可被查出则强制标注多余 `<!-- ROW_MINE: ksummit.messages.5950 -->`
- 【Linux社区】Kosina 称测试辅助类 LLM 使用他不在乎，提交说明自由文本即可；但代码确由 AI 生成者须认真对待，兼涉维护者流程与法律 `<!-- ROW_MINE: ksummit.messages.6007 -->`
- 【Linux社区】McKenney 称法律争议落定前不碰 AI 生成物，援引 DCO 1.1(a) 与版权执法风险；AI 提示与输出留痕可在诉讼中被调取，自述曾被律师复制全部设备 `<!-- ROW_MINE: ksummit.messages.6010 -->`

## 174.14 MAINTAINERS列表迁移

- 【Linux社区】Brown 澄清 RFC 意图：并非 LKML 只留核心子系统，而是有更专属列表的条目不再叠加 LKML `<!-- ROW_MINE: ksummit.messages.5953 -->`

## 174.15 信任之网

- 【Linux社区】Ryabitsev 更正 LF“第一人称凭证”计划仅替换 gpg 信任网机制而非 gpg 本身，现有工作流不必改变 `<!-- ROW_MINE: ksummit.messages.5954 -->`
- 【Linux社区】Kleine-König 描述 pgpkeyring 现状为每周跑脚本查 diff 提交推送，质疑自主主权 DID 实为 PGP 翻版，不愿弃 git/邮件集成，志愿协护钥匙环 `<!-- ROW_MINE: ksummit.messages.5963 -->`

## 174.16 峰会经费成本

- 【Linux社区】Pinchart 估算峰会 30 席加 7 赞助席人均日成本约 2500 美元，自述办 15-25 人单日会每人均 100 欧元场地午餐，指成本差距悬殊 `<!-- ROW_MINE: ksummit.messages.5956 -->`

## 174.17 Rust内核政策

- 【Linux社区】Ojeda 澄清 gccrs 是 GCC 前端而 rustc_codegen_gcc 属 Rust 项目后端且双方合作；Tree Borrows 模型经约 30k crate 67 万测试；内核仍将用 rustc，兼顾性能与代码复用 `<!-- ROW_MINE: ksummit.messages.5977 -->`
- 【Linux社区】Ojeda 驳 LLVM 隐性依赖之说为恐惧诉求，称 Rust 非研究语言；Rust for Linux 每个 PR 必须构建部分内核 Rust 代码，较 Crater 更严，Clang/GCC 均无此机制 `<!-- ROW_MINE: ksummit.messages.5994 -->`
- 【Linux社区】Ojeda 指出 Tree Borrows 别名模型论文已于 2024 年 11 月提交发表并附论文链接，回应 Overstreet 关于别名规则仍在研究的说法 `<!-- ROW_MINE: ksummit.messages.6021 -->`

## 174.18 工具生成内容

- 【Linux社区】Hansen 给出修改后的文档条款：提交者须理解并能辩护所提交的一切，否则维护者可整系列拒收 `<!-- ROW_MINE: ksummit.messages.5978 -->`
- 【Linux社区】Stoakes 明言不指望文档在 Linus 立场下落地，但坚持写明“slop”以宣示内核零容忍立场，接受 Bottomley 中性措辞妥协 `<!-- ROW_MINE: ksummit.messages.6030 -->`

## 174.19 stable回移回归

- 【Linux社区】Levin 表明多数回归恰因进入 stable 才暴露因 -rc 测试少，延迟回移只是推迟发现；“紧急”无法定义，stable 标签不可靠因有人就是不标 `<!-- ROW_MINE: ksummit.messages.5984 -->`

## 174.20 错误指针约定

- 【Linux社区】Carpenter 举例链表迭代器在表尾返回错误码致调试刷屏，主张分配失败应返回错误指针而遍历到表尾返回 NULL `<!-- ROW_MINE: ksummit.messages.5987 -->`

## 174.21 峰会远程形式

- 【Linux社区】Rostedt 接受每场设主持人转达远程与会者，认为此后将成常态，但走廊交流与晚间活动仍缺失，提议会末 breakout room 弥合 `<!-- ROW_MINE: ksummit.messages.5995 -->`

## 174.22 AI审阅之辩

- 【Linux社区】Levin 主张 AI 审阅强于写作且审阅不产出代码无法律风险，公开要求 McKenney 给出审阅用途涉诉实例 `<!-- ROW_MINE: ksummit.messages.5998 -->`

## 174.23 Folios文化争论

- 【Linux社区】Mason 回应 Overstreet：避免地盘之争的关键是不必先让人对其子系统感到羞耻，各有优先级与妥协，对改进保持期待即可 `<!-- ROW_MINE: ksummit.messages.6003 -->`
- 【Linux社区】Overstreet 长文抨击内核缺乏先设计后动手文化，跨子系统重构陷地盘之争，MM 代码如 rmap 混乱；folios 实为 extent 不应受固定尺寸约束，bikeshedding 吓退深度重构 `<!-- ROW_MINE: ksummit.messages.6017 -->`

## 174.24 ACPI音频怪癖

- 【Linux社区】Brown 指出 ACPI 平台惯例性抹除 DMI 信息致音频等子系统须持续打每机种 quirk，多数笔记本内置音频问题上报上游后易以 quirk 修复 `<!-- ROW_MINE: ksummit.messages.6027 -->`

## 174.25 文件系统维护

- 【Linux社区】Chinner 反对将失修文件系统砍成只读延寿：只读仍在内核解析不可信数据且无法自建测试镜像更难维护，数据恢复应移用户空间或 FUSE `<!-- ROW_MINE: ksummit.messages.6033 -->`
