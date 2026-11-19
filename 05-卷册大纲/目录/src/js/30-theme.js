(function () {
  var btn = document.getElementById("themeToggle");
  if (!btn) return;
  var root = document.documentElement;
  /* 主题面（2026-11-19 ykla 令“只保留纯黑 OLED 主题和纯彩主题，移除墨水屏和其他配色”）：
     light＝纯彩（纸面底色全彩），oled＝纯黑（AMOLED 夜间）。历史值迁移：dark→oled（153 批）、
     eink→light（本批，墨水屏主题移除后落最近的浅色面）。 */
  var ORDER = ["light", "oled"];
  var GLYPH = { light: "☾", oled: "●" };
  var FALL = { light: "#F9F5F0", oled: "#000000" };
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
    __LB.viewTransition(function () { apply(next); });
  });
  /* 未显式选择过时，跟随系统主题变化 */
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onSys = function () {
      var s = null; try { s = localStorage.getItem("sme-theme"); } catch (e) {}
      if (s === "dark") s = "oled";       /* 153 批：历史值迁移 */
      if (s === "eink") s = "light";      /* 本批：历史值迁移 */
      if (ORDER.indexOf(s) < 0) {
        apply(mq.matches ? "oled" : "light");
      }
    };
    if (mq.addEventListener) mq.addEventListener("change", onSys); else if (mq.addListener) mq.addListener(onSys);
  }
})();
