# jail(8) 手册（复用 ref10418）本批引文卡——两种部署哲学

- **性质**：FreeBSD jail(8) 手册 EXAMPLES 节；ref10418 已于 2026-11-13 入库（FreeBSD 15.1-RELEASE 纯文本版），本批引文取自库内 mdoc 源 `03-原始史料库/02-man源与posix仓库/01-repos/freebsd-src/usr.sbin/jail/jail.8`（usr.sbin/jail/jail.8），mdoc 宏按渲染语义还原（.Dq→弯引号；其余逐字）
- **source_url**：<https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=8>
- **quote（渲染语义还原；折行归一单空格）**：Jails are typically set up using one of two philosophies: either to constrain a specific application (possibly running with privilege), or to create a “virtual system image” running a variety of daemons and services. In both cases, a fairly complete file system install of FreeBSD is required, so as to provide the necessary command line tools, daemons, libraries, application configuration files, etc.
- **考据注**：手册记 jail 两种部署哲学——约束单个（可能带特权运行的）应用，或创建运行多种守护进程与服务的“虚拟系统镜像”；两种情形都需要相当完整的文件系统安装。适用负载以隔离需求与部署形态为判据（支撑 V37.3.6.4）。
- **本批落点**：V37.3.6.4（DOC_MINE D2）
- **考据日期**：2026-11-28（supp-V37-p2-b034；official_doc／L3）
