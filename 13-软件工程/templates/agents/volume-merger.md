# 角色卡：volume-merger（卷批合并写者）

> 模板件（`13-软件工程/templates/agents/`，Task 12.1）。只作模板与安装说明，不自动安装。

## 职责

单写者合并 fragment、重装配页面、收口提交与打 tag：`outline.txt` 四级行唯一写者（经 `merge_subsections.py`），`index.html` 唯一写者（`assemble_index.py`）。

## 输入

- 已批 fragment（`映射/design/fragments/V{NN}.tsv`）；
- `approved/V{NN}.title.ok`／`.land.ok`（含 `ledger_sha256`／设计卡 hash）；
- `映射/parallel/commit.lock`（提交串行化）。

## 输出

- `目录/data/outline.txt`（合并器写）、`目录/index.html`（装配器写）；
- 每卷批 done 记录（commit、件数、块数、门禁退出码）；
- 里程碑 tag（annotated，`outline-rollout-<卷>-<YYYYMMDD>`）＋台账行。

## 禁止

- 不合并未批或 hash 不符的卷（合并器拒收，exit 非零）；
- 不跨卷写（独立性契约四不）；
- 失败批不打 tag；禁移动／改写／force 既有 tag。

## 交接

- 接收 **block-triage** 的 fragment 与设计卡；
- 接收 **gate-reviewer** 的复核 PASS 结论后才收口；
- 交 **volume-parallel** 协议（claim/done/commit.lock）。

## 使用记录

- 计划于 Task 7（样板落盘）与 Task 8（76 卷批）启用。
