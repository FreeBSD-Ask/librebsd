
(function () {
  try {
  var docPage = document.querySelector('.doc-page');
  if (!docPage) return;
  var CN = {一:1,二:2,三:3,四:4,五:5,六:6,七:7,八:8,九:9,十:10,十一:11,十二:12,十三:13,十四:14,
            十五:15,十六:16,十七:17,十八:18,十九:19,二十:20,二十一:21,二十二:22,二十三:23,二十四:24,
            二十五:25,二十六:26,二十七:27};
  var stor = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- 1. 静态节 id（深链）：li#vol-N-ch-M-sec-X-Y ---------- */
  var vols = Array.prototype.slice.call(docPage.querySelectorAll("section[id^='vol-']"));
  var chapters = Array.prototype.slice.call(docPage.querySelectorAll("h3.chapter[id]"));
  var secIndex = [];   /* {id, vol, ch, num, title, note} */
  chapters.forEach(function (ch) {
    var m = ch.id.match(/^vol-(\d+)-ch-(\d+)$/);
    var ul = ch.nextElementSibling;
    if (!ul || !ul.classList || !ul.classList.contains('sections')) return;
    var chNo = m ? m[2] : "";
    Array.prototype.slice.call(ul.children).forEach(function (li) {
      var numEl = li.querySelector(":scope > .sec-num");
      if (!numEl) return;
      var num = numEl.textContent.trim();
      if (!li.id) li.id = "vol-" + (m ? m[1] : "0") + "-ch-" + chNo + "-sec-" + num.replace(/\./g, "-");
      var noteEl = li.querySelector(":scope > .src");
      var t = __LB.pureTitle(li);
      li.dataset.vol = m ? m[1] : "";
      secIndex.push({ id: li.id, ch: ch.id, vol: m ? m[1] : "", num: num, title: t,
                      note: noteEl ? noteEl.textContent : "" });
    });
  });

  /* ---------- 2. 溯源注折叠 ---------- */
  secIndex.forEach(function (s) {
    var li = document.getElementById(s.id);
    if (!li) return;
    var src = li.querySelector(":scope > .src");
    if (!src || li.querySelector(":scope > .note-badge")) return;
    var b = document.createElement("button");
    b.type = "button"; b.className = "note-badge"; b.textContent = U("ui.note.badge");
    b.title = U("ui.note.toggle");
    b.setAttribute("aria-expanded", "false");
    b.setAttribute("aria-label", U("ui.note.toggle"));
    b.addEventListener("click", function (e) {
      e.preventDefault(); e.stopPropagation();
      li.classList.toggle("note-open");
      b.setAttribute("aria-expanded", li.classList.contains("note-open") ? "true" : "false");
    });
    li.insertBefore(b, src);
  });
  var btnNotes = document.getElementById("optNotes");
  function applyNotesAll(on) { document.body.classList.toggle("notes-all", !!on); if (btnNotes) btnNotes.classList.toggle("on", !!on); }
  applyNotesAll(stor.get("sme-notes") === "all");
  if (btnNotes) btnNotes.addEventListener("click", function () {
    var on = !document.body.classList.contains("notes-all");
    applyNotesAll(on); stor.set("sme-notes", on ? "all" : "none");
  });

  /* ---------- 3. 分工注自动链接化 ---------- */
  var chByVolNo = {};
  chapters.forEach(function (ch) {
    var m = ch.id.match(/^vol-(\d+)-ch-(\d+)$/); if (m) chByVolNo[m[1] + "-" + m[2]] = true;
  });
  var secByChNo = {};
  secIndex.forEach(function (s) { secByChNo[s.ch + "|" + s.num] = s.id; });
  function resolve(volNo, chNo, secNo) {
    if (!chByVolNo[volNo + "-" + chNo]) return null;
    if (secNo && secByChNo["vol-" + volNo + "-ch-" + chNo + "|" + secNo]) return secByChNo["vol-" + volNo + "-ch-" + chNo + "|" + secNo];
    return "vol-" + volNo + "-ch-" + chNo;
  }
  var nLinked = 0;
  secIndex.forEach(function (s) {
    var li = document.getElementById(s.id); if (!li) return;
    var src = li.querySelector(":scope > .src"); if (!src) return;
    var myVol = s.vol, myCh = (s.ch.match(/-ch-(\d+)$/) || [])[1];
    var html = src.innerHTML;
    var out = html.replace(/第([一二三四五六七八九十]+)卷第\s?(\d+)\s?章\s?(\d+\.\d+)?|(本章第\s?(\d+)\s?章\s?(\d+\.\d+)?)|第\s?(\d+)\s?章\s?(\d+\.\d+)/g,
      function (all, cv, cch, csec, _b, bch, bsec, sch, ssec) {
        var target = null, label = all;
        if (cv && CN[cv]) target = resolve(String(CN[cv]), cch, csec);
        else if (bch) target = resolve(myVol, bch, bsec);
        else if (sch && String(sch) === String(myCh)) target = resolve(myVol, sch, ssec);
        if (!target) return all;
        nLinked++;
        return '<a href="#' + target + '" data-xref="1">' + label + '</a>';
      });
    if (out !== html) src.innerHTML = out;
  });

  /* ---------- 4. 面包屑 + 当前章/节高亮 ---------- */
  var bc = document.createElement("div");
  bc.className = "breadcrumb";
  docPage.insertBefore(bc, docPage.firstChild);
  var leftLinks = {}, rightLinks = {};
  function collectLinks() {
    document.querySelectorAll(".toc-left a[data-target], .toc-right a[data-target]").forEach(function (a) {
      var t = a.dataset.target;
      if (/^vol-\d+$/.test(t)) leftLinks[t] = a;
      else if (/^vol-\d+-ch-\d+$/.test(t)) leftLinks[t] = a;
      else rightLinks[t] = a;
    });
  }
  /* 当前项高亮：复用 collectLinks() 已建的 leftLinks／rightLinks 映射。
     原实现每次全量 querySelectorAll 扫遍目录链接（映射建而不用），且清除与置位各扫一遍。 */
  var curLinks = [];
  function linkFor(t) {
    return leftLinks[t] || rightLinks[t] ||
      document.querySelector('.toc-left a[data-target="' + t + '"], .toc-right a[data-target="' + t + '"]');
  }
  function setCurrent(targets) {
    var want = {};
    (Array.isArray(targets) ? targets : [targets]).forEach(function (t) { if (t) want[t] = true; });
    for (var i = 0; i < curLinks.length; i++) {
      curLinks[i].classList.remove("current");
      curLinks[i].removeAttribute("aria-current");
    }
    curLinks = [];
    Object.keys(want).forEach(function (t) {
      var a = linkFor(t);
      if (!a) return;
      a.classList.add("current"); a.setAttribute("aria-current", "true");
      curLinks.push(a);
    });
  }

  var lastStep = { ch: "", sec: "" };
  var bcParts = null;   /* 面包屑结构缓存：一次建、后续只改文本 */
  __LB.stepSync = function (chId, secId) {
    secId = secId || "";
    if (!chId || (chId === lastStep.ch && secId === lastStep.sec)) return;
    lastStep = { ch: chId, sec: secId };
    setCurrent([chId, secId]);
    if (!bc) return;
    var chEl = document.getElementById(chId);
    var secEl = secId ? document.getElementById(secId) : null;
    /* 卷／章计数徽标（.vol-badge／.ch-badge）在版面中靠 margin-left 与题文相隔，
       直取 textContent 会与题文粘连（“…UNIX13 章 · 96 节”）。故剥出徽标文本，
       以 1 个半角空格重新相接；无徽标时原样返回。 */
    var badgeJoin = function (el, sel) {
      if (!el) return "";
      var b = el.querySelector(sel);
      var t = el.textContent;
      if (b) t = t.replace(b.textContent, "");
      return b ? t.trim() + " " + b.textContent.trim() : t.trim();
    };
    var parts = [];
    if (chEl && chEl.closest) {
      var vEl = chEl.closest("section[id^='vol-']");
      if (vEl) { var vTitle = badgeJoin(vEl.querySelector("h2"), ".vol-badge"); if (vTitle) parts.push(vTitle); }
    }
    if (chEl) { var chTitle = badgeJoin(chEl, ".ch-badge"); if (chTitle) parts.push(chTitle); }

    /* 面包屑：一次建结构、之后只就地改文本。
       原实现每步“删光全部 span/b → 建 fragment → 插回 → 再查 .prog”，属每步重建 DOM。 */
    if (!bcParts) {
      bcParts = {};
      var mkSpan = function () { var e = document.createElement("span"); bc.appendChild(e); return e; };
      var mkSep = function () { var e = document.createElement("b"); e.textContent = "›"; bc.appendChild(e); return e; };
      bcParts.vol = mkSpan();
      /* 2026-10-12（138 批 a11y，E2）：面包屑当前项 aria-current="location"
         （TOC 当前项已由 setCurrent() 置 aria-current="true"，2026-09 起） */
      bcParts.vol.setAttribute("aria-current", "location");
      bcParts.sep1 = mkSep();
      bcParts.ch = mkSpan();
      bcParts.sep2 = mkSep();
      bcParts.sec = mkSpan();
      var pr = document.createElement("span");
      pr.className = "prog";
      pr.innerHTML = "<i></i>";
      bc.appendChild(pr);
      bcParts.prog = pr;
    }
    var pv = parts.length > 0 ? parts[0] : "";
    var pc = parts.length > 1 ? parts[1] : "";
    var psec = "";
    if (secEl && secEl.querySelector(":scope > .sec-num")) {
      psec = secEl.querySelector(":scope > .sec-num").textContent.trim();
    }
    if (bcParts.vol.textContent !== pv) bcParts.vol.textContent = pv;
    if (bcParts.ch.textContent !== pc) bcParts.ch.textContent = pc;
    if (bcParts.sec.textContent !== psec) bcParts.sec.textContent = psec;
    /* 2026-09-26 主理人裁定：面包屑只展示卷 */
    bcParts.vol.style.display = pv ? "" : "none";
    bcParts.sep1.style.display = "none";
    bcParts.ch.style.display = "none";
    bcParts.sep2.style.display = "none";
    bcParts.sec.style.display = "none";

    if (window.scrollY > 120) {
      bc.classList.add("visible");
      bc.style.visibility = "visible";
      bc.style.opacity = "1";
    } else {
      bc.classList.remove("visible");
      bc.style.visibility = "hidden";
      bc.style.opacity = "0";
    }
  };
  collectLinks();   /* 目录由前置脚本构建，此处即时收集链接 */
  document.addEventListener("DOMContentLoaded", collectLinks);   /* setupToc 建完目录后立即补齐映射 */
  window.addEventListener("load", collectLinks);

  function volTitle(v) {
    var el = (typeof v === "string") ? document.getElementById(v) : v;
    if (!el) return "";
    return __LB.pureTitle(el.querySelector("h2"));
  }

  /* ---------- 5. 卷级上一卷/下一卷 ---------- */
  vols.forEach(function (v, i) {
    var nav = document.createElement("div");
    nav.className = "vol-nav";
    var prev = i > 0 ? vols[i - 1] : null, next = i < vols.length - 1 ? vols[i + 1] : null;
    nav.innerHTML = (prev ? '<a href="#' + prev.id + '">← ' + volTitle(prev) + "</a>" : "<span></span>") +
                    (next ? '<a href="#' + next.id + '">' + volTitle(next) + " →</a>" : "<span></span>");
    v.appendChild(nav);
  });

  /* ---------- 6. 深链（hashchange） ---------- */
  function jump() {
    var id = decodeURIComponent(location.hash.replace(/^#/, ""));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    var li = el.closest ? el.closest("li") : null;
    if (li && li.querySelector(":scope > .src") && !document.body.classList.contains("notes-all")) {
      li.classList.add("note-open");
      var b = li.querySelector(":scope > .note-badge"); if (b) b.setAttribute("aria-expanded", "true");
    }
    setCurrent(id);
    var ch = el.closest ? el.closest("section") : null;
  }
  window.addEventListener("hashchange", jump);
  window.addEventListener("load", jump);

  /* ---------- 6a. 页内锚点历史中性化（2026-10-14 主理人令） ----------
     无论怎样点击都不产生浏览器历史条目（本页始终只占载入时的那一条）。
     默认锚点导航每点一次即 push 一条同文档记录；滚动智能同步只 replace 当前条目，
     两者叠加使后退键要逐条“页内滑动”方能离开。现将全部页内 `#` 链接统一接管：
     preventDefault → scrollIntoView（与原生锚点同构：尊重 scroll-margin 与 CSS
     scroll-behavior、减动效回落）→ replaceState 改写片段 → jump() 收尾（注展开、高亮）。
     修饰键与非左键一律放行：Ctrl／Cmd／Shift／Alt 及中键保留“新标签打开”等原生语义。 */
  function goInPage(id) {
    var el = document.getElementById(id);
    if (!el) return false;
    try { el.scrollIntoView({ block: "start", inline: "nearest" }); } catch (e) { el.scrollIntoView(); }
    try { history.replaceState(null, "", "#" + id); } catch (e2) {}
    jump();
    return true;
  }
  document.addEventListener("click", function (e) {
    if (e.defaultPrevented) return;
    if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target && e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var href = a.getAttribute("href");
    if (!href || href.length < 2) return;
    var id;
    try { id = decodeURIComponent(href.slice(1)); } catch (e2) { return; }
    e.preventDefault();
    if (!goInPage(id)) { try { history.replaceState(null, "", href); } catch (e3) {} }
  });

  /* ---------- 7. 全文检索（节级） ---------- */
  var panel = document.createElement("dialog");
  panel.className = "opt-panel"; panel.id = "optPanelSearch";
  panel.innerHTML = '<div class="box"><h3>' + U("ui.search.title") + '</h3>' +
    '<input type="search" id="optSearchInput" placeholder="' + U("ui.search.panel_ph") + '" aria-label="' + U("ui.search.aria2") + '">' +
    '<div class="hint">' + U("ui.search.hint") + '<kbd>Esc</kbd>' + U("ui.search.hint2") + '</div>'
    + '<p class="hint" id="optSearchCount" role="status" aria-live="polite"></p>'
    + '<ul id="optSearchResults"></ul></div>';
  document.body.appendChild(panel);
  var chTitleCache = {};
  chapters.forEach(function (c) { chTitleCache[c.id] = __LB.pureTitle(c); });
  var volTitleCache = {};
  vols.forEach(function (v) { volTitleCache[v.id] = __LB.pureTitle(v.querySelector("h2")); });
  var input = panel.querySelector("#optSearchInput"), results = panel.querySelector("#optSearchResults");
  /* 检索词归一（2026-10-04 修）：空格差异不应影响命中——多余空格、缺空格、全角空格
     与 CJK／拉丁混排锚空格，一律以“去空白”二次比较兜底；先精确后宽松，精度不降。 */
  function __normWS(s) { return String(s || "").replace(/\s+/g, ""); }
  function runSearch(q) {
    var exact = String(q || "").trim().toLowerCase();
    var loose = __normWS(exact);
    results.innerHTML = "";
    var hitIds = [];
    if (exact.length < 1) { clearSearchHighlight(); return; }
    var hits = 0;
    for (var i = 0; i < secIndex.length && hits < 300; i++) {
      var s = secIndex[i];
      var hay = (s.title + " " + s.note + " " + (chTitleCache[s.ch] || "") + " " + (volTitleCache["vol-" + s.vol] || "")).toLowerCase();
      if (hay.indexOf(exact) < 0 && !(loose && __normWS(hay).indexOf(loose) >= 0)) continue;
      hits++;
      hitIds.push(s.id);
      var li = document.createElement("li");
      li.innerHTML = __LB.ttt('<span class="path">' + (volTitleCache["vol-" + s.vol] || "") + ' › ' + (chTitleCache[s.ch] || "") +
        ' › ' + s.num + '</span><a href="#' + s.id + '">' + s.title.replace(/</g, "&lt;") + "</a>");
      li.querySelector("a").addEventListener("click", function () { closePanels(); });
      results.appendChild(li);
    }
    if (!hits) results.innerHTML = '<li class="hint">' + U("ui.search.none2") + '</li>';
    var cnt = panel.querySelector("#optSearchCount");
    if (cnt) cnt.textContent = hits ? F("ui.search.hits_fmt", { n: hits }) : U("ui.search.none");
    applySearchHighlight(exact, hitIds);
  }
  /* ---------- 检索命中页内高亮（2026-10-11 载体层批次，CSS Custom Highlight API） ----------
     命中节内的匹配文本以 Range＋::highlight(search-hit) 绘制高亮——**零 DOM 变更**，
     导出与断言面不受污染。仅对 exact 形态定位（loose 去空格命中的节只在结果列表出现、
     正文不高亮，登记语义）。不支持该 API 的引擎（如 Firefox）回退＝现状（无页内高亮），
     结果列表功能不变。上限 800 个 Range 防极端 query 卡顿。 */
  var hlOk = typeof Highlight === "function" && !!(window.CSS && CSS.highlights && CSS.highlights.set) &&
             CSS.supports && CSS.supports("selector(::highlight(search-hit))");
  function clearSearchHighlight() {
    if (hlOk) CSS.highlights.delete("search-hit");
  }
  function applySearchHighlight(exact, hitIds) {
    clearSearchHighlight();
    if (!hlOk || !exact) return;
    var ranges = [], caps = 0;
    for (var k = 0; k < hitIds.length && caps < 800; k++) {
      var li = document.getElementById(hitIds[k]);
      if (!li) continue;
      var walker = document.createTreeWalker(li, NodeFilter.SHOW_TEXT, {
        acceptNode: function (node) {
          var p = node.parentElement;
          if (!p || p.closest(".note-badge, .t-more, .t-short, .sec-num, button")) return NodeFilter.FILTER_REJECT;
          return node.nodeValue && node.nodeValue.toLowerCase().indexOf(exact) >= 0 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
        }
      });
      while (walker.nextNode() && caps < 800) {
        var nv = walker.currentNode.nodeValue, at = nv.toLowerCase().indexOf(exact);
        while (at >= 0 && caps < 800) {
          try { ranges.push(new Range()); ranges[ranges.length - 1].setStart(walker.currentNode, at); ranges[ranges.length - 1].setEnd(walker.currentNode, at + exact.length); caps++; } catch (e) { break; }
          at = nv.toLowerCase().indexOf(exact, at + exact.length);
        }
      }
    }
    if (ranges.length) { try { CSS.highlights.set("search-hit", Reflect.construct(Highlight, ranges)); } catch (e) {} }
  }
  panel.addEventListener("close", clearSearchHighlight);   /* 面板关闭即清（Esc／遮罩／close 均走此） */
  input.addEventListener("input", function () { runSearch(this.value); });
  var btnSearch = document.getElementById("optSearch");
  if (btnSearch) btnSearch.addEventListener("click", function () {
    __LB.decorateDialogs(); __LB.openDialog(panel); input.focus(); input.select();
    /* 点击后收起工具展开态（全部视口统一），避免遮住检索面板 */
    var tt = document.getElementById("optToolsToggle");
    if (tt) tt.parentElement.classList.remove("expanded");
  });

  var optTt = document.getElementById("optToolsToggle");
  if (optTt) optTt.addEventListener("click", function () {
    var bar = this.parentElement;
    var was = bar.classList.contains("expanded");
    bar.classList.toggle("expanded", !was);
    this.setAttribute("aria-expanded", was ? "false" : "true");
  });
  /* 点击外部收起（移动端） */
  document.addEventListener("click", function (e) {
    var bar = document.querySelector(".opt-tools.expanded");
    if (bar && e.target.closest && !e.target.closest(".opt-tools")) {
      bar.classList.remove("expanded");
      var t = document.getElementById("optToolsToggle");
      if (t) t.setAttribute("aria-expanded", "false");
    }
  });

  /* ---------- 8. 导出：JSON / CSV ---------- */
  function buildStructure() {
    /* 卷题/章题/节名一律走 __LB.pureTitle：
       直接取 textContent 会把运行时装饰（“N 章 · N 节”“N 节”“注”）一并带入，
       与内容源 outline.txt 不一致；节名还会受长节名折叠态影响。 */
    return vols.map(function (v) {
      var chs = Array.prototype.slice.call(v.querySelectorAll("h3.chapter[id]")).map(function (c) {
        var ul = c.nextElementSibling, secs = [];
        if (ul && ul.classList && ul.classList.contains("sections")) {
          Array.prototype.slice.call(ul.children).forEach(function (li) {
            var n = li.querySelector(":scope > .sec-num"); if (!n) return;
            var src = li.querySelector(":scope > .src");
            secs.push({ id: li.id, num: n.textContent.trim(), title: __LB.pureTitle(li), note: src ? src.textContent.trim() : "" });
          });
        }
        return { id: c.id, title: __LB.pureTitle(c), sections: secs };
      });
      var h2 = v.querySelector("h2");
      return { id: v.id, title: __LB.pureTitle(h2), chapters: chs };
    });
  }
  function exportPlainText() {
    /* 原实现用尾正则剥徽标（“N 章 · N 节”“N 节”）：徽标与题文之间无分隔符，
       末位数字会与徽标数字连成一体（“V7”+“4 节”→“V74 节”），
       正则遂吞掉真实字符（实测 “V1 至 V7”→“V1 至 V”）。现由 pureTitle 直接给出净题。 */
    var L = ["# \u7ed9\u6211\u81ea\u7531\u2014\u4e00\u90e8 BSD \u53f2 \u5b8c\u6574\u76ee\u5f55\uff08\u7eaf\u6587\u672c\uff09"];
    buildStructure().forEach(function (v) {
      L.push("# " + v.title);
      v.chapters.forEach(function (c) {
        L.push("  ## " + c.title);
        c.sections.forEach(function (s) {
          L.push("    - " + s.num + " " + s.title);
        });
      });
    });
    download(exportFileName("txt"), L.join("\n"), "text/plain;charset=utf-8");
  }
  function download(name, text, type) {
    var blob = new Blob([text], { type: type + ";charset=utf-8" });
    var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  }
  /* ---------- 8a. 导出文件名（2026-10-14，145 批） ----------
     主理人令：导出文件名＝“目录-版本.后缀名”。版本取页面 .page-version
     （UTC+8，形制 YYYY.MM.DD-HH:MM）；冒号在 Windows 下载文件名中不合法，
     统一净化为“-”。页面元素不存在时回退取文案层 shell.page_version（同形制）。 */
  function pageVersionSafe() {
    var el = document.querySelector(".page-version");
    var v = el ? String(el.textContent || "").trim() : "";
    if (!v) v = String(U("shell.page_version") || "").trim();
    return v.replace(/:/g, "-");
  }
  function exportFileName(ext) { return "目录-" + pageVersionSafe() + "." + ext; }
  /* ---------- 导出 HTML 本体（2026-10-14 新增菜单项） ----------
     双通道设计（按打开方式自动选择）：
     ① http(s)：同源 <a download> 触发浏览器下载器直取当前文档的原始资源字节——
        不经页面脚本，CSP connect-src “none” 不约束下载通道，逐字节保真。
     ② file://：Chromium 对 file 源不授同源（含自身），download 属性不生效，
        脚本亦无 API 可直读自身原始字节（fetch／XHR 均被禁）——回退为文档序列化
        导出（blob 通道）：DOCTYPE ＋ documentElement.outerHTML，卷章节数据与
        文案层完整保留，重开仍可完整阅读；含运行时装饰件，非逐字节承诺。
     http 通道剥离 hash 与 query，保证深链状态下仍指向文档自身。 */
  function exportHtmlSelf() {
    var a = document.createElement("a");
    a.download = exportFileName("html");
    if (String(location.protocol) === "file:") {
      a.href = URL.createObjectURL(new Blob(["<!DOCTYPE html>\n" + document.documentElement.outerHTML], { type: "text/html;charset=utf-8" }));
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
      return;
    }
    a.href = String(location.href).split("#")[0].split("?")[0];
    document.body.appendChild(a); a.click(); a.remove();
  }
  /* 页壳不存在的遗留按钮分支 optExportJson / optExportCsv 已删除：
     与导出菜单的 JSON/CSV 两项重复，且其 CSV 实现缺电子表格公式注入防护。 */

  var exportMenu = document.createElement("div");
  exportMenu.id = "exportMenu";
  exportMenu.setAttribute("role", "menu");
  exportMenu.innerHTML =
    '<button type="button" role="menuitem" data-x="summary">' + U("ui.export.summary") + '</button>' +
    '<button type="button" role="menuitem" data-x="json">' + U("ui.export.json") + '</button>' +
    '<button type="button" role="menuitem" data-x="csv">' + U("ui.export.csv") + '</button>' +
    '<button type="button" role="menuitem" data-x="pdf">' + U("ui.export.pdf") + '</button>' +
    '<button type="button" role="menuitem" data-x="txt">' + U("ui.export.txt") + '</button>' +
    '<button type="button" role="menuitem" data-x="html">' + U("ui.export.html") + '</button>';
  document.body.appendChild(exportMenu);
  function menuItems(m) { return [].slice.call(m.querySelectorAll('[role="menuitem"]')); }
  function closeExportMenu(restoreFocus) {
    exportMenu.classList.remove("open");
    var eb = document.getElementById("optExport");
    if (eb) {
      eb.setAttribute("aria-expanded", "false");
      if (restoreFocus) { try { eb.focus(); } catch (e) {} }
    }
  }
  /* role="menu" 承诺 ↑↓/Home/End/Esc/Tab 契约，须补齐，否则误导辅助技术 */
  exportMenu.addEventListener("keydown", function (e) {
    var items = menuItems(exportMenu), i = items.indexOf(document.activeElement);
    if (!items.length) return;
    if (e.key === "ArrowDown") { e.preventDefault(); items[(i + 1) % items.length].focus(); }
    else if (e.key === "ArrowUp") { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
    else if (e.key === "Home") { e.preventDefault(); items[0].focus(); }
    else if (e.key === "End") { e.preventDefault(); items[items.length - 1].focus(); }
    else if (e.key === "Escape") { e.preventDefault(); closeExportMenu(true); }
    else if (e.key === "Tab") { closeExportMenu(false); }
  });

  var FONT_STEPS = [{ k: "s", label: U("ui.font.s"), zoom: 0.85 }, { k: "m", label: U("ui.font.m"), zoom: 1 }, { k: "l", label: U("ui.font.l"), zoom: 1.18 }, { k: "xl", label: U("ui.font.xl"), zoom: 1.4 }];
  var fontMenu = document.createElement("div");
  fontMenu.id = "fontMenu";
  fontMenu.setAttribute("role", "group");
  fontMenu.setAttribute("aria-label", U("ui.font.aria"));
  fontMenu.innerHTML = '<div class="fs-track"><span class="fs-min">' + U("ui.font.s") + '</span>' +
    '<input type="range" min="80" max="160" step="5" id="fontRange" aria-label="' + U("ui.font.slider_aria") + '">' +
    '<span class="fs-max">' + U("ui.font.xl") + '</span></div>' +
    '<div class="fs-val" id="fontVal">100%</div>';
  document.body.appendChild(fontMenu);
  var curPct = 100;
  function applyFontSize(pct) {
    curPct = pct;
    var dp = document.querySelector(".doc-page");
    if (dp) {
      var z = pct / 100;
      /* 2026-09-27 修复“视口收窄后栏宽不回流 → 横向滚动条”：
         原实现以 .doc-page 的**用值 auto 边距**反算宽度，而 auto 边距由宽度自身决定
         （vw 减 mL 减 mR 恒等于当前宽度），构成自指不动点 —— 写入的内联宽度恒等于当时的宽度：
         载入 1920 时固化为 958.391px，此后收窄到 390/320 仍为 958.391px，
         documentElement.scrollWidth 停在 958 而视口只有 390/320 → 横向滚动条加内容右溢。
         100% 档本应零干预，实际也写入内联宽度，桌面端一旦改窗即失去响应式。
         现改为：先撤销上一轮内联覆写，交由样式层按**当前视口**算出设计栏宽；
         100% 档完全不干预（零内联，纯 CSS 驱动）；其余档位令实际栏宽等于设计栏宽
         （字号只放大内容、不改变栏宽），并保底限制在视口内。
         同时修正原式量纲错误：m 取自未缩放空间，原式 vw/z 减 m 使边距被 z 重复缩放，
         140% 时栏宽被压至 573.7px、85% 时放大至 1102.6px（后者与左右目录栏重叠、且随
         视口收窄而右溢）。 */
      dp.style.zoom = "";
      dp.style.width = "";
      if (z !== 1) {
        var vw = document.body.clientWidth;
        var base = dp.getBoundingClientRect().width;
        if (!(base > 0) || base > vw) base = vw;
        dp.style.zoom = String(z);
        dp.style.width = (base / z) + "px";
      }
    }
    try { localStorage.setItem("sme-fs", String(pct)); } catch (e) {}
    var rng = document.getElementById("fontRange");
    if (rng && Math.abs(parseInt(rng.value, 10) - pct) > 0.1) rng.value = String(pct);
    var fv = document.getElementById("fontVal");
    if (fv) fv.textContent = Math.round(pct) + "%";
    var fb = document.getElementById("fontSizeToggle");
    if (fb) fb.textContent = "Aa" + Math.round(pct - 100) + (pct >= 100 ? "+" : "") + "%";
  }
  function closeFontMenu() {
    fontMenu.classList.remove("open");
    var eb = document.getElementById("fontSizeToggle");
    if (eb) eb.setAttribute("aria-expanded", "false");
  }
  var btnFont = document.getElementById("fontSizeToggle");
  if (btnFont) btnFont.addEventListener("click", function (e) {
    e.stopPropagation();
    var willOpen = !fontMenu.classList.contains("open");
    if (willOpen) {
      var r = btnFont.getBoundingClientRect();
      fontMenu.style.top = Math.min(window.innerHeight - 160, r.bottom + 8) + "px";
      fontMenu.style.right = Math.max(8, window.innerWidth - r.right) + "px";
    }
    fontMenu.classList.toggle("open", willOpen);
    btnFont.setAttribute("aria-expanded", willOpen ? "true" : "false");
  });
  document.addEventListener("click", function (e) {
    if (fontMenu.classList.contains("open") && e.target.closest && !e.target.closest("#fontMenu") && !e.target.closest("#fontSizeToggle")) closeFontMenu();
  });
  var fontRange = fontMenu.querySelector("#fontRange");
  if (fontRange) fontRange.addEventListener("input", function (e) {
    e.stopPropagation();
    applyFontSize(parseInt(e.target.value, 10));
  });
  /* 初始应用持久化字号 */
  (function () {
    var v = null; try { v = localStorage.getItem("sme-fs"); } catch (e) {}
    var pct = parseInt(v, 10);
    if (isNaN(pct)) pct = 100;
    if (pct < 80) pct = 80; if (pct > 160) pct = 160;
    applyFontSize(pct);
    window.addEventListener("resize", function () { applyFontSize(curPct); });

  (function () {
    var t = document.getElementById("themeToggle");
    var cont = document.querySelector(".opt-tools");
    if (!t || !cont) return;
    var home = t.parentNode, homeNext = t.nextSibling;
    var mq = window.matchMedia("(max-width: 820px)");
    function place() { if (mq.matches) { if (t.parentNode !== cont) cont.appendChild(t); } else if (home && t.parentNode !== home) { home.insertBefore(t, homeNext); } }
    place();
    if (mq.addEventListener) mq.addEventListener("change", place); else if (mq.addListener) mq.addListener(place);
  })();
  })();

  function exportPdf() {
    function es(x) { return String(x).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    var st = buildStructure();
    var nv = st.length, nc = 0, ns = 0;
    st.forEach(function (v) { nc += v.chapters.length; v.chapters.forEach(function (c) { ns += c.sections.length; }); });
    var H = [];
    H.push('<!DOCTYPE html><html lang="zh-Hans"><head><meta charset="utf-8">');
    H.push('<title>' + U("ui.pdf.title") + '</title>');
    H.push('<style>');
    H.push('@page { size: A4; margin: 16mm 15mm; }');
    H.push('* { box-sizing: border-box; }');
    H.push('body { font-family: "Songti SC","SimSun",serif; font-size: 11px; color:#1a1a1a; line-height:1.5; margin:0; }');
    H.push('h1 { font-size:21px; margin:0 0 2px; }');
    H.push('.sub{ color:#555; font-size:12px; margin:0 0 16px; }');
    H.push('h2{ font-size:15px; margin:20px 0 6px; padding-bottom:3px; border-bottom:1.5px solid #999; page-break-after:avoid; }');
    H.push('h3{ font-size:12.5px; margin:11px 0 3px; color:#333; page-break-after:avoid; }');
    H.push('ul{ margin:0 0 6px; padding-left:15px; }');
    H.push('li{ margin:1px 0; }');
    H.push('li .n{ color:#888; font-size:10px; margin-right:5px; }');
    H.push('li .note{ color:#666; font-size:9px; }');
    H.push('</style></head><body>');
    H.push('<h1>' + U("shell.book_title") + ' <sup style="font-size:.34em;opacity:.55;font-weight:400;letter-spacing:.03em">' + U("shell.page_version") + '</sup></h1>');
    H.push('<p class="sub">' + nv + ' 卷 · ' + nc + ' 章 · ' + ns + ' 节 · 重构2026 现行大纲目录 · ' + new Date().toISOString().slice(0,10) + '</p>');
    st.forEach(function (v) {
      H.push('<h2>' + es(v.title) + '</h2>');
      v.chapters.forEach(function (c) {
        H.push('<h3>' + es(c.title) + '</h3>');
        if (!c.sections.length) return;
        H.push('<ul>');
        c.sections.forEach(function (ss) {
          H.push('<li><span class="n">' + es(ss.num) + '</span>' + es(ss.title) +
                 (ss.note ? ' <span class="note">' + es(ss.note) + '</span>' : '') + '</li>');
        });
        H.push('</ul>');
      });
    });
    H.push('</body></html>');
    /* 以 Blob URL 打开，避免已废弃的 document.write；print() 以幂等守卫确保只调一次 */
    var blob = new Blob([H.join("")], { type: "text/html;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var w = window.open(url, "_blank");
    if (!w) {
      URL.revokeObjectURL(url);
      try { window.alert(U("ui.popup.blocked")); } catch (e) {}
      return;
    }
    var printed = false;
    function doPrint() {
      if (printed) return;
      printed = true;
      try { w.focus(); w.print(); } catch (e) {}
    }
    if (w.addEventListener) w.addEventListener("load", doPrint);
    setTimeout(doPrint, 800);
    setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
  }
  var btnExport = document.getElementById("optExport");
  if (btnExport) btnExport.addEventListener("click", function (e) {
    e.stopPropagation();
    var willOpen = !exportMenu.classList.contains("open");
    exportMenu.classList.toggle("open", willOpen);
    btnExport.setAttribute("aria-expanded", willOpen ? "true" : "false");
    if (willOpen) {
      var r = btnExport.getBoundingClientRect();
      /* 预留高度按菜单项数校正：2026-10-14 增 HTML 本体项后共 6 项，140 已不足，
         提为 180，防低视口下菜单下缘出界。 */
      exportMenu.style.top = Math.min(window.innerHeight - 180, r.bottom + 8) + "px";
      exportMenu.style.right = Math.max(8, window.innerWidth - r.right) + "px";
      var mi = menuItems(exportMenu);
      if (mi.length) mi[0].focus();
    }
  });
  document.addEventListener("click", function (e) {
    if (exportMenu.classList.contains("open") && e.target.closest && !e.target.closest("#exportMenu") && !e.target.closest("#optExport")) closeExportMenu();
  });
  exportMenu.addEventListener("click", function (e) {
    var item = e.target.closest("button[data-x]");
    if (!item) return;
    e.stopPropagation();
    var kind = item.dataset.x;
    if (kind === "summary") {
      download(exportFileName("md"), window.exportSummaryText(), "text/markdown");
    } else if (kind === "json") {
      download(exportFileName("json"), JSON.stringify({ volumes: buildStructure(), metrics: { volumes: vols.length, chapters: chapters.length, sections: secIndex.length } }, null, 1), "application/json");
    } else if (kind === "csv") {
      var lines = [U("ui.export.csv_header")];
      buildStructure().forEach(function (v) {
        v.chapters.forEach(function (c) {
          c.sections.forEach(function (s) {
            /* 防电子表格公式注入：以 = + - @ 或制表/回车起首的单元格前置单引号 */
            var f = function (x) {
              var s = String(x);
              if (/^[=+\-@\t\r]/.test(s)) s = "'" + s;
              return '"' + s.replace(/"/g, '""') + '"';
            };
            lines.push([f(v.title), f(c.title), f(s.num), f(s.title), f(s.note)].join(","));
          });
        });
      });
      download(exportFileName("csv"), "\ufeff" + lines.join("\r\n"), "text/csv");
    } else if (kind === "pdf") {
      exportPdf();
    } else if (kind === "txt") {
      exportPlainText();
    } else if (kind === "html") {
      exportHtmlSelf();
    }
    closeExportMenu();
  });

  /* ---------- 9. 自校验徽标 ---------- */
  var metrics = document.querySelector(".doc-metrics");
  if (metrics) {
    var bad = [];
    vols.forEach(function (v) {
      var chs = Array.prototype.slice.call(v.querySelectorAll("h3.chapter[id]"));
      var nums = chs.map(function (c) { return parseInt((c.id.match(/-ch-(\d+)$/) || [0, 0])[1], 10); });
      nums.forEach(function (n, i) { if (n !== i + 1) bad.push(v.id + " 章号序列"); });
      chs.forEach(function (c) {
        var ul = c.nextElementSibling; if (!ul || !ul.classList || !ul.classList.contains("sections")) return;
        var chNo = (c.id.match(/-ch-(\d+)$/) || [0, 0])[1];
        Array.prototype.slice.call(ul.children).forEach(function (li, i) {
          var n = li.querySelector(":scope > .sec-num"); if (!n) return;
          var exp = chNo + "." + (i + 1);
          if (n.textContent.trim() !== exp) bad.push(c.id + " 节号 " + n.textContent.trim() + "≠" + exp);
          if (i === ul.children.length - 1 && /本章书目述评/.test(n.textContent) === false) { /* 述评可选 */ }
        });
      });
    });
    var d = document.createElement("div");
    // 2026-09-27：本行（序列自校验）在桌面端并入主行（见 §11 的 .sc-seq），仅移动端仍独立显示；
    // 故加 selfcheck-seq 供样式层在桌面端定向隐藏，文案与判据均不变。
    d.className = "selfcheck selfcheck-seq" + (bad.length ? " bad" : "");
    d.innerHTML = '<span class="dot"></span><span>' + (bad.length
      ? F("ui.selfcheck.bad_fmt", { n: bad.length })
      : U("ui.selfcheck.ok")) + "</span>";
    if (bad.length) console.warn(U("diag.toc_selfcheck"), bad.slice(0, 50));
    metrics.appendChild(d);
  }

  /* ---------- 10. 跨卷分工注关系图谱 ---------- */
  var graphPanel = document.createElement("dialog");
  graphPanel.className = "opt-panel"; graphPanel.id = "optPanelGraph";
  graphPanel.innerHTML = '<div class="box"><h3>' + U("ui.graph.h3") + '</h3>' +
    '<div class="hint">' + U("ui.graph.hint") + '<kbd>Esc</kbd>' + U("ui.graph.hint2") + '</div>' +
    '<svg class="graph" id="optGraph" role="img" aria-label="' + U("ui.graph.svg_aria") + '"></svg></div>';
  document.body.appendChild(graphPanel);
  function buildGraph() {
    var edges = {}, vids = vols.map(function (v) { return v.id; });
    vols.forEach(function (v) {
      var vi = vids.indexOf(v.id) + 1;
      Array.prototype.slice.call(v.querySelectorAll("h3.chapter[id]")).forEach(function (c) {
        var ul = c.nextElementSibling; if (!ul || !ul.classList || !ul.classList.contains("sections")) return;
        Array.prototype.slice.call(ul.children).forEach(function (li) {
          var a = li.querySelector(":scope > .src a[data-xref]"); if (!a) return;
          var t = a.getAttribute("href").replace(/^#/, "").match(/^vol-(\d+)/);
          if (!t) return;
          var vj = parseInt(t[1], 10);
          if (vj === vi) return;
          var k = Math.min(vi, vj) + "-" + Math.max(vi, vj);
          edges[k] = (edges[k] || 0) + 1;
        });
      });
    });
    var svg = document.getElementById("optGraph");

    var isMobile = window.innerWidth < 820;
    var W = isMobile ? 480 : 1120, H = isMobile ? 1220 : 820;
    var R = isMobile ? 120 : 240;
    var cx = W / 2, cy = isMobile ? 150 : H / 2;
    var FONT = isMobile ? 15 : 11.5;      // 标签字号（手机单列列表字号）
    var NFONT = isMobile ? 13 : 11;       // 节点数字字号
    var LINESIZE = isMobile ? 9 : 8;      // 每行最大字数
    var LINEGAP = isMobile ? 15 : 13;     // 行距
    var NSZ = isMobile ? 10 : 10;         // 节点圆半径
    var NEWB = isMobile ? 2.0 : 1.4;      // 节点描边宽
    var LW = isMobile ? 1.6 : 0.6;        // leader 线宽
    var N = vols.length, pos = {}, ang = {}, labels = [];
    function volShort(v) {
      var h = v.querySelector("h2");
      var name = __LB.pureTitle(h);
      var noMid = name.indexOf("  ");
      if (noMid >= 0) name = name.slice(noMid + 2);
      return name;
    }
    function volFull(v) {
      return __LB.pureTitle(v.querySelector("h2"));
    }
    vols.forEach(function (v, i) {
      var a = (i / N) * Math.PI * 2 - Math.PI / 2;
      pos[v.id] = [cx + R * Math.cos(a), cy + R * Math.sin(a)];
      ang[v.id] = a;
      labels.push({ id: v.id, idx: i, short: volShort(v), full: volFull(v) });
    });

    var max = 1; Object.keys(edges).forEach(function (k) { if (edges[k] > max) max = edges[k]; });
    var out = '<g stroke="var(--line-strong)" fill="none">';
    Object.keys(edges).forEach(function (k) {
      var p = k.split("-"), a = pos["vol-" + p[0]], b = pos["vol-" + p[1]];
      if (!a || !b) return;
      out += '<line x1="' + a[0] + '" y1="' + a[1] + '" x2="' + b[0] + '" y2="' + b[1] +
             '" stroke-width="' + (0.6 + 3 * edges[k] / max) + '" opacity="' + (0.25 + 0.5 * edges[k] / max) + '"/>';
    });
    out += "</g>";
    var GAP = isMobile ? 8 : 6;
    var LABEL_W_UNUSED = 0; /* 预留位，布局不依赖固定标签宽 */
    function chunk(s, n) {
      var r = [];
      while (s.length > 0) { r.push(s.slice(0, n)); s = s.slice(n); }
      return r.length ? r : [""];
    }

    if (isMobile) {
      var listTop = 320;
      var curY = listTop;
      labels.forEach(function (L) {
        var p = pos[L.id];
        out += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + NSZ + '" fill="var(--surface)" stroke="var(--accent)" stroke-width="' + NEWB + '"/>' +
               '<text x="' + p[0] + '" y="' + (p[1] + 3.6) + '" font-size="' + NFONT + '" font-weight="700" fill="var(--accent)" text-anchor="middle">' + (L.idx + 1) + "</text>";

        var mLines = chunk((L.idx + 1) + ' ' + L.short, LINESIZE);
        var tspansM = "";
        mLines.forEach(function (ln, li) {
          tspansM += '<tspan x="20" dy="' + (li === 0 ? 0 : LINEGAP) + '">' + ln + "</tspan>";
        });
        out += '<text x="20" y="' + curY + '" font-size="' + FONT + '" fill="var(--ink)" class="graph-label" data-vol="' + L.id + '"><title>' + L.full + '</title>' + tspansM + "</text>";
        curY += mLines.length * LINEGAP + 8;
      });
      out += '<text x="20" y="' + (H - 10) + '" font-size="11" fill="var(--faint)">' + U("ui.graph.note") + '</text>';
    } else {
    function layoutSide(group, dirX) {
      group.sort(function (a, b) { return pos[a.id][1] - pos[b.id][1]; });
      var prevBottom = -1e9;
      group.forEach(function (L) {
        var p = pos[L.id];
        var lines = chunk(L.short, LINESIZE);
        var totalH = lines.length * LINEGAP;
        var topY = p[1] - totalH / 2;
        if (topY < prevBottom + GAP) topY = prevBottom + GAP;
        prevBottom = topY + totalH;
        var anchor = dirX < 0 ? "end" : "start";
        var x = dirX < 0 ? p[0] - NSZ - 2 : p[0] + NSZ + 2;
        var tspans = "";
        lines[0] = "第" + (L.idx + 1) + "卷 " + lines[0];
        lines.forEach(function (ln, li) {
          tspans += '<tspan x="' + x + '" y="' + (topY + li * LINEGAP) + '">' + ln + "</tspan>";
        });
        out += '<line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + (x + dirX * 2) + '" y2="' + (topY + LINEGAP / 2) +
               '" stroke="var(--muted)" stroke-width="' + LW + '" opacity="0.55"/>';
        out += '<text x="' + x + '" y="' + topY + '" font-size="' + FONT + '" fill="var(--ink)" text-anchor="' + anchor + '" class="graph-label" data-vol="' + L.id + '"><title>' + L.full + "</title>" + tspans + "</text>";
      });
    }
    var leftGroup = [], rightGroup = [];
    labels.forEach(function (L) {
      if (Math.cos(ang[L.id]) < 0) leftGroup.push(L); else rightGroup.push(L);
    });
    layoutSide(leftGroup, -1);
    layoutSide(rightGroup, 1);
    /* 节点（圆圈数字 + 完整名 title） */
    labels.forEach(function (L) {
      var p = pos[L.id];
      out += '<g class="graph-node" data-vol="' + L.id + '"><title>' + L.full + "</title>" +
             '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + NSZ + '" fill="var(--surface)" stroke="var(--accent)" stroke-width="' + NEWB + '"/>' +
             '<text x="' + p[0] + '" y="' + (p[1] + 3.6) + '" font-size="' + NFONT + '" font-weight="700" fill="var(--accent)" text-anchor="middle">' + (L.idx + 1) + "</text></g>";
    });
    }
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.innerHTML = out;
    /* 点击放大：标签字体放大并置前，再点还原 */
    Array.prototype.slice.call(svg.querySelectorAll("text.graph-label")).forEach(function (t) {
      t.addEventListener("click", function (e) {
        e.stopPropagation();
        var was = this.classList.contains("zoomed");
        svg.querySelectorAll("text.graph-label.zoomed").forEach(function (x) { x.classList.remove("zoomed"); });
        if (!was) this.classList.add("zoomed");
      });
    });
  }
  var bg = document.getElementById("optGraphBtn");
  if (bg) bg.addEventListener("click", function () { __LB.decorateDialogs(); buildGraph(); __LB.openDialog(graphPanel); });

  /* ---------- 11. 面板关闭 / 键盘快捷键 ---------- */
  function closePanels() { __LB.closeDialogs(false); }
  document.addEventListener("keydown", function (e) {
    var tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea") { if (e.key === "Escape") { __LB.closeDialogs(true); e.target.blur(); } return; }
    /* 焦点位于弹层/菜单内时，不触发页面级单键快捷键 */
    if (e.target.closest && (e.target.closest(".opt-panel") || e.target.closest('[role="menu"]'))) return;
    if (e.key === "Escape") { __LB.closeDialogs(true); return; }
    if (e.key === "/") { e.preventDefault(); if (btnSearch) document.getElementById("optSearch").click(); return; }
    if (e.key === "t") { window.scrollTo({ top: 0, behavior: __LB.scrollBehavior() }); return; }
    if (e.key === "n" || e.key === "p") {
      var ids = chapters.map(function (c) { return c.id; });
      var cur = -1;
      for (var i = 0; i < ids.length; i++) { var el = document.getElementById(ids[i]); if (el && el.getBoundingClientRect().top < 140) cur = i; }
      var next = e.key === "n" ? Math.min(cur + 1, ids.length - 1) : Math.max(cur - 1, 0);
      goInPage(ids[next]);   /* 6a：n／p 亦走历史中性跳转（原赋值 location.hash 会 push 条目） */
    }
  });

  /* ---------- 12. 主题跟随系统（无本地选择时） ---------- */
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    function follow() {
      if (stor.get("sme-theme")) return;
      document.documentElement.setAttribute("data-theme", mq.matches ? "oled" : "light");
    }
    follow();
    if (mq.addEventListener) mq.addEventListener("change", follow);
  }

  /* 供哈希跳转使用 */
  __LB.jump = jump;
  } catch (err) {
    if (window.console && console.warn) console.warn(U("diag.generic"), err);
  }
})();
