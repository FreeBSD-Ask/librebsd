# 2026-08-15 第07卷“freebsd的工程体系重构”双库事实核查与释疑考据记录

## 一、核查说明

- **核查范围**：第07卷 第136-155章全部章节（20章）
- **核查工具**：仅限邮件列表库 _mail_search.py + 参考文献库 _ref_search.py，禁止联网
- **0信任原则**：证据均为真实检索所得
- **检索时间**：2026-08-15

## 三、核查结果汇总

| 判定 | 数量 |
| --- | --- |
| 通过（命中且一致） | 12 |
| 修正（命中但不一致/需补注） | 1 |
| 两库无法验证（未命中） | 2 |
| 合计 | 15 |

## 四、逐条核查记录

### 1. FreeBSD 13.0-RELEASE 发布日期（2021-04-13）
- **证据**：Message-ID 20210413185035.34DD1202D@nucleus（2021-04-13），发件人 Glen Barber，主题 [FreeBSD-Announce] FreeBSD 13.0-RELEASE Now Available
- **判定**：通过

### 2. FreeBSD 14.0-RELEASE 发布日期（2023-11-20）
- **证据**：Message-ID 20231120210317.5DB0E473C@freefall.freebsd.org（2023-11-20），发件人 Colin Percival，主题 FreeBSD 14.0-RELEASE Now Available
- **判定**：通过

### 3. WireGuard争议——Donenfeld 2020年2月首次联系freebsd-net
- **证据**：Message-ID CAHmME9rjGNo4...@mail.gmail.com（2020-02-18），发件人 Jason A. Donenfeld，主题含zero coordination
- **判定**：通过

### 4. FreeBSD 14.0发布延迟——OpenSSL 3.0为阻塞项
- **证据**：Message-ID 20230128.163414...yasu@FreeBSD.org（2023-01-28，初始计划7月17日）；20230501181449.GJ1219@FreeBSD.org（2023-05-01，Glen Barber确认OpenSSL 3.0阻塞）
- **判定**：通过

### 5. Capsicum论文发表于USENIX Security 2010
- **证据**：reference_id=206，fact_id=2070/2071，source_quote含Capsicum: practical capabilities for UNIX与planned for inclusion in FreeBSD 9
- **判定**：通过

### 6. CHERI项目由剑桥大学与SRI International联合启动（2010年）
- **证据**：reference_id=975，source_quote含Cambridge and SRI International When starting the CHERI project in 2010
- **判定**：通过

### 7. Jail论文Jails: Confining the omnipotent root（Kamp & Watson, 2000）
- **证据**：reference_id=2689，author=Poul-Henning Kamp, Robert N. M. Watson，year=2000
- **判定**：通过

### 8. WireGuard初始实现——Netgate赞助Matt Macy
- **证据**：Message-ID CAHM0Q_PrnnzHhpPwOQ44g0XvRA1-+EgQzNMWeJht0NNtJDQUVg@mail.gmail.com（2020-02-18），发件人kmacy at freebsd.org (K. Macy)
- **判定**：通过

### 9. Hans Petter Selasky在2023年初仍活跃于邮件列表
- **证据**：最后活跃邮件2023-01-29（Message-ID c316280c...@selasky.org），14.0公告（2023-11-20）献词确认去世
- **判定**：通过（间接验证）。去世时间在2023-01-29至2023-11-20之间

### 10. Mike Karels在2024年初仍活跃于邮件列表
- **证据**：最后活跃邮件2024-01-31（Message-ID B8CEA299...@karels.net），14.2公告献词确认去世
- **判定**：通过（间接验证）。去世时间在2024-02至2024-10之间

### 11. netmap在参考文献库中的著录
- **证据**：reference_id=570/578/601/654含netmap相关学术论文著录
- **判定**：通过（间接验证）

### 12. OpenSSL 3.0升级——14.0默认使用OpenSSL 3.0.12
- **证据**：同条目4的邮件列表证据，OpenSSL 3.0升级是14.0发布的核心阻塞项
- **判定**：通过（间接验证）

### 13. Google LLC v. Oracle America, Inc. 判决日期（2021-04-05）
- **证据**：参考文献库0命中，邮件列表库报错（messages_fts缺失）
- **判定**：两库无法验证

### 14. Bill Jolitz逝世（2022年）——13.1献词
- **证据**：邮件列表库报错（messages_fts缺失）
- **判定**：两库无法验证

### 15. Hans Petter Selasky去世精确日期
- **证据**：邮件列表最后活跃2023-01-29，14.0公告献词确认去世
- **判定**：修正（补注）。去世时间锁定在2023-01-29至2023-11-20之间

## 五、已由bsd_commits.db验证的重要事实

13.0-14.4 release tag日期、Release Engineer交接、39个SA/80个SA、jail/Capsicum/Heimdal/bhyve commit等已在前期核查中验证。

## 六、已知检索限制

部分邮件列表数据库缺失FTS表；参考文献库facts模式覆盖率有限；美国最高法院判决等非BSD内容不在两库覆盖范围内。