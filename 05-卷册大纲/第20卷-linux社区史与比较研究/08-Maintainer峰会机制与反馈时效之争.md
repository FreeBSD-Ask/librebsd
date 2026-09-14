# 08 【Linux社区】Maintainer峰会机制与反馈时效之争

> 对应页面：ksummit-discuss p73（pk 347856-347905，2017-04-20/26 连续讨论 45 封 + KS2014 混档 5 封）
> 判定：50 CAND / 0 NV（本页无纯出席确认信）
> 编号：DSLXC-4078..4127 | claim 已入库（50/50，dslinux_claims.duckdb）

## 8.1 【Linux社区】净收益阈值与文件搬移代价

**要点**：Bottomley 提出“净收益阈值”把关（接受补丁多因看似无害但无用户可见收益）；Corbet 辩护文档重组（面向受众成册手册）；Bottomley 澄清立场（成本 vs 收益先评估、refactor 自带门槛）；Dobriyan 系统调用表/drivers-net 目录 UX 实证；Ingo 修正 syscall 表只搬过一次。

**史料**：`347856`、`347859`、`347860`、`347862`、`347866`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347856 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347859 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347860 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347862 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347866 -->`
**史观**：多方平等（总纲 8：Bottomley 的阈值主张、Corbet 的文档重组辩护、Dobriyan 与 Ingo 的 UX 实证并置）；经验优先（总纲 9：以 syscall_64.tbl 六年前搬移、手指记忆等实作为据）；拒绝进步叙事（总纲 1/3：不将文档重组写作文档工程“进步”）
**辨析**：Bottomley 明言“不反对文档重组，而是行动前先理解成本 vs 收益”，故其阈值主张非否决；Ingo 以 syscall_64.tbl 六年前搬移一次反驳 Dobriyan 的“频繁搬移”印象。
**文献**：DSLXC-4078/4081/4082/4084/4088（`ksummit-discuss.messages.347856`、`.347859`、`.347860`、`.347862`、`.347866`，2017-04-20），全文见 `raw_source.raw_json`

## 8.2 【Linux社区】CI 与测试基础设施

**要点**：Dan Williams：0day+linux-next 非充分 CI，cmock mock 化打硬件路径，测试发现/判定“干净运行”痛点；Brown：kernelci（Kevin Hilman）与 Linaro 自动化、测试 miniconf 呼声、discoverability 问题。

**史料**：`347863`、`347867`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347863 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347867 -->`
**史观**：经验优先（总纲 9：以 cmock mock 化、kernelci.org 实际运行为据）；偶然性优先（总纲 5：议题由 0day+linux-next 覆盖面不足这一具体缺口引出）；动手者叙事（总纲 10：基建由 Dan Williams、Kevin Hilman 等当事人自陈）
**辨析**：Dan Williams 称 0day+linux-next“非充分 CI”系其个人判断；Brown 强调 kernelci 的关键在 Kevin Hilman 个人，提示基建依赖人而非制度。
**文献**：DSLXC-4085/4089（`ksummit-discuss.messages.347863`、`.347867`，2017-04-20），全文见 `raw_source.raw_json`

## 8.3 【Linux社区】distro 与 semi-distro 视角

**要点**：Brown 论 longterm 与更新意愿（Debian 排期+缺意愿+业务模型）；Ledford Fedora 无痛、RHEL 才是痛并修正代言立场；Chris Mason（btrfs semi-distro）：大部分平稳、性能回归怪自己基准。

