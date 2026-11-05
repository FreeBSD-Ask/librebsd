# 字体：霞鹜文楷屏幕阅读版（子集）

## 来源与许可

| 项 | 内容 |
| --- | --- |
| 字体 | LXGW WenKai Screen（霞鹜文楷屏幕阅读版） |
| 版本 | v1.530 |
| 上游仓库 | <https://github.com/lxgw/LxgwWenKai-Screen> |
| 原始字体 | <https://github.com/lxgw/LxgwWenKai-Screen/releases/download/v1.530/LXGWWenKaiScreen.ttf>（约 26 MB，未入库，子集化后删除） |
| 许可原文 | <https://raw.githubusercontent.com/lxgw/LxgwWenKai-Screen/main/OFL.txt>（本目录 `OFL.txt` 逐字保留） |
| 许可 | SIL Open Font License 1.1 |

## 子集文件

`LXGWWenKaiScreen-subset.woff2`：WOFF2，563,892 字节（约 0.54 MB），2,538 个码位。

## 子集口径

字符集由以下五部分并集而成（脚本一次性生成，未保留生成脚本）：

1. `05-卷册大纲/映射/title-design/V*.tsv`（76 卷，19,461 行）中 `title` 与 `thesis` 两列的全部字符；
2. ASCII：U+0020–U+007E；
3. 常用标点：U+2000–U+206F（弯引号、破折号、省略号、间隔号等）；
4. CJK 标点与全角形式：U+3000–U+303F、U+FF00–U+FFEF；
5. 前端源码（`../*.html`、`../*.css`、`../*.js`、`../*.webmanifest`）中出现的全部字符，即界面文案用字。

## 缺失字与回退

并入字符集但上游字体无对应字形的码位共 41 个，全部是格式控制符或未分配码位（U+202A–U+202E 双向控制、U+2060–U+206F、U+302E／U+302F、U+3031／U+3032、U+FF00、U+FFA0、U+FFBF–U+FFE7 部分空位），不含任何可见汉字或标点，故不构成现实缺失。

若日后题名出现子集外的新字符，浏览器按 `font-display: swap` 与 CSS `font-family` 回退链（系统 PingFang SC／Microsoft YaHei 等）渲染，不依赖外网；此时应重新生成子集。

## 更新方式

1. 下载 v1.530（或新版）TTF 与 `OFL.txt`；
2. 用 fontTools＋brotli 按上述五部分字符集子集化为 WOFF2，覆盖本文件；
3. 同步更新本 README 的版本号、字节数与码位数。
