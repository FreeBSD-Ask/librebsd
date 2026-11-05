'use strict';
/* 非正文文案层（2026-09-30 立）：装配器在行为脚本之前注入
   （装配器在行为脚本之前注入的 id 为 ui-strings 的 application/json 脚本），此处解析为 __UI；
   U(键[, 默认]) 取文案、F(键, 对象) 做 {n} 式插值。
   文案的**唯一真相源**＝ `05-卷册大纲/目录/data/ui-strings.json`（改文案只改该文件后重装）。 */
var __UI = (function () {
  try { return JSON.parse(document.getElementById("ui-strings").textContent); } catch (e) { return {}; }
})();
function U(k, d) { var v = __UI[k]; return v === undefined ? (d === undefined ? k : d) : v; }
function F(k, o) {
  return String(U(k)).replace(/\{(\w+)\}/g, function (m, n) {
    return (o && Object.prototype.hasOwnProperty.call(o, n)) ? String(o[n]) : m;
  });
}
/* 行为层整体运行于严格模式：隐式全局、静默失败、八进制字面量等一律抛错，
   以便缺陷在开发期即暴露，而非在生产期静默降级。 */
  /* 单一命名空间：本层全部对外钩子与工具函数收敛于此，避免散落的隐式全局。 */
  var __LB = (function () {
  var policy = (window.trustedTypes && window.trustedTypes.createPolicy) ? window.trustedTypes.createPolicy('librebsd', { createHTML: function (html) {
    try {
      if (window.Sanitizer && Sanitizer.supported) { return new Sanitizer().sanitizeToString(String(html)); }
      var d = new DOMParser().parseFromString(String(html), 'text/html'); var r = d.body;
      r.querySelectorAll('script,iframe,object,embed,link,meta,style,form,base,template').forEach(function (e) { e.remove(); });
      r.querySelectorAll('*').forEach(function (e) {
        for (var i = e.attributes.length - 1; i >= 0; i--) {
          var a = e.attributes[i], n = a.name.toLowerCase();
          if (n.indexOf('on') === 0 || ((n === 'href' || n === 'src' || n === 'xlink:href') && /^\s*javascript:/i.test(a.value || ''))) e.removeAttribute(a.name);
        }
      });
      return r.innerHTML;
    } catch (err) { return String(html).replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  } }) : null;
  function ttt(h) { return policy ? policy.createHTML(h) : h; }

  /* 尊重“减少动效”偏好：显式 behavior 会覆盖 CSS 的 scroll-behavior，故须在 JS 侧判定 */
  var rmq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
  /* 墨水屏（2026-10-22）：慢刷新屏上任何过渡与补间都既耗刷新又留残影，故 eink 与
     “减少动效”偏好同等对待——任一命中即走静态路径（瞬时落点、零交叉淡入）。 */
  function inkTheme() {
    var r = document.documentElement;
    return !!r && r.getAttribute("data-theme") === "eink";
  }
  function staticMode() { return inkTheme() || !!(rmq && rmq.matches); }
  function scrollBehavior() { return staticMode() ? "auto" : "smooth"; }

  /* 对话框收口：关闭面板并把焦点交回其触发按钮（触发按钮由 aria-controls 反查）。
     dialog 化（2026-10-11）：面板为原生 <dialog>，一并调 close()（原生 Esc 关闭后
     的 .open 同步由 close 事件监听兜底）。 */
  function closeDialogs(restoreFocus) {
    document.querySelectorAll(".opt-panel.open").forEach(function (p) {
      p.classList.remove("open");
      if (typeof p.close === "function" && p.open) { try { p.close(); } catch (e) {} }
      if (!restoreFocus) return;
      var t = p.id ? document.querySelector('[aria-controls="' + p.id + '"]') : null;
      if (t && t.focus) { try { t.focus(); } catch (e) {} }
    });
  }

  /* dialog 化初始化（幂等，由 decorateDialogs 对全部面板挂接）：
     ①原生 close 事件（含 Esc 的 cancel→close 路径）同步移除 .open 类；
     ②点击 dialog 本体（遮罩区，.box 之外）视为“点遮罩关闭”，替代原 .scrim 监听。 */
  function initDialog(p) {
    if (!p || p.dataset.dlgInit === "1") return;
    p.dataset.dlgInit = "1";
    p.addEventListener("close", function () { p.classList.remove("open"); });
    p.addEventListener("click", function (e) { if (e.target === p) closeDialogs(true); });
  }

  /* 面板开启：类切换（兼容既有选择器与断言）＋原生模态 showModal——顶层置顶、
     背景 inert、Esc 关闭与焦点归还均由浏览器内置；不支持 showModal 时以 open 属性兜底。 */
  function openDialog(p) {
    if (!p) return;
    p.classList.add("open");
    if (typeof p.showModal === "function") {
      if (!p.open) { try { p.showModal(); } catch (e) { p.setAttribute("open", ""); } }
    } else {
      p.setAttribute("open", "");
    }
  }

  /* 为全部面板补对话框语义（role/aria-modal/aria-labelledby）＋ dialog 化初始化，幂等 */
  function decorateDialogs() {
    document.querySelectorAll(".opt-panel").forEach(function (p) {
      initDialog(p);
      if (p.getAttribute("role") === "dialog") return;
      var h = p.querySelector("h3");
      if (h) {
        if (!h.id) h.id = (p.id || "optPanel") + "-title";
        p.setAttribute("aria-labelledby", h.id);
      }
      p.setAttribute("role", "dialog");
      p.setAttribute("aria-modal", "true");
    });
  }

  /* Tab 焦点圈定：模态面板打开时不得逃逸到背景 */
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Tab") return;
    var open = document.querySelector(".opt-panel.open");
    if (!open) return;
    var f = open.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), select, textarea, [tabindex]:not([tabindex="-1"])');
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1], ae = document.activeElement;
    if (!open.contains(ae)) { e.preventDefault(); first.focus(); return; }
    if (e.shiftKey && ae === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && ae === last) { e.preventDefault(); first.focus(); }
  }, true);

  /* 标题净化：剥离**运行时注入**的装饰元素，返回目录“内容层”原文。
     对象含：卷/章计数徽标（.vol-badge/.ch-badge）、溯源注徽标与注文（.note-badge/.src）、
     长节名折叠控件（.t-short/.t-more）、节号（.sec-num）及浮层类（.path/.pv）。
     长节名折叠态（li.long-title）另取 .t-full 完整标题——否则会拼出“短标题＋展开＋完整标题”。
     2026-11-06（ADR-0020）：增 .subsections——节 li 含嵌套小节列表时，小节文本不得拼入节题。 */
  function pureTitle(el) {
    if (!el) return "";
    var clone = el.cloneNode(true);
    var full = clone.querySelector(".t-full");
    if (full) return full.textContent.trim();
    clone.querySelectorAll(".vol-badge, .ch-badge, .note-badge, .t-more, .t-short, .src, .sec-num, .path, .pv, .subsections").forEach(function (n) { n.remove(); });
    return clone.textContent.trim();
  }

  /* View Transitions（2026-10-11 载体层批次）：视觉状态切换（主题／研阅）走原生交叉淡入；
     不支持该 API、用户偏好减少动效、或当前为墨水屏主题时同步执行（零副作用降级）。 */
  function viewTransition(fn) {
    if (typeof document.startViewTransition === "function" && !staticMode()) {
      try { return document.startViewTransition(fn); } catch (e) {}
    }
    fn();
    return null;
  }

  return { ttt: ttt, scrollBehavior: scrollBehavior, closeDialogs: closeDialogs,
           decorateDialogs: decorateDialogs, openDialog: openDialog, viewTransition: viewTransition,
           staticMode: staticMode, rmq: rmq, pureTitle: pureTitle };
  })();

/* ========== 行为层（单一块，按序合并自 3 个历史 script 块） ========== */

/* 块 1 doc.js 嵌入：目录引擎 */

