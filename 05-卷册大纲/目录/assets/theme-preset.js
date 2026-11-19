'use strict';
(function () {
  var t = null;
  try { t = localStorage.getItem("sme-theme"); } catch (e) {}
  if (t === "dark") { t = "oled"; }    /* 153 批：默认夜间模式删除，历史选择迁移至 AMOLED 纯黑 */
  if (t === "eink") { t = "light"; }   /* 本批（2026-11-19）：墨水屏主题移除，历史选择迁移至纯彩 */
  var KNOWN = t === "light" || t === "oled";
  if (!KNOWN) {
    t = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "oled" : "light";
  }
  document.documentElement.setAttribute("data-theme", t);
  var MC = { light: "#F9F5F0", oled: "#000000" };
  var mt = document.querySelector('meta[name="theme-color"]');
  if (mt) mt.setAttribute("content", MC[t] || "#F9F5F0");
})();
