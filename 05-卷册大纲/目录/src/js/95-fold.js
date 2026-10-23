
/* ========== 卷/章折叠（2026-09-26 主理人要求） ==========
   2026-09-27 修正（主理人报障“章卷文字在网页上无法选中”）：题面文字须可选中，故
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
