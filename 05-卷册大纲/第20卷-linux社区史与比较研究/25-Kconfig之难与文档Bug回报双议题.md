# 25-Kconfig之难与文档Bug回报双议题.md

> 对应页面：ksummit-discuss p77（pk 348056-348105，2017-06-26/27 多线程同日并进 + 2014 档案信）
> 判定：49 CAND / 1 NV（048 两句寒暄）
> 编号：DSLXC-4882..4931（缺 4929＝误入 NV 行已剔除） | claim 已入库（49/49，dslinux_claims.duckdb）

## 25.1 Kconfig 之难：Linus 三连长文与多方应答（8 例）

**要点（判定表逐字）**：Sergey Senozhatsky发问：Kconfig有时真难，硬化选项能否归一并举CONFIG_SLAB_MERGE_DEFAULT为例，想做硬化的人是否干脆全开；Linus长文一：我恨我们的Kconfig，它是内核最讨厌的部分、问的全是无人能答的疯问题；设想Kconfig片段增量喂入如启动Fedora 25或SuSE 12 sp2所需最小集，ISDN/ATM/PCCARD已死不该再问，安全选项全是疯了；mcgrof答kvmconfig与xenconfig已存在；梳理Moraru 2016 GSoC使udevadm可吐kconfig符号、Hellwig另提Makefile折入Kconfig；LPS Santa Fe纪要：Arnd认领Suggests标签、Howells认领已启用特性缓存、众人认定depends与select并存不智应先修工具出selectconfig与dependsconfig；Linus长文二：defconfigs根本坏了因为从来不存在一劳永逸配置，该做的是modernpcconfig/f25config/amdconfig类子配置；唯一讲得通的默认是新特性默认n因人人自觉其代码至关重要；SAT求解器只会把热衷SAT的不相干人引进来；/etc/kernel-config机器专属缓存已存在；Kees Cook：单一硬化开关此前已失败过有CONFIG_EXPERIMENTAL先例；发行版对安全特性耐受度不同颗粒度仍属必要，但Kconfig依旧一团糟；Kees Cook愿见make paranoidconfig之类尝试，自陈无暇做只把建议清单撒进KSPP wiki，当前精力在编译器特性探测；Olof Johansson把Linus意图概括为元配置层：特性选择而非驱动选择，可经现有Kconfig后端拼装kconfig片段实现；Linus长文三：确认要特性选择元配置层；多数人答得了有没有笔记本答不了有没有broadcom无线、CGROUPS细节更无从答起；构想localpciconfig按PCI设备清单生成符号乃至读系统日志看上月用过的USB设备；忆1991年内核无选项故无需配置