/* embedded from assets/doc.js */
(function () {
  function setupToc() {
    const leftNav = document.querySelector(".toc-left");
    const rightNav = document.querySelector(".toc-right");
    const page = document.querySelector(".doc-page");
    if (!leftNav || !rightNav || !page) return;

    const volumes = Array.from(page.querySelectorAll("section[id^='vol-']"));
    const chapters = Array.from(page.querySelectorAll("h3[id]"));

    chapters.forEach((ch) => {
      const ul = ch.nextElementSibling;
      if (!ul || !ul.classList || !ul.classList.contains("sections")) return;
      /* 2026-11-06（ADR-0020）：:scope > li 只处理节——嵌套小节 li 的静态 id
         （…-sub-P 形制）由装配器给出，不得在此被改写成无 sub- 段形态。 */
      ul.querySelectorAll(":scope > li").forEach((li) => {
        const secNum = li.querySelector(":scope > .sec-num");
        if (!secNum) return;
        const num = secNum.textContent.trim().replace(/\./g, "-");
        li.id = ch.id + "-sec-" + num;
      });
    });

    const leftList = document.createElement("ul");
    leftList.className = "toc-left-list";
    const volItems = [];
    volumes.forEach((vol) => {
      const h2 = vol.querySelector("h2");
      const volItem = document.createElement("li");
      volItem.className = "toc-vol";
      const fold = document.createElement("button");
      fold.type = "button";
      fold.className = "toc-fold";
      fold.setAttribute("aria-label", U("ui.fold.aria"));
      fold.innerHTML = '<span class="fold-arrow">▾</span>';
      const volLink = document.createElement("a");
      volLink.href = "#" + vol.id;
      volLink.dataset.target = vol.id;
      volLink.textContent = __LB.pureTitle(h2);
      volItem.appendChild(fold);
      volItem.appendChild(volLink);

      const chList = document.createElement("ul");
      chList.className = "toc-ch-list";
      const chItems = [];
      vol.querySelectorAll("h3[id]").forEach((ch) => {
        const chItem = document.createElement("li");
        const chLink = document.createElement("a");
        chLink.href = "#" + ch.id;
        chLink.dataset.target = ch.id;
        chLink.textContent = __LB.pureTitle(ch);
        chItem.appendChild(chLink);
        chList.appendChild(chItem);
        chItems.push({ li: chItem, link: chLink, text: chLink.textContent.toLowerCase() });
      });
      fold.addEventListener("click", function () {
        volItem.classList.toggle("collapsed");
      });
      volItem.appendChild(chList);
      leftList.appendChild(volItem);
      volItems.push({
        li: volItem,
        link: volLink,
        text: volLink.textContent.toLowerCase(),
        chItems: chItems,
      });
    });
    leftNav.replaceChildren(leftList);

    const searchWrap = document.createElement("div");
    searchWrap.className = "toc-search";
    const searchInput = document.createElement("input");
    searchInput.type = "search";
    searchInput.placeholder = U("ui.search.placeholder");
    searchInput.id = "tocSearchInput";
    searchInput.name = "tocSearch";
    searchInput.setAttribute("aria-label", U("ui.search.aria"));
    searchWrap.appendChild(searchInput);
    leftNav.insertBefore(searchWrap, leftList);

    searchInput.addEventListener("input", function () {
      const q = this.value.trim().toLowerCase();
      leftNav.classList.toggle("searching", q !== "");
      volItems.forEach((vol) => {
        const volHit = q !== "" && vol.text.includes(q);
        let anyChHit = false;
        vol.chItems.forEach((ch) => {
          const hit = q !== "" && (ch.text.includes(q) || volHit);
          ch.li.style.display = q === "" || hit ? "" : "none";
          if (hit) anyChHit = true;
        });
        vol.li.style.display = q === "" || volHit || anyChHit ? "" : "none";
      });
    });

    const chapterSecMap = new Map();
    chapters.forEach((ch) => {
      const ul = ch.nextElementSibling;
      const secs = [];
      if (ul && ul.classList && ul.classList.contains("sections")) {
        /* 2026-11-06（ADR-0020）：:scope > li 只收节；小节入 subs（右栏嵌套渲染与静态 TOC 同构）。 */
        ul.querySelectorAll(":scope > li").forEach((li) => {
          const secNum = li.querySelector(":scope > .sec-num");
          const title = __LB.pureTitle(li);
          const subs = [];
          const subUl = li.querySelector(":scope > ul.subsections");
          if (subUl) {
            subUl.querySelectorAll(":scope > li").forEach((sli) => {
              const sn = sli.querySelector(":scope > .sec-num");
              subs.push({ id: sli.id, num: sn ? sn.textContent.trim() : "", title: __LB.pureTitle(sli) });
            });
          }
          secs.push({ id: li.id, num: secNum ? secNum.textContent.trim() : "", title: title, subs: subs });
        });
      }
      chapterSecMap.set(ch.id, secs);
    });

    const rightCache = new Map();
    function renderRight(chapterId) {
      const ch = chapters.find((c) => c.id === chapterId);
      if (!ch) return;
      let cached = rightCache.get(chapterId);
      if (!cached) {
        const title = document.createElement("div");
        title.className = "toc-sec-title";
        title.textContent = __LB.pureTitle(ch);
        const ul = document.createElement("ul");
        ul.className = "toc-sec-list";
        (chapterSecMap.get(chapterId) || []).forEach((sec) => {
          const li = document.createElement("li");
          const a = document.createElement("a");
          a.href = "#" + sec.id;
          a.dataset.target = sec.id;
          a.textContent = sec.title;
          if (sec.num) {
            const n = document.createElement("span");
            n.className = "sec-num";
            n.textContent = sec.num;
            a.insertBefore(n, a.firstChild);
          }
          li.appendChild(a);
          /* 2026-11-06（ADR-0020）：节下嵌套渲染小节（与静态 TOC 同构；无小节零差异）。 */
          if (sec.subs && sec.subs.length) {
            const su = document.createElement("ul");
            su.className = "toc-sub-list";
            sec.subs.forEach((sb) => {
              const sli = document.createElement("li");
              const sa = document.createElement("a");
              sa.href = "#" + sb.id;
              sa.dataset.target = sb.id;
              sa.textContent = sb.title;
              if (sb.num) {
                const sn = document.createElement("span");
                sn.className = "sec-num";
                sn.textContent = sb.num;
                sa.insertBefore(sn, sa.firstChild);
              }
              sli.appendChild(sa);
              su.appendChild(sli);
            });
            li.appendChild(su);
          }
          ul.appendChild(li);
        });
        cached = { title: title, ul: ul };
        rightCache.set(chapterId, cached);
      }
      rightNav.replaceChildren(cached.title, cached.ul);
    }

    const leftLinks = Array.from(leftNav.querySelectorAll("a[data-target]"));

    function findScrollParent(link) {
      let el = link.parentElement;
      while (el) {
        const st = getComputedStyle(el);
        if (/(auto|scroll)/.test(st.overflowY)) return el;
        el = el.parentElement;
      }
      return null;
    }
    function scrollLinkIntoPanel(link) {
      if (!link) return;
      const volLi = link.closest(".toc-vol");
      if (volLi) volLi.classList.remove("collapsed");
      const sp = findScrollParent(link);
      if (!sp) return;
      const PAD = 12;

      const lr = link.getBoundingClientRect();
      const sr = sp.getBoundingClientRect();
      const above = lr.top - sr.top;
      const below = (sr.top + sr.height) - (lr.top + lr.height);
      if (above < PAD) {
        sp.scrollTop += above - PAD;
      } else if (below < PAD) {
        sp.scrollTop += PAD - below;
      }
    }

    function onTocClick(e) {
      const a = e.target.closest && e.target.closest("a[data-target]");
      if (!a) return;
      if (a.scrollIntoView) {
        try { a.scrollIntoView({ block: 'nearest', inline: 'nearest' }); } catch (e2) { a.scrollIntoView(); }
      }
    }
    document.querySelectorAll(".toc-left a[data-target], .toc-right a[data-target]").forEach(function (a) {
      a.addEventListener("click", onTocClick);
    });

    function setActive(id, volId) {
      let focusLink = null;
      leftLinks.forEach((link) => {
        const t = link.dataset.target;
        const on = t === id || (volId && t === volId);
        link.classList.toggle("active", on);
        if (on && t === id) focusLink = link;
      });
      if (!focusLink && volId) {
        focusLink = leftLinks.find((l) => l.dataset.target === volId) || null;
      }
      scrollLinkIntoPanel(focusLink);
    }

    let currentChapterId = null;
    let currentVolId = null;

    let hashSyncArmed = false;
    let offsetsDirty = true;
    const volTops = new Map();
    const chTops = new Map();
    const secTops = new Map();
    function rebuildOffsets() {
      volTops.clear();
      chTops.clear();
      secTops.clear();

      /* content-visibility 复活（2026-10-11 载体层批次）：量测前把跳过态卷临时置为 visible，
         量测后按实测高改写各卷 contain-intrinsic-size（占位空间=真实空间：滚高零漂移、offsets 恒准），
         再复原 auto。特性不支持时整段为空操作（原“height < 40”条件系零占位原型遗留，已废）。 */
      var cvRestored = [];
      if (window.CSS && CSS.supports && CSS.supports('content-visibility: auto')) {
        volumes.forEach(function (v) {
          if (getComputedStyle(v).contentVisibility === 'auto') {
            v.style.contentVisibility = 'visible'; cvRestored.push(v);
          }
        });
      }
      volumes.forEach((v) => volTops.set(v.id, v.offsetTop));
      chapters.forEach((c) => {
        chTops.set(c.id, c.offsetTop);
        const ul = c.nextElementSibling;
        if (ul && ul.classList && ul.classList.contains("sections")) {
          Array.prototype.slice.call(ul.children).forEach((li) => {
            const secNum = li.querySelector(":scope > .sec-num");
            if (secNum) secTops.set(li.id, li.offsetTop);
          });
        }
      });
      if (cvRestored.length) {
        cvRestored.forEach(function (v) {
          v.style.containIntrinsicSize = 'auto ' + Math.ceil(v.getBoundingClientRect().height) + 'px';
        });
        cvRestored.forEach(function (v) { v.style.contentVisibility = ''; });
      }
      offsetsDirty = false;
    }

    function updateCurrentChapter() {
      if (offsetsDirty) rebuildOffsets();
      const line = window.scrollY + Math.round(window.innerHeight * 0.4);
      let currentVol = null;
      for (const v of volumes) {
        if (volTops.get(v.id) <= line) currentVol = v;
        else break;
      }
      let current = null;
      for (const ch of chapters) {
        if (chTops.get(ch.id) <= line) current = ch;
        else break;
      }
      let target = current;
      if (currentVol && current && !currentVol.contains(current)) {
        const firstCh = currentVol.querySelector("h3[id]");
        target = firstCh || current;
      }
      const id = target ? target.id : (chapters[0] ? chapters[0].id : null);
      const volId = currentVol ? currentVol.id : (volumes[0] ? volumes[0].id : null);
      const changed = id !== currentChapterId || volId !== currentVolId;
      currentChapterId = id;
      currentVolId = volId;
      if (changed) {
        setActive(id, volId);
        renderRight(id);
      }

      var navs = [leftNav];
      var drawerNav = document.querySelector('#tocDrawer .toc-left, #tocDrawer nav');
      if (drawerNav && drawerNav !== leftNav) navs.push(drawerNav);
      navs.forEach(function (nav) {
        var actEl = nav.querySelector('a.active');
        var volLink = volId ? nav.querySelector('a[data-target="' + volId + '"]') : null;
        if (volLink && nav.dataset.followVol !== volId) {
          try { volLink.scrollIntoView({ block: 'start', inline: 'nearest' }); } catch (e3) { volLink.scrollIntoView(); }
          nav.dataset.followVol = volId;
        } else if (actEl && actEl.scrollIntoView) {
          try { actEl.scrollIntoView({ block: 'nearest', inline: 'nearest' }); } catch (e3) { actEl.scrollIntoView(); }
        }
      });
      updateCurrentSection(id);
      try {
        if (hashSyncArmed && !pendingInitialHash) history.replaceState(null, "", "#" + id);
      } catch (e) {}
    }
    function updateCurrentSection(chapterId) {
      if (!chapterId) return;
      const ch = document.getElementById(chapterId);
      if (!ch) return;
      const secLine = window.scrollY + Math.round(window.innerHeight * 0.5);
      const ul = ch.nextElementSibling;
      if (!ul || !ul.classList || !ul.classList.contains("sections")) return;
      const lis = Array.prototype.slice.call(ul.children);
      let currentSec = null;
      for (const li of lis) {
        if (!li.id || !secTops.has(li.id)) continue;
        if (secTops.get(li.id) <= secLine) currentSec = li;
        else break;
      }
      if (__LB.stepSync) __LB.stepSync(chapterId, currentSec ? currentSec.id : null);
    }

  var stepPend = null;
  var lastStepY = -1;
  var lastStepCh = "";
  function rAFStep() {
    stepPend = false;
    var chId = currentChapterId;
    if (!chId) return;
    var y = window.scrollY;
    if (y === lastStepY && chId === lastStepCh) return;
    lastStepY = y; lastStepCh = chId;
    updateCurrentSection(chId);
  }
  function onScroll() {
    hashSyncArmed = true;
    updateCurrentChapter();
    if (!stepPend) { stepPend = true; requestAnimationFrame(rAFStep); }
  }
    function onLayoutChange() {
      offsetsDirty = true;
      updateCurrentChapter();
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onLayoutChange);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(onLayoutChange);
    }

    var pendingInitialHash = false;
    var initialHash = decodeURIComponent(location.hash.slice(1));
    if (initialHash) {
      var initialEl = document.getElementById(initialHash);
      if (initialEl) {
        pendingInitialHash = true;
        initialEl.scrollIntoView({ behavior: "instant" });
        setTimeout(function () {
          pendingInitialHash = false;
        }, 1200);
      }
    }
    updateCurrentChapter();

    document.addEventListener("keydown", function (e) {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (e.target && /INPUT|TEXTAREA|SELECT/.test(e.target.tagName)) return;
      var k = e.key.toLowerCase();
      if (k !== "j" && k !== "k") return;
      e.preventDefault();
      var idx = chapters.findIndex((c) => c.id === currentChapterId);
      if (idx < 0) idx = 0;
      var next = k === "j" ? Math.min(idx + 1, chapters.length - 1) : Math.max(idx - 1, 0);
      var t = chapters[next];
      if (!t) return;

      t.scrollIntoView({ behavior: __LB.scrollBehavior(), block: "start" });
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    setupToc();
  });
})();
(function () {
  var btn = document.getElementById("themeToggle");
  if (!btn) return;
  var root = document.documentElement;
  var ORDER = ["light", "oled", "eink"];
  var GLYPH = { light: "☾", oled: "●", eink: "□" };
  var FALL = { light: "#F9F5F0", oled: "#000000", eink: "#ffffff" };
  function apply(theme) {
    root.setAttribute("data-theme", theme);
    btn.textContent = GLYPH[theme] || "☾";
    /* theme-color 须随主题同步，否则移动端浏览器 UI 会与页面主题脱钩 */
    var mt = document.querySelector('meta[name="theme-color"]');
    if (mt) {
      var pg = "";
      try { pg = getComputedStyle(root).getPropertyValue("--page").trim(); } catch (e) {}
      mt.setAttribute("content", pg || FALL[theme] || "#F9F5F0");
    }
  }
  /* 初值已由 head 内 theme-preset.js 同步写入（避免 FOUC），此处只读取，不重复推导 */
  var cur = root.getAttribute("data-theme");
  if (ORDER.indexOf(cur) < 0) cur = "light";
  apply(cur);
  btn.addEventListener("click", function () {
    var now = root.getAttribute("data-theme");
    var idx = ORDER.indexOf(now);
    var next = ORDER[(idx < 0 ? 0 : idx + 1) % ORDER.length];
    try { localStorage.setItem("sme-theme", next); } catch (e) {}
    /* 墨水屏切换（2026-10-22）：进出 eink 一律瞬时落位——切入时 inkTheme() 尚为旧值，
       故须另判目标主题，否则会留下一次交叉淡入。 */
    if (next === "eink") { apply(next); return; }
    __LB.viewTransition(function () { apply(next); });
  });
  /* 未显式选择过时，跟随系统主题变化；单色／慢刷新屏直接落墨水屏 */
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onSys = function () {
      var s = null; try { s = localStorage.getItem("sme-theme"); } catch (e) {}
      if (s === "dark") s = "oled";   /* 153 批：历史值迁移 */
      if (ORDER.indexOf(s) < 0) {
        var mono = false, slow = false;
        try { mono = window.matchMedia("(monochrome: 1)").matches; } catch (e1) {}
        try { slow = window.matchMedia("(update: slow)").matches; } catch (e2) {}
        apply(mono || slow ? "eink" : (mq.matches ? "oled" : "light"));
      }
    };
    if (mq.addEventListener) mq.addEventListener("change", onSys); else if (mq.addListener) mq.addListener(onSys);
  }
})();

