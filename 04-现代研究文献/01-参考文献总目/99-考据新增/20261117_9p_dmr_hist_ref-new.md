# ref 新建卡：Ritchie《The Evolution of the UNIX Time-sharing System》（9p.io dmr 页）

- 著录：Ritchie D M. The Evolution of the UNIX Time-sharing System[Z/OL]. Murray Hill: Bell Laboratories, 1979[2026-11-17]. https://9p.io/who/dmr/hist.html.
- URL: https://9p.io/who/dmr/hist.html
- 取证：2026-11-17 curl 直取 HTML（45,354 B，`/tmp/v08b001/hist.html`），剥标签取正文，引文由正文程序化切片。
- 证据等级判定：L2“学术记载”（tier=primary，source_type=academic_work）——当事 Ritchie 1979 年史述（后正式发表），与 ref1575（McKusick 回顾章，同型 L2）口径一致；fh=1／ct=0／retro=1。
- 逐字引文（两段，分属两题）：

  Pipes appeared in Unix in 1972, well after the PDP-11 version of the system was in operation, at the suggestion (or perhaps insistence) of M. D. McIlroy, a long-time advocate of the non-hierarchical control flow that characterizes coroutines.

  Perhaps the most important watershed occurred during 1973, when the operating system kernel was rewritten in C. It was at this point that the system assumed its modern form; the most far-reaching change was the introduction of multi-programming.

- 卡内说明：
  - 同页另有 “I believe I contributed the idea of device files.” 与 “Special files describing devices.” 等统一接口史述，本批只取上两段；2.4.4（统一接口的覆盖范围）需两独立来源，其 CACM74 第二腿留 b002（TUHS 仅有扫描件，无排印本可逐字引）。
  - 9p.io 为 dmr 页现行载体；9p.io/who/dmr/cacm74.html 不存在（404 实测），CM-Bell 镜像域名不解析——披露于批记。
  - 用途：V08.1.5.1（pipe 1972 年 McIlroy 建议句）与 V08.6.3.1（1973 watershed 句）第二源。
