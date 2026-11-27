# FreeBSD Handbook Jails 章（复用 ref10265）本批引文卡

- **性质**：docs.freebsd.org 官方手册 Jails 章（17.1 节）；Tavily extract 实抓；ref10265 已于 2026-11 入库，本批引 chroot 逃逸与按面虚拟化段（新增引文）
- **source_url**：<https://docs.freebsd.org/en/books/handbook/jails/>
- **quote（逐字；折行归一单空格；markdown 链接取纯文本）**：However, a chroot has several limitations. It is suited to easy tasks which do not require much flexibility or complex, advanced features. Over time, many ways have been found to escape from a chrooted environment, making it a less than ideal solution for securing services. Jails improve on the concept of the traditional chroot environment in several ways. In a traditional chroot environment, processes are only limited in the part of the file system they can access. The rest of the system resources, system users, running processes, and the networking subsystem are shared by the chrooted processes and the processes of the host system. Jails expand this model by virtualizing access to the file system, the set of users, and the networking subsystem. More fine-grained controls are available for tuning the access of a jailed environment. Jails can be considered as a type of operating system-level virtualization.
- **考据注**：手册记 chroot 逃逸路径经年累积（"many ways have been found to escape"），jail 把虚拟化扩展到文件系统、用户集与网络子系统三个攻击面并以细粒度控制调校访问——越狱风险按各攻击面逐一评估与收窄的官方表述（支撑 V37.3.2.5）。
- **本批落点**：V37.3.2.5（DOC_MINE D2）
- **考据日期**：2026-11-28（supp-V37-p2-b034；official_doc／L3）