(function () {
  var btn = document.getElementById("tocToggle");
  var drawer = document.getElementById("tocDrawer");
  var scrim = document.getElementById("tocScrim");
  if (!btn || !drawer) return;
  function setOpen(open) {
    drawer.classList.toggle("open", open);
    if (scrim) scrim.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
    btn.setAttribute("aria-expanded", String(open));
    btn.setAttribute("aria-label", open ? U("ui.toc.close") : U("ui.toc.open"));
  }
  btn.addEventListener("click", function () {
    setOpen(!drawer.classList.contains("open"));
  });
  if (scrim) {
    scrim.addEventListener("click", function () {
      setOpen(false);
    });
  }
  drawer.addEventListener("click", function (e) {
    if (e.target.closest("a")) setOpen(false);
  });
})();

(function () {
  /* 标题净化器统一由 __LB.pureTitle 提供（本块原有一份同名局部实现，已上提去重） */
  window.exportSummaryText = function () {
    var page = document.querySelector(".doc-page");
    var vols = Array.from(page.querySelectorAll("section[id^='vol-']"));
    var chCount = 0;
    var secCount = 0;
    var lines = [];
    lines.push("# Summary");
    lines.push("");
    lines.push(U("ui.export.sum_title"));
    lines.push(U("ui.export.sum_source"));
    lines.push(U("ui.export.sum_note"));
    lines.push(U("ui.export.sum_time") + new Date().toLocaleString("zh-CN", { hour12: false }));
    lines.push("");
    lines.push(U("ui.export.sum_head"));
    lines.push("");
    vols.forEach(function (vol, vi) {
      var vNo = String(vi + 1).padStart(2, "0");
      var h2 = vol.querySelector("h2");
      lines.push("### " + __LB.pureTitle(h2));
      lines.push("");
      var chInVol = 0;
      vol.querySelectorAll("h3[id]").forEach(function (ch) {
        chCount++;
        chInVol++;
        var chTitle = __LB.pureTitle(ch);
        var m = chTitle.match(/第\s*(\d+)\s*章/);
        var chNo = m ? m[1] : String(chInVol);
        var chDir = "第" + vNo + "卷/第" + chNo + "章";
        lines.push("- [" + chTitle + "](./" + chDir + "/概述.md)");
        var ul = ch.nextElementSibling;
        if (!ul || !ul.classList || !ul.classList.contains("sections")) return;
        ul.querySelectorAll("li").forEach(function (li) {
          secCount++;
          var numEl = li.querySelector(".sec-num");
          var num = numEl ? numEl.textContent.trim() : "";
          /* 节号已由 .sec-num 的移除而剥离，此处不得再做子串替换：
             否则题文本身以节号字面量开头时（如 “4.2BSD 的版本组成与前代继承”）会被误删开头。 */
          var title = __LB.pureTitle(li);
          lines.push("  - [" + num + " " + title + "](./" + chDir + "/" + num + ".md)");
        });
      });
      lines.push("");
    });
    lines.push("");
    lines.push("---");
    lines.push("");
    lines.push(F("ui.export.stats_fmt", { v: vols.length, c: chCount, s: secCount }));
    return lines
      .join("\n")
      .replace(/\u3000/g, " ")
      .replace(/\u00a0/g, " ")
      .replace(/[ \t]+$/gm, "");
  };
})();

(function () {
  var bar = document.createElement("div");
  bar.className = "read-progress";
  document.body.appendChild(bar);
  function update() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var r = max > 0 ? window.scrollY / max : 0;
    bar.style.transform = "scaleX(" + r + ")";
  }
  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
})();

