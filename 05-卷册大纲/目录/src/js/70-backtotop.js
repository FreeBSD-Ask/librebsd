
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
    /* 2026-10-10（128 号文批 5，主理人报障：向下的按钮失效）：原实现恒调 scrollToTop()——
       而顶部附近字形为 ↓（语义即到底部），点击仍回顶（原地不动），表现为失效。
       现按字形状态分派：顶部附近（scrollY 不超 400）回到底部，否则回顶部。 */
    if (nearTop()) { scrollToBottom(); } else { scrollToTop(); }
  });
  window.addEventListener("scroll", toggle, { passive: true });
  window.addEventListener("scroll", setGlyph, { passive: true });
  toggle();
  setGlyph();
})();
