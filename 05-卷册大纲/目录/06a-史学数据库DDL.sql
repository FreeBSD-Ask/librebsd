-- ============================================================
-- 史学主张数据库 historical_claims.db · 完整 DDL v0.2
-- （v0.1 = Task #10 五层隔离主库；v0.2 = Task #19 知识图谱分类学 + 一致性检查，见文末补编）
-- 【设计文本 · 不建库 · 不执行】（与 07 号文档同约束）
--
-- 依据：
--   02-数据库盘点与史料字段差距分析.md（Task #1，洗澄明）
--   01-编纂原则清单.md  P41（史料五层级）/ P43（三重形式主义化）/ P44（六期分期）
--   07-因果链与影响分类体系.md（claim_id/evidence_id/object_ref 接口、L1-L5 证据等级门禁）
--   09-语境术语记忆反事实争议五系统.md（controversy_id、sources 层级编码接口）
--
-- 双轨编码警示（方向相反，勿混）：
--   source_layer   INTEGER 1-5 —— P41 史料五层级，1=代码产物（最强）→ 5=二手研究（最弱）
--   evidence_level TEXT 'L1'-'L5' —— 任务书第29阶段证据等级，L5=直接代码来源（最强）→ L1=仅相关性（最弱）
--
-- 五层隔离：raw_source(L1) → evidence(L2) → claim(L3) → interpretation(L4) → narrative(L5)
--   层间只允许向下引用一层；narrative 禁止直接引用 raw_source（视图审计）。
-- ============================================================

PRAGMA foreign_keys = ON;
-- 实际建库时再开：PRAGMA journal_mode = WAL;

-- ============ 0. 元信息（全仓三件套惯例） ============

