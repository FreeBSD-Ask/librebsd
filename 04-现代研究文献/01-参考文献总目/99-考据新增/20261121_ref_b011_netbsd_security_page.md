# ref-netbsd-security-page 登记卡（V61 b011 新登记：The NetBSD Project《NetBSD Security》页）

- **来源**：The NetBSD Project. NetBSD Security[EB/OL]. [2026-11-21]. https://www.netbsd.org/security/.
- **性质**：NetBSD 官方安全页（三组分工、advisory 发布机制与多渠道、跨发行版沟通延迟说明），official_doc 类。
- **取文途径**：netbsd.org/security/ 经 curl 直取全文（17 089 字节，2026-11-21）。
- **四键查重**：source_url（netbsd.org/security/，库内无命中）；题名"NetBSD Security"（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（项目官方页自述）。
- **用途**：V61 b011（1.11.1 公告从事件应对转为按期发布〔advisory 发布机制三连句〕、1.11.2 职责边界写进流程文本〔三组分工句〕、1.11.5 惯例扩散快于机制移植〔跨发行版沟通句〕，三题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述页面正文；HTML 剥离后空白归一取连续句）

1. [1.11.1 用] When serious security problems in NetBSD are discovered and corrected, we issue a security advisory, describing the problem and containing a pointer to the fix. These are announced to our netbsd-announce mailing list and our security-announce mailing list as well as to various other mailing lists and websites. In addition, they are archived on this site as well as provided as an RSS feed.

2. [1.11.2 用] Security issues in NetBSD are handled by three groups: the Security Team, the Security Alert Team, and the Security Officer. These groups investigate, document and update code in response to newly reported security issues.

3. [1.11.5 用] Communication with vendors and other distributions shipping the same code may also cause these delays.
   - **回指披露（b011）**："these delays" 回指前句（the security team may delay the release of a Security Advisory, so that one unique, comprehensive Security Advisory covering several vulnerabilities can be issued）；本句独立完整，回指对象已在前句、块内 fact 说明。

4. [备用（多漏洞合并公告面），照录] the security team may delay the release of a Security Advisory, so that one unique, comprehensive Security Advisory covering several vulnerabilities can be issued
