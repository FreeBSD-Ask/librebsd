# ref-nvd-general-page 登记卡（V61 b010 新登记：NIST NVD《General Information》页）

- **来源**：National Institute of Standards and Technology. NVD General Information[EB/OL]. (2022-09-20/2024-06-27)[2026-11-21]. https://nvd.nist.gov/general.
- **性质**：NVD 官方 General 页（政府 repository 定位、对 CVE List 的 enrichment 承接、聚合字段自述），official_doc 类。
- **取文途径**：nvd.nist.gov 经 web_reader 通道实取全文（2026-11-21；curl/WebFetch 被 Cloudflare 拦，web_reader 放行）。页面标注 Created September 20, 2022, Updated June 27, 2024。
- **四键查重**：source_url（nvd.nist.gov/general，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（美国政府官方数据库自述）。
- **用途**：V61 b010（1.10.3 字段缺省削弱可检索性〔聚合字段自述句〕、1.10.4 映射误差〔enrichment 承接句〕、1.10.5 计数口径受收录策略影响〔政府 repository 定位句〕，三题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述页面正文；web_reader 转写形态）

1. [1.10.4 用] The NVD performs enrichment on CVEs that have been published to the CVE List.

2. [1.10.3 用] NVD staff are tasked with enrichment of CVEs by aggregating data points from the description, references supplied and any supplemental data that can be found publicly at the time.

3. [1.10.5 用] The NVD is the U.S. government repository of standards based vulnerability management data represented using the Security Content Automation Protocol (SCAP).

4. [备用（属性变更面），照录] As additional information becomes available CVSS assessments, CWEs, and applicability statements are subject to change.
