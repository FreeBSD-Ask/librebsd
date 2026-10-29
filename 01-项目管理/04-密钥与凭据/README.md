# 密钥与凭据（独立存放，不入库）

- 建立时间：2026-10-29
- 处置口径：本目录除本 README 外**整目录不入库**（`.gitignore` 负向例外只放行 README），
  远端仓库永不含密钥本体；库内文件只在本机留存，随 `12-数据库备份/` 之外单独保管。
- 背景：全库扫描（`sk-` 前缀高熵串）命中 16 件，原散落于 `script/` 与 `.tmp/`（均在忽略区，从未入库），
  但两处均为可随时清理的临时目录，存在随清理丢失或误提交的双重风险，故集中归集。

## 处置要求

1. 任何脚本不得在本目录之外硬编码密钥；运行期一律从本目录读取或走环境变量。
2. 新增密钥先落本目录，再在调用处引用路径；不得回写 `script/`、`.tmp/`。
3. 本目录不参与 `git add`、不打包外发、不进任何归档件；备份另行处置。
4. 疑似泄露即轮换，轮换后旧值在本目录内就地标注失效日期，不删除、不覆盖。

## 清单（16 件）

| # | 库内路径 | 原路径 | 字节 |
| ---: | --- | --- | ---: |
| 1 | `script/zcode_fix_backup_20261022/20261022-164157/C_tasks-index.sqlite` | `script/zcode_fix_backup_20261022/20261022-164157/C_tasks-index.sqlite` | 11210752 |
| 2 | `script/zcode_fix_backup_20261022/20261022-164157/D_tasks-index.sqlite` | `script/zcode_fix_backup_20261022/20261022-164157/D_tasks-index.sqlite` | 11235328 |
| 3 | `script/_db_row_mining/fpo_b185_forread.txt` | `script/_db_row_mining/fpo_b185_forread.txt` | 4600944 |
| 4 | `script/_glm_line_alive_keys_20261006.txt` | `script/_glm_line_alive_keys_20261006.txt` | 2040 |
| 5 | `script/_keytest_tmp/keys.txt` | `script/_keytest_tmp/keys.txt` | 203 |
| 6 | `script/_keytest_tmp/keys_gl2_20261003.txt` | `script/_keytest_tmp/keys_gl2_20261003.txt` | 2040 |
| 7 | `script/_keytest_tmp/keys_gl2_20261003.txt.result.txt` | `script/_keytest_tmp/keys_gl2_20261003.txt.result.txt` | 3884 |
| 8 | `script/_keytest_tmp/keys_gl_after.txt` | `script/_keytest_tmp/keys_gl_after.txt` | 1587 |
| 9 | `script/_keytest_tmp/keys_gl_after.txt.result.txt` | `script/_keytest_tmp/keys_gl_after.txt.result.txt` | 3420 |
| 10 | `script/_keytest_tmp/keys_gl_current.txt` | `script/_keytest_tmp/keys_gl_current.txt` | 1587 |
| 11 | `script/_keytest_tmp/keys_gl_current.txt.result.txt` | `script/_keytest_tmp/keys_gl_current.txt.result.txt` | 3624 |
| 12 | `_tmp/keys_gl_batch_20261008.txt` | `.tmp/keys_gl_batch_20261008.txt` | 1088 |
| 13 | `_tmp/probe_keys_models_20261008.py` | `.tmp/probe_keys_models_20261008.py` | 2566 |
| 14 | `_tmp/probe_keys_xian6_20261008.py` | `.tmp/probe_keys_xian6_20261008.py` | 4361 |
| 15 | `_tmp/_check_keys_gl4.py` | `.tmp/_check_keys_gl4.py` | 3951 |
| 16 | `_tmp/_probe_gl_all.result.json` | `.tmp/_probe_gl_all.result.json` | 4499 |

## 维护

- 复核扫描命令（本目录已排除）：
  `grep -rlE "sk-[A-Za-z0-9]{20}" script/ .tmp/ state/ specs/`
- 命中即迁入本目录并在上表登记，保持“库外零密钥”。