**史料**：`348083、`348085、`348092、`348095、`348097、`348098、`348099、`348100

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348083 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348085 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348092 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348095 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348097 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348098 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348099 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348100 -->` 

## 25.2 Documentation issues 全弧（9 例）

**要点（判定表逐字）**：Mark Brown支持Corbet开不在源码树层级内的子系统维护会题，自述靠主题行过滤邮件且regulator DocBook被无声转成RST，主张建立让维护者至少知情的机制；Rafael论sysfs与debugfs文档归类困境：框架经sysfs暴露接口而驱动须提供回调，debugfs既是高级管理员排障工具又是驱动开发者工具；Rafael解释kernel-parameters.txt无交叉引用只因未列入知名文档清单，设计意图是把此类引用数目压到最少；Rafael对Takashi提议旧txt与ReST分置docs/*表示赞成，只疑为时已晚；Corbet裁定从不为移动的文档留符号链接、文档文件应与代码同规；愿景是ls Documentation能给出可浏览的小清单，符号链接恰破坏此目标；Daniel Vetter统计MAINTAINERS下Documentation仅约450条目且多为单文件、4.12残留DocBook无一条目，主张按目录归置并补条目，忆Jon上届KS提过无果；Vetter反对再分docs/*：为时已晚、gpu等活跃子系统的docbook转rst已痛过、rst卖点本是融入txt堆、DocBook子目录本是隔都；Mauro认为git对重命名的处理远好于docbook转rst故再改名伤不了多少，但目录一改内核内外引用与网址都得跟着改恐又添一套符号链接；Brown追问文档维护缺位是有人作梗还是大家不关心，并自承未复查过全貌

**史料**：`348056、`348067、`348069、`348070、`348071、`348075、`348076、`348077、`348084

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348056 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348067 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348069 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348070 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348071 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348075 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348076 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348077 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348084 -->` 

## 25.3 Bug reporting feedback loop 九连（9 例）

**要点（判定表逐字）**：Luis R. Rodriguez实证KOTD价值：XFS九成缺陷经KOTD反向bisect即可定位、余下一成是坏回移；linux-next亦有每日KOTD rpm，回移经Coccinelle改写反而更正确；Laurent Pinchart补linux-media已有media_build构建脚本与回移补丁可在旧内核编最新子系统供测试；James Bottomley质疑linux-next经常起不来是误判、正名应为很少失败；提议发行版至少每周发-next试用版，称最靠近主线的测试者时间最宝贵；Takashi Iwai称可仿KOTD为子系统for-next分支做定期内核包，cron拉取重打包送OBS即可；Vetter以DRM CI数据反驳：合并窗口落地时打掉约三成CI机器（含挂起恢复）、e1000e回归修复在CI分支滞留无人收，不敢称很少失败；mcgrof与Bottomley达成口径：开发机linux-next很少失败、生产测试机有时失败；引Roeck维护的linux-next跨架构编译与qemu运行地图；定论每日而非每周，KOTD到linux-next到邮件列表；mcgrof指出媒体与无线已有for-next定期包树，其余子系统未知；Guenter Roeck给出next-20170627实测：编译145过140败5、qemu 122过120败2，细分口径x86_64 defconfig约每月一两次失败而全部qemu启动测试几乎总是有败，末窗前涌入提交是失败大户；Jiri Kosina给出OBS Kernel:linux-next仓库实证发行版已发-next，但收到近零缺陷报告——或极少人用该多宣传，或会用者足以上游直报

**史料**：`348086、`348087、`348088、`348089、`348091、`348093、`348094、`348096、`348105

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348086 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348087 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348088 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348089 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348091 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348093 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348094 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348096 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348105 -->` 

## 25.4 mobile phones：N900/droid4 主线现状与音频架构之争（13 例）

**要点（判定表逐字）**：Pavel以drivers/hsi/clients/cmt_speech.c反驳已有框架可用的说法，称该HSI话音驱动2010年已并入主线；Pavel追问一个设计得当的系统实例，称出于安全不愿基带CPU直连扬声器麦克风并想留录音与处理弹性，N900证明延迟可在软件解决；Pavel盘点N900现状：X可用、gprs/edge/umts数据、短信、WiFi、GPS、1.2Mpix相机、续航一天，通话音质是成为主力机的最后一关；另证3.6V电池剩余不足百分之一；Tony Lindgren报droid4进展：X配HDMI大体可用、六枚omapdrm补丁尚在树外、LCD背光补丁待收，指Sebastian Reichel网站有n900与droid4主线驱动状态矩阵；Brown给出行业实况：现代手机基带音频直连主音频子系统、整个系统是一块声卡，50-70ms全路径延迟预算几乎全烧在网络上，处理靠专用音频DSP；处方是以标准ALSA驱动重写；Pavel问droid4本机X可用性与容屏操控、ofonod支持度与LTE 700MHz欧洲缺频，并晒N900为日常机细节；Alexandre Belloni指garmin_gps不宜在内核，用户态处理更好并给出openstreetmap方案链接；Pavel承认garmin用户态驱动现胜内核版，但主张非简单串行总线上的GPS若搞内核用户态双驱动是错的；Tony细述droid4：USB host仅电池VBUS供电、i3窗口管理器、atmel_mxt_ts在next失效、t5可断电池、watchdog可用、音混在CPCAP PMIC并指MC13783UG.pdf可参；Brown考据cmt_speech入库实为2015年3月而非2010，判其为标准DSP流接口可作ALSA压缩流支持，无理由游离于音频框架之外；Sebastian Reichel报N950 GPS为i2c未知协议待逆向、Ti WiLink经共享UART以类蓝牙头送GPS，赞同应设GPS子系统；又证Nokia加载器可为空电充电；Pavel获知droid4音频不经CPU更觉中意；报N900相机仅1.2Mpix且用户态代码缺、DSP协处理器连支持形态都无人知晓、N950蓝牙可用；Pavel贴出电池保护补丁diff：bq27xxx驱动加generic_protect，过热或电池死亡即orderly_poweroff、低于2.95V关机、内阻修正内压低于3.15V关机；并述NoLo充电过慢致低压循环重启、问N950双GPS是否都接有用天线

**史料**：`348058、`348059、`348060、`348061、`348063、`348066、`348072、`348073、`348074、`348078、`348080、`348102、`348104

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348058 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348059 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348060 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348061 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348063 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348066 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348072 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348073 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348074 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348078 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348080 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348102 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348104 -->` 

## 25.5 版本号与重绑定余波（3 例）

**要点（判定表逐字）**：Sasha Levin质疑删除MODULE_VERSION会破坏ABI：各公司脚本从模块里抽版本号做配套校验，值消失时脚本会全坏；Lee Duncan请求参与多驱动设备重绑定讨论，称常涉iSCSI目标器与发起端并拟另提iSCSI-boot议题；Leon Romanovsky转述社区结论：MODULE_VERSION不是ABI，靠控制台输出写脚本按设计即坏

**史料**：`348062、`348064、`348065

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348062 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348064 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348065 -->` 

## 25.6 PM 依赖与 DT/ACPI（2014 档案线，4 例）

**要点（判定表逐字）**：Brown答DT绑定能否当标准：FDT是纯数据期望内核全做而ACPI预期配合活动固件，两者对何处处理何事的模型本就不同；Brown论PM依赖：运行时PM引用不必沿设备拓扑，到父设备的默认引用计数也常被打破如SPI控制器先于活动设备挂起，suspend_late与resume_early正为此类互相依赖而生；Tomasz Figa接受PM依赖议题提名，自陈正关注IOMMU用例并将整理三星平台场景另行发帖；Rafael补2014线：实践中ACPI多配活动固件但ACPI本身并无此原则要求

**史料**：`348057、`348068、`348079、`348090

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348057 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348068 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348079 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348090 -->` 

## 25.7 printk 收尾、峰会组织与性能回归八年之叹（3 例）

**要点（判定表逐字）**：Sergey Senozhatsky自愿协助Vetter五步fbcon改造计划（fbcon并入fb.ko、一年观察期、拆notifier、下推console_lock、修锁）并称来协调；Vetter因行程失误缺席2017 KS，转达DRM维护者推Sean Paul为代表（drm-misc committer模型加cros视角）、Jani盖房Alex为备选；Greg KH回应Chris Mason升级至3.10+留10-30%性能回归：这场讨论谈了八年，性能测试须常做却没人听，要改须企业出钱承诺而无人愿出

**史料**：`348081、`348082、`348101

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.348081 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348082 -->` `<!-- ROW_MINE: ksummit-discuss.messages.348101 -->` 

---
注：本文件由判定表程序化生成（25.1-25.7 共 7 块，覆盖 49/49 CAND，两遍计数核对通过）；要点逐字取自判定表「要点」列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
