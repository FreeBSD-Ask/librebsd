
(function () {
  /* 标题净化器统一由 __LB.pureTitle 提供（本块原有一份同名局部实现，已上提去重） */
  window.exportSummaryText = function () {
    var page = document.querySelector(".doc-page");
    var vols = Array.from(page.querySelectorAll("section[id^='vol-']"));
    var chCount = 0;
    var secCount = 0;
    var lines = [];
    lines.push("# Summary");
    lines.push("");
    lines.push(U("ui.export.sum_title"));
    lines.push(U("ui.export.sum_source"));
    lines.push(U("ui.export.sum_note"));
    lines.push(U("ui.export.sum_time") + new Date().toLocaleString("zh-CN", { hour12: false }));
    lines.push("");
    lines.push(U("ui.export.sum_head"));
    lines.push("");
    vols.forEach(function (vol, vi) {
      var vNo = String(vi + 1).padStart(2, "0");
      var h2 = vol.querySelector("h2");
      lines.push("### " + __LB.pureTitle(h2));
      lines.push("");
      var chInVol = 0;
      vol.querySelectorAll("h3[id]").forEach(function (ch) {
        chCount++;
        chInVol++;
        var chTitle = __LB.pureTitle(ch);
        var m = chTitle.match(/第\s*(\d+)\s*章/);
        var chNo = m ? m[1] : String(chInVol);
        var chDir = "第" + vNo + "卷/第" + chNo + "章";
        lines.push("- [" + chTitle + "](./" + chDir + "/概述.md)");
        var ul = ch.nextElementSibling;
        if (!ul || !ul.classList || !ul.classList.contains("sections")) return;
        ul.querySelectorAll("li").forEach(function (li) {
          secCount++;
          var numEl = li.querySelector(".sec-num");
          var num = numEl ? numEl.textContent.trim() : "";
          /* 节号已由 .sec-num 的移除而剥离，此处不得再做子串替换：
             否则题文本身以节号字面量开头时（如 “4.2BSD 的版本组成与前代继承”）会被误删开头。 */
          var title = __LB.pureTitle(li);
          lines.push("  - [" + num + " " + title + "](./" + chDir + "/" + num + ".md)");
        });
      });
      lines.push("");
    });
    lines.push("");
    lines.push("---");
    lines.push("");
    lines.push(F("ui.export.stats_fmt", { v: vols.length, c: chCount, s: secCount }));
    return lines
      .join("\n")
      .replace(/\u3000/g, " ")
      .replace(/\u00a0/g, " ")
      .replace(/[ \t]+$/gm, "");
  };
})();
