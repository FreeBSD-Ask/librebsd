# 卡片草稿：FreeBSD mitigations(7)

- 题名：mitigations(7) — FreeBSD Security Vulnerability Mitigations
- 作者／机构：FreeBSD Project
- 出版者／站点：man.freebsd.org（FreeBSD 15.1 man 页）
- 出版年：2025（页脚 January 29, 2025）
- URL：https://man.freebsd.org/cgi/man.cgi?query=mitigations&sektion=7&format=ascii
- 引用格式（GB/T 7714-2015）：FreeBSD Project. mitigations(7): FreeBSD security vulnerability mitigations[EB/OL]. FreeBSD 15.1, 2025-01-29. https://man.freebsd.org/cgi/man.cgi?query=mitigations&sektion=7&format=ascii [2026-11-27].
- 引文摘录："When enabled in combination with RELRO (which is enabled by default) this provides full RELRO. The entire GOT (.got and .got.plt) are made read-only at program startup, preventing attacks on the relocation table. Note that this results in a nonstandard Application Binary Interface (ABI), and it is possible that some applications may not function correctly."
- 备注：以 man CGI 的 ascii 格式抽取纯文本；同页另载 ASLR 的全局 sysctl 与 proccontrol(1) 按进程控制、W^X 的 allow_wx 开关、SSP 的栈帧哨兵说明，可作同节其他题的交叉参照。roff 断词在引文区段之外，引文本身无断词。
