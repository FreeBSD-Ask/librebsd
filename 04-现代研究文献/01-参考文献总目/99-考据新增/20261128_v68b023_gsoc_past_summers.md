# Google Developers《Archive》（past-summers 归档入口页）引用卡（新 ref）

- **性质**：GSoC 官方“History → Archive”历年入口页（developers.google.com，页脚 Last updated 2024-07-23 UTC）
- **数据库**：拟新建 ref（2026-11-28 V68 补证批 b023；source_url 四键查重后定号）
- **source_url**：https://developers.google.com/open-source/gsoc/past-summers
- **取源方式**：2026-11-28 经 Tavily extract 取页全文；链接分组逐字核对；另经 Playwright 实测 summerofcode.withgoogle.com 新归档
- **来源定级**：official_doc／L3（主办方官方页面）

## 一、逐字引文（英文，未翻译）

入口句与历年链接分组（2005—2008 指 developers 年页，2009—2015 指 google-melange 域，2016 起指 withgoogle archive）：

> Learn more about previous iterations of Google Summer of Code:

> * 2005 (/open-source/gsoc/2005)
> * 2006 (/open-source/gsoc/2006)
> * 2007 (/open-source/gsoc/2007)
> * 2008 (/open-source/gsoc/2008)
> * 2009 (https://www.google-melange.com/gsoc/homepage/google/gsoc2009)
> * 2010 (https://www.google-melange.com/gsoc/homepage/google/gsoc2010)
> * 2011 (https://www.google-melange.com/gsoc/homepage/google/gsoc2011)
> * 2012 (https://www.google-melange.com/gsoc/homepage/google/gsoc2012)
> * 2013 (https://www.google-melange.com/gsoc/homepage/google/gsoc2013)
> * 2014 (https://www.google-melange.com/gsoc/homepage/google/gsoc2014)
> * 2015 (https://www.google-melange.com/gsoc/homepage/google/gsoc2015)
> * 2016 (https://summerofcode.withgoogle.com/archive)（其后各年同域）

## 二、实测注记（2026-11-28）

1. google-melange.com 域已下线，访问重定向至 summerofcode.withgoogle.com 主站，原归档内容不再可达（Tavily extract 实测，返回主站首页文案）。
2. summerofcode.withgoogle.com 新归档实测：`/archive/2005/organizations` 返回“No results found”且页脚诊断“Archived program '2005' not found”；`/archive/2010/organizations` 同报 not found（Playwright 实测）。
3. 新归档主页面年条目自 2016 年起可直达（2026—2016），2026 Program 行读数“1127 projects were completed with 184 open source organizations”（Tavily 快照两次命中）。

## 三、读用界限

1. 官方现行“归档”对首年（2005）无条目，首年记录实际承载于 developers.google.com 年页（ref10025 快照：39 个组织条目＋逐项目清单）。
2. 题面所称“仅十条记录”之确数未获一手确证，落块以实测“无条目”为准并披露差异。
3. 不得把“归档缺条目”引为“项目未发生”；首年规模另有统计页（410 学生／42 组织／80%）与官方年页清单两路官方记载。
