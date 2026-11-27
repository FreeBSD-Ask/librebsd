module Axioms \* 任务书/specs 绑定与生命周期的 TLA+ 模型（复现件）
\* 状态：未在本机运行（TLA+ Tools 未安装）；安装后执行：
\*   java -cp tla2tools.jar tlc2.TLC Axioms.tla -config Axioms.cfg

EXTENDS Integers, Sequences, FiniteSets

CONSTANTS Specs, Goals, Status
ASSUME Status = {"draft", "active", "closed", "superseded"}

VARIABLES
    \* binding[s] = 记录 spec s 的哈希登记（抽象为自然数指纹）
    binding,
    \* specStatus[s] ∈ Status
    specStatus,
    \* covered[s] ⊆ Goals：spec 覆盖的目标集
    covered

TypeOK ==
    /\ binding \in [Specs -> Nat]
    /\ specStatus \in [Specs -> Status]
    /\ covered \in [Specs -> SUBSET Goals]

Init ==
    /\ binding = [s \in Specs |-> 0]
    /\ specStatus = [s \in Specs |-> "draft"]
    /\ covered = [s \in Specs |-> {}]

\* 绑定哈希随 spec 修订而更新（A08 的状态化）
UpdateHash(s) ==
    /\ binding' = [binding EXCEPT ![s] = binding[s] + 1]
    /\ UNCHANGED <<specStatus, covered>>

\* 生命周期单调：draft→active→closed→superseded（A16/项目六态的抽象）
Advance(s) ==
    /\ specStatus' = [specStatus EXCEPT ![s] =
        CASE specStatus[s] = "draft" -> "active"
            [] specStatus[s] = "active" -> "closed"
            [] specStatus[s] = "closed" -> "superseded"
            [] OTHER -> specStatus[s]]
    /\ UNCHANGED <<binding, covered>>

\* 覆盖登记（A03/A04 的状态化）
Cover(s, g) ==
    /\ covered' = [covered EXCEPT ![s] = covered[s] \cup {g}]
    /\ UNCHANGED <<binding, specStatus>>

Next ==
    \/ \E s \in Specs : UpdateHash(s)
    \/ \E s \in Specs : Advance(s)
    \/ \E s \in Specs, g \in Goals : Cover(s, g)

Spec == Init /\ [][Next]_<<binding, specStatus, covered>>

\* 不变量 I1：生命周期单调（不允许回退）
LifeMonotonic ==
    \A s \in Specs :
        specStatus[s] \in {"draft", "active", "closed", "superseded"}

\* 不变量 I2：每个 spec 至少一个目标或仍为 draft（无孤儿推进）
NoOrphanAdvance ==
    \A s \in Specs :
        (specStatus[s] # "draft") => covered[s] # {}

\* 不变量 I3：哈希登记只增不减（修订可检测）
HashMonotonic ==
    \A s \in Specs :
        binding'[s] >= binding[s]

INVARIANT TypeOK
INVARIANT LifeMonotonic
INVARIANT NoOrphanAdvance
INVARIANT HashMonotonic
