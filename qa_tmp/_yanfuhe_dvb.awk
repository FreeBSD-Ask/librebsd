# 临时脚本：提取各章概述 DVB 指标（审计后删除）
function flush() {
  if (file != "") {
    vol = file; ch = file
    if (match(vol, /第[0-9]+卷/)) vol = substr(vol, RSTART, RLENGTH); else vol = "?"
    if (match(ch, /第[0-9]+章/)) ch = substr(ch, RSTART, RLENGTH); else ch = "?"
    printf "%s|%s|%s|%s|%d\n", vol, ch, anchor, ref, dvb
  }
}
FNR == 1 { flush(); file = FILENAME; anchor = "NA"; ref = "NA"; dvb = 0 }
anchor == "NA" && /锚定素材 \|/ {
  s = $0; sub(/.*锚定素材 \| /, "", s); sub(/[^0-9].*/, "", s); if (s != "") anchor = s
}
ref == "NA" && /参考文献匹配 \|/ {
  s = $0; sub(/.*参考文献匹配 \| /, "", s); sub(/[^0-9].*/, "", s); if (s != "") ref = s
}
/DATA_VERIFY_BLOCK/ { dvb++ }
END { flush() }
