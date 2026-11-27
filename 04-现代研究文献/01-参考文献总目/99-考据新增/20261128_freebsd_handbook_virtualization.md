# FreeBSD Handbook virtualization 章（新 ref）引用卡

- **性质**：docs.freebsd.org 官方手册 virtualization 章（25.7.9 Jailing bhyve／25.7.13 Persistent Configuration）；Tavily extract 实抓
- **数据库**：新建 ref（2026-11-28 supp-V37-p2-b034；source_url 四键查重 0 命中）
- **source_url**：<https://docs.freebsd.org/en/books/handbook/virtualization/>
- **著录（GB/T 7714-2015）**：THE FREEBSD DOCUMENTATION PROJECT. FreeBSD Handbook: Chapter 25. Virtualization[EB/OL]. [2026-11-28]. https://docs.freebsd.org/en/books/handbook/virtualization/.
- **quote A（25.7.9；逐字；markdown 链接取纯文本）**：For improved security and separation of virtual machines from the host operating system, it is possible to run bhyve in a jail. See Jails for an in-depth description of jails and their security benefits.
- **quote B（25.7.13；逐字；行内代码反引号照录）**：To connect the virtual machine’s tap device to the network via a bridge, persisting the device settings in /etc/rc.conf is needed. Additionally, load the necessary kernel modules `vmm` for bhyve and `nmdm` for nmdm devices through the `kld_list` configuration variable.
- **考据注**：A 段记 bhyve 可运行于 jail 以改进安全并使虚拟机与宿主操作系统分离（混合部署的编排层）；B 段记 bhyve 客户机开机自启须把 tap 设备设置持久化到 /etc/rc.conf 并经 kld_list 加载 vmm／nmdm 内核模块——bhyve 运维界面依赖手工配置文件改动（分别支撑 V37.3.6.5／V37.3.6.3）。
- **本批落点**：V37.3.6.3（B）／V37.3.6.5（A）两题（DOC_MINE D2）
- **考据日期**：2026-11-28（supp-V37-p2-b034；official_doc／L3）
