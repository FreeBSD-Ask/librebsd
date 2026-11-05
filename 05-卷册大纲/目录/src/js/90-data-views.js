
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