**史料**：`347861`、`347864`、`347865`、`347891`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347861 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347864 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347865 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347891 -->`
**史观**：多方平等（总纲 8：Brown 的更新意愿论、Ledford 的 Fedora/RHEL 对照、Mason 的 btrfs semi-distro 视角并置）；自反性声明（总纲 7/23：明示本块为下游/semi-distro 视角，不代表上游全貌）；经验优先（总纲 9：以 Debian 排期、业务模型等实况为据）
**辨析**：Ledford 随后自纠“不该替 Laura 代言”，其 Fedora/RHEL 对照只应作个人视角读；Mason 的“性能回归怪自己基准”为 semi-distro 自我归因，非普遍结论。
**文献**：DSLXC-4083/4086/4087/4113（`ksummit-discuss.messages.347861`、`.347864`、`.347865`、`.347891`，2017-04-19 至 04-25），全文见 `raw_source.raw_json`

## 8.4 【Linux社区】patchwork 通知标准化与维护者脚本

**要点**：Belloni 指出 MAINTAINERS B: 未被推广、patchwork 通知仅账号者；Julia 更正（无账号也收）；Sang：可配置全列表（ozlabs 先例）；Ellerman：通知应发原收信列表、便捷我也用 git-notes；Mauro：linuxtv 默认全列表、附 post-receive mailbomb Perl 脚本全文；Bottomley 附同类脚本+错误发送前科。

**史料**：`347871`、`347872`、`347873`、`347874`、`347875`、`347877`、`347878`、`347880`、`347881`、`347882`、`347883`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347871 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347872 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347873 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347874 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347875 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347877 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347878 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347880 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347881 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347882 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347883 -->`
**史观**：多方平等（总纲 8：Belloni 的问题陈述与 Julia、Sang、Ellerman 的更正/补充并置）；经验优先（总纲 9：以 ozlabs、linuxtv 的既存配置与 post-receive 脚本全文为据）；动手者叙事（总纲 10：脚本与规则由 Mauro、Bottomley 当事人给出）
**辨析**：Belloni 称“patchwork 通知仅账号者”被 Julia 以亲历更正，故该“问题”不成立；Bottomley 自曝脚本错误发送前科，提示自动化脚本本身亦有风险。
**文献**：DSLXC-4093/4094/4095/4096/4097/4099/4100/4102/4103/4104/4105（`ksummit-discuss.messages.347871`、`.347872`、`.347873`、`.347874`、`.347875`、`.347877`、`.347878`、`.347880`、`.347881`、`.347882`、`.347883`，2017-04-21），全文见 `raw_source.raw_json`

## 8.5 【Linux社区】sub-maintainer 名单与 co-maintainership 实践

**要点**：Belloni 自荐：coccinelle 补丁泛滥之恶（devm 转换害处）与 RTC 依赖 I2C/SPI 想早被纳入讨论；Ferre（at91）：6 年 co-maintainership 教训——非万能药、有真实缺陷限制，须谈 best practice。

**史料**：`347876`、`347884`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347876 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347884 -->`
**史观**：动手者叙事（总纲 10：自荐与六年教训均由 Belloni、Ferre 本人陈述）；经验优先（总纲 9：以 devm 转换之弊与 at91 六年 co-maintainership 实作教训为据）；多方平等（总纲 8：coccinelle 补丁泛滥与 co-maintainership 局限两类经验并置）
**辨析**：Ferre 明言 co-maintainership“非万能药、有真实缺陷限制”，故本块不得读作 co-maintainership 的推广史料；Belloni 的自荐含具体动机（RTC 依赖 I2C/SPI），非泛泛表态。
**文献**：DSLXC-4098/4106（`ksummit-discuss.messages.347876`、`.347884`，2017-04-21/04-24），全文见 `raw_source.raw_json`

## 8.6 【Linux社区】不可变分支与跨树协作

**要点**：Vetter 对 arm-soc 拆树批评（bisect 落 merge、启用补丁整版延迟）；Brown 指出跨子系统问题非 ARM 独有；Olof 回应 DT/ARM（绑定先 review、冲突 quiet 惯例）；Linus Walleij：immutable topic branch 与 MFD/dt-bindings 头文件 nexus；Olof：clk per-driver 分支推回“仅为数值 define”加依赖；Brown：cross-merge 只需 sign a tag；Lee Jones：MFD 1-7 个 immutable tag 实践与硬依赖门。

**史料**：`347858`、`347869`、`347885`、`347886`、`347887`、`347888`、`347889`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347858 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347869 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347885 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347886 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347887 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347888 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347889 -->`
**史观**：多方平等（总纲 8：Vetter 的拆树批评、Brown 的“非 ARM 独有”回应、Olof/Walleij/Lee Jones 的机制实践并置）；动手者叙事（总纲 10：immutable tag 做法由 Walleij、Olof、Lee Jones 自陈）；拒绝进步叙事（总纲 1/3：不将 immutable branch 写作协作机制“进步”）
**辨析**：Brown 指出跨子系统碎片不只 ARM，故 Vetter 对 arm-soc 的批评不构成 ARM 特例；Lee Jones 的“MFD 1-7 个 immutable tag”与“硬依赖门”为其实践总结。
**文献**：DSLXC-4080/4091/4107/4108/4109/4110/4111（`ksummit-discuss.messages.347858`、`.347869`、`.347885`、`.347886`、`.347887`、`.347888`、`.347889`，2017-04-20 至 04-25），全文见 `raw_source.raw_json`

