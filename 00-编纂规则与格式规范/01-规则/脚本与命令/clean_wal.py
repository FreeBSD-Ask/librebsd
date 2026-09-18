#!/usr/bin/env python3
"""清理所有WAL/SHM残留，恢复数据库写入能力"""
import os, sqlite3, glob

ROOT = r"D:\librebsd"

# 先清理脚本目录中的（backup/staging）
for d in ['script/_backup_*', 'script/_staging/*', 'script/_tmp_*']:
    for f in glob.glob(os.path.join(ROOT, d, '*.db-wal'), recursive=False):
        db = f[:-4]
        if os.path.exists(db):
            try:
                conn = sqlite3.connect(db)
                conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
                conn.close()
            except:
                pass
        try: os.remove(f)
        except: pass
        shm = f[:-4] + '-shm'
        try: os.remove(shm)
        except: pass

# 核心数据库 checkpoint并删除WAL
core_dirs = [
    r'01-项目管理\00-变更记录',
    r'02-sacred源材料',
    r'03-原始史料库',
    r'03-原始史料库\01-代码仓库史料\01-数据库本体',
    r'03-原始史料库\01-代码仓库史料\02-FreeBSD\db',
    r'03-原始史料库\01-代码仓库史料\03-NetBSD\db',
    r'03-原始史料库\01-代码仓库史料\04-OpenBSD\db',
    r'03-原始史料库\01-代码仓库史料\05-DragonFlyBSD\db',
    r'03-原始史料库\01-代码仓库史料\06-OpenZFS\db',
    r'03-原始史料库\01-代码仓库史料\07-BSD衍生项目\db',
    r'03-原始史料库\01-代码仓库史料\08-跨项目对比\db',
    r'03-原始史料库\01-代码仓库史料\09-Darwin\db',
    r'03-原始史料库\01-代码仓库史料\10-LinuxKernel\db',
    r'04-现代研究文献',
    r'04-现代研究文献\05-参考文献全文数据库',
    r'04-现代研究文献\06-存疑数据库',
    r'07-事实核查记录',
    r'08-核查报告与多轮复核',
    r'10-交叉索引',
    r'11-元数据接口',
]

for d in core_dirs:
    full = os.path.join(ROOT, d)
    for f in glob.glob(os.path.join(full, '*.db-wal')):
        db = f[:-4]
        try:
            conn = sqlite3.connect(db)
            conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
            conn.close()
            print(f"  checkpoint: {os.path.basename(db)}")
        except Exception as e:
            print(f"  skip: {os.path.basename(db)}: {e}")
        try: os.remove(f)
        except: pass
        shm = f[:-4] + '-shm'
        try: os.remove(shm)
        except: pass

print("\n✅ WAL清理完成")
