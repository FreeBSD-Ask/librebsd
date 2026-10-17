# ads_rules.md — 四刊广告判别规则（T004 侦察结论）

侦察日：2026-10-05。方法：每刊抽样 3 期（早年/中年/晚年）全目录 grep `advert` ＋ TOC 页全文通读＋命中上下文人工判读。

## 结论：本 DVD 无整页广告版面

1. `advert` 关键字命中（DDJ 12/CUJ 15/SA 7/TPJ 2–5 per sample years）逐条核验**全部为正文英文词**（如 inadvertently、advertising 的行文提及），无一是广告版面。
2. TOC 页（DDJ `9001toc.htm`、CUJ `tocjan.htm`、SA `a1.htm` 卷首页、TPJ `ewtoc.html`）无广告栏目、无 advertiser index。
3. 该 DVD（Dr. Dobb's Developer Library DVD-ROM Release 6）为**随刊文章＋源码伴侣盘**，不含杂志印刷版的广告版面扫描。

## 判别规则（全量抽取阶段执行）

- **R-A1 文字广告页**：不以文件名/关键词猜测；仅当某 HTML 页 60% 以上内容为价格/订购/促销话术（命中 ≥3 个促销词：order/call now/price/$/subscribe/free trial/discount 且无正文代码块）才判为广告页 → 入 `ads.ad_text`。预计命中 0，如实记录。
- **R-A2 图片广告**：figures 判别阶段，凡图片内容为促销/订购单/价格表 → 建 figures 行（disposition 按内容转写/base64）＋挂 `ads.figure_id`、ad_kind='image'。预计命中 0–个位数。
- **R-A3 营销性栏目**（非广告、按栏目入库）：CUJ `newprod/`（New Products 栏，TITLE 实证 "January 1990/New Products"）与各刊产品发布/公告类栏目 → 一律按 **article 行（section=NEW PRODUCTS 等）** 入库，不进 ads。
- **R-A4 期刊社务页**（masthead/订阅信息/征稿启事）→ 按文章行入库（section=MASTHEAD/ADMIN），不进 ads。

## 空 ads 表的口径

若全量抽取后 ads 行数＝0 或个位数，**这是经侦察证实的“本盘无广告版面”结论**，不是遗漏；核验判据改为：①R-A1 判别在抽样期全量执行且原始输出留档；②命中数与侦察规则一致。此口径已回填 spec research.md §R6。
