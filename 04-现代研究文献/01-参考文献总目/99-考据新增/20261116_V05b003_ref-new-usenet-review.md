<!-- 网页条目卡｜TUHS Usenet 存档：comp.unix 1984 年 1 月书评（chuqui at nsc.UUCP）｜本卡为 Task 8.2 G1 V05 b003 联网补证批引文载体 -->

# Review: The Unix Programming Environment（comp.unix, 1984-01）

来源：TUHS Usenet Archive, comp.unix, 1984-January, message 004526 `https://www.tuhs.org/Usenet/comp.unix/1984-January/004526.html`（访问日 2026-11-16；本机直连该页 TLS 握手不稳，经 WebFetch 通道取全文转录，关键段与搜索引擎抓取的同页文本逐句核对一致）。

## 逐字原文（关键段）

Speaking of reviewing the book, I have just finished it and was about to, so without further ado:

\*\*\* The Review \*\*\*

The Unix Programming Environment
Brian W. Kernighan, Rob Pike
Prentice Hall Software Series, $19.95 (355 pages softcover)

For those that missed it, Rob Pike gave a talk at Unicom in Toronto on 'The Philosophy of Unix Programming (or cat -v considered harmful)'. In it, he discussed the pro's and con's of some of the trends he sees in Unix programming and alternatives. He promoted very heavily the tool orientation of small programs with single purposes put together in flexible ways. Two programs he took to task were 'more' (for the very obvious reasons of excessive functionality to the point on unmaintainability) and 'cat -v' because it took a filter that moves information and modified it to be a filter that modified information.

The book is an expansion of this talk, and describes in detail (with many examples) how Rob and Brian feel Unix programs should be written. They discuss shell programming and C programming in detail, and also look at programs like sed, awk, lex, and yacc. There is some tutorial for all of these, but the real audience seems to be programmers with Unix experience.

There are a lot of good programs in the example (such as vis, their replacement for cat -v, and p, their pager (with filename spelling correction, no less, which you'll never find in a tty driver (\*hint\*))).

I do NOT recommend it as a first book on Unix programming (I much prefer the Bourne book for that), but it should be required reading for every Unix programmer.

On the chuqui scale: \*\*\*\*\* (out of a possible 5)

This book should be on everyones bookshelf.

## 著录

Chuq（chuqui at nsc.UUCP）. Review: The Unix Programming Environment[J/OL]. comp.unix, 1984-01-25. https://www.tuhs.org/Usenet/comp.unix/1984-January/004526.html [2026-11-16].
