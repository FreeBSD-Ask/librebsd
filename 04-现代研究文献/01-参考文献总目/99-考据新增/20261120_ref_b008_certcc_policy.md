# ref-certcc-policy 登记卡（V61 b008 新登记：CERT/CC《Vulnerability Disclosure Policy》现行版）

- **来源**：CERT Coordination Center. Vulnerability Disclosure Policy[EB/OL]. [2026-11-20]. https://certcc.github.io/certcc_disclosure_policy/.
- **性质**：CERT 协调中心（CMU SEI）现行漏洞披露政策正式文本（45 天披露期限、例外条款、FAQ），official_doc 类。
- **取文途径**：certcc.github.io（CERT/CC GitHub Pages）经 curl 直取全文（28 742 字节，2026-11-20）。页面未标发布日期，著录省发布项。kb.cert.org/vuls/vpolicy/ 壳页（JS 渲染）与本页同文，取 GitHub Pages 载体。
- **四键查重**：source_url（certcc.github.io/certcc_disclosure_policy/，库内无命中）；题名"Vulnerability Disclosure Policy"命中 ref6160（旧式无 URL 登记：CERT/CC 2000 版 cert.org 政策，库内卡面无 URL 无引文池）——**同题名异版本披露**：本卡为 certcc.github.io 现行版（45 天条款），与 2000 版系政策演进非同文镜像，新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方政策文书）。
- **用途**：V61 b008（1.8.1 时序本身成为制度对象〔balance 句〕、1.8.2 惯例靠声誉而非强制维持〔45 天条款句〕、1.8.3 同步脱节让公开变成倒计时〔FAQ 句〕，三题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述政策页正文）

1. [1.8.2 用] Vulnerabilities reported to the CERT/CC will be disclosed to the public 45 days after the initial report, regardless of the existence or availability of patches or workarounds from affected vendors.

2. [1.8.1 用] It is the goal of this policy to balance the need of the public to be informed of security vulnerabilities with vendors' need for time to respond effectively. The final determination of a publication schedule will be based on the best interests of the community overall.

3. [1.8.3 用，政策页 FAQ] Vulnerabilities are routinely discovered and disclosed, frequently before vendors have had a fair opportunity to provide a fix, and disclosure often includes working exploits.

4. [备用（1.8.2 例外条款面），照录] Extenuating circumstances, such as active exploitation, threats of an especially serious (or trivial) nature, or situations that require changes to an established standard may result in earlier or later disclosure.

## b009 追加引文（2026-11-20，G7 全责线 supp-V61-b009 复用，异句异锚 J84）

5. [1.9.1 用] Vulnerabilities will be disclosed in Vulnerability Notes.

6. [1.9.2 用] Vulnerabilities reported to us will be forwarded to the affected vendors as soon as practical after we receive the report.

7. [1.9.3 用，FAQ 后半句] In our experience, if there is not responsible, qualified disclosure of vulnerability information then researchers, programmers, system administrators, and other IT professionals who discover vulnerabilities often feel they have no choice but to make the information public in an attempt to coerce vendors into addressing the problem.

8. [1.9.5 用] Disclosures made by the CERT/CC will include credit to the reporter unless otherwise requested by the reporter.

- **形态披露（b009）**：条目 5"Vulnerability Notes"系超链接元素（原 HTML `<a>Vulnerability Notes</a>.` 句号紧贴链接尾），引文按渲染形态取（剥离脚本会生句号前伪影空格，勿误录）。
