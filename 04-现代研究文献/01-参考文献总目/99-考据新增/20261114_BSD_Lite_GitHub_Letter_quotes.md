# 4.4BSD-Lite 发行信原文（GitHub BSD-Lite 归档页转载）引文卡

- **著录（GB/T 7714-2015）**：CSRG. 4.4BSD-Lite Release Letter（1994-03）[EB/OL]. 0x16000/BSD-Lite 归档页转载[2026-11-14]. https://github.com/0x16000/BSD-Lite.（库内 ref 6201）
- **来源 URL**：https://github.com/0x16000/BSD-Lite
- **访问日期**：2026-11-14
- **用途**：Task 8.2 G3-V24 P2 b004（清单著录／源码树重组／已知局限披露／信体分区）

## 逐字引文

Q1（纯源码发行）:
The distribution is a source distribution only, and
does not contain program binaries for any architecture.

Q2（内容构成）:
It includes source code and manual pages
for the C library, approximately 90% of the utilities dis-
tributed as part of 4.4BSD, and most of the kernel

Q3（内核源码按架构归目录）:
The kernel sources have been reorganized to collect all
machine-dependent files for each architecture under one
directory, and most of the machine-independent code is now
free of code conditional on specific machines.

Q4（x86 已知不稳）:
More specifi-
cally, the support for the x86 architectures is known to be
unstable.

Q5（验证套件未跑）:
We have not run it through any of the verification test suites, thus, you
should not claim conformance with either standard without
first validating the code.

Q6（手册随版重写并自注失真）:
almost
the entire manual suite has been rewritten to reflect the
POSIX defined interfaces, and in some instances it does not
correctly reflect the current state of the software.

Q7（发行信分区标题）:
Distribution contents

Q8（分区标题二）:
How to obtain 4.4BSD-Lite

Q9（分区标题三）:
Special Cases

Q10（分区标题四）:
A Special Note

Q11（1994-03 公告语）:
We are delighted, at long last, to send you information
about our March 1994 release of 4.4BSD-Lite.
