#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bsdnow_igpu_transcribe.py —— 播客音频转录并写入 DuckDB（固定脚本，2026-10-22 重建）。

背景
----
原脚本在 2026-10 丢失，`流程规则.md` 的播客收尾节仍以它为转录依赖。
本脚本按现有 `episodes／transcripts／segments／update_log` 表结构重建，
不依赖原实现；只做“本地音频 → faster-whisper → DuckDB”的单集写入。
原临时件 `script/_bsdnow_igpu_transcribe.py` 已移入本目录作为唯一权威副本。

用法
----
    python bsdnow_igpu_transcribe.py --selftest
    python bsdnow_igpu_transcribe.py --db bsd-now.duckdb --audio-dir audio --limit 1
    python bsdnow_igpu_transcribe.py --db bsd-now.duckdb --audio-dir audio \
        --episode-id 159 --model tiny --clip-seconds 30

依赖：duckdb、faster-whisper；`--clip-seconds` 需要 ffmpeg。
"""
import argparse
import datetime
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

import duckdb

REPO = pathlib.Path(__file__).resolve().parents[3]
PODCAST_DIR = REPO / "03-原始史料库" / "14-播客史料"
AUDIO_EXTS = (".wav", ".mp3", ".m4a", ".opus", ".webm", ".flac")

TRANSCRIPT_COLS = (
    "id, episode_id, full_text, model, language, transcribed_at, "
    "review_status, reviewed_at, quality_score, quality_flags, quality_checked_at"
)
SEGMENT_COLS = (
    "id, episode_id, transcript_id, segment_index, start_time, end_time, speaker, text"
)
UPDATE_COLS = (
    "id, file_id, operation, field_changed, old_value, new_value, timestamp, operated_by, notes"
)


def _now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _resolve(path, default_dir=PODCAST_DIR):
    p = pathlib.Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p
    return default_dir / p


def _next_id(con, table):
    row = con.execute(
        "SELECT COALESCE(MAX(TRY_CAST(id AS BIGINT)), 0) + 1 FROM %s" % table
    ).fetchone()
    return int(row[0])


def _find_audio(audio_dir, episode_id, audio_url=""):
    """按 episode_id 在 audio_dir 中找音频；支持 159.mp3、bsdnow_159.mp3 等。"""
    if audio_url:
        p = pathlib.Path(audio_url)
        if p.is_absolute() and p.is_file():
            return p
    audio_dir = pathlib.Path(audio_dir)
    if not audio_dir.is_dir():
        return None
    pat = re.compile(r"(^|[_-])%s([_.-]|$)" % re.escape(str(episode_id)))
    candidates = []
    for ext in AUDIO_EXTS:
        for p in audio_dir.rglob("*" + ext):
            if pat.search(p.stem):
                candidates.append(p)
    if not candidates:
        return None
    return sorted(candidates, key=lambda p: (len(p.name), p.name))[0]


def _make_transcriber(model, device, compute_type):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("依赖缺失：需要 faster-whisper。请先安装后再运行。", file=sys.stderr)
        return None
    engine = WhisperModel(model, device=device, compute_type=compute_type)

    def transcribe(path, language):
        segments, info = engine.transcribe(str(path), language=language, vad_filter=True)
        rows = [(float(s.start), float(s.end), (s.text or "").strip()) for s in segments]
        return rows, getattr(info, "language", language)

    return transcribe


def _clip_audio(src, seconds):
    if seconds <= 0:
        return pathlib.Path(src)
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("--clip-seconds 需要 ffmpeg 在 PATH 中")
    fd, name = tempfile.mkstemp(prefix="clip_", suffix=".wav")
    os.close(fd)
    dst = pathlib.Path(name)
    subprocess.run(
        [ffmpeg, "-y", "-i", str(src), "-t", str(seconds), "-ar", "16000", "-ac", "1", str(dst)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return dst


def _write(con, episode_id, segments, model, language, note=""):
    """在事务中写入 1 条 transcript、N 条 segment、1 条 update_log。"""
    transcript_id = _next_id(con, "transcripts")
    full_text = " ".join(t for _s, _e, t in segments if t).strip()
    con.execute("BEGIN")
    try:
        con.execute(
            "INSERT INTO transcripts (%s) VALUES (?,?,?,?,?,?,?,?,?,?,?)" % TRANSCRIPT_COLS,
            [str(transcript_id), str(episode_id), full_text, model, language,
             _now(), "unreviewed", None, None, [], None],
        )
        seg_id = _next_id(con, "segments")
        for i, (start, end, text) in enumerate(segments):
            con.execute(
                "INSERT INTO segments (%s) VALUES (?,?,?,?,?,?,?,?)" % SEGMENT_COLS,
                [str(seg_id + i), str(episode_id), str(transcript_id), str(i),
                 "%.2f" % start, "%.2f" % end, None, text],
            )
        log_id = _next_id(con, "update_log")
        con.execute(
            "INSERT INTO update_log (%s) VALUES (?,?,?,?,?,?,?,?,?)" % UPDATE_COLS,
            [str(log_id), str(transcript_id), "transcribe", "transcripts",
             None, model, _now(), "bsdnow_igpu_transcribe.py",
             note or ("episode %s, %d segments" % (episode_id, len(segments)))],
        )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    return transcript_id, len(segments)


def _schema(con):
    con.execute("CREATE TABLE episodes (id VARCHAR, title VARCHAR, audio_url VARCHAR, audio_deleted_at VARCHAR)")
    con.execute(
        "CREATE TABLE transcripts (id VARCHAR, episode_id VARCHAR, full_text VARCHAR, model VARCHAR, "
        "language VARCHAR, transcribed_at VARCHAR, review_status VARCHAR, reviewed_at VARCHAR, "
        "quality_score FLOAT, quality_flags VARCHAR[], quality_checked_at VARCHAR)"
    )
    con.execute(
        "CREATE TABLE segments (id VARCHAR, episode_id VARCHAR, transcript_id VARCHAR, "
        "segment_index VARCHAR, start_time VARCHAR, end_time VARCHAR, speaker VARCHAR, text VARCHAR)"
    )
    con.execute(
        "CREATE TABLE update_log (id VARCHAR, file_id VARCHAR, operation VARCHAR, field_changed VARCHAR, "
        "old_value VARCHAR, new_value VARCHAR, timestamp VARCHAR, operated_by VARCHAR, notes VARCHAR)"
    )


def _selftest():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="td009_selftest_"))
    db = tmp / "test.duckdb"
    con = duckdb.connect(str(db))
    try:
        _schema(con)
        con.execute("INSERT INTO episodes VALUES ('1','Test','',NULL)")
        tid, n = _write(con, "1", [(0.0, 2.5, "hello"), (2.5, 5.0, "world")], "tiny", "en")
        t = con.execute("SELECT full_text, model, language, review_status FROM transcripts").fetchone()
        s = con.execute("SELECT count(*), min(segment_index), max(segment_index) FROM segments").fetchone()
        u = con.execute("SELECT count(*) FROM update_log").fetchone()[0]
        assert t == ("hello world", "tiny", "en", "unreviewed"), t
        assert s == (2, "0", "1"), s
        assert u == 1, u
        print("  \u2705 selftest PASS: transcript=%s segments=%d update_log=%d" % (tid, n, u))
        return 0
    finally:
        con.close()
        shutil.rmtree(tmp, ignore_errors=True)


def _candidates(con, episode_id):
    sql = (
        "SELECT e.id, e.title, e.audio_url FROM episodes e "
        "LEFT JOIN transcripts t ON t.episode_id = e.id "
        "WHERE t.id IS NULL"
    )
    args = []
    if episode_id:
        sql += " AND e.id = ?"
        args.append(str(episode_id))
    sql += " ORDER BY TRY_CAST(e.id AS BIGINT), e.id"
    return con.execute(sql, args).fetchall()


def main():
    ap = argparse.ArgumentParser(description="播客音频转录并写入 DuckDB（TD-009 重建）")
    ap.add_argument("--db", default="bsd-now.duckdb")
    ap.add_argument("--audio-dir", default="audio")
    ap.add_argument("--episode-id", default="")
    ap.add_argument("--limit", type=int, default=0, help="0=全部待转录集")
    ap.add_argument("--model", default="small")
    ap.add_argument("--language", default="en")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--compute-type", default="int8")
    ap.add_argument("--clip-seconds", type=float, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    db = _resolve(args.db)
    audio_dir = _resolve(args.audio_dir)
    if not db.is_file():
        print("依赖缺失：找不到 %s" % db, file=sys.stderr)
        return 2
    con = duckdb.connect(str(db))
    try:
        episodes = _candidates(con, args.episode_id)
        if args.limit > 0:
            episodes = episodes[: args.limit]
        if not episodes:
            print("没有待转录集（或指定 episode 已有 transcript）。")
            return 0

        print("待处理 %d 集；db=%s；audio=%s；model=%s" %
              (len(episodes), db.name, audio_dir, args.model))
        transcribe = None if args.dry_run else _make_transcriber(
            args.model, args.device, args.compute_type)
        if transcribe is None and not args.dry_run:
            return 2

        done = 0
        skipped = 0
        for ep_id, title, audio_url in episodes:
            audio = _find_audio(audio_dir, ep_id, audio_url or "")
            if audio is None:
                print("  [SKIP] %s %s：未找到音频" % (ep_id, (title or "")[:60]))
                skipped += 1
                continue
            print("  [RUN ] %s %s：%s" % (ep_id, (title or "")[:60], audio.name))
            if args.dry_run:
                continue
            clip = _clip_audio(audio, args.clip_seconds)
            try:
                segments, language = transcribe(clip, args.language)
                if not segments:
                    print("  [SKIP] %s：转录结果为空" % ep_id)
                    skipped += 1
                    continue
                tid, n = _write(con, ep_id, segments, args.model, language,
                                "episode %s, audio %s, %d segments" % (ep_id, audio.name, len(segments)))
                print("  [OK  ] %s：transcript=%s segments=%d" % (ep_id, tid, n))
                done += 1
            finally:
                if args.clip_seconds > 0 and clip != audio:
                    clip.unlink(missing_ok=True)
        print("完成：写入 %d 集，跳过 %d 集。" % (done, skipped))
        if args.dry_run:
            return 0
        return 0 if done or not episodes else 1
    finally:
        con.close()


if __name__ == "__main__":
    sys.exit(main())
