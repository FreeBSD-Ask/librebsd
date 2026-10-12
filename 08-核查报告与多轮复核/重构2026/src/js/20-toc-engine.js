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
      ul.querySelectorAll("li").forEach((li) => {
        const secNum = li.querySelector(".sec-num");
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
        ul.querySelectorAll("li").forEach((li) => {
          const secNum = li.querySelector(".sec-num");
          const title = __LB.pureTitle(li);
          secs.push({ id: li.id, num: secNum ? secNum.textContent.trim() : "", title: title });
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
