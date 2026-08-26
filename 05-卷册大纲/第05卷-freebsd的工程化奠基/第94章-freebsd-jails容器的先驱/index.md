---
chapter: 第 94 章
id: CH94
volume: 05
---

# 第94章 freebsd-jails容器的先驱

## 要点

- Poul-Henning Kamp（波尔-亨宁·坎普）(phk) 于 1999 年 4 月 28 日在 FreeBSD 4.0-CURRENT 开发周期内提交 Jails 初始实现（早于 4.0-RELEASE 2000.3.20 约 11 个月），起源是为一家托管客户提供安全隔离环境，发现 chroot 不够用，遂在一天下午写了 **jail(2)** 系统调用；Jails 随 4.0-RELEASE 2000.3.20 正式发布；Jails 比 Docker 早 13 年
- 2000 年互联网泡沫期 ISP 托管需求激增，共享主机需要安全隔离，chroot 仅隔离文件系统不隔离网络与进程，phk 的托管客户需要 “每个客户独立 IP 与进程视图”，催生 Jails
- phk 的设计动机是 “让 root 不那么全能”，通过 **jail(2)** 限制 root 权限 (如禁止修改网络配置、禁止加载内核模块)，使 jailed 进程即使被攻破也无法影响主机
- phk 的 Jails 史料保存较好，BSDCon 论文与 commit log 完整，但设计动机的部分细节散落在邮件列表中
- 针对 FreeBSD 阵营“批评基于旧版本”的反批评，VMware 阵营的再回应指出四点：其一，VMware 2018.2.27 博客"The Story of Containers"批评的是 Jails 设计层面的结构性限制——"a jail could only have one IPv4 address for communication and could only use UDP or TCP for communication (no raw sockets, no IPv6, etc.)"，这些限制在 Jails 设计之初即存在，并非“旧版本”问题；其二，VMware 博客明确指出 FreeBSD 后期放宽限制是"In response to the emergence of not so restricting container capabilities in other operating systems"，即在外部容器生态压力下的被动跟进，这一判断基于 Jails 改进时间线（VNET 于 8.0 引入、IPv6 支持更晚）与 Solaris Zones（2004）、LXC（2008）发展的对应关系，是结构性观察而非版本偏见；其三，“批评基于旧版本”的反批评本身可能是形式主义——以“版本更新”为标准否定批评的有效性，忽略了 Jails 在容器生态中的结构性位置（共享内核、缺乏镜像分发、缺乏编排层）并未因版本更新而根本改变；其四，外部批评与 jails 作者的自我评价在“虚拟化能力不足”这一判断上形成交叉印证——phk 本人在其个人网站 jails saga 中将文章标题直书为"Jails – High value but shitty Virtualization"，即“高价值但糟糕的虚拟化”，并明确承认 jails 不是优秀的虚拟化方案，这表明 VMware 阵营"severe restrictions"的批评并非外部偏见，而是与作者自我认知一致的工程判断，FreeBSD 阵营“批评基于旧版本”的反批评因此失去效力——作者本人未将“限制”视为待修正的缺陷，而是将其重新框定为“不完美虚拟化往往更可取”的有意设计

## 史观

- 总纲第 1 条——偶然性改写历史，phk 因托管客户需求偶然发明 Jails
  - 辨析：经 bsd_commits.db commits 表与 commit_files 表交叉验证，Jails 的确切诞生日为 1999-04-28（commit 02daf150a4434305b9181b0ac9150762afb4c8ce），旧叙事 “2000.3.14 与 2000.3 两种说法” 均不准
- 总纲第 11 条——商品是形式主义，“版本更新”话语本身是市场形式主义的运作
  - 辨析：VMware 博客是否构成“VMware 阵营”的正式立场须审慎判断——博客作者 Rostislav M. Georgiev 以 VMware Open Source Technology Center 工程师身份署名、发布于 VMware 官方开源博客，属员工署名技术博客性质，非 VMware 公司正式立
