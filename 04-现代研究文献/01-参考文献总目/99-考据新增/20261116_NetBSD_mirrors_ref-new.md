# NetBSD Mirrors（官方镜像与 AnonCVS 页）（新 ref）引用卡

- **性质**：netbsd.org 官方镜像页（含 AnonCVS 取码段）；curl 实抓 2026-11-16（HTTP 200，30 055 B）
- **数据库**：新建 ref（supp-V75-b012；四键查重：库内该 URL 0 条）
- **source_url**：<https://www.netbsd.org/mirrors/>
- **quote（逐字三处）**：
  1. AnonCVS mirrors
  2. CVSROOT=anoncvs@anoncvs.NetBSD.org:/cvsroot
  3. cvs co -P src
- **考据注**：AnonCVS 段给出主站地址、CVSROOT 与检出命令，并附 SSH 主机密钥两类指纹（MD5 与 SHA256）——匿名取码不需要账号，代码树的一手获取路径成文；同页另有 FTP／HTTP 镜像与 NetBSD-daily 快照目录。取码命令中的 src 为仓库模块名，与 cvs-repos 页的顶层模块表互证。
- **本批落点**：V75.2.1.1（D2 ref-new#url）
- **考据日期**：2026-11-16（supp-V75-b012；official_doc／L3，项目官网）