(function () {
  var btn = document.getElementById("backToTop");
  if (!btn) return;
  var LONG_PRESS_MS = 600;
  var pressTimer = null;
  var longPressed = false;

  function nearTop() { return window.scrollY <= 400; }
  function setGlyph() {
    /* 视觉语义：在页面顶部附近→按钮变“到底部”；否则→“回顶部” */
    btn.textContent = nearTop() ? "↓" : "↑";
    btn.setAttribute("aria-label", nearTop() ? U("ui.top.bottom") : U("ui.top.top"));
  }
  function toggle() {
    /* 2026-09-30（98 号文 §八·乙-2）：原判据 `window.scrollY > 400 || nearTop()` 恒为真
       —— nearTop() 即 `scrollY <= 400`，两式互补。本按钮设计为“常显”（顶部时字形“↓”
       表示到底部，其余“↑”表示回顶部），故直书意图，去掉冗余死条件。 */
    btn.classList.add("visible");
    setGlyph();
  }
  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: __LB.scrollBehavior() });
  }
  function scrollToBottom() {
    window.scrollTo({ top: document.documentElement.scrollHeight, behavior: __LB.scrollBehavior() });
  }

  /* 长按检测：pointer 事件统一鼠标/触摸；contextmenu 抑制长按弹菜单 */
  function pressStart(e) {
    if (e.button && e.button !== 0) return; // 仅左键/触摸
    longPressed = false;
    clearTimeout(pressTimer);
    pressTimer = setTimeout(function () {
      longPressed = true;
      /* 长按达成：立即到底部 */
      scrollToBottom();
    }, LONG_PRESS_MS);
  }
  function pressEnd() {
    clearTimeout(pressTimer);
    pressTimer = null;
    /* 长按达成时保留 longPressed 标记到 click 处理器消费（勿在此重置）——
       pointerup 的合成 click 紧随其后，若此处清零会漏吞导致回顶 */
  }

  btn.addEventListener("pointerdown", pressStart);
  btn.addEventListener("pointerup", pressEnd);
  btn.addEventListener("pointerleave", function () { clearTimeout(pressTimer); pressTimer = null; });
  btn.addEventListener("pointercancel", function () { clearTimeout(pressTimer); pressTimer = null; });
  btn.addEventListener("contextmenu", function (e) { e.preventDefault(); }); // 触摸长按禁系统菜单
  btn.addEventListener("click", function (e) {

    if (longPressed) { longPressed = false; return; }
    /* 2026-10-10（128 号文批 5，ykla 报障：向下的按钮失效）：原实现恒调 scrollToTop()——
       而顶部附近字形为 ↓（语义即到底部），点击仍回顶（原地不动），表现为失效。
       现按字形状态分派：顶部附近（scrollY 不超 400）回到底部，否则回顶部。 */
    if (nearTop()) { scrollToBottom(); } else { scrollToTop(); }
  });
  window.addEventListener("scroll", toggle, { passive: true });
  window.addEventListener("scroll", setGlyph, { passive: true });
  toggle();
  setGlyph();
})();

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
    /* 2026-09-26 ykla 裁定：面包屑只展示卷 */
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

  /* ---------- 6a. 页内锚点历史中性化（2026-10-14 ykla 令） ----------
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
          /* 2026-11-06（ADR-0020）：:scope > li 只收节；小节入 subs（导出四格式随之含小节层级）。 */
          Array.prototype.slice.call(ul.querySelectorAll(":scope > li")).forEach(function (li) {
            var n = li.querySelector(":scope > .sec-num"); if (!n) return;
            var src = li.querySelector(":scope > .src");
            var subs = [];
            var subUl = li.querySelector(":scope > ul.subsections");
            if (subUl) {
              Array.prototype.slice.call(subUl.querySelectorAll(":scope > li")).forEach(function (sli) {
                var sn = sli.querySelector(":scope > .sec-num"); if (!sn) return;
                var ssrc = sli.querySelector(":scope > .src");
                subs.push({ id: sli.id, num: sn.textContent.trim(), title: __LB.pureTitle(sli), note: ssrc ? ssrc.textContent.trim() : "" });
              });
            }
            secs.push({ id: li.id, num: n.textContent.trim(), title: __LB.pureTitle(li), note: src ? src.textContent.trim() : "", subs: subs });
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
          (s.subs || []).forEach(function (sb) {
            L.push("      - " + sb.num + " " + sb.title);
          });
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
     ykla 令：导出文件名＝“目录-版本.后缀名”。版本取页面 .page-version
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
    H.push('<p class="sub">' + nv + ' 卷 · ' + nc + ' 章 · ' + ns + ' 节 · 现行大纲目录 · ' + new Date().toISOString().slice(0,10) + '</p>');
    st.forEach(function (v) {
      H.push('<h2>' + es(v.title) + '</h2>');
      v.chapters.forEach(function (c) {
        H.push('<h3>' + es(c.title) + '</h3>');
        if (!c.sections.length) return;
        H.push('<ul>');
        c.sections.forEach(function (ss) {
          H.push('<li><span class="n">' + es(ss.num) + '</span>' + es(ss.title) +
                 (ss.note ? ' <span class="note">' + es(ss.note) + '</span>' : ''));
          if (ss.subs && ss.subs.length) {
            H.push('<ul>');
            ss.subs.forEach(function (sb) {
              H.push('<li><span class="n">' + es(sb.num) + '</span>' + es(sb.title) +
                     (sb.note ? ' <span class="note">' + es(sb.note) + '</span>' : '') + '</li>');
            });
            H.push('</ul>');
          }
          H.push('</li>');
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
            /* 2026-11-06（ADR-0020）：小节行 chapter 列留空、num 为 M.N.P 三段形态。 */
            (s.subs || []).forEach(function (sb) {
              lines.push([f(v.title), f(""), f(sb.num), f(sb.title), f(sb.note)].join(","));
            });
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
        /* 2026-11-06（ADR-0020）：:scope > li 只数节——嵌套小节 ul 不再使索引偏移误报。 */
        var secLis = Array.prototype.slice.call(ul.querySelectorAll(":scope > li"));
        secLis.forEach(function (li, i) {
          var n = li.querySelector(":scope > .sec-num"); if (!n) return;
          var exp = chNo + "." + (i + 1);
          if (n.textContent.trim() !== exp) bad.push(c.id + " 节号 " + n.textContent.trim() + "≠" + exp);
          if (i === secLis.length - 1 && /本章书目述评/.test(n.textContent) === false) { /* 述评可选 */ }
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

/* 块 3 数据联动·视图·版式：DATA 装配点（embed.py 维护 var DATA） */

(function () {

  var DATA = null;
  function __b64ToU8(b64) {
    var bin = atob(b64);
    var u8 = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) u8[i] = bin.charCodeAt(i);
    return u8;
  }

  function __waitStable(maxFrames, cb) {
    var last = -1, stable = 0, left = maxFrames, t0 = Date.now();
    function tick() {
      var h = document.documentElement.scrollHeight;
      var dt = Date.now() - t0;
      if (dt >= 600 && h === last && h > 0) stable++; else stable = 0;
      last = h;
      var fontsOk = !(document.fonts && document.fonts.status) || document.fonts.status === "loaded";
      if ((stable >= 2 && fontsOk) || left <= 0) { cb(); return; }
      left--;
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var __dataReady = (function () {
    /* data-opt-ready＝目录引擎就绪诊断标记（0＝初始化降级，1＝全部就绪；供 DevTools/排障读取，无样式消费者） */
    function fail(msg) { document.documentElement.setAttribute("data-opt-ready", "0"); if (window.console && console.info) console.info(U("diag.fail_head") + msg + U("diag.fail_tail")); return false; }
    try {
      var el = document.getElementById("opt-data-blob");
      if (!el) return Promise.resolve(fail("数据块缺失"));
      var b64 = (el.textContent || "").replace(/\s+/g, "");
      var integrity = el.getAttribute("data-integrity") || "";
      /* SRI 等价：对数据块文本做 SHA-256，比对内嵌期望哈希；不符则拒绝加载（篡改检测） */
      var verify = Promise.resolve(true);
      if (integrity && window.crypto && crypto.subtle && window.TextEncoder) {
        verify = crypto.subtle.digest("SHA-256", new TextEncoder().encode(b64)).then(function (d) {
          var got = btoa(String.fromCharCode.apply(null, new Uint8Array(d)));
          return got === (integrity.split("-")[1] || "");
        }, function () { return false; });
      }
      return verify.then(function (ok) {
        if (!ok) return fail("数据块完整性校验失败（数据可能被篡改）");
        var u8;
        try { u8 = __b64ToU8(b64); } catch (e) { return fail("base64 解码失败"); }
        if (typeof DecompressionStream !== "function") return fail("浏览器不支持 Compression Streams");
        var out = new Blob([u8]).stream().pipeThrough(new DecompressionStream("gzip"));
        return new Response(out).text().then(function (t) { DATA = JSON.parse(t); return true; },
          function () { return fail("解压或解析失败"); });
      });
    } catch (e) { return Promise.resolve(fail("装载异常")); }
  })();
  __dataReady.then(function (ok) {
    if (!ok) return;
    try {

    var docPage = document.querySelector('.doc-page');
    if (!docPage) return;
    var stor = { get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
                 set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };
    var chapters = [].slice.call(docPage.querySelectorAll('h3.chapter[id]'));
    var vols = [].slice.call(docPage.querySelectorAll("section[id^='vol-']"));
    var secs = [];
    chapters.forEach(function (ch) {
      var ul = ch.nextElementSibling; if (!ul || !ul.classList || !ul.classList.contains('sections')) return;
      [].slice.call(ul.children).forEach(function (li) {
        var n = li.querySelector(':scope > .sec-num'); if (!n) return;
        var src = li.querySelector(':scope > .src');
        var t = __LB.pureTitle(li);
        secs.push({ li: li, id: li.id, num: n.textContent.trim(), title: t, note: src ? src.textContent : '',
                    noteEl: src, ch: ch, vol: ch.closest("section[id^='vol-']") });
      });
    });
    var chTitle = {}, volTitles = {};
    chapters.forEach(function (c) { chTitle[c.id] = __LB.pureTitle(c); });
    vols.forEach(function (v) { volTitles[v.id] = __LB.pureTitle(v.querySelector('h2')); });

      } catch (err) { console.error(U("diag.data"), err); }

  /* ---------- 共享工具：转义与浮层容器（2026-09-19 严格模式修复） ----------
     缘由：原实现将 pop／showPop／hidePop／esc 声明于“人物索引联动”分块之内，靠宽松模式的
     Annex B 语义提升至外层作用域；严格模式下函数声明为**块级作用域** → 兄弟分块
     （ref 编号联动／长节名折叠／浮层／时间线视图／修订差异视图）调用即抛 ReferenceError。
     故上提至本回调顶层：既跨块可见，也不受任一分块失败影响。 */
  var pop = document.createElement('div');
  pop.className = 'opt-pop'; pop.id = 'optPop';
  pop.setAttribute('popover', 'auto');
  document.body.appendChild(pop);
  /* Popover／Anchor Positioning（2026-10-11 载体层批次）：
     有 popover API → showPopover 进顶层（Esc／点外部 light dismiss 浏览器内置），定位用
     JS 补位（fixed 视口坐标＋双向 clamp）。
     🔴 anchor 定位（showPopover({source})＋position-anchor:implicit＋position-area）在该
     引擎实测不稳：打开态 dTop=558（应 14）且内联定位被 position-area 机制吞掉——弃用，
     CSS 守卫保留待显式 anchor-name 方案（本批留痕，几何取证 script/_pop_geom_20261011.mjs）。
     无 popover API → 原路径（.open 类＋absolute 页面坐标＋全局点击关闭监听）。
     .open 类全程同步（toggle 事件——light dismiss 实测只发 beforetoggle/toggle），
     供测试与样式判态。 */
  var popApi = typeof pop.showPopover === 'function';
  /* JS 定位（fixed 视口坐标，视口内双向 clamp）——top layer 态的唯一定位路径。 */
  var popPlace = function (x, y) {
    var w = pop.offsetWidth, h = pop.offsetHeight;
    var left = Math.max(8, Math.min(x, window.innerWidth - w - 12));
    var top = Math.max(8, Math.min(y + 14, window.innerHeight - h - 12));
    pop.style.setProperty('left', left + 'px', 'important');
    pop.style.setProperty('top', top + 'px', 'important');
  };
  var showPop = function (html, x, y, trigger) {
    pop.innerHTML = __LB.ttt(html); pop.classList.add('open');
    if (popApi) {
      try {
        if (pop.matches(':popover-open')) pop.hidePopover();
        pop.showPopover();
        popPlace(x, y);
        return;
      } catch (e) { /* 落回退路径 */ }
    }
    var w2 = pop.offsetWidth;
    pop.style.left = Math.max(8, Math.min(x, window.innerWidth - w2 - 12)) + 'px';
    pop.style.top = (y + window.scrollY + 14) + 'px';
  };
  var hidePop = function () {
    if (popApi && pop.matches(':popover-open')) { try { pop.hidePopover(); } catch (e) {} }
    pop.classList.remove('open');
  };
  /* .open 同步：light dismiss（Esc／点外部）实测只派发 beforetoggle/toggle（不发 close），
     故以 toggle 为权威；close 监听保留作兼容。 */
  pop.addEventListener('toggle', function (e) { if (e.newState === 'closed') pop.classList.remove('open'); });
  pop.addEventListener('close', function () { pop.classList.remove('open'); });
  if (!popApi) {
    /* 回退路径专属：无 light dismiss 时以全局点击代之（popover 路径由浏览器内置接管） */
    document.addEventListener('click', function (e) {
      if (!e.target.closest || !e.target.closest('.opt-pop')) hidePop();
    });
  }
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var personCard = function (p) {
    var h = '<h4>' + esc(p.n[0]) + '</h4><dl>';
    if (p.n[1]) h += '<dt>' + U("ui.card.name_orig") + '</dt><dd>' + esc(p.n.slice(1).join('／')) + '</dd>';
    if (p.r) h += '<dt>' + U("ui.card.role") + '</dt><dd>' + esc(p.r) + '</dd>';
    if (p.p) h += '<dt>' + U("ui.card.prio") + '</dt><dd>' + esc(p.p) + '</dd>';
    if (p.v) h += '<dt>' + U("ui.card.from") + '</dt><dd>' + esc(p.v) + '</dd>';
    if (p.af) h += '<dt>' + U("ui.card.org") + '</dt><dd>' + esc(p.af) + '</dd>';
    if (p.s) h += '<dt>' + U("ui.card.alive") + '</dt><dd>' + esc(p.s) + '</dd>';
    return h + '</dl>';
  };

  try {
    /* ---------- 1. 注三色分类 ---------- */
    var kCount = { x: 0, m: 0, s: 0 };
    secs.forEach(function (s) {
      if (!s.noteEl) return;
      var txt = s.noteEl.textContent, k = 's';
      if (/(迁入|并入|拆分迁入|移入|原第)/.test(txt)) k = 'm';
      else if (/(分工|正身|互注|交叉引用|本节载|彼处载)/.test(txt)) k = 'x';
      s.noteEl.classList.add('note-x', 'k-' + (k === 'm' ? 'mig' : k === 'x' ? 'xref' : 'src'));
      kCount[k]++;
    });
    var legend = document.createElement('div');
    legend.className = 'note-legend';
    legend.innerHTML = '<span><i class="a"></i>' + U("ui.legend.x") + '' + kCount.x + '</span>' +
                       '<span><i class="b"></i>' + U("ui.legend.m") + '' + kCount.m + '</span>' +
                       '<span><i class="c"></i>' + U("ui.legend.s") + '' + kCount.s + '</span>' +
                       '<span>' + U("ui.legend.total") +  + (kCount.x + kCount.m + kCount.s) + U("ui.legend.unit") + '</span>';
    var met = docPage.querySelector('.doc-metrics');
    if (met) met.parentNode.insertBefore(legend, met.nextSibling);

      } catch (err) { console.error(U("diag.legend"), err); }
  try {
    /* ---------- 2. 人物索引联动 ---------- */
    var persons = (DATA.persons || []).map(function (p) {

      var zh = (p.names && p.names.zh) || [];
      var en = (p.names && p.names.en) || [];
      var legacy = p.accounts && p.accounts.legacy ? [p.accounts.legacy] : [];
      return {
        n: zh.concat(en).concat(legacy),
        r: p.role || "",
        p: p.priority || "P2",
        v: p.volume || "",
        s: (function () {
          var st = p.status || {};
          var parts = [];
          if (st.alive !== undefined) parts.push("{\"status\": \"" + (st.alive ? "在世" : "已故") + "\"");
          if (st.birth) parts.push("\"birth\": \"" + st.birth + "\"");
          if (st.death) parts.push("\"death\": \"" + st.death + "\"");
          if (st.note) parts.push("\"note\": \"" + String(st.note).replace(/"/g, "\\\"") + "\"");
          return parts.length ? parts.join(", ") + "}" : "";
        })(),
        af: p.affiliations || [],
      };
    });

    function cleanNames(arr) {
      var out = [];
      (arr || []).forEach(function (x) {
        if (!x || typeof x !== "string") return;
        var hasCN = /[\u4e00-\u9fff]/.test(x);
        /* 中文名整体保留（JSON 残片里的中文名也是纯文本，如“肯·汤普森”） */
        if (hasCN) { out.push(x.trim()); return; }
        /* 提取英文 JSON 残片中的 value */
        var m = x.match(/"value"\s*:\s*"([^"]+)"/g);
        if (m) {
          m.forEach(function (mm) {
            var v = mm.match(/"value"\s*:\s*"([^"]+)"/);
            if (v && v[1] && v[1] !== "null") out.push(v[1]);
          });
        }
        if (!/[\\":{}\[\]]/.test(x) && x.trim().length >= 2) out.push(x.trim());
      });

      return out.filter(function (x) {
        if (!x || typeof x !== "string") return false;
        if (/@/.test(x)) return false;
        if (/^(person_id_(legacy|new):|freebsd_account|openbsd_account|netbsd_account|dragonflybsd_account|name_variant|nickname|other)\b/.test(x)) return false;
        if (/[\u4e00-\u9fff]/.test(x)) return x.replace(/[\s·\-]/g, '').length >= 2;
        if (/^[a-z0-9_-]{6,}$/.test(x)) return false;
        if (!/^[A-Z]/.test(x)) return false;
        return true;
      });
    }
    persons.forEach(function (p) { p.n = cleanNames(p.n); });
    var lookup = {};
    persons.forEach(function (p) {
      p.n.forEach(function (x) {
        var key = x.toLowerCase();
        if (!lookup[key]) lookup[key] = [];
        lookup[key].push(p);
      });
    });
    var namesSorted = Object.keys(lookup).filter(function (x) { return x.length >= 3; }).sort(function (a, b) { return b.length - a.length; });
    /* pop／showPop／hidePop／esc／personCard 已上提至本回调顶层（见“共享工具”段），此处不再重复声明 */

      } catch (err) { console.error(U("diag.person"), err); }
  try {
    /* ---------- 3. ref 编号联动 ---------- */
    var refs = DATA.refs || {};
    var nRef = 0;
    var refMiss = 0;
    secs.forEach(function (s) {
      if (!s.noteEl) return;
      var html = s.noteEl.innerHTML;
      html = html.replace(/\bref\s?(\d{1,5})/g, function (m, id) {
        /* 2026-09-30（98 号文 §八·乙-1）：原实现直接 `return m` 丢弃未著录编号且不计数，
           致下游“ref 编号可解析”自校验因无 `.reflink[data-ref]` 可查而结构性恒为 0。
           现于此处计数（SRC-mat 系内部史料编号，另有著录说明，不计入未著录）。 */
        if (!refs[id]) { refMiss++; return m; }
        nRef++;
        return '<a class="reflink" href="#ref-' + id + '" data-ref="' + id + '">' + m + '</a>';
      });
      html = html.replace(/\bSRC-mat:(\d+)/g, function (m, id) {
        nRef++;
        return '<a class="reflink" href="#ref-SRC-mat-' + id + '" data-ref="SRC-mat:' + id + '">' + m + '</a>';
      });
      s.noteEl.innerHTML = __LB.ttt(html);
    });
    __LB.refMiss = refMiss;
    docPage.querySelectorAll('a.reflink').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var id = a.dataset.ref;
        var be = refs[id];
        var body = be ? '<dd>' + esc(be) + '</dd>' : '<dd>' + U("ui.card.src_mat") + '</dd>';
        showPop('<h4>' + U("ui.card.ref_prefix") + esc(id) + '</h4><dl><dt>' + U("ui.card.biblio") + '</dt>' + body +
                '<dt>' + U("ui.card.lib_link") + '</dt><dd>' + (be ? U("ui.card.lib_path") : U("ui.card.dash")) + '</dd></dl>',
                a.getBoundingClientRect().left, a.getBoundingClientRect().top, a);
      });
    });

      } catch (err) { console.error(U("diag.ref"), err); }
  try {

    /* 原 cite/currentVol/currentCh/currentSec 与 optCiteGb/optCiteCh 按钮已删除 */

      } catch (err) { console.error(U("diag.deleted"), err); }
  try {
    /* ---------- 5. 卷章节数徽标 ---------- */
    vols.forEach(function (v) {
      var h = v.querySelector('h2');
      var cs = [].slice.call(v.querySelectorAll('h3.chapter[id]'));
      var ns = 0;
      cs.forEach(function (c) {
        var ul = c.nextElementSibling;
        /* 2026-11-06（ADR-0020）：:scope > li 只数节——嵌套小节 ul 不计入节数。 */
        if (ul && ul.classList && ul.classList.contains('sections')) ns += ul.querySelectorAll(':scope > li').length;
      });
      if (h) { var b = document.createElement('span'); b.className = 'vol-badge'; b.textContent = cs.length + ' 章 · ' + ns + ' 节'; h.appendChild(b); }
    });
    chapters.forEach(function (c) {
      var ul = c.nextElementSibling;
      if (!ul || !ul.classList || !ul.classList.contains('sections')) return;
      /* 2026-11-06（ADR-0020）：:scope > li 只数节（嵌套小节 ul 不计入）。 */
      var b = document.createElement('span'); b.className = 'ch-badge'; b.textContent = ul.querySelectorAll(':scope > li').length + ' 节'; c.appendChild(b);
    });

      } catch (err) { console.error(U("diag.badge"), err); }
  try {
    /* ---------- 6. 长节名折叠 ---------- */
    var nLong = 0;
    secs.forEach(function (s) {
      if (s.title.length < 150) return;
      nLong++;
      var short = s.title.slice(0, 120) + '…';
      var numEl = s.li.querySelector(':scope > .sec-num');
      var srcEl = s.noteEl;
      var head = '<span class="sec-num">' + numEl.textContent + '</span> ';
      var badge = srcEl ? '<button type="button" class="note-badge" aria-expanded="false">' + U("ui.note.badge") + '</button>' : '';
      var html = head + '<span class="t-short">' + esc(short) + '</span><button class="t-more" type="button">' + U("ui.more.expand") + '</button>' +
                 '<span class="t-full">' + esc(s.title) + '</span>' + badge + (srcEl ? srcEl.outerHTML : '');
      /* 2026-11-06（ADR-0020）：先摘下嵌套 ul.subsections 再重写，写后放回末尾（顺序与装配一致）。 */
      var subUlKeep = s.li.querySelector(':scope > ul.subsections');
      s.li.innerHTML = __LB.ttt(html);
      if (subUlKeep) s.li.appendChild(subUlKeep);
      s.li.classList.add('long-title');
      s.li.querySelector('.t-more').addEventListener('click', function () {
        s.li.classList.toggle('open');
        this.textContent = s.li.classList.contains('open') ? U("ui.more.collapse") : U("ui.more.expand");
      });
      var bb = s.li.querySelector('.note-badge');
      if (bb) bb.addEventListener('click', function (e) {
        e.preventDefault(); e.stopPropagation();
        s.li.classList.toggle('note-open');
        bb.setAttribute('aria-expanded', s.li.classList.contains('note-open') ? 'true' : 'false');
      });
    });

      } catch (err) { console.error(U("diag.longtitle"), err); }
  try {

    /* 根因复盘：人名词典键清洗后 lookup 正常（1446 中文键），但原注入在
       secs 构建时的 innerHTML 改写后，被第 6 节 long-title 的 DOM 重建抹除；
       且匹配只扫标题、漏注文本。现改为 DOM 终态后 TreeWalker 文本节点注入，
       不依赖 innerHTML 结构，标题与注文本全覆盖。 */
    var humanNames2 = namesSorted.filter(function (nm) {
      if (!nm || nm.length < 2) return false;
      if (/[\u4e00-\u9fff]/.test(nm)) return true;

      return /[a-zA-Z]/.test(nm);
    }).sort(function (a, b) { return b.length - a.length; });

    var shortNameOwners = {};
    persons.forEach(function (p) {
      (p.n || []).forEach(function (x) {
        if (typeof x !== "string") return;
        var k = x.toLowerCase();
        if (/^[a-z]{1,3}$/.test(k)) {
          shortNameOwners[k] = (shortNameOwners[k] || 0) + 1;
        }
      });
    });
    var blockedShort = {};
    Object.keys(shortNameOwners).forEach(function (k) {
      if (shortNameOwners[k] > 1) blockedShort[k] = true; // 跨人冲突短名禁用

    if (blockedShort["phk"]) delete blockedShort["phk"];
    });

    ["bill", "ed", "ben", "sam", "matt", "bob", "joe", "dan", "tom", "ken", "ted", "art", "lee", "wayne",
     "max", "ian", "guy", "dean", "gil", "raf", "niv", "rob", "christos",
     "steve", "peter", "drew", "nate", "larry", "otto", "florian", "gordon", "henning",
     "markus", "patrick", "claudio", "beck", "benno", "jimmy", "manu", "neel", "terry",
     "kirk", "jamal", "javen", "dragon", "glass", "trouble", "lick"].forEach(function (w) { blockedShort[w] = true; });
    humanNames2 = humanNames2.filter(function (nm) {
      var key = nm.toLowerCase();
      if (blockedShort[key]) return false;          // 黑名单任意长度生效（bill/christos/ed…）

      if (/^[a-z]{1,3}$/.test(key) && key !== 'phk') return false;   // ≤3 字符短名一律不进注入（phk 特例除外）
      return true;
    });
    var nPlink2 = 0;

    var firstCharIdx = {};
    var nmOrder = {};
    humanNames2.forEach(function (nm, i) {
      nmOrder[nm] = i;
      var c = nm.charAt(0).toLowerCase();
      (firstCharIdx[c] = firstCharIdx[c] || []).push(nm);
    });
    /* O-3（2026-10-11）：injectAllPlink 的正则匹配 offload 到 Blob Worker，
       避免主线程长任务阻塞（实测同步版约 1.2s）。Worker 内做候选筛选＋
       正则替换，返回每节点 HTML；主线程只做 DOM 套用与事件绑定。
       Worker 不可用或报错时回退原同步逻辑，保证功能不退化。 */
    var __plinkWorkerCode = [
      'self.onmessage=function(e){',
      'var texts=e.data.texts,firstCharIdx=e.data.firstCharIdx,nmOrder=e.data.nmOrder,nPlink=0;',
      'function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}',
      'var htmls=texts.map(function(orig){',
      'if(!orig||orig.trim().length<2)return orig;',
      'var html=orig,changedThis=false,htmlLower=html.toLowerCase();',
      'var charSet={};for(var ci=0;ci<htmlLower.length;ci++)charSet[htmlLower[ci]]=1;',
      'var cand=[],seen={};',
      'Object.keys(charSet).forEach(function(ch){(firstCharIdx[ch]||[]).forEach(function(nm){if(!seen[nm]){seen[nm]=1;cand.push(nm);}});});',
      'cand.sort(function(a,b){return b.length-a.length||nmOrder[a]-nmOrder[b];});',
      'cand.some(function(nm){',
      'if(nPlink>900)return true;',
      'var isCN=/[\\u4e00-\\u9fff]/.test(nm);',
      'var hay=isCN?html:htmlLower,needle=isCN?nm:nm.toLowerCase();',
      'if(hay.indexOf(needle)<0)return false;',
      'var anchors=[];',
      'html=html.replace(/<a\\b[^>]*>[\\s\\S]*?<\\/a>/g,function(a){anchors.push(a);return"\\u0000"+(anchors.length-1)+"\\u0000";});',
      'var re3=new RegExp(nm.replace(/[.*+?^${}()|[\\]\\\\]/g,"\\\\$&")+(/[\\u4e00-\\u9fff]/.test(nm)?"":"(?![\\\\u4e00-\\\\u9fffA-Za-z0-9])"),"gi");',
      'html=html.replace(re3,function(m){nPlink++;changedThis=true;return \'<a class="plink" href="#person-\'+encodeURIComponent(nm)+\'" data-nm="\'+esc(nm)+\'">\'+m+"</a>";});',
      'html=html.replace(/\\u0000(\\d+)\\u0000/g,function(mm,i){return anchors[+i];});',
      'return false;',
      '});',
      'return html;',
      '});',
      'self.postMessage({htmls:htmls,nPlink:nPlink});',
      '};'
    ].join('\n');

    function injectAllPlinkSync(targets) {
      targets.forEach(function (t) {
        if (nPlink2 > 900) return;
        var orig = t.text, html = orig, changedThis = false, htmlLower = html.toLowerCase();
        var charSet = {};
        for (var ci = 0; ci < htmlLower.length; ci++) charSet[htmlLower[ci]] = 1;
        var cand = [], seen = {};
        Object.keys(charSet).forEach(function (ch) {
          (firstCharIdx[ch] || []).forEach(function (nm) { if (!seen[nm]) { seen[nm] = 1; cand.push(nm); } });
        });
        cand.sort(function (a, b) { return b.length - a.length || nmOrder[a] - nmOrder[b]; });
        cand.some(function (nm) {
          if (nPlink2 > 900) return true;
          var isCN = /[\u4e00-\u9fff]/.test(nm);
          var hay = isCN ? html : htmlLower, needle = isCN ? nm : nm.toLowerCase();
          if (hay.indexOf(needle) < 0) return false;
          var anchors = [];
          html = html.replace(/<a\b[^>]*>[\s\S]*?<\/a>/g, function (a) { anchors.push(a); return '\u0000' + (anchors.length - 1) + '\u0000'; });
          var re3 = new RegExp(nm.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + (/[\u4e00-\u9fff]/.test(nm) ? '' : '(?![\\u4e00-\\u9fffA-Za-z0-9])'), 'gi');
          html = html.replace(re3, function (m) { nPlink2++; changedThis = true; return '<a class="plink" href="#person-' + encodeURIComponent(nm) + '" data-nm="' + esc(nm) + '">' + m + '</a>'; });
          html = html.replace(/\u0000(\d+)\u0000/g, function (mm, i) { return anchors[+i]; });
          return false;
        });
        if (changedThis) {
          var span = document.createElement('span');
          span.innerHTML = html;
          var frag = document.createDocumentFragment();
          while (span.firstChild) frag.appendChild(span.firstChild);
          t.node.parentNode.replaceChild(frag, t.node);
        }
      });
      return nPlink2;
    }

    function injectAllPlink() {
      var walker = document.createTreeWalker(docPage, NodeFilter.SHOW_TEXT, {
        acceptNode: function (node) {
          var p = node.parentElement;
          if (!p) return NodeFilter.FILTER_REJECT;
          if (p.closest('a, button, .sec-num')) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      });
      var allNodes = [];
      while (walker.nextNode()) allNodes.push(walker.currentNode);
      /* 仅节列表项（ul.sections > li）内文本参与注入 */
      var targets = [];
      allNodes.forEach(function (tn) {
        if (!tn.parentElement || !tn.parentElement.closest ||
            !tn.parentElement.closest('ul.sections > li')) return;
        /* 2026-11-06（ADR-0020）：嵌套小节文本不参与节级注入（小节锚为静态 id）。 */
        if (tn.parentElement.closest('ul.subsections')) return;
        var orig = tn.textContent;
        if (!orig || orig.trim().length < 2) return;
        targets.push({ node: tn, text: orig });
      });

      if (typeof Worker === 'undefined' || typeof Blob === 'undefined' || typeof URL === 'undefined' || !URL.createObjectURL) {
        injectAllPlinkSync(targets);
        return Promise.resolve();
      }
      return new Promise(function (resolve) {
        var blob, url, worker;
        try {
          blob = new Blob([__plinkWorkerCode], { type: 'application/javascript' });
          url = URL.createObjectURL(blob);
          worker = new Worker(url);
        } catch (e) {
          injectAllPlinkSync(targets);
          resolve();
          return;
        }
        worker.onmessage = function (e) {
          var htmls = e.data.htmls;
          nPlink2 = e.data.nPlink;
          targets.forEach(function (t, i) {
            if (htmls[i] !== t.text) {
              var span = document.createElement('span');
              span.innerHTML = htmls[i];
              var frag = document.createDocumentFragment();
              while (span.firstChild) frag.appendChild(span.firstChild);
              t.node.parentNode.replaceChild(frag, t.node);
            }
          });
          URL.revokeObjectURL(url);
          worker.terminate();
          resolve();
        };
        worker.onerror = function () {
          injectAllPlinkSync(targets);
          try { URL.revokeObjectURL(url); } catch (e) {}
          worker.terminate();
          resolve();
        };
        worker.postMessage({ texts: targets.map(function (t) { return t.text; }), firstCharIdx: firstCharIdx, nmOrder: nmOrder });
      });
    }
    var __plinkDone = injectAllPlink().then(function () {
      /* 长标题折叠后的 .t-full/.t-short 内容更新：Tooltip 已含复制，无需再动 */
      docPage.querySelectorAll('a.plink').forEach(function (a) {
        a.addEventListener('click', function (e) {
          e.preventDefault();
          e.stopPropagation();
          var ps = lookup[a.dataset.nm] || [];
          var html = ps.slice(0, 3).map(personCard).join('<hr class="opt-hr">');
          showPop(html || '<h4>' + esc(a.dataset.nm) + '</h4><dl><dt>' + U("ui.card.note") + '</dt><dd>' + U("ui.card.no_person") + '</dd></dl>',
                  a.getBoundingClientRect().left, a.getBoundingClientRect().top, a);
        });
      });
      __LB.nPlink = nPlink2;   /* 执行断言点：供回归测试校验注入是否倒退 */
    });

      } catch (err) { console.error(U("diag.pop"), err); }
  try {
    /* ---------- 7. 粘性卷章页眉（进度） ---------- */
    var bc = docPage.querySelector('.breadcrumb');
    if (bc) {
      /* 复用已存在的 .prog：原实现无条件再追加一个，与 setCurrent 所建者合计两个进度条
         （并排且同为 flex:1，视觉上被掩盖；实为冗余节点与冗余动画）。 */
      var pr = bc.querySelector('.prog');
      if (!pr) { pr = document.createElement('span'); pr.className = 'prog'; pr.innerHTML = '<i></i>'; bc.appendChild(pr); }
      var bar = bc.querySelector('.prog i');
      var updRaf = null;
      function upd() {
        /* 支持 animation-timeline 的引擎（Chromium／WebKit 实测均支持）走 CSS 路径，此处早退。
           墨水屏例外（2026-10-22）：该路径的进度由滚动驱动动画实现，e-ink 下动画被全禁，
           进度条会停在 0——故不走 CSS 路径，改由下方 rAF 直接赋值（阶跃、无补间）。 */
        if (!__LB.staticMode() && window.CSS && CSS.supports && CSS.supports('animation-timeline: scroll()')) return;
        if (updRaf !== null) return;
        updRaf = requestAnimationFrame(function () {
          updRaf = null;
          if (!bar) return;
          /* 与 CSS 路径语义对齐：modern.css 的 `animation-timeline: scroll(root block)` ＋
             `@keyframes prog-grow { from{width:0%} to{width:100%} }` 表示**整页滚动进度**。
             🔴 原实现算的是“当前活跃章**已滚过**的比例”（done = −rect.top）：活跃章的 top 通常
             仍为正（尚未滚过其顶部），一旦滚过即被下一章取代 → done 恒为 0 → 宽度恒 0。
             实测（Firefox 1497 走本回退路径）面包屑进度条**完全不显示**；又因支持该特性的引擎
             一律早退，本分支实为**从未生效的死代码**。故改为整页进度。 */
          var max = document.documentElement.scrollHeight - window.innerHeight;
          var r = max > 0 ? window.scrollY / max : 0;
          bar.style.width = Math.min(100, Math.round(r * 100)) + '%';
        });
      }
      window.addEventListener('scroll', upd, { passive: true });
      window.addEventListener('resize', upd); upd();
    }

      } catch (err) { console.error(U("diag.sticky"), err); }
  try {
    /* ---------- 8. 研究版 / 阅读版 ---------- */
    function applyMode(m) {
      document.body.classList.toggle('read-mode', m === 'read');
      var b = document.getElementById('optMode');
      if (b) { b.classList.toggle('on', m === 'read'); b.textContent = m === 'read' ? U("ui.mode.read") : U("ui.mode.study"); }

      if (m === 'read') {
        document.body.classList.remove('notes-all');
        var bn = document.getElementById('optNotes');
        if (bn) bn.classList.remove('on');
      }
    }

    applyMode(stor.get('sme-mode') || (window.innerWidth <= 820 ? 'read' : 'research'));
    var bm = document.getElementById('optMode');
    if (bm) bm.addEventListener('click', function () {
      var n = document.body.classList.contains('read-mode') ? 'research' : 'read';
      stor.set('sme-mode', n);
      __LB.viewTransition(function () { applyMode(n); });
    });

      } catch (err) { console.error(U("diag.mode"), err); }
  try {
    /* ---------- 9. 时间线视图（节名年份抽取） ---------- */
    var years = {};
    secs.forEach(function (s) {
      var ys = (s.title + ' ' + chTitle[s.ch.id]).match(/(1[6-9]\d\d|20[0-4]\d)/g);
      if (!ys) return;
      var y = ys[0];
      (years[y] = years[y] || []).push(s);
    });
    var tlPanel = document.createElement('dialog');
    tlPanel.className = 'opt-panel'; tlPanel.id = 'optPanelTl';
    tlPanel.innerHTML = '<div class="box"><h3>' + U("ui.tl.h3") + '</h3>' +
      '<div class="hint">' + U("ui.tl.pre") + '<b>' + Object.keys(years).length + '</b>' + U("ui.tl.mid") + '<b>' + secs.length + '</b>' + U("ui.tl.post") + '</div>' +
      '<div id="tlView"></div></div>';
    document.body.appendChild(tlPanel);
    var btnTl = document.getElementById('optTl');
    if (btnTl) btnTl.addEventListener('click', function () {
      var host = tlPanel.querySelector('#tlView');
      if (!host.dataset.built) {
        var ks = Object.keys(years).sort();
        var html = '';
        ks.forEach(function (y) {
          html += '<div class="yr"><b>' + y + '</b><ul>';
          years[y].slice(0, 40).forEach(function (s) {
            html += '<li><span class="pv">' + esc(volTitles[s.vol.id] || '') + ' / ' + esc(s.num) + '</span>' +
                    '<a href="#' + s.id + '">' + esc(s.title.slice(0, 70)) + '</a></li>';
          });
          html += '</ul></div>';
        });
        host.innerHTML = __LB.ttt(html || '<p>' + U("ui.tl.empty") + '</p>');
        host.dataset.built = '1';
        host.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeTl); });
      }
      __LB.decorateDialogs(); __LB.openDialog(tlPanel);
    });
    function closeTl() { __LB.closeDialogs(true); }

      } catch (err) { console.error(U("diag.timeline"), err); }
  try {
    /* ---------- 10. 修订差异视图 ---------- */
    var REVS = DATA.revs || [];
    var rvPanel = document.createElement('dialog');
    rvPanel.className = 'opt-panel'; rvPanel.id = 'optPanelRev';
    rvPanel.innerHTML = '<div class="box" id="revView"><h3>' + U("ui.rv.h3") + '</h3>' +
      '<button type="button" class="opt-close" aria-label="' + U("ui.rv.close") + '">×</button>' +
      '<div class="rev-scroll"><table><thead><tr><th>' + U("ui.rv.th1") + '</th><th>' + U("ui.rv.th2") + '</th><th>' + U("ui.rv.th3") + '</th><th>' + U("ui.rv.th4") + '</th></tr></thead><tbody>' +
      REVS.map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + r[1] + '</td><td>' + esc(r[2]) + '</td><td>' + r[3] + '</td></tr>'; }).join('') +
      '</tbody></table></div><div class="hint">' + U("ui.rv.hint") + '</div>' +
      '<div class="hint">' + U("ui.rv.cur") + ' ' + String(((document.querySelector('.page-version') || {}).textContent || '')).replace(/^\s+|\s+$/g, '') + '</div></div>';
    document.body.appendChild(rvPanel);
    var bRev = document.getElementById('optRev');
    if (bRev) bRev.addEventListener('click', function () {
      __LB.decorateDialogs();
      /* 151 批：补 .opt-close 关闭钮并改开合切换——面板行数随修订史增长，打开的模态
         参与全局视觉捕获，长表必须可关且表体限高滚动（深检序列 150ms 预算实测教训） */
      if (rvPanel.open || rvPanel.classList.contains('open')) { __LB.closeDialogs(true); return; }
      __LB.openDialog(rvPanel);
    });
    var rvClose = rvPanel.querySelector('.opt-close');
    if (rvClose) rvClose.addEventListener('click', function () { __LB.closeDialogs(true); });

      } catch (err) { console.error(U("diag.revisions"), err); }
  try {
    /* ---------- 11. 自校验扩展（6 项） ---------- */
    var checks = [];
    // (1) 节号连续 (2) 章号连续 (3) 述评恒末 (4) 注链接可解析 (5) 注分类齐备 (6) 卷内章题唯一
    vols.forEach(function (v) {
      var cs = [].slice.call(v.querySelectorAll('h3.chapter[id]'));
      cs.forEach(function (c, i) {
        if (parseInt((c.id.match(/-ch-(\d+)$/) || [0, 0])[1], 10) !== i + 1) checks.push(['章号连续', v.id]);
        var ul = c.nextElementSibling; if (!ul || !ul.classList || !ul.classList.contains('sections')) return;
        var chNo = (c.id.match(/-ch-(\d+)$/) || [0, 0])[1];
        /* 2026-11-06（ADR-0020）：:scope > li 只数节——嵌套小节 ul 不再使索引偏移误报。 */
        var secLis = [].slice.call(ul.querySelectorAll(':scope > li'));
        secLis.forEach(function (li, k) {
          var n = li.querySelector(':scope > .sec-num'); if (!n) return;
          if (n.textContent.trim() !== chNo + '.' + (k + 1)) checks.push(['节号连续', c.id + ' ' + n.textContent.trim()]);
        });
        var lisArr = secLis, bibIdx = -1;
        lisArr.forEach(function (li, k) {
          var n2 = li.querySelector(':scope > .sec-num'); if (!n2) return;
          var tt = __LB.pureTitle(li);
          if (/本章书目述评/.test(tt)) bibIdx = k;
        });
        if (bibIdx >= 0 && bibIdx !== lisArr.length - 1) checks.push(['述评恒末', c.id]);
      });
    });
    var dupTitles = 0;
    vols.forEach(function (v) {
      var t = {};
      v.querySelectorAll('h3.chapter[id]').forEach(function (c) { var k = __LB.pureTitle(c); if (t[k]) dupTitles++; t[k] = 1; });
    });
    /* 2026-09-30（98 号文 §八·乙-1）：原扫描 `a.reflink[data-ref]` 恒为空集
       （未著录者从不生成为链接），故该项结构性恒 0、永远“通过”。现改读上游实数。 */
    var refUnresolved = (typeof __LB.refMiss === "number") ? __LB.refMiss : 0;
    var sc = docPage.querySelector('.selfcheck');
    if (sc) {
      var nSeq = checks.filter(function (x) { return ['节号连续', '章号连续', '述评恒末'].indexOf(x[0]) >= 0; }).length;
      var badCount = (nSeq > 0 ? 1 : 0) + (dupTitles > 0 ? 1 : 0);
      var ok = badCount === 0;
      var nNotes = kCount.x + kCount.m + kCount.s;
      var nPersons = DATA.persons ? DATA.persons.length : 0;
      var nYears = Object.keys(years).length;
      sc.className = 'selfcheck' + (ok ? '' : ' bad');
      // 2026-09-27：桌面端把序列自校验（原独立一行）并入本行，故通过时补 .sc-seq 段；
      // 有异常时不宣称“序列连续”，异常明细仍列于详情区。移动端由样式层隐藏该段并保留独立行。
      var sum = '目录自校验 ' + (6 - badCount) + '/6' + (ok ? ' 通过' : ' · ' + badCount + ' 项异常') +
        (ok ? '<span class="sc-seq">' + U("ui.selfcheck.seq") + '</span>' : '');
      var li = [];
      if (nSeq > 0) li.push('<li class="bad-item">' + U("ui.selfcheck.b1") + '' + nSeq + '' + U("ui.selfcheck.b1s") + '</li>');
      if (dupTitles > 0) li.push('<li class="bad-item">' + U("ui.selfcheck.b3") + '' + dupTitles + '' + U("ui.selfcheck.b3s") + '</li>');
      if (refUnresolved > 0) li.push('<li class="bad-item">' + U("ui.selfcheck.b4") + '' + refUnresolved + '' + U("ui.selfcheck.b4s") + '</li>');
      li.push('<li class="ok-item">' + (refUnresolved ? '④ ref 未解析 ' + refUnresolved + ' 处 · ' : '') +
        '② 溯源注 ' + nNotes + ' · ⑤ 人名 ' + nPersons + ' · ⑥ 年份 ' + nYears + ' / 节 ' + secs.length + '</li>');
      sc.innerHTML = '<span class="dot"></span><span class="sc-sum">' + sum + ' · 注 ' + nNotes + ' · 人名 ' + nPersons + ' · 年份 ' + nYears + ' · 节 ' + secs.length + '</span>' +
        '<button type="button" class="sc-toggle" aria-expanded="false">' + U("ui.selfcheck.details") + '</button>' +
        '<ul>' + li.join('') + '</ul>';
      var sct = sc.querySelector('.sc-toggle');
      sct.addEventListener('click', function () {
        var open = sc.classList.toggle('open');
        this.setAttribute('aria-expanded', open ? 'true' : 'false');
        this.textContent = open ? '收起 ⌃' : '详情 ⌄';
      });

      var ssum = sc.querySelector('.sc-sum');
      ssum.addEventListener('click', function () {
        sc.classList.toggle('open');
        sct.setAttribute('aria-expanded', sc.classList.contains('open') ? 'true' : 'false');
        sct.textContent = sc.classList.contains('open') ? '收起 ⌃' : '详情 ⌄';
      });
      if (!ok) { sc.classList.add('open'); sct.setAttribute('aria-expanded', 'true'); sct.textContent = '收起 ⌃'; }
      if (nSeq) console.warn(U("diag.toc_seq"), checks.filter(function (x) { return ['节号连续', '章号连续', '述评恒末'].indexOf(x[0]) >= 0; }).slice(0, 30));
      sc.setAttribute('data-checks', '6');
    }

      } catch (err) { console.error(U("diag.selfcheck"), err); }
  /* ---------- 12.（已移除）原“接入检索（含人名与文献题名）”为死代码 ----------
     缘由：该块以 window.__optSearchRun 作功能门，而该标识符全库从未赋值 → 分支恒不返回；
     且现行检索词表仅含节名／溯源注／章题／卷题，未含人名与文献题名，改 placeholder 亦属误导。
     如需人名／文献检索，请另行实现并同步 placeholder 与面板说明。 */
  try {
    /* ---------- 13. 节级力导向（简化为按卷聚簇的静态布局，边＝注指向） ---------- */
    var btnG = document.getElementById('optGraphBtn');
    if (btnG) {
      btnG.title = U("ui.graph.title");
    }

    function closePanels() { __LB.closeDialogs(true); }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closePanels();
      if (e.key === 'r' && e.altKey) { var b = document.getElementById('optMode'); if (b) b.click(); }
    });
  } catch (err) {
    if (window.console && console.warn) console.warn(U("diag.r3"), err);
  }
    /* O-3 修正（2026-10-11）：data-opt-ready=1 的语义须为“plink 注入亦已完成”——
       Worker 异步化后若不门控，冷载实测 ready 早于 plink 套用（ready=1 时 plink=0），
       full_matrix 移动端 412x915 三组合断言读空。异步门控恢复基线语义。 */
    (__plinkDone || Promise.resolve()).then(function () {
      __LB.decorateDialogs();
      __waitStable(300, function () {

        try { window.dispatchEvent(new Event("resize")); } catch (e) {}
        document.documentElement.setAttribute("data-opt-ready", "1");
      });
    });
  });
})();

/* ========== 卷/章折叠（2026-09-26 ykla 要求） ==========
   2026-09-27 修正（ykla 报障“章卷文字在网页上无法选中”）：题面文字须可选中，故
   ①modern.css 撤去 h2／h3.chapter 本体上的 user-select:none（仅装饰箭头仍不可选）；
   ②本处补“选择判据”——纯点题才是折叠手势，凡带选择语义的手势一律不折：
      a. 拖选：down→up 位移 > 4px 的 click 非折叠手势（含拖选出界后仍落在题面的收尾 click）；
      b. click 落点时选中区非空（同上，双保险）；
      c. 确认窗：单击不当场折，先等 250ms 确认无第二击再折；第二击（双击／三击，
         detail>1）到达即撤单——故双击选词、三击选段**全程版面零跳动**
         （初版“先折后折回”会令整卷闪一下）；手速慢于确认窗者由 dblclick 兜底折回。
   点题内交互件（链接／按钮／徽标）与键盘 Enter 触发的 click（detail=0）行为不变。 */
var __foldDown = null;
document.addEventListener('mousedown', function (e) { __foldDown = { x: e.clientX, y: e.clientY }; });
function __foldBox(el) {
  if (!el || !el.closest) return null;
  var h2 = el.closest('.doc-block > h2');
  return h2 ? h2.parentElement : el.closest('h3.chapter');
}
function __foldSelectGesture(e) {
  if (__foldDown && (Math.abs(e.clientX - __foldDown.x) > 4 || Math.abs(e.clientY - __foldDown.y) > 4)) return true;
  var sel = window.getSelection ? window.getSelection() : null;
  return !!(sel && sel.rangeCount && !sel.isCollapsed);
}
var __foldTimer = 0, __foldLast = null;   /* __foldLast＝已折的折叠体，供手速慢者的 dblclick 兜底折回 */
function __foldToggle(box) {
  box.classList.toggle('folded');
  __foldLast = { box: box, t: Date.now() };
}
document.addEventListener('click', function (e) {
  var t = e.target;
  var box = __foldBox(t);
  if (!box) return;
  if (t.closest('a, button, input, select, textarea, label, [role="button"]')) return;
  if (e.detail > 1) { clearTimeout(__foldTimer); __foldTimer = 0; return; }   /* 第二、三击＝选择手势，撤单 */
  if (__foldSelectGesture(e)) return;
  clearTimeout(__foldTimer);
  __foldTimer = setTimeout(function () { __foldTimer = 0; __foldToggle(box); }, 250);
});
document.addEventListener('dblclick', function (e) {
  var last = __foldLast;
  __foldLast = null;
  if (!last || Date.now() - last.t > 400) return;    /* 超窗即非本次双击所致 */
  if (__foldBox(e.target) !== last.box) return;
  last.box.classList.toggle('folded');               /* 兜底折回：两击间隔慢于确认窗的双击 */
});
document.addEventListener('keydown', function (e) {
  if (e.altKey && (e.key === 's' || e.key === 'S')) {
    document.body.classList.toggle('sec-only');
  }
});