- 总纲第 11 条——商品是形式主义，容器市场的选择是形式主义权力运作
  - 辨析：Docker 是否“工程粗糙”存在争议，Docker 阵营会反驳镜像与编排是工程创新而非营销；“劣币驱逐良币”的判定标准须明确——若以“生态完整性”为标准，Docker 非劣币 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]；phk 自评"shitty Virtualiz
- 总纲第 25 条——终结与延续，Jails 终结 chroot 安全用途，延续文件隔离
  - 辨析：chroot 是否 “完全不安全” 存在争议，非 root 进程仍有一定隔离
  - 文献：chroot(2) 手册页；4.2BSD 文档；安全分析论文 ［A］

## 93.2.2 **jail(2)** 的系统调用设计

- 要点：**jail(2)** 系统调用接受 jail 结构 (hos
- 总纲第 1 条——偶然性改写历史，Jails 概念早于市场认可
  - 辨析：OS 级虚拟化的 “首创” 归属存在争议，chroot 是早期形式
  - 文献：容器技术史论文；Jails/Zones/LXC/Docker 文档 ［B］

## 93.3.2 与 Docker 的时间差

- 要点：Jails(2000) 比 Docker(2013) 早 13 年，比 Solaris Zones(2

## 辨析

- 经 bsd_commits.db commits 表与 commit_files 表交叉验证，Jails 的确切诞生日为 1999-04-28（commit 02daf150a4434305b9181b0ac9150762afb4c8ce），旧叙事 “2000.3.14 与 2000.3 两种说法” 均不准确，2000.3.20 为 4.0-RELEASE 发布日期而非 Jails commit
- VMware 博客是否构成“VMware 阵营”的正式立场须审慎判断——博客作者 Rostislav M. Georgiev 以 VMware Open Source Technology Center 工程师身份署名、发布于 VMware 官方开源博客，属员工署名技术博客性质，非 VMware 公司正式立场声明；“被动跟进”的判定标准须明确——若以“主动预告”为标准，Jails 的 VNET 改
- Docker 是否“工程粗糙”存在争议，Docker 阵营会反驳镜像与编排是工程创新而非营销；“劣币驱逐良币”的判定标准须明确——若以“生态完整性”为标准，Docker 非劣币 [考据完成：2026-07-28 该处存疑标注属史料缺口，须待原始档案公开后方可补充确证]；phk 自评"shitty Virtualization"是否构成“劣币”的自我承认须结合其行文风格判断——phk 行文惯用自嘲，
- chroot 是否 “完全不安全” 存在争议，非 root 进程仍有一定隔离
  - 文献：chroot(2) 手册页；4.2BSD 文档；安全分析论文 ［A］

## 93.2.2 **jail(2)** 的系统调用设计

- 要点：**jail(2)** 系统调用接受 jail 结构 (hostname、path、ip4addr、ip6addr)，在 chroot 基础上增加网络绑定、进程可见
- OS 级虚拟化的 “首创” 归属存在争议，chroot 是早期形式
  - 文献：容器技术史论文；Jails/Zones/LXC/Docker 文档 ［B］

## 93.3.2 与 Docker 的时间差

- 要点：Jails(2000) 比 Docker(2013) 早 13 年，比 Solaris Zones(2004) 早 4 年，比 LXC(2008) 早 8 年；但 Docker 的

## 文献

- Kamp "Jails: Confining the Omnipotent Root"(BSDCon 2000)；jail(2) 手册页；phk 个人网站；Poul-Henning Kamp. Add the jail system call. freebsd-src [DB/OL]. 1999-04-28T11:28:49Z. 02daf150a4434305b9181b0ac9150762afb4c8ce ［A］

## 93.1.2 2000 年的工程语境

- 要点：2000 年互联网泡沫期 ISP 托管需求激增，共享主机需要安全隔离，chroot 仅隔离文件系统不隔离网络与进程，ph
- VMware 开源博客（Georgiev 撰）；phk 个人网站 jails saga；FreeBSD 8.0 Release Notes；Solaris Zones 文档；LXC 文档 ［A］

## 93.10.2 Rutgers 阵营的再回应

- 要点：针对 FreeBSD 阵营“课程笔记非权威”或“批评未标注版本”的反批评，Rutgers 阵营的再回应指出三点：其一，Rutgers 课程笔记的批评"lacked fine-grained resource management"针对的是 Jails 的资源管理模型——Jails 早期缺乏 CPU、内存、进程数的细粒度配额，这是设计层面
- 项目史观总纲第 11 条；Docker 官方文档；VMware 开源博客（Georgiev 撰）；phk 个人网站 jails saga；Docker 市场报告 ［B］

## 93.11.2 总纲第 15 条审视：文化即形式主义

- 要点：从项目史观总纲第 15 条“文化即形式主义。传统在形式主义化过程中被遮蔽与重构。知音难觅同样适用于技术社区”审视 jails 作为容器先驱叙事的文化命运。容器技术的“传统”在形式主义化过程中被遮蔽与重构——今日开发者谈及“容器”，默认指向 Docker 镜像与 Kubernetes Pod，chroot→ **jail(2)** →Solaris Zon
- chroot(2) 手册页；4.2BSD 文档；安全分析论文 ［A］

## 93.2.2 **jail(2)** 的系统调用设计

- 要点：**jail(2)** 系统调用接受 jail 结构 (hostname、path、ip4addr、ip6addr)，在 chroot 基础上增加网络绑定、进程可见性隔离、超级权限限制；**jail_set(2)** 在 8.x 扩展为更灵活的 API
- 史料：jail(2) 与 jail_set(2) 手册页、sys/kern/kern_jail.c 实现 ［A］
- 史观：总纲第 4 条——分离与聚合，**jail(2)** 聚合文件/网
- 容器技术史论文；Jails/Zones/LXC/Docker 文档 ［B］

## 93.3.2 与 Docker 的时间差

- 要点：Jails(2000) 比 Docker(2013) 早 13 年，比 Solaris Zones(2004) 早 4 年，比 LXC(2008) 早 8 年；但 Docker 的镜像与编排生态使其市场认可远超 Jails
- 史料：Docker 发布文档、容器技术史论文、市场分析报告 ［B］
- 史观：总纲第 22 条——开源运动，Docker 的市场成功得益于开源运动与商业生态
- 辨析：时间差是否 “应” 转化为市场优势存在争议
- 文
- jail(8) 手册页；VNET 文档；VMware 2018 容器史博客 ［A］

## 93.4.2 特权分离机制不足

- 要点：早期 Jails 的特权分离较粗，root in jail 仍能执行部分特权操作 (如绑定低端口)，后续通过 **mac_jail(4)** 与 **jail_set(2)** 参数细化；Rutgers 课程笔记批评 "lacked fine-grained resource management"
- 史料：mac_jail(4) 手册页、Rutgers 课程笔记、jail_set(2) 文档 ［A］
- 史观：总纲第 3 条——形式主义膨胀，早期
- VMware 2018 博客；Rutgers 课程笔记；jail(8) 手册页 ［A］

## 93.5.2 Solaris Zones 的工程否定

- 要点：Sun 在推出 Solaris Zones(2004) 时以 Jails 为反面论证，强调 Zones 的细粒度资源管理 (如 CPU/shm 限制) 与全局区域管理，暗示 Jails 工程不足
- 史料：Solaris Zones 设计文档、Sun White Paper、BSDCon 2004 Zones vs Jails 讨论[考据完成：2026-07-28 经穷尽联网考据，上述史料清单为已知公开来源汇总，部分原始档案未公开
- Kamp 2000; FreeBSD Handbook ［A］

## 自反性声明

本章所书皆是形式主义化的重构，并非对“真实的 BSD 历史”的呈现。本章的章节划分、事件选择、叙事策略、因果归因——全部基于编纂者的哲学设定。本章承认这些局限，不声称客观或中立，欢迎被更诚实的叙事所超越。
