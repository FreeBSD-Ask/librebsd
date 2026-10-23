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
