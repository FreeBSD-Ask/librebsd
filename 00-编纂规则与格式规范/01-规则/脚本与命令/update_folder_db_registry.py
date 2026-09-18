r"""Update folder_db_registry.csv db_path from .db to .duckdb.

Rules:
- Functional DBs (12 功能库): <dir>/<name>.db → <dir>/<name>.duckdb
- Code repo DBs (15 代码仓库): <dir>/db/<name>.db → <dir>/db/duckdb/<name>.duckdb
- Mail merge DBs (4 邮件合并): <dir>/<name>.db → <dir>/duckdb/<name>.duckdb
- Mail split DBs (FreeBSD/NetBSD 拆分子库): <dir>/db/<name>.db → <dir>/db/<name>.duckdb
- Podcast DBs: <dir>/<name>.db → <dir>/<name>.duckdb
- linuxkernel_mail: already .duckdb, skip
"""

import csv
import os
import re

CSV_PATH = r"d:\librebsd\11-元数据接口\09-文件夹数据库索引\folder_db_registry.csv"
OUTPUT_PATH = CSV_PATH  # overwrite in place

# Known groups for path transformation
# 12 functional DBs - direct replacement .db → .duckdb
FUNCTIONAL_DBS = {
    "changelog", "sacred_sources", "original_sources", "research_notes",
    "historical_claims", "causal_graph", "references_fulltext",
    "doubts_standalone", "fact_checks", "review_reports",
    "cross_indexes", "metadata_interfaces",
}

# Code repo DBs - db/<name>.db → db/duckdb/<name>.duckdb
CODE_REPO_DBS = {
    "freebsd", "netbsd", "openbsd", "dragonfly", "openzfs",
    "bsd-derivatives", "illumos-gate", "openssh-apple", "openssh",
    "darwin", "linux-kernel",
}

# Mail merge DBs - <name>.db → duckdb/<name>.duckdb
MAIL_MERGE_DBS = {
    "openbsd_mail", "dragonfly_mail", "other-bsd_mail", "usenet_mail",
}

# Special DBs (phoronix_news, 资料数据库) - direct replacement
SPECIAL_DBS = {"phoronix_news", "资料数据库"}

# Podcast DBs - direct replacement
PODCAST_DBS = {"bsdnow_podcast", "bsd_podcasts_external"}

# Mail split DBs (FreeBSD ~145, NetBSD ~110) - db/<name>.db → db/<name>.duckdb
# These are identified by top_folder containing "邮件列表史料/01-freebsd" or "02-netbsd"


def transform_path(db_name, old_path):
    if old_path.endswith(".duckdb"):
        return old_path  # already updated

    if db_name in FUNCTIONAL_DBS or db_name in SPECIAL_DBS or db_name in PODCAST_DBS:
        return old_path.replace(".db", ".duckdb")

    if db_name in CODE_REPO_DBS:
        # db/<name>.db → db/duckdb/<name>.duckdb
        return old_path.replace(".db", ".duckdb").replace("/db/", "/db/duckdb/", 1)

    if db_name in MAIL_MERGE_DBS:
        # <name>.db → duckdb/<name>.duckdb
        dirname = os.path.dirname(old_path)
        basename = os.path.basename(old_path).replace(".db", ".duckdb")
        return os.path.join(dirname, "duckdb", basename).replace("\\", "/")

    # Mail split DBs (db/<name>.db → db/<name>.duckdb)
    if "/db/" in old_path and old_path.endswith(".db"):
        return old_path.replace(".db", ".duckdb")

    # Default: just replace .db → .duckdb
    if old_path.endswith(".db"):
        return old_path.replace(".db", ".duckdb")

    return old_path


def main():
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data_rows = rows[1:]

    updated_count = 0
    for row in data_rows:
        db_name = row[0]
        old_path = row[1]
        new_path = transform_path(db_name, old_path)
        if new_path != old_path:
            row[1] = new_path
            updated_count += 1
            print(f"  {db_name}: {old_path} → {new_path}")

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(data_rows)

    print(f"\nUpdated {updated_count} rows out of {len(data_rows)} total.")
    print(f"Output written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()