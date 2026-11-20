# ref-nvd-vuln-page 登记卡（V61 b010 新登记：NIST NVD《Vulnerabilities》页）

- **来源**：National Institute of Standards and Technology. Vulnerabilities: National Vulnerability Database[EB/OL]. (2022-09-20/2023-08-03)[2026-11-21]. https://nvd.nist.gov/vuln.
- **性质**：NVD 官方 Vulnerabilities 页（CVE 标识覆盖声明、CVE 唯一标识使命转述、CNA Rules 指引链接），official_doc 类。
- **取文途径**：nvd.nist.gov 经 web_reader 通道实取全文（2026-11-21；curl/WebFetch 均被 Cloudflare 拦（5 681 字节拦截页），web_reader 代理出口放行）。页面标注 Created Sep 20, 2022, Updated Aug 03, 2023。
- **四键查重**：source_url（nvd.nist.gov/vuln，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（美国政府官方数据库自述）。
- **用途**：V61 b010（1.10.1 一个漏洞对应一条记录〔跨方确信指称句〕、1.10.2 授权结构决定谁能定名〔CNA Rules 指引句〕、1.10.4 映射误差沿引用链逐级放大〔thesis 预设句逐字核得〕，三题异句异锚 J84）。

## 逐字引文池（供本批取用，均取自上述页面正文；web_reader 转写形态）

1. [1.10.4 用] All vulnerabilities in the NVD have been assigned a CVE identifier and thus, abide by the definition below.

2. [1.10.1 用] The use of CVEs ensures that two or more parties can confidently refer to a CVE identifier (ID) when discussing or sharing information about a unique vulnerability.

3. [1.10.2 用] For detailed information regarding CVE please refer to https://cve.org/ or the CNA Rules at https://www.cve.org/ResourcesSupport/AllResources/CNARules
   - **链接元素披露（b010）**：句中 cve.org 与 CNA Rules 为两处超链接元素，web_reader 转写时链接间产生分段（渲染文本为连续句）；引文按渲染合并形态取，未含句末标点（原页句号随元素分段难以逐字锚定，如实披露）。

4. [备用（CVE 漏洞定义面），照录] A weakness in the computational logic (e.g., code) found in software and hardware components that, when exploited, results in a negative impact to confidentiality, integrity, or availability.
   （CVE 漏洞定义引文首句节选；NVD 页以 block quote 转引 CVE 定义，源属 CVE Program）
