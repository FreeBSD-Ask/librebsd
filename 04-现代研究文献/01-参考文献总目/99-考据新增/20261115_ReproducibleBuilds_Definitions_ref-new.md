# reproducible-builds.org“Definitions”页（新 ref）引用卡

- **性质**：reproducible-builds.org 的 Definitions 页（“When is a build reproducible?”）；本机 curl 对 **https** 报 schannel 握手失败（`SSL/TLS connection failed`），改走 **http://** 得 200、37,681 B——按既有教训（TLS 失败≠站点不可达）先换协议再判
- **数据库**：新建 ref（2026-11-15 V34 P2 联网补证批 b010；source_url 四键查重：库内 reproducible-builds.org 零命中）
- **source_url**：https://reproducible-builds.org/docs/definition/
- **quote（逐字，两处，取自 http 同域同路径页）**：
  1. A build is reproducible if given the same source code, build environment and build instructions, any party can recreate bit-by-bit identical copies of all specified artifacts.
  2. The relevant attributes of the build environment, the build instructions and the source code as well as the expected reproducible artifacts are defined by the authors or distributors.
- **考据注**：第 1 句是“可复现”的定义（同源码＋同环境＋同指令→任何一方可造出逐位相同产物），第 2 句把**边界**交给作者或分发者声明（环境相关属性、指令、源码、期望产物各由谁定义）。两句合起来正是 2.2.6“比对结论的可复现要求”：既要能被他方重做，也要先写明重做什么。**取源说明**：本批从 http 取得正文（https 本机不通），cite 仍用 https 规范地址；若日后 https 可达，须复核两版内容一致
- **本批落点**：V34.2.2.6 第 1、2 块
- **考据日期**：2026-11-15（Task 8.2 G4 V34 P2 批 b010；official_doc／L3）
