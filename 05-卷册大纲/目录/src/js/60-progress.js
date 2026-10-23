
(function () {
  var bar = document.createElement("div");
  bar.className = "read-progress";
  document.body.appendChild(bar);
  function update() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var r = max > 0 ? window.scrollY / max : 0;
    bar.style.transform = "scaleX(" + r + ")";
  }
  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
})();
