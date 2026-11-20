# FreeBSD 2.0.5 `sys/i386/conf/LINT` 引用卡

- **性质**：FreeBSD 2.0.5 时代 `sys/i386/conf/LINT`（i386 内核全量校验配置）纯文本（25,085 字节），取自 FreeBSD 官方 cgit plain 视图（release/2.0.5 标签；文件头版本戳 `$Id: LINT,v 1.183 1995/05/27 04:32:12 davidg Exp $`＝1995-05、提交者 davidg＝David Greenman）
- **数据库**：新建 ref（2026-11-21 V36 P2 联网补证批 b011；source_url 四键查重：库内 LINT 仅 ref11046＝releng/1 分支（1.x），本 ref 为 release/2.0.5 分支（2.x），同路径异分支以 query 区分，登记时保留 h= 参数——b006 跨域镜像教训的“同路径异分支”面亦须比对，本例两分支实为不同文件版本，非重复）
- **source_url**：<https://cgit.freebsd.org/src/plain/sys/i386/conf/LINT?h=release/2.0.5>
- **quote（逐字三处；原文制表符缩进，引文按行原样保留）**：
  1. `config		kernel	root on wd0 dumps on wd0`（config 行）
  2. `options		KERNFS			#Kernel filesystem`…`options		UNION			#Union filesystem`（文件系统 options 清单段，KERNFS 至 UNION 九行连续）
  3. `# Only the root, /usr, and /tmp filesystems need be statically`…`# currently be demand-loaded.)`（按需装载注释段四行连续）
- **考据注**：第 1 处是**内核层结构差异的直证**：2.x config 行内核名从 1.x 的 `"386bsd"` 改为 `kernel`，且 swap 设定（`swap on wd0 and sd0`）整段移除——以 Lite 替换代码基带来的配置层结构差异由同一文件的版本对比自证（1.x 形态见 ref11046）。第 2 处是**文件系统支持扩展面**：KERNFS／MSDOSFS／UNION 等九类文件系统选项在册——MS-DOS、unionfs、kernfs 的加入由配置清单自证。第 3 处是**可装载途径**：除根／usr／tmp 需静态编入外，其余文件系统在挂载时自动按需装载（UFS 族 FFS/MFS/LFS 除外）——扩展方式由重编内核转为按需装载的机制自证。**年代披露**：v1.183＝1995-05-27，属 2.0.5 时代文本；所证为 2.x 形态存在与机制，不证 2.0（1994-12）首发时的逐字清单。
- **本批落点**：V36.2.3.1 第 1 块（第 1 处）、V36.2.3.2 第 1 块（第 2 处）、V36.2.3.3 第 1 块（第 3 处）
- **考据日期**：2026-11-21（Task 8.2 G4 全责线 V36 P2 批 b011；official_doc／L3）
