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

