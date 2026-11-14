# 3B 逐卷人工审定工具

用于 ykla 本人逐条审定 1—75 卷的全部章、节、小节（**第 76 卷整卷排除**），是 Task 5 的前置。审定对象共 **23,722** 条：章 539、节 3,918、小节 19,265。结论不直接回写台账，经“导出→AI 重拟批→二审→回写批”落地。

## 启动

```text
C:\Python314\python.exe "05-卷册大纲\映射\title-review\3b-review\serve_3b_review.py"
```

- 默认端口 8899，绑定 `0.0.0.0`；启动会逐卷自校验（539／3,918／19,265／23,722），不一致即拒绝启动并报差异卷号。
- 可选参数：`--port 8899`、`--root <仓库根>`。
- 启动后终端打印本机局域网地址（如 `http://192.168.1.20:8899/`）。

## 手机接入

1. 手机与电脑接同一 Wi-Fi。
2. 浏览器打开启动时打印的地址（Edge／Chrome 均可）。
3. 首次进页面后点“开始沉浸审阅”进入全屏（浏览器要求用户手势才能全屏）；底部可一键退出。
4. 若打不开：在 Windows 防火墙放行该 Python 进程或 8899 端口；确认路由器未开启“AP 隔离”。

**边界**：本工具不设访问令牌，仅供家庭／个人局域网内使用。不要在公共 Wi-Fi 或映射到公网的环境启动。

## 作答口径

- **✓（对勾）**：维持现状，通过；按钮只显示对勾符号，不出现“对勾”二字。
- **重拟**：交 AI 重拟，不填写内容（进入重拟清单）。
- **自定义**：当场写定新题（1—120 字），在条目内就地编辑，保存即生效。
- 备注可选（≤500 字）；支持清除作答（回待审）与撤销上一次（含整节一键通过的整批撤销）。
- **整节通过**：节标题行右侧，底部弹层二次确认后将该节全部小节置为对勾，可逐条改判；章级不提供。
- 筛选：待审／已改／已通过；可按卷·章·节定位；“继续上次”回到上次位置。
- 列表默认按目录顺序（不做风险排序），仅触控交互。

## 实时建议（重拟即取候选）

点“重拟”后在标签条里选好标签，按**获取建议**即把请求入队：

1. 页面每 1.5 秒轮询 `/api/suggest?id=…`，等待期间显示“已提交给 LLM 会话，等待返回建议… 已等 N 秒”，可随时取消（超过 5 分钟自动放弃）。
2. **Python 侧常驻轮询器**负责接件与投递（不依赖页面是否打开）：
   ```text
   C:\Python314\python.exe "05-卷册大纲\映射\title-review\3b-review\llm_bridge.py" --watch
   ```
   每 2 秒轮询一次：发现新请求即写入 `data/suggest/inbox.jsonl` 并打印 `[NEW]`；同时扫描 `data/suggest/outbox/*.json`，发现回执即投递并打印 `[SENT]`，投递后移入 `outbox/sent/`。心跳写 `data/suggest/watch.heartbeat`。
3. 主代理读收件箱、按标签生成候选，把回执写成 `outbox/<任意名>.json`（格式见下），轮询器在 2 秒内投递，页面随即展开候选（各附理由，可选“采纳”“改写后采纳”）。
4. 回填的候选同时写入 `data/candidates/llm-live.json`（`source` 标为 `llm-session`），刷新或重开也会重现；同一单元同一标签组合重复提交会自动去重。
5. 刷新页面时自动接回未完成的请求（`/api/suggest?pending=1`），不必重新点。

回执格式：

```json
[{"id": "s17938928582254f5a", "candidates": [
  {"candidate_id": "c1", "new_title": "……", "rationale": "……"},
  {"candidate_id": "c2", "new_title": "……", "rationale": "……"}]}]
```

一次性取件仍可用 `--list`／`--status`／`--result`。

**用法**：轮询器常驻后，您在手机上点“获取建议”，主代理侧读收件箱生成候选并写回执即可；在本会话发任意一句（如“处理”），主代理立即按收件箱回填。

## 配置上传

页面“配置”面板提供两个入口，均可导出复用（`3B-config-*.json`）：

- **参数配置**：`vol_start`／`vol_end`（1—75）、`daily_goal`（1—5000）、`theme`（`amoled｜day`）、`font_size`（`s｜m｜l`）、`labels`（三个选项文案，各 ≤8 字）、`only_flagged`（只看有异常徽标的条目）。
- **审阅清单**：`{"unit_keys": ["V07.03.02.01", …]}`，空数组＝全量。含第 76 卷或不存在的键会被整批拒绝并逐条报错。

生效后页面显示“当前作用域 x 条（原 23,722）”，可一键恢复全量；切换作用域不删除已作答数据。

## 数据与恢复

- 答案：`data/answers/answers.json`（原子写）；快照 `data/answers/snapshots/`，保留最近 10 份。
- 配置：`data/config/config.json`、`data/config/scope.json`。
- 候选：`data/candidates/<batch_id>.json`。
- 导出与归档：`data/exports/`（含 `archive_log.jsonl`）。
- 三层留存：浏览器 localStorage（即时）＋服务端（1.5 秒防抖）＋轮转快照；离线时继续作答，顶部显示“未同步 N 条”，服务恢复后自动重推。
- 导出：JSON（含轮次统计与 `source_hash`）、TSV（十列）、回写清单（十一列，供回写批直接消费）；“收工归档”把当日答案、TSV 与回写清单打包入带时间戳目录。

## 四阶段流程

