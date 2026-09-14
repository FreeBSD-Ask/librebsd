# 核查报告：05-卷册大纲/第13卷-bsd衍生操作系统/第260章-truenas/index.md

- 源文件：D:\librebsd\05-卷册大纲\第13卷-bsd衍生操作系统\第260章-truenas\index.md（148 行，一次完整通读）
- 批次：C369（第 42 块第 2/3）；检查日期：2026-09-15；检查方式：逐文件完整阅读人工核对（TrueNAS 章目录）
- SUMMARY.md 收录：在档（260 index）
- 检查项速览：A 占位符——史观待回填见条 1；B 内容完整性——要点/史料/史观/辨析/文献＋PODCAST 六期；C 编号与标题——旧章号残留见条 1；D 格式规范——DB_REF 重复见条 1；E 学术规范——库错挂见条 1；F SUMMARY 一致性——在档

## 问题清单

1. P2 | 旧章号 259 残留＋DB_REF 模板重复＋史观待回填＋库错挂 | 行 33/42 文献栏混入“## 259.2.2 外部贡献者”“## 259.4.2 CVE-2021-20316...”子节标题（现 260）；行 31-46 多个 DB_REF 块重复注入；行 24 史观栏“(待人工回填——详见子节文件史观/辨析字段)”；行 28“openbsd.duckdb 查询 L7.6.1”库错挂（openbsd 承载 freebsd/bsd_derivatives 数据） | 259 改 260、DB_REF 精简、史观回填、openbsd 改实际持有库名
2. P3 | PODCAST 承接不均 | 六期（SPARCbook/Hacker News/OpenBSD 漏洞/NetBSD 9/基准测试/TUHS 文物等）多数为通用 BSD 新闻，与“TrueNAS”章题承接不均 | 承接校正或改宿

- 结论：存在问题 2 项（P0 0、P1 0、P2 1、P3 1）

## 补充说明（正样本与复核留痕）

- TrueNAS 商业谱系一手准确：FreeNAS 2005（基于 m0n0wall+PHP Web 界面）、iXsystems 源自 BSDi（曾售 BSD/386）、经与 Walnut Creek CD-ROM 合并/Wind River 转手后 2007 收购 FreeNAS——商业谱系完整（EP552 Liam Proven 记者综述）
- TrueNAS CORE 维持工程阶段辨析：iXsystems 重心转向 Debian 基底 SCALE、CORE 计划 FreeBSD 13.3 后不再规划 14 基底——“BSD 衍生在企业存储中的分化”定位（EP552 一手）
- CVE-2011-2522/2694 Samba 修复一手：2011-08-09 truenas-middleware commit 85d6a4ef（Xin Li/delphij，更新 Samba 3.5.11 修 VUZZI+代码）——CVE 考据 commit hash 自足
- JFK 图书馆 TrueNAS M50（2500 万文档/依赖 ZFS 擦洗校验和快照复制百年级只读归档）——企业用例一手（但辨析注明厂商单方口径须馆方披露）
- 辨析 0 信任：ixsystems_contributors 邮箱域名识别低估（@gmail.com 等个人邮箱）、SCALE 转向反映存储软件栈容器/K8s 生态压力须客观论述
- 交办提示：条 1 的 259→260 旧章号与 DB_REF 批量重复同族；库错挂（openbsd.duckdb 承载多库数据）与 279/263 同族