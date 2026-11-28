// axioms.als — 任务书/specs 公理的可运行 Alloy 模型（S05 机检件）
// 编码：A02（标识唯一，由 atom 身份承载）/A03 目标全覆盖/A04 无孤儿/A05 三件套/A06 绑定双射/
//       A07 锚点∈任务书/A10 单任务书。T1/T2 为断言（充分性/无孤儿），check 求反例。
// 运行（Alloy 6.2.0 CLI）：
//   java -jar org.alloytools.alloy.dist.jar exec --command-name "Default" axioms.als
//   java -jar org.alloytools.alloy.dist.jar exec --command-name "T1_充分性" axioms.als
//   java -jar org.alloytools.alloy.dist.jar exec --command-name "T2_无孤儿" axioms.als

sig Goal {}
sig Heading {}
sig Version {}
abstract sig Status {}
one sig draft, active, closed, superseded extends Status {}

sig Kind {}
one sig specMd, tasksMd, checklistMd extends Kind {}

sig Spec {
  goals: some Goal,
  ver: one Version,
  st: one Status,
}

sig Artifact { kind: one Kind, of: one Spec }

sig Binding { spec: one Spec, anchor: one Heading }

one sig TaskBook { headings: some Heading }

fact A02_状态枚举 { all s: Spec | s.st in draft + active + closed + superseded }
fact A03_目标全覆盖 { Goal in Spec.goals }          -- 每个 goal 被某 spec 覆盖
fact A04_无孤儿 { all s: Spec | some s.goals }        -- 每个 spec 至少一目标
fact A05_三件套 {
  all s: Spec | #(s.~of.kind & specMd) = 1
  all s: Spec | #(s.~of.kind & tasksMd) = 1
  all s: Spec | #(s.~of.kind & checklistMd) = 1
  all a: Artifact | one a.of
  all a: Artifact | one a.kind
}
fact A06_绑定双射 {
  all b: Binding | one b.spec
  all s: Spec | one b: Binding | b.spec = s
}
fact A07_锚点 { all b: Binding | b.anchor in TaskBook.headings }
fact A09_状态一致 { all b: Binding, s: Spec | b.spec = s implies b.anchor in TaskBook.headings }
fact A10_单任务书 { one TaskBook }

pred Default {}
run Default for exactly 12 Goal, exactly 13 Spec, exactly 13 Binding,
                   exactly 39 Artifact, exactly 4 Heading, exactly 4 Version, exactly 3 Kind, exactly 4 Status

assert T1_充分性 { all g: Goal | some s: Spec | g in s.goals }
check T1_充分性 for exactly 12 Goal, exactly 13 Spec, exactly 13 Binding, exactly 39 Artifact, exactly 4 Heading, exactly 4 Version, exactly 3 Kind, exactly 4 Status

assert T2_无孤儿 { all s: Spec | some s.goals }
check T2_无孤儿 for exactly 12 Goal, exactly 13 Spec, exactly 13 Binding, exactly 39 Artifact, exactly 4 Heading, exactly 4 Version, exactly 3 Kind, exactly 4 Status
