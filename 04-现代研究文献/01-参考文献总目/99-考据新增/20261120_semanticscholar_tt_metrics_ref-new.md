# 考据快照：Semantic Scholar API 计量记录（Reflections on trusting trust）

- URL：https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/358198.358210?fields=title,year,citationCount,influentialCitationCount,externalIds
- 访问日：2026-11-20（curl 直取 JSON）
- 定性：Semantic Scholar 学术计量库官方 API 响应（第三方学术计量数据，非出版方亦非聚合网页转述）；source_type=web_archive（API 响应转写），L3。作为 1.4.5 题“高频引用件”的计量证据面；出版方 ACM DL 著录页（ref11051，在库）页面不含引用计数显示，故计量值取 S2 API。
- 注意：S2 计数随时点漂移，claim 与块内已固定取值时点（2026-11-20）。

## 著录要素

> Semantic Scholar Graph API（paper by DOI 10.1145/358198.358210），fields=title,year,citationCount,influentialCitationCount,externalIds。取值日 2026-11-20。

## 逐字摘录（API 响应 JSON 全文）

> {"paperId": "49f95eb02480e740fc4431338ac8f744a40a2bea", "externalIds": {"MAG": "2257724910", "DBLP": "journals/cacm/Thompson84", "DOI": "10.1145/358198.358210", "CorpusId": 34854438}, "title": "Reflections on trusting trust", "year": 1984, "citationCount": 786, "influentialCitationCount": 32}

## 披露

- API 响应为单行 JSON，本卡按原样转写（键序照响应原序）；quote 以省略号分段取 title／year／citationCount／influentialCitationCount 四字段。
- externalIds 含 MAG 2257724910（微软学术遗留号）与 DBLP journals/cacm/Thompson84，旁证著录一致性。