CREATE TABLE IF NOT EXISTS schema_meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS update_log (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    op         TEXT NOT NULL,
    detail     TEXT,
    operator   TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ============ 1. 受控词表与分期 ============

-- P44 六期表：年份允许交叠（第五、六期与第四期重叠），分期是建构而非编年
CREATE TABLE IF NOT EXISTS historical_period (
    period_id   TEXT PRIMARY KEY,              -- 'P1'..'P6'
    name        TEXT NOT NULL,                 -- 如 '伯克利 CSRG 时期'
    year_start  INTEGER NOT NULL,
    year_end    INTEGER NOT NULL,
    volumes     TEXT,                          -- JSON 数组：对应卷号，如 '[2,3]'
    cycle_phase TEXT CHECK (cycle_phase IN
                  ('prelude','aggregation','separation','re-aggregation','reflection')),
    note        TEXT,
    CHECK (year_start <= year_end)
);

-- 统一受控词表（消解 02 报告指出的 mat_type/source_tier/ref_type 三套分类互不对齐）
CREATE TABLE IF NOT EXISTS controlled_vocab (
    vocab_type TEXT NOT NULL,                  -- 'source_type'/'carrier'/'reliability_grade'/'entity_type'/'relation_type'
    code       TEXT NOT NULL,
    label      TEXT NOT NULL,
    definition TEXT,
    PRIMARY KEY (vocab_type, code)
);

-- 07 号 2.3 节措辞门禁表落库（审计视图按此扫描措辞越档）
CREATE TABLE IF NOT EXISTS wording_gate_rule (
    evidence_level  TEXT PRIMARY KEY CHECK (evidence_level IN ('L1','L2','L3','L4','L5')),
    evidence_nature TEXT NOT NULL,
    allowed_wording TEXT NOT NULL,
    forbidden_wording TEXT NOT NULL
);

-- ============ 2. 实体主数据（知识图谱节点） ============

CREATE TABLE IF NOT EXISTS entity (
    entity_id      TEXT PRIMARY KEY,           -- 'ENT-P-nnnn' 人 / ENT-O 机构 / ENT-J 项目 / ENT-T 技术 / ENT-E 事件 / ENT-L 地点
    entity_type    TEXT NOT NULL CHECK (entity_type IN
                     ('person','org','project','technology','event','place')),
    canonical_name TEXT NOT NULL,
    aliases        TEXT,                       -- JSON 数组
    attrs          TEXT,                       -- JSON：类型特有属性（person: bio/出生卒; org: 成立年; event: 描述）
    legacy_refs    TEXT,                       -- JSON：迁移溯源 [{"db":"cross_indexes","table":"person_records","id":...}]
    merged_into    TEXT REFERENCES entity(entity_id),
    created_at     TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at     TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_entity_type ON entity(entity_type);
CREATE INDEX IF NOT EXISTS idx_entity_name ON entity(canonical_name);

CREATE TABLE IF NOT EXISTS entity_relation (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    from_entity   TEXT NOT NULL REFERENCES entity(entity_id) ON DELETE CASCADE,
    to_entity     TEXT NOT NULL REFERENCES entity(entity_id) ON DELETE CASCADE,
    relation_type TEXT NOT NULL,               -- 'member_of'/'employed_by'/'forked_from'/'successor_of'/'participated_in'/'developed'/'funded_by'
    time_start    TEXT,
    time_end      TEXT,
    evidence_id   TEXT REFERENCES evidence(evidence_id),   -- 关系本身须有证据（前向引用，建库时生效）
    note          TEXT,
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (from_entity, to_entity, relation_type, time_start)
    -- 注：SQLite UNIQUE 视 NULL 互不相等，time_start 为 NULL 的重复行需应用层去重
);
CREATE INDEX IF NOT EXISTS idx_er_from ON entity_relation(from_entity);
CREATE INDEX IF NOT EXISTS idx_er_to   ON entity_relation(to_entity);

-- ============ 3. L1 原始史料层（注册制：不复制正文，只存坐标+哈希） ============

CREATE TABLE IF NOT EXISTS raw_source (
    source_id    TEXT PRIMARY KEY,             -- 'SRC-<namespace>:<本地键>'，如 'SRC-mat:1' 'SRC-mail:<Message-ID>' 'SRC-commit:<repo>:<hash>'
    namespace    TEXT NOT NULL CHECK (namespace IN
                   ('mat','mail','commit','ref','doc','sa','other')),
    source_db    TEXT,                         -- 原库文件路径（登记，不搬迁）
    source_table TEXT,
    local_pk     TEXT,                         -- 原库主键 / Message-ID / commit hash
    content_hash TEXT,                         -- 正文 SHA-256（正文留原库，哈希防漂移）
    title        TEXT,

    -- —— 史料分类 20 字段（02 报告差距表的落点）——
    source_type    TEXT NOT NULL,              -- controlled_vocab('source_type') 受控词
    carrier        TEXT CHECK (carrier IN
                     ('email','commit','code','doc_official','doc_personal','sa_errata',
                      'news','interview','memo','book','paper','web_archive','other')),
    source_layer   INTEGER NOT NULL CHECK (source_layer BETWEEN 1 AND 5),  -- P41：1 代码产物 → 5 二手研究
    tier_basis     TEXT,                       -- 层级判定理由（P43 诚实性：判定须留痕）
    source_date    TEXT,                       -- 史料生成日期（ISO 8601，允许 '1993'/'1993-06'）
    date_precision TEXT CHECK (date_precision IN ('year','month','day','range','unknown')),
    author         TEXT,                       -- 创作者原文
    author_entity  TEXT REFERENCES entity(entity_id),
    organization   TEXT,                       -- 所属机构原文
    org_entity     TEXT REFERENCES entity(entity_id),
    first_hand     INTEGER NOT NULL DEFAULT 0 CHECK (first_hand IN (0,1)),
    contemporary   INTEGER NOT NULL DEFAULT 0 CHECK (contemporary IN (0,1)),   -- 事件当时记录
    retrospective  INTEGER NOT NULL DEFAULT 0 CHECK (retrospective IN (0,1)),  -- 事后追述

    -- —— 出处（provenance）——
    provenance_url     TEXT,
    provenance_commit  TEXT,
    provenance_archive TEXT,                   -- web.archive 快照 URL
    acquired_at        TEXT,                   -- 采集时间
    acquisition_method TEXT,                   -- 'crawl'/'mbox_import'/'git_clone'/'scan_ocr'/'manual'

    -- —— 可靠性 ——
    reliability_grade TEXT CHECK (reliability_grade IN ('A','B','C','D','U')),  -- A高/B中/C低/D伪或禁/U未评
    reliability_rationale TEXT,
    banned_source  INTEGER NOT NULL DEFAULT 0 CHECK (banned_source IN (0,1)),   -- P41 禁用来源（百科/CSDN 类）
    doubt_flag     INTEGER NOT NULL DEFAULT 0 CHECK (doubt_flag IN (0,1)),      -- 迁资料库 doubt_flag

    legacy_status TEXT CHECK (legacy_status IN ('pending','migrated','verified')),
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at    TEXT NOT NULL DEFAULT (datetime('now')),

    -- 表级约束必须位于所有列定义之后（SQLite 语法要求）
    CHECK (NOT (contemporary = 1 AND retrospective = 1))
);
CREATE INDEX IF NOT EXISTS idx_rs_type   ON raw_source(source_type);
CREATE INDEX IF NOT EXISTS idx_rs_layer  ON raw_source(source_layer);
CREATE INDEX IF NOT EXISTS idx_rs_date   ON raw_source(source_date);
CREATE INDEX IF NOT EXISTS idx_rs_ns     ON raw_source(namespace, local_pk);

-- 史料 × 时期（六期年份交叠 → 多值）
CREATE TABLE IF NOT EXISTS source_period (
    source_id TEXT NOT NULL REFERENCES raw_source(source_id) ON DELETE CASCADE,
    period_id TEXT NOT NULL REFERENCES historical_period(period_id),
    PRIMARY KEY (source_id, period_id)
);

-- 史料 × 章节（迁移资料库现有 vol/ch/sec —— 全仓唯一 ✅ 字段，必须无损保留）
CREATE TABLE IF NOT EXISTS source_chapter (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT NOT NULL REFERENCES raw_source(source_id) ON DELETE CASCADE,
    vol       INTEGER NOT NULL,
    ch        INTEGER NOT NULL,
    sec       TEXT NOT NULL DEFAULT '',        -- '1.1.1'；'' = 仅到章
    link_type TEXT NOT NULL DEFAULT 'used' CHECK (link_type IN ('used','mentioned','background')),
    UNIQUE (source_id, vol, ch, sec)
);
CREATE INDEX IF NOT EXISTS idx_sc_chapter ON source_chapter(vol, ch, sec);

-- 史料间独立性（多源互证：02 报告 🔴 independence 的落点）
CREATE TABLE IF NOT EXISTS source_independence (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    source_a   TEXT NOT NULL REFERENCES raw_source(source_id),
    source_b   TEXT NOT NULL REFERENCES raw_source(source_id),
    relation   TEXT NOT NULL CHECK (relation IN
                 ('independent','dependent','repost','conflict','common_source')),
    note       TEXT,
    assessed_by TEXT,
    assessed_at TEXT,
    UNIQUE (source_a, source_b, relation),
    CHECK (source_a < source_b)                -- 无向边去重
);

-- ============ 4. L2 抽取证据层（升级 references_fulltext.key_facts 结构为全仓通用） ============

CREATE TABLE IF NOT EXISTS evidence (
    evidence_id   TEXT PRIMARY KEY,            -- 'EV-nnnnnn'
    source_id     TEXT NOT NULL REFERENCES raw_source(source_id),
    anchor        TEXT NOT NULL,               -- 'block:<id>'/'page:<n>'/'para:<n>'/'msg:<Message-ID>'/'file:<path>@<commit>'
    quote         TEXT NOT NULL,               -- 原文引句（source_quote 升格）
    quote_lang    TEXT,
    fact_text     TEXT,                        -- 抽取后的规范化表述
    evidence_kind TEXT CHECK (evidence_kind IN ('fact','timeline_event','mention','decision','quote')),
    event_date    TEXT,                        -- evidence_kind='timeline_event' 时
    event_date_precision TEXT CHECK (event_date_precision IN ('year','month','day','range','unknown')),
    confidence    REAL CHECK (confidence IS NULL OR (confidence BETWEEN 0 AND 1)),
    extracted_by  TEXT,                        -- 'human:<name>'/'llm:<model>'/'rule:<script>'
    extraction_review TEXT NOT NULL DEFAULT 'pending'
                    CHECK (extraction_review IN ('pending','checked','rejected')),
    legacy_refs   TEXT,                        -- 迁移溯源 JSON（如来自 key_facts.id）
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at    TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_ev_source ON evidence(source_id);
CREATE INDEX IF NOT EXISTS idx_ev_kind   ON evidence(evidence_kind);
CREATE INDEX IF NOT EXISTS idx_ev_date   ON evidence(event_date);

CREATE TABLE IF NOT EXISTS evidence_entity (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    evidence_id TEXT NOT NULL REFERENCES evidence(evidence_id) ON DELETE CASCADE,
    entity_id   TEXT NOT NULL REFERENCES entity(entity_id),
    role        TEXT NOT NULL DEFAULT 'mentioned'
                CHECK (role IN ('subject','object','agent','mentioned','location')),
    UNIQUE (evidence_id, entity_id, role)
);
CREATE INDEX IF NOT EXISTS idx_ee_entity ON evidence_entity(entity_id);

-- ============ 5. L3 历史主张层（07 号等待的"主张库"本体） ============

CREATE TABLE IF NOT EXISTS claim (
    claim_id      TEXT PRIMARY KEY,            -- 'CL-<卷>-<序号>'；影响主张用 'IC-' 前缀同表（claim_type='INFLUENCE_CLAIM'）
    claim_text    TEXT NOT NULL,               -- 一句话原子主张（禁笼统式，07 §2.0）
    claim_type    TEXT NOT NULL CHECK (claim_type IN (
                    'FACT','CAUSAL_CLAIM','INTERPRETATION','COMPARISON','INFLUENCE_CLAIM',
                    'ORIGIN_CLAIM','FIRST_APPEARANCE','MOTIVATION','CONTROVERSY','UNVERIFIED')),
    time_start    TEXT,
    time_end      TEXT,
    time_precision TEXT CHECK (time_precision IN ('year','month','day','range','unknown')),
    evidence_level TEXT CHECK (evidence_level IN ('L1','L2','L3','L4','L5')),  -- 任务书29阶段，L5 最强
    wording_gate  TEXT,                        -- 措辞档位快照（07 §2.3 门禁表）
    status        TEXT NOT NULL DEFAULT 'proposed'
                  CHECK (status IN ('proposed','supported','contested','refuted','superseded')),
    parent_claim_id TEXT REFERENCES claim(claim_id),   -- 分解溯源（笼统→原子留痕）
    impact_subtype TEXT CHECK (impact_subtype IN   -- claim_type='INFLUENCE_CLAIM' 时：07 十二分类
                    ('source_code','technical','api','architectural','design',
                     'organizational','cultural','licensing','personnel',
                     'academic','commercial','indirect')),
    linked_arrow_id TEXT,                      -- 关联因果箭头 AR-*（07）
    controversy_id  TEXT,                      -- → controversy（FK 在 controversy 建表后由应用层校验）
    created_by    TEXT,
    reviewed_by   TEXT,
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at    TEXT NOT NULL DEFAULT (datetime('now')),
    CHECK ( (claim_type = 'INFLUENCE_CLAIM' AND impact_subtype IS NOT NULL)
         OR (claim_type <> 'INFLUENCE_CLAIM') )
);
CREATE INDEX IF NOT EXISTS idx_cl_type   ON claim(claim_type);
CREATE INDEX IF NOT EXISTS idx_cl_status ON claim(status);
CREATE INDEX IF NOT EXISTS idx_cl_level  ON claim(evidence_level);

-- 主张 × 证据（支撑/反证同表；即 07 causal_arrow_evidence.evidence_id 的对端）
CREATE TABLE IF NOT EXISTS claim_evidence (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id       TEXT NOT NULL REFERENCES claim(claim_id) ON DELETE CASCADE,
    evidence_id    TEXT NOT NULL REFERENCES evidence(evidence_id),
    role           TEXT NOT NULL CHECK (role IN ('supporting','contradicting')),
    strength       TEXT CHECK (strength IN ('decisive','strong','weak','contextual')),
    disposition    TEXT,                       -- 反证处置：NULL=未处置；'已排除'/'并存'/'已采信推翻'
    search_log_ref TEXT,                       -- 反证检索留痕（"找了没找到"）
    created_at     TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (claim_id, evidence_id, role)
);
CREATE INDEX IF NOT EXISTS idx_ce_ev ON claim_evidence(evidence_id);

CREATE TABLE IF NOT EXISTS claim_entity (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id  TEXT NOT NULL REFERENCES claim(claim_id) ON DELETE CASCADE,
    entity_id TEXT NOT NULL REFERENCES entity(entity_id),
    role      TEXT NOT NULL DEFAULT 'subject'
              CHECK (role IN ('subject','object','agent','location')),
    UNIQUE (claim_id, entity_id, role)
);

CREATE TABLE IF NOT EXISTS claim_period (
    claim_id  TEXT NOT NULL REFERENCES claim(claim_id) ON DELETE CASCADE,
    period_id TEXT NOT NULL REFERENCES historical_period(period_id),
    PRIMARY KEY (claim_id, period_id)
);

-- 主张间关系（relevant_claims 的落点：主张-主张网络）
CREATE TABLE IF NOT EXISTS claim_relation (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    from_claim TEXT NOT NULL REFERENCES claim(claim_id) ON DELETE CASCADE,
    to_claim   TEXT NOT NULL REFERENCES claim(claim_id) ON DELETE CASCADE,
    relation   TEXT NOT NULL CHECK (relation IN
                 ('supports','contradicts','supersedes','decomposes_from','presupposes','related')),
    note       TEXT,
    UNIQUE (from_claim, to_claim, relation),
    CHECK (from_claim <> to_claim)
);

-- 争议登记簿（09 controversy_id 约定；迁 doubts_standalone 1,987 条）
CREATE TABLE IF NOT EXISTS controversy (
    controversy_id  TEXT PRIMARY KEY,          -- 如 'openbsd_fork_motive'
    title           TEXT NOT NULL,
    summary         TEXT,
    status          TEXT NOT NULL DEFAULT 'open'
                    CHECK (status IN ('open','adjudicated','irresolvable','merged')),
    adjudication    TEXT,                      -- 暂定判断（P43：呈现多面性，不宣布真相）
    legacy_refs     TEXT,                      -- doubts_standalone 迁移溯源 JSON
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS controversy_position (
    id                     INTEGER PRIMARY KEY AUTOINCREMENT,
    controversy_id         TEXT NOT NULL REFERENCES controversy(controversy_id) ON DELETE CASCADE,
    position_label         TEXT NOT NULL,      -- 'A'/'B'/'C' 或阵营名
    position_text          TEXT NOT NULL,
    sources_per_position   TEXT,               -- JSON: [{"source_id":"SRC-...","source_layer":2}]（09 约定）
    claim_id               TEXT REFERENCES claim(claim_id),   -- 该立场主张化后
    UNIQUE (controversy_id, position_label)
);

-- ============ 6. L4 历史解释层（多解释并存，P10 本体平等） ============

CREATE TABLE IF NOT EXISTS interpretation (
    interp_id     TEXT PRIMARY KEY,            -- 'ITP-nnnn'
    interp_text   TEXT NOT NULL,
    paradigm      TEXT,                        -- 解释框架（如 '权力再分配观（总纲13）'/'分离聚合循环（总纲14）'）
    interpreter   TEXT,
    coexists_with TEXT,                        -- JSON 数组：并存的 interp_id（并存≠择一）
    status        TEXT NOT NULL DEFAULT 'draft'
                  CHECK (status IN ('draft','active','superseded')),
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at    TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS interp_claim (
    interp_id TEXT NOT NULL REFERENCES interpretation(interp_id) ON DELETE CASCADE,
    claim_id  TEXT NOT NULL REFERENCES claim(claim_id),
    role      TEXT NOT NULL DEFAULT 'basis' CHECK (role IN ('basis','target','contrast')),
    PRIMARY KEY (interp_id, claim_id, role)
);

-- 解释可直接引证据（限引用层内动作），但不得越过证据直引原始史料
CREATE TABLE IF NOT EXISTS interp_evidence (
    interp_id   TEXT NOT NULL REFERENCES interpretation(interp_id) ON DELETE CASCADE,
    evidence_id TEXT NOT NULL REFERENCES evidence(evidence_id),
    PRIMARY KEY (interp_id, evidence_id)
);

-- ============ 7. L5 叙事层（chapter 迁 metadata_interfaces.chapter_metadata 348 章） ============

CREATE TABLE IF NOT EXISTS chapter (
    vol         INTEGER NOT NULL,
    ch          INTEGER NOT NULL,
    sec         TEXT NOT NULL DEFAULT '',
    title       TEXT NOT NULL,
    status      TEXT NOT NULL DEFAULT 'outline'
                CHECK (status IN ('outline','draft','reviewed','final')),
    legacy_refs TEXT,
    PRIMARY KEY (vol, ch, sec)
);

CREATE TABLE IF NOT EXISTS narrative_unit (
    unit_id    TEXT PRIMARY KEY,               -- 'NU-<卷>-<章>-<序号>'
    vol        INTEGER NOT NULL,
    ch         INTEGER NOT NULL,
    sec        TEXT NOT NULL DEFAULT '',
    unit_kind  TEXT NOT NULL DEFAULT 'section'
               CHECK (unit_kind IN ('section','sidebar','footnote_block','appendix')),
    draft_text TEXT,
    status     TEXT NOT NULL DEFAULT 'draft'
               CHECK (status IN ('draft','internal_review','final')),
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (vol, ch, sec) REFERENCES chapter(vol, ch, sec)
);

-- 叙事引用：五层隔离硬约束 —— target_type 不含 'raw_source'（L5 禁直引 L1）
CREATE TABLE IF NOT EXISTS narrative_citation (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id       TEXT NOT NULL REFERENCES narrative_unit(unit_id) ON DELETE CASCADE,
    target_type   TEXT NOT NULL CHECK (target_type IN ('claim','interpretation','evidence')),
    target_id     TEXT NOT NULL,
    citation_form TEXT CHECK (citation_form IN ('body','footnote','source_note')),
    UNIQUE (unit_id, target_type, target_id)
);
CREATE INDEX IF NOT EXISTS idx_nc_target ON narrative_citation(target_type, target_id);

-- ============ 8. 跨库引用与流转链 ============

-- 统一跨库引用（替代各三件套库失效的 target_db/target_record_id 机制；入库前校验 target 存在）
CREATE TABLE IF NOT EXISTS cross_ref (
    ref_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    from_type         TEXT NOT NULL,           -- 'raw_source'/'evidence'/'claim'/'entity'/'interpretation'/'narrative_unit'
    from_id           TEXT NOT NULL,
    to_db             TEXT,                    -- 目标库文件路径；本库内部引用为 NULL
    to_type           TEXT NOT NULL,
    to_id             TEXT NOT NULL,
    validation_status TEXT NOT NULL DEFAULT 'pending'
                      CHECK (validation_status IN ('pending','valid','dangling')),
    validated_at      TEXT,
    created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_xr_from ON cross_ref(from_type, from_id);
CREATE INDEX IF NOT EXISTS idx_xr_to   ON cross_ref(to_type, to_id);

-- 史料流转链（多跳 provenance：谁从哪转载、何时采集、何时归档）
CREATE TABLE IF NOT EXISTS provenance_history (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id  TEXT NOT NULL REFERENCES raw_source(source_id) ON DELETE CASCADE,
    seq        INTEGER NOT NULL,
    event_type TEXT NOT NULL CHECK (event_type IN
                 ('created','copied','reposted','archived','migrated','verified')),
    detail     TEXT,
    at         TEXT,
    UNIQUE (source_id, seq)
);

-- ============ 9. 审计视图 ============

-- 五层隔离违规（双保险：CHECK 已禁 raw_source，此视图兼容未来扩展）
CREATE VIEW IF NOT EXISTS v_layer_violation AS
SELECT unit_id, target_type, target_id, 'L5_cites_L1' AS violation
FROM narrative_citation
WHERE target_type NOT IN ('claim','interpretation','evidence');

-- 无证据主张（UNVERIFIED 类型与已否决主张除外）
CREATE VIEW IF NOT EXISTS v_claim_unsupported AS
SELECT c.claim_id, c.claim_text, c.claim_type, c.status
FROM claim c
WHERE c.claim_type <> 'UNVERIFIED'
  AND c.status NOT IN ('refuted','superseded')
  AND NOT EXISTS (
      SELECT 1 FROM claim_evidence ce
      WHERE ce.claim_id = c.claim_id AND ce.role = 'supporting');

-- 禁用来源（P41 百科类/不可溯源网络来源）
CREATE VIEW IF NOT EXISTS v_banned_source AS
SELECT source_id, title, source_type, provenance_url
FROM raw_source
WHERE banned_source = 1;

-- 悬空跨库引用（02 报告：旧机制 13 条中 7 条悬空，新库必须零容忍）
CREATE VIEW IF NOT EXISTS v_dangling_ref AS
SELECT ref_id, from_type, from_id, to_db, to_type, to_id
FROM cross_ref
WHERE validation_status = 'dangling';

-- ============ 10. 预置数据 ============

-- P44 六期（年份交叠为设计特性，非错误）
INSERT OR IGNORE INTO historical_period (period_id, name, year_start, year_end, volumes, cycle_phase, note) VALUES
 ('P1','UNIX 的史前与诞生',        1965, 1977, '[1]',     'prelude',        '卷 1'),
 ('P2','伯克利 CSRG 时期',         1979, 1995, '[2,3]',    'aggregation',    '卷 2-3'),
 ('P3','大分裂与四大 BSD 诞生',     1992, 2000, '[4]',      'separation',     '卷 4；与 P2 交叠'),
 ('P4','并行发展与生态扩张',        2000, 2015, '[5,6,7,8,9,10,11,12]', 're-aggregation', '卷 5-12；与 P3 交叠'),
 ('P5','商业深化与合规治理',        2005, 2025, '[13,14,15,16]', 're-aggregation', '卷 13-16；与 P4 交叠'),
 ('P6','全球社区与反思',           1993, 2025, '[17,18]',  'reflection',     '卷 17-18；与 P4/P5 交叠');

-- 措辞门禁表（07 §2.3 原文落库）
INSERT OR IGNORE INTO wording_gate_rule (evidence_level, evidence_nature, allowed_wording, forbidden_wording) VALUES
 ('L5','直接代码来源证据（commit/vendor 记录、代码谱系、版权头链）',
   '"X 中包含来自 BSD 的代码（文件 F，commit C）"；可写继承',
   '不得扩大到代码之外的类型'),
 ('L4','作者开发者明确陈述（当事人邮件、访谈、自述；须尽量配当时文本 P41）',
   '"据 X 本人陈述……"；可写影响，须带归源限定',
   '不得写"必然""注定"'),
 ('L3','技术文档论文明确说明（官方文档、设计文档、论文中的明确记载）',
   '"文档 D 记载……"；可写影响',
   '不得写"必然""注定"'),
 ('L2','强技术对应但缺直接证明（实现高度同构但无传承路径证据）',
   '只许"存在强技术对应，传承路径待证"',
   '禁止"继承/影响/源自/借鉴"'),
 ('L1','仅历史相关性相似性（时序相伴、表面相似、共同祖先遗产）',
   '只许"A 与 B 在时间上相伴/表面相似/共享共同祖先"',
   '禁止一切"继承/影响/源自/借鉴/抄自"；书稿中只能以相关性句式或存疑脚注出现');

-- source_type 受控词表（消解 mat_type/source_tier/ref_type 三套旧分类；旧值映射见设计文档 §4.3）
INSERT OR IGNORE INTO controlled_vocab (vocab_type, code, label, definition) VALUES
 ('source_type','code_artifact','代码与构建产物','源码、commit、二进制、构建产物（P41 第 1 层）'),
 ('source_type','mailing_list','邮件列表','列表邮件、讨论串（P41 第 2 层）'),
 ('source_type','irc_bugzilla','即时通讯与工单','IRC 记录、Bugzilla/issue（P41 第 2 层）'),
 ('source_type','official_doc','官方文档与公告','手册、SA/Errata、Release Notes、官网（P41 第 3 层）'),
 ('source_type','talk_interview','演讲与访谈','事后口述（P41 第 4 层）'),
 ('source_type','memoir_blog','回忆录与博客','个人追述（P41 第 4 层）'),
 ('source_type','academic_work','学术论文与专著','二手研究（P41 第 5 层）'),
 ('source_type','reference_book','工具书与参考','辞典、年表、标准文本'),
 ('source_type','news','新闻报道','Phoronix 等媒体（须核）'),
 ('source_type','web_archive','网页存档','archive.org 快照等'),
 ('source_type','banned','禁用来源','百科类/CSDN/不可溯源网络来源（P41 绝对禁用，banned_source=1）');

-- 证据等级门禁说明入 schema_meta
INSERT OR IGNORE INTO schema_meta (key, value) VALUES
 ('schema_version','0.1'),
 ('status','design_text_not_executed'),
 ('created_by','data-engineer 洗澄明'),
 ('created_for','Task #10 Phase 6-8'),
 ('source_layer_convention','P41 五层级：1=代码产物(最强) → 5=二手研究(最弱)'),
 ('evidence_level_convention','任务书29阶段：L1=仅相关性(最弱) → L5=直接代码来源(最强)'),
 ('layer_isolation','raw_source(L1)→evidence(L2)→claim(L3)→interpretation(L4)→narrative(L5)，只许向下引用一层'),
 ('claim_id_convention','CL-<卷>-<序号>；影响主张 IC-<卷>-<序号>（与 07 号文档一致）'),
 ('evidence_id_convention','EV-<六位序号>'),
 ('source_id_convention','SRC-<namespace>:<本地键>，namespace ∈ mat/mail/commit/ref/doc/sa/other');

-- ============ 11. 维护触发器 ============

CREATE TRIGGER IF NOT EXISTS trg_claim_touch AFTER UPDATE ON claim
BEGIN UPDATE claim SET updated_at = datetime('now') WHERE claim_id = NEW.claim_id; END;

CREATE TRIGGER IF NOT EXISTS trg_evidence_touch AFTER UPDATE ON evidence
BEGIN UPDATE evidence SET updated_at = datetime('now') WHERE evidence_id = NEW.evidence_id; END;

CREATE TRIGGER IF NOT EXISTS trg_raw_source_touch AFTER UPDATE ON raw_source
BEGIN UPDATE raw_source SET updated_at = datetime('now') WHERE source_id = NEW.source_id; END;

CREATE TRIGGER IF NOT EXISTS trg_interp_touch AFTER UPDATE ON interpretation
BEGIN UPDATE interpretation SET updated_at = datetime('now') WHERE interp_id = NEW.interp_id; END;

-- ============================================================
-- v0.2 补编（Task #19 Phase 31-33 知识图谱分类学 + 一致性检查）
-- 扩展点全部为增量 ALTER/新表/新视图，v0.1 表结构零改动。
-- ============================================================

-- 12. 实体类型扩展：任务书 18 类实体 → 6 基类的映射（entity.entity_type 仍用基类，细分走 subtype）
CREATE TABLE IF NOT EXISTS entity_type_class (
    entity_subtype TEXT PRIMARY KEY,            -- 任务书 18 类细分
    base_class     TEXT NOT NULL CHECK (base_class IN
                   ('person','org','project','technology','event','place')),
    label          TEXT NOT NULL,
    note           TEXT
);

INSERT OR IGNORE INTO entity_type_class (entity_subtype, base_class, label, note) VALUES
 ('person','person','人物',NULL),
 ('org','org','机构（通用）',NULL),
 ('university','org','大学',NULL),
 ('company','org','公司',NULL),
 ('community','org','社区','虚拟组织，无注册实体'),
 ('project','project','项目','含操作系统项目与子项目'),
 ('distribution','project','发行版','GhostBSD/OPNsense 类衍生发行'),
 ('version','technology','版本','如 4.4BSD-Lite、FreeBSD 2.0；挂 parent 项目于 attrs'),
 ('code','technology','代码','模块/文件级代码对象'),
 ('technology','technology','技术（通用）',NULL),
 ('standard','technology','标准','POSIX/SUS/RFC 等'),
 ('paper','technology','论文','作为被引用知识对象；其载体另在 raw_source(namespace=ref)'),
 ('book','technology','书籍','同上'),
 ('license','technology','许可证','P41 要求落到文本与决策，不落理念'),
 ('event','event','事件（通用）',NULL),
 ('conference','event','会议','BSDCan/EuroBSDCon 等'),
 ('legal_event','event','法律事件','诉讼/判决/和解，如 USL v. BSDi'),
 ('funding','event','资金事件','资助/合同；资助方与受助方经 entity_relation 挂接'),
 ('hardware','technology','硬件','物质文化史料（03-原始史料库/09 对应）'),
 ('place','place','地点',NULL);

-- 13. 关系类型受控词表（任务书 Phase 31 关系清单落库；entity_relation.relation_type 取值于此）
CREATE TABLE IF NOT EXISTS entity_relation_type (
    relation_code     TEXT PRIMARY KEY,
    label             TEXT NOT NULL,
    definition        TEXT,
    requires_temporal_order INTEGER NOT NULL DEFAULT 0 CHECK (requires_temporal_order IN (0,1)),
                                             -- 1 = 时序敏感（fork/derive/copy/port/rewrite/acquire/merge/split），触发 T1 检查
    requires_evidence INTEGER NOT NULL DEFAULT 1 CHECK (requires_evidence IN (0,1))
);

INSERT OR IGNORE INTO entity_relation_type VALUES
 ('created','创造','主体创造/发起了客体',1,1),
 ('worked_on','参与开发','人在项目/代码上的工作',0,1),
 ('employed_by','受雇于','人对机构的雇佣关系',0,1),
 ('funded','资助','资金/机构→项目',1,1),
 ('forked','分支','项目→项目的分离（P14 分离聚合）',1,1),
 ('derived_from','派生自','派生关系的伞类型（07 影响分类之外的谱系关系）',1,1),
 ('copied','复制','代码对象间的复制',1,1),
 ('ported','移植','代码/技术跨平台移植',1,1),
 ('rewritten','重写','代码对象被重写',1,1),
 ('influenced','影响','须先有 INFLUENCE_CLAIM 主张支撑，禁止裸挂（07 措辞门禁）',1,1),
 ('adopted','采纳','项目/组织采纳技术/方案',1,1),
 ('rejected','拒绝','项目/组织拒绝技术/方案',1,1),
 ('licensed_under','以许可证发布','项目/代码→许可证',1,1),
 ('acquired','收购','机构→机构/项目',1,1),
 ('merged','合并','两实体合并为一',1,1),
 ('split','分裂','一实体分裂为多',1,1),
 ('published','发表','人/机构→论文/书籍/文档',1,1),
 ('discussed','讨论','邮件/会议中讨论某对象（P42 讨论串追踪）',0,1),
 ('criticized','批评','主体对客体的公开批评',0,1),
 ('remembered_as','被记忆为','记忆史维度（09 记忆系统）：后世如何记述该对象',0,1),
 ('member_of','隶属于','人对组织/社区',0,1),
 ('participated_in','参与事件','人/机构→事件',1,1),
 ('located_in','位于','机构/事件→地点',0,0),
 ('successor_of','继承于','项目/组织的后继关系',1,1);

-- 14. 一致性规则登记（规则库：编号稳定，供审计报告引用）
CREATE TABLE IF NOT EXISTS consistency_rule (
    rule_id     TEXT PRIMARY KEY,                -- 'T1'/'T5'/'N3'...（15 号文档编号一致）
    rule_class  TEXT NOT NULL CHECK (rule_class IN ('temporal','narrative')),
    name        TEXT NOT NULL,
    description TEXT NOT NULL,
    severity    TEXT NOT NULL DEFAULT 'block' CHECK (severity IN ('block','warn','info')),
    sql_impl    TEXT,                            -- 检查 SQL 文本（审计脚本执行，非触发器）
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

-- 15. 一致性检查结果（每次审计 run 落一张快照）
CREATE TABLE IF NOT EXISTS consistency_check (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id        TEXT NOT NULL,                 -- 'AUDIT-YYYYMMDD-nn'
    rule_id       TEXT NOT NULL REFERENCES consistency_rule(rule_id),
    target_type   TEXT NOT NULL,                 -- 'entity'/'entity_relation'/'claim'/'evidence'/'narrative_unit'
    target_id     TEXT NOT NULL,
    severity      TEXT NOT NULL CHECK (severity IN ('block','warn','info')),
    detail        TEXT,                          -- 冲突描述（含两个竞争取值）
    resolution    TEXT,                          -- NULL=未处置；'已修正'/'并存标注'/'已裁决'
    resolved_by   TEXT,
    resolved_at   TEXT,
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (run_id, rule_id, target_type, target_id)
);
CREATE INDEX IF NOT EXISTS idx_cc_run    ON consistency_check(run_id);
CREATE INDEX IF NOT EXISTS idx_cc_target ON consistency_check(target_type, target_id);

-- 实体生命窗字段（T1/T2/T5 类检查的比较基准；NULL=未知，未知不判违规、触发补考）
ALTER TABLE entity ADD COLUMN time_start TEXT;   -- ISO 8601；人=生年/机构=成立/项目=发起/技术=出现
ALTER TABLE entity ADD COLUMN time_end   TEXT;   -- 人=卒年/机构=解散/项目=终止；NULL=存续中或未知

-- 实体别名冲突扫描：两个不同实体的 canonical_name/aliases 撞名 → N1 候选
CREATE VIEW IF NOT EXISTS v_entity_alias_conflict AS
SELECT a.entity_id AS entity_a, b.entity_id AS entity_b, a.canonical_name
FROM entity a JOIN entity b
  ON a.canonical_name = b.canonical_name
 AND a.entity_id < b.entity_id
 AND a.merged_into IS NULL AND b.merged_into IS NULL;

-- 时序敏感关系缺时间窗：requires_temporal_order=1 的关系而任一端无 time_start → T1 不可判定，须补考
CREATE VIEW IF NOT EXISTS v_temporal_gap AS
SELECT er.id AS relation_row, er.relation_type, er.from_entity, er.to_entity
FROM entity_relation er
JOIN entity_relation_type rt ON rt.relation_code = er.relation_type
JOIN entity fe ON fe.entity_id = er.from_entity
JOIN entity te ON te.entity_id = er.to_entity
WHERE rt.requires_temporal_order = 1
  AND (fe.time_start IS NULL OR te.time_start IS NULL);

-- 无证据关系（requires_evidence=1 而未挂 evidence_id）
CREATE VIEW IF NOT EXISTS v_relation_unsupported AS
SELECT er.id AS relation_row, er.relation_type, er.from_entity, er.to_entity
FROM entity_relation er
JOIN entity_relation_type rt ON rt.relation_code = er.relation_type
WHERE rt.requires_evidence = 1 AND er.evidence_id IS NULL;

-- 未决一致性冲突（书稿流水线门禁：block 级未处置即拦截）
CREATE VIEW IF NOT EXISTS v_unresolved_conflict AS
SELECT run_id, rule_id, target_type, target_id, severity, detail
FROM consistency_check
WHERE resolution IS NULL;

-- v0.2 预置规则（完整 SQL 实现与判定细则见 15 号文档第三、四部分）
INSERT OR IGNORE INTO consistency_rule (rule_id, rule_class, name, description, severity, sql_impl) VALUES
 ('T1','temporal','时序可行性','时序敏感关系中，结果端 time_start 不得早于来源端 time_start（fork/derive/copy/port/rewrite/acquire/merge/split/influenced/adopted 等）',
  'block','SELECT er.* FROM entity_relation er JOIN entity_relation_type rt ON rt.relation_code=er.relation_type JOIN entity fe ON fe.entity_id=er.from_entity JOIN entity te ON te.entity_id=er.to_entity WHERE rt.requires_temporal_order=1 AND fe.time_start IS NOT NULL AND te.time_start IS NOT NULL AND te.time_start < fe.time_start'),
 ('T2','temporal','参与时存在性','participated_in/employed_by/member_of/created：事件或雇佣发生时主体须已存在（event.time_start ≥ person/org.time_start，且 ≤ time_end 或 time_end 为空）',
  'block',NULL),
 ('T3','temporal','许可证先行','licensed_under 关系的时间不得早于该许可证实体的 time_start',
  'block',NULL),
 ('T4','temporal','术语时代性','evidence/claim 使用的术语不得早于 terminology_index/controlled_vocab 登记的该术语首次出现时间（09 术语史接口）',
  'warn',NULL),
 ('T5','temporal','引用时代性','叙事单元引用的史料 source_date 不得晚于该单元所述事件的 time_end（不能用事后材料充当当时记录，P41 第四层降权联动）',
  'warn',NULL),
 ('N1','narrative','身份唯一性','同一人物实体在不同叙事单元中的身份描述不得矛盾；撞名实体须经 v_entity_alias_conflict 审查后合并或区分',
  'block',NULL),
 ('N2','narrative','起源唯一性','同一技术/项目的起源主张（ORIGIN_CLAIM/FIRST_APPEARANCE）多于一条且互不支持时，须裁决或并存标注（多起源并存须显式声明）',
  'block',NULL),
 ('N3','narrative','日期唯一性','同一事件实体在不同层出现两个互斥的 event_date/source_date 时冲突（容差=精度等级；精度不同取粗粒度兼容判定）',
  'block',NULL),
 ('N4','narrative','许可证定义一致性','同一许可证在不同章节的条款叙述不得矛盾（BSD 广告条款存废等经典争议须走 controversy）',
  'block',NULL),
 ('N5','narrative','判断一致性','同一 claim 在不同章节的采信状态（status/措辞档位）不得矛盾；跨卷须一致（09 争议簿跨卷一致义务）',
  'block',NULL),
 ('N6','narrative','动机一致性','对同一主体的 MOTIVATION 主张互斥时须登记争议（controversy），不得在两个章节各采一说而不标注',
  'block',NULL);

-- 版本号升级用 UPDATE（v0.1 已以 INSERT 占用 schema_version 主键，OR IGNORE 会被静默忽略）
UPDATE schema_meta SET value = '0.2' WHERE key = 'schema_version';
INSERT OR IGNORE INTO schema_meta (key, value) VALUES
 ('v0_2_scope','Task #19：实体 18 类细分（entity_type_class）+ 24 关系类型（entity_relation_type）+ 一致性规则 T1-T5/N1-N6 + entity.time_start/time_end'),
 ('entity_subtype_convention','entity.entity_type 用 6 基类，细分写 entity.attrs JSON 的 subtype 键，取值限 entity_type_class.entity_subtype');

-- ============================================================
-- END OF DDL v0.2 —— 32 表 + 8 视图 + 4 触发器 + 预置数据
-- v0.1：五层隔离主库；v0.2：知识图谱分类学 + 一致性检查（Task #19）
-- 规则判定细则、伪 SQL、审计流程见 15-知识图谱与一致性检查.md
-- ============================================================
