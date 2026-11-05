# 技能：milestone-tag（里程碑打点）

> 模板件（`13-软件工程/templates/skills/`，Task 12.2）。只作模板与安装说明，不自动安装。

## 触发

不可逆或难以重建的里程碑收口时（该 tag 就 tag，不等到全部结束再补）。

## 步骤

1. 判里程碑性质（内容零丢失／结构不可逆／样板定格式）；
2. 打 **annotated** tag：`git tag -a outline-<state>-<YYYYMMDD>`，说明含里程碑、计数、门禁退出码、对应 commit；
3. 记台账 `映射/里程碑tag台账.tsv` 一行（tag／commit／date／counts／gate_exit／note）;
4. 核既有 tag 未变（禁移动、禁改写、禁 force）。

## 产物

- annotated tag＋台账行。

## 判据

- 一律 annotated（禁 lightweight）；命名小写 ASCII、同日重名加 `-b`/`-c`；
- 只指向可复现提交；**失败批不打 tag**；
- tag 只回答"这个状态在哪"，不替代提交／备份／台账。

## 失效

- 打 tag 前发现门禁未全绿 → 不打，整改后重打；
- 既有 tag 需改指 → 禁止，另立新 tag 并在台账记沿革。