1. **一审**（本工具）：逐条对勾／重拟／自定义；导出 JSON、TSV 与回写清单。
2. **AI 重拟批**（另批）：按“重拟待办”产出多候选，写 `data/candidates/<batch_id>.json` 并导入。
3. **二审**（本工具）：旧题与新题候选并列（各附理由），采纳（可改写）／保留旧题／再次重拟。
4. **回写批**（另批）：按回写清单改台账与 `outline.txt`，走门禁链并重批相关卷；落地后 Task 5 方可开工。

`source_hash` 对 `outline.txt` 与 75 份台账取 sha256；回写批须校验导出件指纹与当前源一致，防止审阅期间源漂移。

## 界面

- 主题：AMOLED 夜间（纯黑背景、绿色强调、正文浅灰白）与日间浅底绿；绿色只作强调，正文不用绿色。
- 分组浏览：卷下拉含“**全部卷**”（75 卷并列，逐卷可折叠，卷头显示该卷进度）；卷头、章头、节头均可点击收起／展开，折叠状态记在本机，刷新后保留；三级头均显示 `已判/总数 · 百分比`。
- 层级标识：卷、章、节头用绿色且字号依次递减（18／16／14px）；小节题名不用绿色（浅灰白，保持阅读字号）；节块左侧竖线＋缩进、小节卡再缩进一级，配合节卡与小节卡的编号（`1.1`／`1.1.1`）区分归属。
- 手机适配：针对 2400×1080／6.67 英寸 OLED（CSS 视口约 393×873）优化——工具栏底部固定（避开手势条）；按钮 44px、卡片内边距与间距按原版减半（一屏约 4—5 条）；`overscroll-behavior: none` 防过滚白边，横幅不设大面积亮块以降低烧屏风险。
- 字号三档：小/中/大；6.67 英寸高屏上题名为 19／21／24px，窄屏为 18／20／22px。
- 字体：霞鹜文楷屏幕阅读版（LXGW WenKai Screen，v1.530，SIL OFL 1.1），本地 woff2 子集（约 550 KB，2,538 码位），见 `web/fonts/README.md` 与 `web/fonts/OFL.txt`；不依赖外网 CDN。
- PWA：页面外壳、样式、脚本与字体可离线打开（Service Worker 缓存）。

## 测试

```text
C:\Python314\python.exe -m pytest "05-卷册大纲\映射\title-review\3b-review\tests" -q
C:\Python314\python.exe "05-卷册大纲\映射\title-review\3b-review\tests\e2e_playwright.py"
C:\Python314\python.exe "05-卷册大纲\映射\title-review\3b-review\tests\e2e_stage_resume.py"

# 有头（visible browser）模式
set E2E_HEADED=1
C:\Python314\python.exe "05-卷册大纲\映射\title-review\3b-review\tests\e2e_playwright.py"
C:\Python314\python.exe "05-卷册大纲\映射\title-review\3b-review\tests\e2e_stage_resume.py"
```

当前结果：pytest **57 passed**（`test_server.py` 30 例：75 卷逐卷对位、23,722 总数、V76 零单元、指纹、徽标、合并／清除、快照轮转、配置与清单、三种导出、归档、候选、重拟标签、TSV 转义与 JSON 保真、导入合并语义、导出排序、建议队列校验与去重、建议回填与幂等、空题拒绝、错误与未知 id；`test_mobile_layout.py` 27 例：媒体查询方向、底部固定工具栏、44px 触控、题名字号档位、末条遮挡、过滚抑制、对勾符号化、浅色主题、PWA manifest、平板不套用手机规则、三级绿色与字号递减、章／节折叠、全部卷筛选与卷级进度、节头吸顶）；E2E **16 passed / 0 skip**（含“实时建议轮询”）、暂存／续点／导入导出专项 **30 passed / 0 fail**（E2E 与专项均 headless 与 `E2E_HEADED=1` 有头各一轮）。有头随机 5% 抽测（1,186 条，seed 20261105）提交耗时 0.13 s，分布 720／300／166、TSV 1,187 行、回写清单 467 行、归档与界面进度均一致。

`e2e_stage_resume.py` 覆盖：Service Worker 接管、在线作答落库、localStorage 暂存与游标、停服后离线作答、离线刷新暂存不丢、起服自动重推、V07 续点与“继续上次”、JSON／TSV／回写清单三类导出的列序与内容保真（含逗号、弯引号、标签）、清库清缓存归零、导入回灌逐条全字段还原与重复导入幂等。

## 版本管理说明

根 `.gitignore` 的 `*.py` 规则本会使 `serve_3b_review.py` 与 `tests/*.py` 不入库；2026-11-05 ykla 明示批准后已强制纳入版本管理（提交 `9aa38e5a4`，提交说明含 `APPROVED-IGNORED` 放行标记）；`web/` 资产、字体与本文档亦在库。

## 文件

```text
serve_3b_review.py        本地服务（只读源台账，写 data/）
llm_bridge.py             会话侧取件／回填（--list／--status／--result）
web/index.html            单页外壳
web/app.css               主题、字号、卡片与安全区
web/app.js                作答、配置、导出、二审、离线队列
web/sw.js                 Service Worker 缓存
web/manifest.webmanifest  PWA 清单（全屏优先）
web/fonts/                霞鹜文楷子集、OFL 许可与说明
web/icons/                PWA 图标 192／512
tests/test_server.py      API 全量测试
tests/test_mobile_layout.py  手机适配静态单元测试
tests/e2e_playwright.py   移动视口端到端测试
tests/e2e_stage_resume.py 暂存／续点／导入导出专项测试
data/                     答案、配置、候选、导出（运行时生成）
```
