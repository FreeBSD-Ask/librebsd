r"""Update folder_db_registry.csv sha256/size fields from actual DuckDB files on disk."""
import csv
import hashlib
import os

BASE = r"d:\librebsd"
CSV_PATH = os.path.join(BASE, r"11-元数据接口\09-文件夹数据库索引\folder_db_registry.csv")

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data_rows = rows[1:]

updated = 0
skipped = 0
for row in data_rows:
    db_name = row[0]
    db_path = row[1]
    full_path = os.path.join(BASE, db_path)
    if os.path.exists(full_path):
        size = os.path.getsize(full_path)
        sha = sha256_of(full_path)
        old_size = row[4]
        old_sha = row[5]
        if old_size != str(size) or old_sha != sha[:16]:
            row[4] = str(size)
            row[5] = sha[:16]
            updated += 1
            print(f"  {db_name}: size {old_size}->{size}, sha {old_sha}->{sha[:16]}")
        else:
            skipped += 1
    else:
        skipped += 1
        print(f"  [跳过] {db_name}: 文件不存在: {full_path}")

with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(data_rows)

print(f"\n更新 {updated} 行，跳过 {skipped} 行（共 {len(data_rows)} 行）")