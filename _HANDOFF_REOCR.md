# 交接书 REOCR —— GLM 视觉重 OCR 战役（参考文献库 327 件 7741 页）

> 交接时点：2026-09-27（会话 sess_f2483abb）。本书记录战役定义、实测复核后的精确进度、38 件闭环清单、续作 SOP、全部纪律坑与后验基线。下一会话读此书即可无损接续。
> 状态总入口：`_tmp/REOCR_STATE.md`（逐日续作记账）；相关记忆：`reocr-campaign-20260927-and-session-interrupt-rootcause`。

## 〇、主理人指令链（全部有效）

1. 参考文献全文库（references_fulltext.duckdb，表名 "references" 须带引号）逐个复核提取有价值信息；译本并存不采纳译本；修正增补大纲与错误。
2. OCR 质量差的 PDF：**GLM 直接视觉识别重 OCR（禁本地引擎），现有 303 件 7129 页全部逐页转录，不得按质量筛选跳过**（不使用本地模型）；乱码件（27 件 612 页）另加逐个全量；源文件有问题的重新下载（子代理任务）。
3. 不使用子代理跑转录；主代理直接读图转录（用户指令）。当前有效并发授权见记忆 `subagent-40-allowed-and-recommended`（转录线仍按"主代理直读"执行）。

## 一、战役定义与完成标准

- 对象＝`_tmp/reocr_worklist.json`（**300 件 / 7129 页**）＋ `_tmp/mojibake_worklist.json`（**27 件 / 612 页**），无交集，合计 **327 件 / 7741 页**。
- **完成定义**：327 件全部以 `glm_vision_20260924` 写回（`select count(*) from fulltext where extraction_method='glm_vision_20260924'` ≥ 327），且**每件转录页数与 worklist 相符**（逐件核验脚本见 §五.10）。
- 渲染页：`_tmp/reocr/<ref>/pNNNN.png`（300+27 件已全部渲染完，**渲染不是瓶颈，转录才是**）。
- 转录产出：`_tmp/reocr_out/pages/<ref>_pNNNN.txt` → `_ingest.py` 并入 `_tmp/reocr_out/w1_c.jsonl`（5454→w1_a_me.jsonl；早期批次 2817/3565-3568/5454 在 w1_b.jsonl/w1_a.jsonl）→ `merge_reocr.py --apply` 写回 DB（block_type='ocr_glm_vision'、reference_update_log 留痕）。

## 二、当前状态（2026-09-27 实测复核）

| 口径 | 件 | 页 |
|---|---|---|
| worklist 总量 | 300 | 7,129 |
| worklist 已全覆盖（DB glm 写回＋页数相符） | **38** | **658** |
| worklist 未做 | **262** | **6,471** |
| 乱码件总量 | 27 | 612 |
| 乱码件已做 | 0 | 0 |
| **合计未做（唯一口径）** | **289** | **7,083** |

- 库内 `glm_vision_20260924` = **38 件**，与 worklist 内 38 件完全对应、页数逐件相符（核验脚本输出 38/38 OK）。
- 早期 5 个 MISMATCH 疑点已澄清＝计数口径问题：2817/3565/3566/3567/3568 的转录数据在 `w1_b.jsonl`（2817=10、3565=17、3566=16、3567=8、3568=9+2(w1_c)=11 页，均与 worklist 相符，DB blocks 同数）；5454 的 w1_c 里 p9-40 共 32 页是早期重复分件（无害，merge 按 ref 全覆盖替换，DB 153 页正确）。
- **下一件游标（worklist 顺序）**：**#2520（12 页）** → 2521（6）→ 2522（6）→ 2523（6）→ 2524（7）→ …（`_tmp/reocr_worklist.json` 顺序即队列）。

## 三、已闭环 38 件清单（按时间序，全部写回 DB）

**早期批次（09-24/25/26 上午）**：#5454 Computerworld 1988-10-24 全刊 153 页（BoCoEx 二手指数表、AT&T Unix group/Sun blasts OSF、CERN-Oracle LEP 等）；#2817 UNIX 4.0 手册 10pp；#3565 17pp；#3566 Ritchie&Thompson 论文 UNIX 4.0 重印本 16pp；#3567 8pp；#3568 Editor Tutorial 11pp（3568 补 p10-11 于 09-26）；#3586-3599 516-TSS 十二件（3594 THREAD SAVE BLOCKS＝thread 术语史一手、3593 RING INTERRUPT＝1968 环网协议一手）。

