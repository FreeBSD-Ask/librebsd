'use strict';
(function () {
  var t = null;
  try { t = localStorage.getItem("sme-theme"); } catch (e) {}
  if (t === "dark") { t = "oled"; }   /* 153 批：默认夜间模式删除，历史选择迁移至 AMOLED 纯黑 */
  var KNOWN = t === "light" || t === "oled" || t === "eink";
  if (!KNOWN) {
    var mono = false, slow = false;
    try { mono = !!(window.matchMedia && window.matchMedia("(monochrome: 1)").matches); } catch (e1) {}
    try { slow = !!(window.matchMedia && window.matchMedia("(update: slow)").matches); } catch (e2) {}
    if (mono || slow) { t = "eink"; }
    else { t = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "oled" : "light"; }
  }
  document.documentElement.setAttribute("data-theme", t);
  var MC = { light: "#F9F5F0", oled: "#000000", eink: "#ffffff" };
  var mt = document.querySelector('meta[name="theme-color"]');
  if (mt) mt.setAttribute("content", MC[t] || "#F9F5F0");
})();
