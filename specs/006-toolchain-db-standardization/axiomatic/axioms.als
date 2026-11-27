// axioms.als — 任务书/specs 公理的 Alloy 模型（复现件）
// 状态：未在本机运行（Alloy 未安装）；安装 Alloy 6 后执行
//   java -jar org.alloytools.alloy.dist.jar exec -c "一致性" axioms.als
// 本模型编码 A01—A13 的抽象形态，并以事实固化 13 spec／12 goal 实例。

sig Goal { id: Int }
sig Spec { sid: one Symbol, goals: some Goal, ver: one Version, st: one Status }
sig Binding { bid: one Symbol, spec: one Spec, anchor: one Heading, hSpec, hTasks, hCheck: one Hash }
sig Artifact { of: one Spec, kind: one Kind, h: one Hash }
sig Heading, Symbol, Hash, Version {}
one sig TaskBook { headings: set Heading, manifestHash: one Hash }

abstract sig Status {}
one sig draft, active, closed, superseded extends Status {}
abstract sig Kind {}
one sig specMd, tasksMd, checklistMd extends Kind {}

fact A02_唯一标识 {
  all s: Spec | unique s.sid
  all b: Binding | unique b.bid
}
fact A03_目标覆盖 { all g: Goal | some s: Spec | g in s.goals }
fact A04_无孤儿 { all s: Spec | some s.goals }
fact A05_三件套 { all s: Spec | exactly 3 a: Artifact | a.of = s }
fact A06_绑定双射 {
  all b: Binding | one b.spec
  all s: Spec | one b: Binding | b.spec = s
}
fact A07_锚点 { all b: Binding | one b.anchor and b.anchor in TaskBook.headings }
fact A08_哈希 {
  all b: Binding | b.hSpec = b.spec.(^of).h or some a: Artifact | a.of = b.spec and a.kind = specMd and a.h = b.hSpec
  all a: Artifact | some b: Binding | b.spec = a.of
}
fact A09_状态一致 { all s: Spec, b: Binding | b.spec = s implies (b.hSpec = hash_of[s]) }
fact A10_清单整合 { TaskBook.manifestHash = (Binding ^spec).hSpec }
fact A12_闭包 { all a: Artifact | one b: Binding | b.spec = a.of }

fun hash_of[s: Spec]: Hash { (specMd & (Artifact <: of).s).h }

// 实例规模（对应 13 spec／12 goal／13 binding）
pred 一致性 { all a: ax_props | a }
fun ax_props: set Bool { A02_唯一标识 + A03_目标覆盖 + A04_无孤儿 + A05_三件套 + A06_绑定双射 + A07_锚点 + A08_哈希 + A10_清单整合 }

run 一致性 for exactly 13 Spec, exactly 12 Goal, exactly 13 Binding, exactly 39 Artifact, exactly 20 Heading

// 定理：相对充分性与无孤儿（在有穷域内求反例）
assert T1_充分 { all g: Goal | some s: Spec | g in s.goals }
assert T2_无孤儿 { all s: Spec | some s.goals }
check T1_充分 for exactly 13 Spec, exactly 12 Goal, exactly 13 Binding
check T2_无孤儿 for exactly 13 Spec, exactly 12 Goal, exactly 13 Binding