**09-26 上午 worklist 顺序批**：#1437《DV over IP 软件兼容与人机界面》4pp；#1535《RISC I》（Patterson & Séquin 1981 ISCA）18pp；#1557《Bug fixes and changes in 4.1bsd》（Joy 1981-05-10）9pp；#1567《;login: 16:3》USENIX 全刊 42pp；#1735《Proposals for enhancement of UNIX on the VAX》CSRG TR/4 59pp（**socket/portals/符号链接/命名目录/圆柱组文件系统最初设计文档**）；#1571《USL v. BSDi Settlement Agreement》45pp（**BSD 许可证起源一手**，Exhibit A-F 全录）。

**09-26/27 会话（sess_f2483abb）**：#1756 DTIC AD-A290431 18pp；#1760 DTIC ADA419594《An Empirical Study of Operating Systems Errors》17pp（Stanford 静态分析查 Linux/OpenBSD 内核错误）；#1827《Changes in the VAX system in the Fourth Berkeley Distribution》Bill Joy 1980-11 10pp（4BSD 变更一手）；#1830《UNIX REVIEW》1984-08 Bill Joy 专访 13pp（vi 起源全链口述）；#1994《Second Distribution of Berkeley Software for UNIX》2BSD 公告 1979 4pp；#2006《Hints on Configuring VAX* Systems for UNIX》Kridle & Joy 1981-05-04 20pp（4.1bsd 选型一手、Berkeley Upgrade Kit）；#2008 USL v. BSDi 45pp＝**与 #1571 同一 PDF（md5 `7f136ad4…` 逐字节相同）直接复用转录**；#2371《United States v. Microsoft》97 F. Supp. 2d 59（D.D.C. 2000）17pp（救济判决＋Final Judgment 全文：OS/App 两业务拆分、OEM 条款、API 披露、定义全表）；#2420 南京中院（2021）苏01民初3229号 27pp（**国内首起采纳 GPL 抗辩生效判决**：主程序系 SharpZipLib GPL 衍生作品须开源、预览程序不受 GPL 约束、惩罚性赔偿 300 万，附件 38 文件比对表全录）；#2430 深圳中院（2019）粤03民初3928号 罗盒 v. 风灵/腾讯 16pp（**GPLv3 合同性质、授权自动解除、贡献者默示许可、50 万**）；#2451 TUHS《SCCS is awesome》4pp（McVoy：weave/set/include-exclude/merge=copy by reference）；#2477 最高法（2021）最高法知民终2063号 14pp（**GPLv3 二审终审：项目管理人无须贡献者授权即可维权、"通知-改正"非前置程序、第 10 条仅限专利权、贡献者份额预留机制**）。

**重磅史料待提 key_facts/大纲增补（挂账）**：1735（socket/portals/符号链接/命名目录/圆柱组）、2420/2430/2477（中国 GPL 判例三件套→开源法律章）、2451（SCCS weave 术语史）、2006（VAX 选型/Berkeley Upgrade Kit）、1830（vi 起源口述）。

## 四、续作 SOP（逐件循环）

1. **查源**：`reocr_meta.json` 取 title/path；`python -c "from PIL import Image; print(Image.open(f'_tmp/reocr/<ref>/p0001.png').size)"` 定页面尺寸与版式。
2. **切带**：按 §五.2-4 的口径用 `_tmp/reocr_out/_zoom.py <ref> <page> x0 y0 x1 y1 [scale] [tag]` 产出 `_tmp/reocr_out/zoom/` 条带；中文判决/密排页用三段（s1/s2/s3）；大 DPI 扫描件整页直读或上下半页。
3. **转录**：逐字、禁总结、[?] 占位；判例保案号日期；表格用 `｜` 分隔行转录；图用 [图] 描述＋可辨行；报纸按栏。
4. **入库**：`python _tmp/reocr_out/_ingest.py _tmp/reocr_out/pages/<ref>_p00*.txt`（5454→w1_a_me，其余→w1_c；已入库自动 SKIP）。
5. **写回**：`python -c`（从 w1_c.jsonl 抽该 ref 生成 `_tmp/_merge_<ref>.jsonl`）→ `python _tmp/merge_reocr.py --apply _tmp/_merge_<ref>.jsonl`（**勿用默认 glob**）。
6. **验**：`select count(*),char_count from fulltext where reference_id='<ref>'`＋blocks 页数与 worklist 相符。
7. **记账**：`_tmp/REOCR_STATE.md` 追加该件要点；重磅史料随手提 key_facts。
8. **重复件先 md5**：worklist 内同文档多卷（如 2008=1571），先 `hashlib.md5` 比对源 PDF，同 md5 才复用转录（同时落 pages/<ref>_p*.txt 存证）。

