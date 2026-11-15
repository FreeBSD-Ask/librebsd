# 4.4BSD contrib/gcc-2.3.3/README.BSD（新 ref）引用卡

- **性质**：TUHS 源码树收录的 4.4BSD `usr/src/contrib/gcc-2.3.3/README.BSD`（4.4BSD 发行附带的 GCC 构建说明，含“不要用 configure 脚本”等本地化改法）；本机 Chrome UA urllib 直取，`<pre>` 块 587 字符
- **数据库**：新建 ref（2026-11-16 V31 P2 联网补证批 b003；source_url 四键查重：库内 gcc-2.3.3 相关条目仅有通用收录，`README.BSD` 无重合）
- **source_url**：<https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/src/contrib/gcc-2.3.3/README.BSD>
- **quote（逐字，两处）**：
  1. Notes for the 4.4BSD distribution of gcc-2.3.3:
  2. There are 2 makefiles: 'makefile', which builds the compiler throughout all the stages from start to finish and supplies the 'all', 'clean' and 'install' targets using the 2nd makefile: 'Makefile' which is a GNU Makefile containing *significant* modifications to suit the BSD build.
- **考据注**：第 1 句坐实**转折的事实层**：GCC 2.3.3 已随 4.4BSD 发行，且由 BSD 自订说明（并注明“DO NOT USE THE 'configure' SCRIPT!!!”）。第 2 句坐实**供给方式**：构建不是照抄 GNU 流程，而是经“显著修改”的 GNU Makefile 适配 BSD 构建。**能证与不能证**：两处只证“随发行供给且经本地改造”，不证何时起用 GCC、也不证彼时是否已完全取代原生编译器——年代与替代过程须另取发行说明或提交记录。**渲染记账**：第 2 句中的 `*significant*` 为原文星号强调，照录；原页此句跨行，引时并作一段
- **本批落点**：V31.4.2.1 第 1 块（第 1 句）、V31.4.2.5 第 1 块（第 2 句）
- **考据日期**：2026-11-16（Task 8.2 G4 V31 P2 批 b003；official_doc／L3）
