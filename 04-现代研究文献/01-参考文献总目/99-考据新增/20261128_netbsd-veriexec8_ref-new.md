# 卡片草稿：NetBSD veriexec(8) 文件完整性子系统

- 题名：veriexec(8) — file integrity subsystem
- 作者／机构：Elad Efrat（NetBSD Project）
- 出版者／站点：man.netbsd.org（NetBSD Manual Pages）
- 出版年：2017（页脚 NetBSD 11.99 September 13, 2017）
- URL：https://man.netbsd.org/veriexec.8
- 引用格式（GB/T 7714-2015）：NetBSD Project. veriexec(8) — file integrity subsystem[EB/OL]. NetBSD-current, 2017-09-13. https://man.netbsd.org/veriexec.8 [2026-11-28].
- 引文摘录："Veriexec is an in-kernel, real-time, file-system independent, file integrity subsystem. It can be used for a variety of purposes, including defense against trojaned binaries, indirect attacks via third-party remote file-systems, and malicious configuration file corruption."
- 引文摘录二："The only level at which the fingerprint tables can be modified, this level is used to help fine-tune the signature database."
- 引文摘录三："Veriexec requires a signatures database -- a list of monitored files, along with their digital fingerprint and (optionally) access modes."
- 备注：页载 strict 四级（0 Learning／1 IDS／2 IPS／3 Lockdown）；快照由 tvly extract 取得，正文完整（CONFIGURATION／STRICT LEVELS／RUNTIME INFORMATION 各节齐）。本批 2.9.1／2.9.3／2.9.5 三题引文出自该页。
