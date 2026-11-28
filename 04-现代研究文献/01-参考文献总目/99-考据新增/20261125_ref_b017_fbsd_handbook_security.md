# ref-fbsd-handbook-security-rl 登记卡（V61 b017 新登记：FreeBSD Handbook 第 16.14 节《Resource Limits》）

- **来源**：The FreeBSD Project. Resource Limits[EB/OL]. FreeBSD Handbook, §16.14[2026-11-25]. https://docs.freebsd.org/en/books/handbook/security/.
- **性质**：FreeBSD 官方手册资源限制节（限制的目的与作用、登录类传统法、rctl 细粒度法、资源类型表），official_doc 类。
- **取文途径**：docs.freebsd.org 经 curl 直取 Handbook Security 章全文（201 076 字节 HTML，剥标签后 1489 行，2026-11-25）；§16.14 起于剥标签文本 “16.14. Resource Limits”。
- **四键查重**：source_url（docs.freebsd.org/en/books/handbook/security/，references 表无命中）；题名（references 表无 Handbook 资源限制节卡片）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b017（2.6.1 类授予、2.6.2 粒度扩展、2.6.5 限制的作用目标）。

## 逐字引文池（取自 §16.14 正文；空白归一照录）

1. [2.6.1 用] Each user account can be assigned to a login class, where default is the default login class.
2. [2.6.2 用] This command supports more than user limits as it can also be used to set resource constraints on processes and jails.
3. [2.6.5 用] These limits are designed to prevent a single process or user from consuming an excessive amount of resources, which could lead to performance degradation or system instability.

- 原页 §16.14 首段另有定义句（“resource limits refer to the mechanisms that control and manage the allocation of various system resources to processes and users”）；剥标签时 `/etc/login.conf` 后残留一个空格（HTML 标签边界），故 2.6.1 引文改取同节无标签干扰的句式。引文三条均无弯引号或特殊符号。
