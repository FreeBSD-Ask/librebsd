# V1-Ch7-新增：McIlroy 组件化——"Do One Thing Well" 作为哲学的工程转译

#### 要点

Doug McIlroy 在 1964 年的内部备忘录中提出组件化软件设计思想，这一思想在 1978 年 Bell System Technical Journal 特刊中被系统化为 "do one thing and do it well" 原则。McIlroy 并非从底层推导出组件化——他首先观察到数学证明中的抽象隔离（一个引理只证明一个结论），然后将这种抽象隔离类比到软件工程领域。这正是 §15 技术哲学中指出的 “计算程序只有三个结构（循环、顺序、选择）” 的工程前身——组件化不是技术发明而是哲学转译：将形式主义化的数学抽象结构（逻辑域）移植到贝尔实验室的工程实践（经验域）。McIlroy 明确提出 "Write programs that do one thing and do it well. Write programs to work together"——管道（pipe）机制是此原则的最纯粹技术实现：一个程序的标准输出直接成为另一个程序的标准输入，不同程序通过文本流耦合而非代码耦合。

从 §14 文化哲学视角分析，McIlroy 的组件化不仅仅是工程方法，更是 UNIX 文化的形而上学基础。当 Ken Thompson 在 PDP-7 上实现管道时（1973 年），他将数学抽象转译为机械操作——按下 `|` 键即建立两个进程之间的数据通道。这一动作的文化后果远超出工程范畴：管道使 “小而专的工具” 成为一种社群共识而非个人偏好。任何违反组件化的程序（如 monolithic 工具）被视为 “不 UNIX”，这种审美判断掩盖了其底层机制——组件化不是 “自然” 的设计哲学，而是 McIlroy 等人在特定历史阶段的形式主义建构。

#### 史料

- McIlroy D M. "Internal Bell Labs memo on component programming"（1964），未公开发表，McIlroy 本人在 1978 年 BSTJ 中引用。
- McIlroy M D, Pinson E N, Tague B A. "UNIX Time-Sharing System: Foreword" [J]. *Bell System Technical Journal*, 1978, 57(6): 1899-1904.
- Ritchie D M. "The Evolution of the UNIX Time-Sharing System" [C]. *Language Design and Programming Methodology*, Springer LNCS 79, 1980: 25-35——Ritchie 确认管道由 McIlroy 概念化、Thompson 实现。
- Kernighan B W, Pike R. *The UNIX Programming Environment* [M]. Englewood Cliffs: Prentice Hall, 1984——第 1 章首次系统化阐述管道与过滤器的工程哲学。
- Raymond E S. *The Art of UNIX Programming* [M]. Boston: Addison-Wesley, 2003——第 1 章将 McIlroy 列为 UNIX 哲学第一准则。

#### 史观

**总纲 15（文化即形式主义）**——管道机制在 UNIX 社群中被内化为“理所当然”的自然法则，但这一“自然性”是形式主义的建构：管道使文本流成为组件间的唯一耦合方式，二元数据格式（如二进制协议）被排除在这种耦合之外。Linux、BSD、Windows PowerShell 各自以不同方式继承或改造 McIlroy 的组件化方案——每一次继承都是“传统”的形式主义化重构（7.2 节）。

**总纲 12（科学是形式主义）**——McIlroy 在 1964 年备忘录中将数学证明的抽象隔离类比到软件工程，这一类比本身是认识形式主义：数学证明的严格抽象（理想化的形式主义结构）与工程实践的经验耦合（现实中的进程通信开销）之间存在不可逾越的鸿沟。管道不是 “正确的工程”，而是 “可操作的形式主义”。

**自反性声明**：本子节将 McIlroy 的组件化叙述为 “哲学向工程的转译”——但 “哲学” 与 “工程” 之区分本身就是形式主义。McIlroy 并非自觉地进行哲学思辨；"do one thing well" 可能只是他对 AT&T 内部巨型程序（如 Multics）混乱现状的实操反应。本子节承认编史学解读的建构性质。

#### 辨析

**McIlroy 贡献与 Thompson 实现的区分**：部分二手文献将管道发明的全部功劳归于 Thompson。考据结论：管道概念由 McIlroy 在 1964 年提出，Thompson 在 1973 年实现 UNIX 管道系统调用与 shell 语法（`|`）。二者不可混淆——McIlroy 提供抽象模型（形式），Thompson 提供具体实现（实例）。

**"Do one thing well" 的神圣化辨析**：ESR 在 *The Art of UNIX Programming*（2003）中将 "do one thing well" 提升为 UNIX 第一原则，但 McIlroy 原始措辞中不存在 “神圣法则” 意涵。ESR 将工程建议建构为哲学信条——从经验准则到形而上学教条的转变是解释学循环（§25）的典型案例：前理解决定了释读的方向与结论。

#### 文献

[1] McIlroy M D, Pinson E N, Tague B A. UNIX Time-Sharing System: Foreword [J]. Bell System Technical Journal, 1978, 57(6): 1899-1904.

[2] Ritchie D M. The Evolution of the UNIX Time-Sharing System [C]. Language Design and Programming Methodology, Springer LNCS 79, 1980: 25-35.

[3] Kernighan B W, Pike R. The UNIX Programming Environment [M]. Englewood Cliffs: Prentice Hall, 1984.

[4] Raymond, E S. The Art of UNIX Programming [M]. Boston: Addison-Wesley, 2003.

---

