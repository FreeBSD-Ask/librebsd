# 插件模板包：librebsd-outline-roles

> 模板件（`13-软件工程/templates/qoder-plugin/`，Task 12.3）。**只作模板与安装说明，不自动安装、不入根目录**（ykla 2026-10-29 裁定；`plugin.json` 的 `install.manual_only=true` 固化该语义）。

## 包内容

| 类型 | 件 | 用途 |
| ---- | ---- | ---- |
| 角色卡 | `../agents/title-designer.md` | 四源合成拟题与题名自检 |
| 角色卡 | `../agents/block-triage.md` | 史料块逐块判读归属与 J4 处置 |
| 角色卡 | `../agents/gate-reviewer.md` | 门禁独立复核与 FAIL 清单 |
| 角色卡 | `../agents/volume-merger.md` | 单写者合并、重装配、收口与 tag |
| 技能 | `../skills/four-source-title.md` | 四源合成流程（触发：标题线开工） |
| 技能 | `../skills/gate-runner.md` | 门禁执行回路（触发：批收口／编辑后） |
| 技能 | `../skills/milestone-tag.md` | 里程碑打点（触发：里程碑收口） |
| 技能 | `../skills/volume-parallel.md` | 按卷并行协议（触发：卷批开工） |

## 使用映射（Task 12.6）

| 任务 | 角色 | 技能 |
| ---- | ---- | ---- |
| Task 3A 标题设计 | `title-designer` | `four-source-title` |
| Task 6／8 块研读与门禁 | `block-triage`＋`gate-runner`（技能） | `gate-runner` |
| Task 7／8 合并与收口 | `volume-merger` | `milestone-tag` |
| Task 1／2／3A／8 卷批开工 | — | `volume-parallel` |
| Task 6.9／10 独立复核 | `gate-reviewer` | — |

## 复用说明

复制到其他项目时：保留本 README 与各件"模板件"抬头；按宿主平台的智能体／技能定义格式转换后手工装载；本项目不安装。