## 8.7 【Linux社区】反馈时效、评审机制与信任因子

**要点**：Rafael：无人认领代码、review 自愿无偿“让 review 更有回报”、比例 2/3+1/3 36-45 人；Bart 实例（block/SCSI/RDMA 快、两块慢）；Brown：老议题能否爆新意——“处在新老维护者之间的新子系统无人正向”；Guenter：obscure 子系统唯一行 view 者应获宽松；Geert 反题；Carpenter 几周 OK 几月不 OK；Petersen：简单补丁立复、复杂核心需整块时间、厂商 30+ patch 全渠前；Brown 观察“人消失/无兴趣无候选”；Kosina Reviewed-by 廉价化；Lunn：netdev 模式 NACK+拆小批教学提交者；Bottomley：信任因子与 SCSI 史式 hold-until-review 实验（mixed、仍建议）。

**史料**：`347870`、`347892`、`347893`、`347894`、`347895`、`347896`、`347897`、`347898`、`347899`、`347900`、`347902`、`347903`、`347904`、`347905`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347870 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347892 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347893 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347894 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347895 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347896 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347897 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347898 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347899 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347900 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347902 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347903 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347904 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347905 -->`
**史观**：多方平等（总纲 8：Rafael、Bart、Brown、Guenter、Geert、Carpenter、Petersen、Kosina、Lunn、Bottomley 十方并置）；经验优先（总纲 9：以 block/SCSI/RDMA 快慢实例、厂商 30+ patch 全渠前等实况为据）；自反性声明（总纲 7/23：本块为多立场实录，不取单一结论）
**辨析**：Brown 追问“老议题能否爆出新意”，提示该议题历年重复；Bottomley 的 SCSI 式 hold-until-review 实验自陈“mixed、仍建议”，属未定论；Geert 的“行为人可能无时间”与 Bart 的“为何不找替代”构成正面分歧。
**文献**：DSLXC-4092/4114/4115/4116/4117/4118/4119/4120/4121/4122/4124/4125/4126/4127（`ksummit-discuss.messages.347870`、`.347892`、`.347893`、`.347894`、`.347895`、`.347896`、`.347897`、`.347898`、`.347899`、`.347900`、`.347902`、`.347903`、`.347904`、`.347905`，2017-04-21 至 04-26），全文见 `raw_source.raw_json`

## 8.8 【Linux社区】KS2014 档案混档（2014-05-12）

**要点**：本页 KS2014 档案信 5 封（002 QR oops 防重复/043 Energy bias CPU 解析/024 Iyer Energy 调度器条件/035 QR cut-here 行数提示/046 tinification bloat-o-meter）已入 claim。

**史料**：`347857`、`347868`、`347879`、`347890`、`347901`

**史料锚**：`<!-- ROW_MINE: ksummit-discuss.messages.347857 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347868 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347879 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347890 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347901 -->`
**史观**：自反性声明（总纲 7/23：明示本块为跨年混档，不与 2017 线程混叙）；偶然性优先（总纲 5：档案信因页面切片规则而混入）；拒绝进步叙事（总纲 1/3：不将 2014 议题写作其后讨论的“前身”）
**辨析**：5 封均为 2014-05-12 同日档案信（Jason Cooper×2、Preeti、Iyer、Sang），与 p73 主体 2017-04-20/26 线程无回复关系；本块只作归卷登记。
**文献**：DSLXC-4079/4090/4101/4112/4123（`ksummit-discuss.messages.347857`、`.347868`、`.347879`、`.347890`、`.347901`，2014-05-12），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（8.1-8.8 共 8 块，覆盖 50/50 CAND）；要点逐字取自判定表“要点”列（审读实录），史料锚与 CAND 一一对应。