## 五、纪律与坑（血泪全清单）

1. **转录用主代理直读图**（用户指令）；子代理只用于源文件重下载。
2. **pages/ 有文件 ≠ 已入库**（#1760 p1-15 曾只落盘未进 jsonl，差点漏 15 页）——接手先查 `w1_c.jsonl` 是否已有该 ref 的行；早期批次数数据在 `w1_b.jsonl`/`w1_a.jsonl`，**对账必须扫全部 w1_*.jsonl**。
3. **重复件先 md5**（2008=1571 实例）；不同 md5 必须逐页重读。
4. **库写回按件单独跑** `--apply _tmp/_merge_<ref>.jsonl`，默认 glob 会把已写回件整批重写、徒增 reference_update_log 行。
5. **超大渲染页按原生像素切带**：2006=10584×13650（144.5M 像素，PIL 只报 DecompressionBombWarning 可继续）、1994=5309×6873、5454/1830=1275×1650——**绝对像素坐标不可跨件套用**（曾按 1275×1650 假设切出空白条带）；条带起点用 1/4 缩放行投影判定，勿信整页缩略图目测。
6. **中文判决书（维基文库/微信导出小字密排）整页直读曾两次落笔走样**（2420 p3、2430 p2，均重读重写）——**必须 2.2x 三条带（y60-620/610-1180/1170-1720）核读后再落笔，落笔走样必须整页重写而非打补丁**。
7. **英文 pipermail 归档页用行投影先定墨迹区**（2451 p4 仅页首 3 小行＋页脚，勿按整页扫带）。
8. **网页打印件右缘系统性截断**（2477，每行末尾缺 2-6 字符）：按上下文以方括号补足并逐件注明"未经原印件核实"；人名/数字 **XXX 脱密如实保留**（可从同案一审判决交叉核对）。
9. **知产宝/微信导出件**：水印遮挡处标〔被"知产宝"水印遮挡〕；原插图未随 PDF 的空白处标〔原扫描件此处有空白〕；行序错乱段须放大重核，不得臆造"重排"。
10. **逐件页数核验**（完成定义）：`transcribed(全部 w1_*.jsonl)==worklist pages` 且 `fulltext_blocks count==pages`——38 件已验 38/38 OK。
11. **中断根因（环境，非内容）**：共享 provider 429 `rpm exhausted`（同日 7+ 并行会话重灾）、模型切换致 `TURN_CANCELLED`（"v4 session stopped"）、会话库 1.5GB+WAL——长 turn 中勿切模型；工具调用可能 30s TOOL_TIMEOUT 但文件已落盘（写后必 ls 复核）。
12. 图片读图消耗大：本轮经验＝每页 1-3 次 Read；上下文吃紧时按 §四.2-7 逐件闭环、及时记账再续，断点不丢。
13. 学术规范：引文逐字＋URL＋页脚水印（hallapproved.com／tuhs.org／zh.wikisource.org／mp.weixin.qq.com／ipc.court.gov.cn）随文转录；负结果如实记。

## 六、后验基线（续作后必须复跑）

- `select count(*) from fulltext where extraction_method='glm_vision_20260924'` ≥ 38（当前 38；目标 327）。
- 全部 w1_*.jsonl 各 ref 页数 == worklist 页数（38 件已验）；`fulltext_blocks` 每件 count==页数。
- 已写回件 char_count 抽验（当前实测见 §二脚注脚本输出：1760=89732、1827=36379、1830=46691、1994=7759、2006=56485、2008=107613、2371=48389、2420=38747、2430=32119、2451=7715、2477=33924…）。
- 乱码件 27 件仍未动（0/612 页）；3 件渲染失败另案：#2739（803 页市政档案）、#2787（CHM）、#5442（Custer 书 md 版；其 PDF 扫描=#5443 无文本层，选段处理）。
