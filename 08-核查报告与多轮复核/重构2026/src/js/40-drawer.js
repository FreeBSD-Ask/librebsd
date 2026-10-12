
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
