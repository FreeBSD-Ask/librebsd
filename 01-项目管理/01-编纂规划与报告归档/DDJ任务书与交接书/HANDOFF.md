# HANDOFF: dvd6 期刊四库战役 — 交接台账（2026-10-05 会话末）

**Spec**: specs/002-dvd6-journal-db（含主理人三修正案）｜**库**: `C:\ddj_stage\{ddj,cuj,sa,tpj}.duckdb`（本地暂存）｜**最终推送**: `\\DESKTOP-M5P610N\d\librebsd\dvd6\Website\ddj\`（T038）

## 已完成（全部门禁绿）

- T001–T025（US1 全链）：侦察→骨架→issues/articles/sources/figures/ads→**T025 核验 26/26 PASS**（`script/_ddj_out/verify_all_report.json`）
- T027：refs 著录四库 10,068 条（GB/T 7714，0 孤儿）
- T004/T024：广告侦察＋促销密度扫描（25,498 页 4 候选全为正文词）→ **ads 空表为证实结论**（ads_candidates.json）
- T022 图片 LLM 转写：**TPJ 54/106 批完成并已加载**（301 transcribed＋28 base64，余 327 uncertain）；CUJ/SA/DDJ 批次已生成未开工。⚠️ 2026-10-06 压缩点：055–057 三路被取消、磁盘 batch_tpj_055.jsonl 等仍是清单桩（无 kind/text 字段），**续跑从 dispatch_tpj_055.txt 重派**；加载时桩文件会因无 kind 字段而 miss（kind 缺省 mixed 误挂），故必须先判别文件是否含 kind 字段再 load（安全：桩无 "kind" 键时 json 会 KeyError？不会——load 用 r.get("kind","mixed")，会误入库！故 load 前先 grep -l '"kind"' 过滤）。

## 四库现状

| 库 | issues | articles | source_files | refs | figures |
|----|--------|----------|--------------|------|---------|
| ddj | 324(含 09loose) | 5,272 | 27,736 | 5,272 | 7,711 uncertain |
| cuj | 195 | 2,586 | 21,717 | 2,586 | 1,934 uncertain |
| sa | 180 | 1,710 | 3,120 | 1,710 | 1,646 uncertain |
| tpj | 55 | 500 | 302 | 500 | 363 uncertain／272 done／21 base64 |

## 续跑命令（任何会话照此滚动，勿重侦察）

```sh
# 0) 铁律：脚本先复制到本地再跑（UNC 读缓存会拿到旧版！）
cp "//DESKTOP-M5P610N/d/librebsd/script/_ddj_*.py" /c/ddj_stage/_exec/

# 1) 图片转写滚动（每波 3 路 Agent 并发，勿超 3；派单词已生成好）：
#    Agent prompt＝“读取派单词文件 \\DESKTOP-M5P610N\d\librebsd\script\_ddj_out\transcribe_batches\dispatch_<j>_NNN.txt 并严格执行…”
#    完成后加载（文件名列表即批次号）：
C:/Python314/python.exe C:/ddj_stage/_exec/_ddj_transcribe_pipeline.py load --journal <j> <batch文件...>
#    进度判据：figures uncertain 计数下降；.src.jsonl 是清单、.jsonl 是结果
#    待办批次：tpj 049–106｜cuj 001–305｜sa 001–275｜ddj 001–1240

# 2) 转写全清后：figures uncertain=0 断言 + T025 重跑
C:/Python314/python.exe C:/ddj_stage/_exec/_ddj_verify_all.py

# 3) T028 summaries（每 article 一条中文概述，子代理读 body_text 批量产 JSONL）——加载器可复用
#    T029 key_facts（12 列 schema，reference_id 指 refs.id，id=kf-<db>-<ref>-<seq>）
#    T032 卷归属（重构2026 目录 54 卷对号→06-考据记录/20261005_dvd6期刊卷归属考据.md）
#    T033 key_facts.related_chapter 写回；T034 卷末书目述评 bullet（- **ref <DB>-<id>**｜体例，write_guard）
#    T035 大纲门禁（audit_disk_terminology 等）

# 4) T038 推送：C:\ddj_stage\*.duckdb → //DESKTOP-M5P610N/d/librebsd/dvd6/Website/ddj/
#    逐库 sha256 双侧一致＋行数断言后才算交付
```

## 关键陷阱（违者返工）

1. **UNC 脚本陈旧缓存**（本会话三次坐实）：改完脚本必须 cp 到 `C:\ddj_stage\_exec\` 再跑本地副本。
2. 本会话宿主 **D: 是网络映射非本地盘**；PowerShell 走 D:、python 用 C: 本地副本。
3. DuckDB 写连接开着时只读连不上（IOException）；写与验分进程。
4. 1990s PKZIP 老压缩法→`_ddj_lib_extract` 已接 7z 回退；TPJ 树部分图片有 FTP 文本模式损坏（CRLF 混入二进制），子代理会临时修复副本转写、不改源文件。
5. 并发上限：Agent 并发 ≤3（超发即 user concurrency limit exceeded，重派即可）。
6. `references` 是 DuckDB 保留字；references.id 是 VARCHAR。
7. figures 主键 figure_id 逐库独立；转写应用按 (image_name, bytes) 匹配 uncertain 行。

## 遗留与豁免（已在核验报告留痕）

- DDJ 1 篇 thin body＝源页面即 "This article currently unavailable."（照录豁免）
- no_author：ddj 365／cuj 611／sa 146／tpj 2——页面真无署名（含匿名专栏），NULL 正确不猜
- DDJ 年包根目录散件归入 `<YY>loose` 兜底期（如实标注）；DDJ 二进制 20,399 件、CUJ 1,177 件、SA 69 件、TPJ 28 件按禁令拦截（build_log 有数）
- 3 件伪文本二进制（NUL 深藏）已删并留痕：CASINO.PPR/SHSUDRVX.ASM/rave.mcb
