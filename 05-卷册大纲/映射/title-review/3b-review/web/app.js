/* 3B 标题审定 · 前端逻辑（原生 JS，无构建、无外网依赖） */
(function () {
  'use strict';

  var LS_KEY = '3b_review_v1';
  var DEBOUNCE_MS = 1500;
  var RETRY_MS = 30000;
  var LABELS_DEFAULT = { ok: '通过', reroll: '重拟', custom: '自定义' };

  var ICONS = {
    ok: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg>',
    reroll: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.35-5.65"/><path d="M20 4v4h-4"/></svg>',
    custom: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4l10-10-4-4L4 16z"/><path d="M14 6l4 4"/></svg>'
  };

  var state = {
    manifest: null,
    config: null,
    scope: null,
    scopeKeys: null,
    vols: [],
    units: [],
    volIndex: null,
    unitsLoaded: false,
    unitsLoading: false,
    unitsError: null,
    answers: {},
    candidates: {},
    todayCount: { date: '', count: 0 },
    cursor: null,
    theme: 'dark',
    fontSize: 2,
    dailyGoal: 500,
    sessionStart: null,
    sessionCount: 0,
    lastTags: ['content'],
    quickTags: false,
    fold: { vols: {}, chapters: {}, sections: {} },
    suggest: {}
  };

  var ui = {
    view: 'group',
    filter: 'all',
    vol: null,
    all: false,
    singleIdx: 0,
    editing: null,
    tagging: null
  };

  var sync = {
    pendingPut: false,
    pendingDeletes: new Set(),
    dirty: new Set(),
    timer: null,
    retry: null,
    inflight: false
  };

  var undoStack = [];
  var toastTimer = null;

  /* ---------------- 小工具 ---------------- */

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function $$(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function pad2(n) {
    return n < 10 ? '0' + n : '' + n;
  }

  function todayStr() {
    var d = new Date();
    return d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate());
  }

  function nowISO() {
    return new Date().toISOString();
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function labels() {
    var l = (state.config && state.config.labels) || {};
    return {
      ok: l.ok || LABELS_DEFAULT.ok,
      reroll: l.reroll || LABELS_DEFAULT.reroll,
      custom: l.custom || LABELS_DEFAULT.custom
    };
  }

  function statusOf(key) {
    var a = state.answers[key];
    return a && a.verdict ? a.verdict : 'pending';
  }

  function cloneAnswer(a) {
    return {
      verdict: a.verdict,
      custom_title: a.custom_title,
      note: a.note,
      tags: (a.tags || []).slice(),
      merge_target: a.merge_target || '',
      updated_at: a.updated_at
    };
  }

  var TAG_DEFS = [
    { id: 'content', label: '内容' },
    { id: 'length', label: '字数' },
    { id: 'merge', label: '合并' },
    { id: 'split', label: '拆分' },
    { id: 'format', label: '格式' },
    { id: 'delete', label: '删除' },
    { id: 'term', label: '术语' }
  ];

  function tagLabel(id) {
    for (var i = 0; i < TAG_DEFS.length; i += 1) {
      if (TAG_DEFS[i].id === id) return TAG_DEFS[i].label;
    }
    return id;
  }

  function tagLabels(list) {
    if (!list || !list.length) return '无标签';
    return list.map(tagLabel).join('+');
  }

  function mergeLabel(id) {
    return { prev: '上一条', next: '下一条', parent: '本节题' }[id] || id;
  }

  function newerAnswer(a, b) {
    if (!a) return false;
    if (!b) return true;
    var ta = Date.parse(a.updated_at) || 0;
    var tb = Date.parse(b.updated_at) || 0;
    return ta > tb;
  }

  /* ---------------- 本地持久化 ---------------- */

  function readLocal() {
    try {
      var raw = window.localStorage.getItem(LS_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  }

  function loadLocal() {
    var o = readLocal();
    if (!o || typeof o !== 'object') return;
    if (o.answers && typeof o.answers === 'object') state.answers = o.answers;
    if (o.cursor && typeof o.cursor === 'object') state.cursor = o.cursor;
    if (o.theme === 'dark' || o.theme === 'light') state.theme = o.theme;
    if (o.fontSize === 1 || o.fontSize === 2 || o.fontSize === 3) state.fontSize = o.fontSize;
    if (typeof o.dailyGoal === 'number' && o.dailyGoal > 0) state.dailyGoal = o.dailyGoal;
    if (o.todayCount && typeof o.todayCount === 'object') {
      state.todayCount = { date: o.todayCount.date || '', count: Number(o.todayCount.count) || 0 };
    }
    if (Array.isArray(o.lastTags)) {
      state.lastTags = o.lastTags.filter(function (t) {
        return TAG_DEFS.some(function (d) { return d.id === t; });
      });
    }
    state.quickTags = !!o.quickTags;
    if (o.fold && typeof o.fold === 'object') {
      ['vols', 'chapters', 'sections'].forEach(function (k) {
        if (o.fold[k] && typeof o.fold[k] === 'object') state.fold[k] = o.fold[k];
      });
    }
  }

  function saveState() {
    try {
      window.localStorage.setItem(LS_KEY, JSON.stringify({
        answers: state.answers,
        cursor: state.cursor,
        theme: state.theme,
        fontSize: state.fontSize,
        dailyGoal: state.dailyGoal,
        todayCount: state.todayCount,
        lastTags: state.lastTags,
        quickTags: state.quickTags,
        fold: state.fold
      }));
    } catch (e) {
      /* 配额或隐私模式：静默失败，仍可在内存中作答 */
    }
  }

  /* ---------------- API ---------------- */

  function apiSend(method, path, body) {
    var opts = { method: method, cache: 'no-store', headers: {} };
    if (body !== undefined) {
      opts.headers['Content-Type'] = 'application/json';
      opts.body = JSON.stringify(body);
    }
    return fetch(path, opts).then(function (res) {
      if (!res.ok) {
        if (method === 'DELETE' && res.status === 404) return null;
        throw new Error(method + ' ' + path + ' → ' + res.status);
      }
      if (res.status === 204) return null;
      var ct = res.headers.get('content-type') || '';
      if (ct.indexOf('application/json') >= 0) return res.json();
      return res.text();
    });
  }

  function apiGet(path) {
    return apiSend('GET', path);
  }

  /* ---------------- 同步（防抖 PUT + 离线队列） ---------------- */

  function markDirty(keys) {
    keys.forEach(function (k) {
      sync.dirty.add(k);
    });
    updateDirtyBadge();
  }

  function updateDirtyBadge() {
    var el = $('#p-dirty');
    if (!el) return;
    if (sync.dirty.size > 0) {
      el.hidden = false;
      el.textContent = '未同步 ' + sync.dirty.size + ' 条';
    } else {
      el.hidden = true;
    }
  }

  function scheduleSync(delay) {
    clearTimeout(sync.timer);
    sync.timer = setTimeout(flush, delay == null ? DEBOUNCE_MS : delay);
  }

  function flush() {
    if (sync.inflight) return;
    if (!sync.pendingPut && sync.pendingDeletes.size === 0) return;
    sync.inflight = true;
    var batch = { put: sync.pendingPut, dels: Array.prototype.slice.call(sync.pendingDeletes) };
    sync.pendingPut = false;
    sync.pendingDeletes.clear();

    var chain = Promise.resolve();
    batch.dels.forEach(function (k) {
      chain = chain.then(function () {
        return apiSend('DELETE', '/api/answers?key=' + encodeURIComponent(k));
      });
    });
    if (batch.put) {
      chain = chain.then(function () {
        return apiSend('PUT', '/api/answers', { answers: state.answers });
      });
    }

    chain
      .then(function () {
        sync.dirty.clear();
        updateDirtyBadge();
        clearTimeout(sync.retry);
        sync.retry = null;
        if (sync.pendingPut || sync.pendingDeletes.size) scheduleSync(0);
      })
      .catch(function () {
        if (batch.put) sync.pendingPut = true;
        batch.dels.forEach(function (k) {
          sync.pendingDeletes.add(k);
        });
        clearTimeout(sync.retry);
        sync.retry = setTimeout(flush, RETRY_MS);
      })
      .then(function () {
        sync.inflight = false;
      });
  }

  /* ---------------- 作答 ---------------- */

  function bumpToday() {
    var d = todayStr();
    if (state.todayCount.date !== d) {
      state.todayCount = { date: d, count: 0 };
    }
    state.todayCount.count += 1;
  }

  function setCursor(u) {
    state.cursor = {
      key: u.key,
      vol: u.vol,
      chapter_no: u.chapter_no,
      section_no: u.section_no == null ? null : u.section_no
    };
  }

  function snapshot(keys) {
    var o = {};
    keys.forEach(function (k) {
      o[k] = state.answers[k] ? cloneAnswer(state.answers[k]) : null;
    });
    return o;
  }

  function pushUndo(label, snap) {
    undoStack.push({ label: label, snap: snap });
    if (undoStack.length > 30) undoStack.shift();
  }

  function applyAnswer(key, verdict, customTitle, note, extra) {
    var prev = state.answers[key];
    var next = {
      verdict: verdict,
      custom_title: verdict === 'custom'
        ? String(customTitle == null ? (prev && prev.custom_title) || '' : customTitle)
        : null,
      note: note != null ? String(note) : (prev && prev.note) || '',
      tags: [],
      merge_target: '',
      updated_at: nowISO()
    };
    if (verdict === 'reroll') {
      next.tags = (extra && extra.tags) ? extra.tags.slice()
        : (prev && prev.verdict === 'reroll' ? (prev.tags || []).slice() : []);
      next.merge_target = (extra && extra.merge_target != null) ? extra.merge_target
        : (prev && prev.merge_target) || '';
      if (next.tags.indexOf('merge') < 0) next.merge_target = '';
      state.lastTags = next.tags.slice();
    }
    state.answers[key] = next;
    bumpToday();
    state.sessionCount += 1;
    if (!state.sessionStart) state.sessionStart = Date.now();
    markDirty([key]);
    sync.pendingPut = true;
    scheduleSync();
    saveState();
  }

  function removeAnswer(key) {
    if (!state.answers[key]) return false;
    delete state.answers[key];
    sync.pendingDeletes.add(key);
    markDirty([key]);
    scheduleSync();
    saveState();
    return true;
  }

  function undoLast() {
    var item = undoStack.pop();
    if (!item) {
      showToast('没有可撤销的操作');
      return;
    }
    var now = nowISO();
    Object.keys(item.snap).forEach(function (k) {
      var v = item.snap[k];
      if (v) {
        v = cloneAnswer(v);
        v.updated_at = now;
        state.answers[k] = v;
        sync.pendingPut = true;
      } else {
        delete state.answers[k];
        sync.pendingDeletes.add(k);
      }
      markDirty([k]);
    });
    scheduleSync(0);
    saveState();
    renderActive();
    showToast('已撤销：' + item.label);
  }

  /* ---------------- 数据载入 ---------------- */

  function hasLocalTheme() {
    var o = readLocal();
    return !!o && (o.theme === 'dark' || o.theme === 'light');
  }

  function hasLocalFont() {
    var o = readLocal();
    return !!o && (o.fontSize === 1 || o.fontSize === 2 || o.fontSize === 3);
  }

  function loadAll() {
    $('#view-group').innerHTML = '<p class="loading">正在连接服务端…</p>';
    return apiGet('/api/manifest')
      .then(function (m) {
        state.manifest = m;
        state.vols = m.vols || [];
        state.totals = m.totals || {};
        state.scope = m.scope || null;
        state.config = m.config || {};
        if ((state.config.theme === 'light' || state.config.theme === 'dark') && !hasLocalTheme()) {
          state.theme = state.config.theme;
        }
        if ([1, 2, 3].indexOf(state.config.font_size) >= 0 && !hasLocalFont()) {
          state.fontSize = state.config.font_size;
        }
        if (typeof state.config.daily_goal === 'number' && state.config.daily_goal > 0) {
          state.dailyGoal = state.config.daily_goal;
        }
      })
      .then(function () {
        return apiGet('/api/config').catch(function () {
          return null;
        });
      })
      .then(function (cfg) {
        if (cfg && cfg.config) state.config = cfg.config;
        if (cfg && cfg.scope) {
          state.scopeKeys = cfg.scope.unit_keys ? new Set(cfg.scope.unit_keys) : null;
        }
        return apiGet('/api/answers').catch(function () {
          return null;
        });
      })
      .then(function (ans) {
        mergeServerAnswers(ans);
        return apiGet('/api/candidates').catch(function () {
          return null;
        });
      })
      .then(function (cands) {
        if (cands && cands.candidates) state.candidates = cands.candidates;
        applyChrome();
        renderProgress();
        renderActive();
        loadUnits();
        resumeSuggest();
      })
      .catch(function (err) {
        $('#view-group').innerHTML =
          '<p class="loading">服务端不可用：' + esc(err.message || err) +
          '<br>请确认审阅服务已在同源地址启动。</p>';
      });
  }

  function mergeServerAnswers(payload) {
    var srv = (payload && payload.answers) || {};
    var localWins = [];
    Object.keys(srv).forEach(function (k) {
      var s = srv[k];
      if (!s || !s.verdict) return;
      var l = state.answers[k];
      if (!l) {
        state.answers[k] = cloneAnswer(s);
      } else if (newerAnswer(l, s)) {
        localWins.push(k);
      } else {
        state.answers[k] = cloneAnswer(s);
      }
    });
    Object.keys(state.answers).forEach(function (k) {
      if (!srv[k]) localWins.push(k);
    });
    if (localWins.length) {
      markDirty(localWins);
      sync.pendingPut = true;
      scheduleSync(0);
    }
  }

  function loadUnits() {
    if (state.unitsLoading || state.unitsLoaded) return;
    state.unitsLoading = true;
    var all = [];
    var errors = [];
    var idx = 0;
    var vols = state.vols.slice();
    if (!ui.vol) ui.vol = pickVol();
    // 当前卷优先：断网时首卷即可渲染，其余失败三次即止
    vols.sort(function (a, b) {
      return (b.vol === ui.vol ? 1 : 0) - (a.vol === ui.vol ? 1 : 0) || a.vol - b.vol;
    });

    if (!vols.length) {
      state.unitsLoaded = true;
      state.unitsLoading = false;
      return;
    }

    function step() {
      if (idx >= vols.length) {
        all.sort(function (a, b) {
          return (
            (a.vol || 0) - (b.vol || 0) ||
            (a.chapter_no || 0) - (b.chapter_no || 0) ||
            (a.section_no || 0) - (b.section_no || 0) ||
            (a.order || 0) - (b.order || 0)
          );
        });
        state.units = all;
        state.volIndex = new Map();
        all.forEach(function (u) {
          state.volIndex.set(u.key, u.vol);
        });
        state.unitsLoaded = true;
        state.unitsLoading = false;
        state.unitsError = errors.length ? errors.length + ' 卷载入失败' : null;
        if (!ui.vol) ui.vol = pickVol();
        renderActive();
        return;
      }
      var v = vols[idx];
      if (!state.unitsLoaded && ui.view === 'group') {
        var ld = $('#view-group .loading');
        if (ld) ld.textContent = '正在载入条目 ' + (idx + 1) + ' / ' + vols.length + ' 卷…';
      }
      apiGet('/api/units?vol=' + v.vol)
        .then(function (d) {
          if (d && d.units) all = all.concat(d.units);
        })
        .catch(function () {
          errors.push(v.vol);
          if (errors.length >= 3) idx = vols.length - 1;  // 断网时停止逐卷空等
        })
        .then(function () {
          idx += 1;
          step();
        });
    }

    step();
  }

  /* 单卷按需载入：断网期间首轮只载入当前卷，切到未载入的卷时补拉一次 */
  var volQueue = {};

  function ensureVolUnits(vol, then) {
    if (!vol) {
      if (then) then();
      return;
    }
    if (state.units.some(function (u) { return u.vol === vol; })) {
      if (then) then();
      return;
    }
    if (volQueue[vol]) {
      if (then) volQueue[vol].push(then);
      return;
    }
    volQueue[vol] = then ? [then] : [];
    apiGet('/api/units?vol=' + vol)
      .then(function (d) {
        if (d && d.units && d.units.length) {
          state.units = state.units.concat(d.units);
          state.units.sort(function (a, b) {
            return (
              (a.vol || 0) - (b.vol || 0) ||
              (a.chapter_no || 0) - (b.chapter_no || 0) ||
              (a.section_no || 0) - (b.section_no || 0) ||
              (a.order || 0) - (b.order || 0)
            );
          });
          state.unitsError = null;
        }
      })
      .catch(function () {})
      .then(function () {
        var cbs = volQueue[vol] || [];
        delete volQueue[vol];
        cbs.forEach(function (fn) {
          if (fn) fn();
        });
        renderActive();
      });
  }

  /* “全部卷”按需补载：逐卷拉取，连续失败 3 次即停（离线时不全量空等） */
  var allVolsRunning = false;

  function ensureAllVols(then) {
    if (allVolsRunning) {
      if (then) then();
      return;
    }
    var missing = state.vols.filter(function (v) {
      return !state.units.some(function (u) {
        return u.vol === v.vol;
      });
    });
    if (!missing.length) {
      if (then) then();
      return;
    }
    allVolsRunning = true;
    var i = 0;
    var fails = 0;

    function next() {
      if (i >= missing.length || fails >= 3) {
        allVolsRunning = false;
        if (then) then();
        return;
      }
      var v = missing[i];
      i += 1;
      apiGet('/api/units?vol=' + v.vol)
        .then(function (d) {
          if (d && d.units && d.units.length) {
            state.units = state.units.concat(d.units);
            fails = 0;
          }
        })
        .catch(function () {
          fails += 1;
        })
        .then(function () {
          if (i >= missing.length || fails >= 3) {
            state.units.sort(function (a, b) {
              return (
                (a.vol || 0) - (b.vol || 0) ||
                (a.chapter_no || 0) - (b.chapter_no || 0) ||
                (a.section_no || 0) - (b.section_no || 0) ||
                (a.order || 0) - (b.order || 0)
              );
            });
          }
          if (i % 10 === 0) renderActive();
          next();
        });
    }

    next();
  }

  /* ---------------- 计数 ---------------- */

  function scopeTotal() {
    if (state.scope && typeof state.scope.effective === 'number' && state.scope.effective > 0) {
      return state.scope.effective;
    }
    return (state.totals && state.totals.units) || state.units.length;
  }

  function originalTotal() {
    return (state.totals && state.totals.units) || 0;
  }

  function inScope(key) {
    return !state.scopeKeys || state.scopeKeys.has(key);
  }

  function answeredCount() {
    var n = 0;
    Object.keys(state.answers).forEach(function (k) {
      if (inScope(k)) n += 1;
    });
    return n;
  }

  function renderProgress() {
    var total = scopeTotal();
    var done = answeredCount();
    var pct = total > 0 ? Math.min(100, Math.round((done / total) * 1000) / 10) : 0;
    $('#p-answered').textContent = String(done);
    $('#p-total').textContent = String(total);
    $('#p-pct').textContent = pct + '%';
    $('#progress-fill').style.width = pct + '%';
    updateDirtyBadge();
  }

  /* ---------------- 过滤与定位 ---------------- */

  function passFilter(u) {
    if (state.config && state.config.only_flagged && !(u.flag_machine || u.flag_human)) return false;
    var st = statusOf(u.key);
    if (ui.filter === 'pending') return st === 'pending';
    if (ui.filter === 'changed') return st === 'custom' || st === 'reroll';
    if (ui.filter === 'ok') return st === 'ok';
    return true;
  }

  function pickVol() {
    if (state.cursor && state.cursor.vol) return state.cursor.vol;
    var last = null;
    for (var i = 0; i < state.units.length; i += 1) {
      var u = state.units[i];
      if (u.level !== 'subsection') continue;
      last = u.vol;
      if (statusOf(u.key) === 'pending') return u.vol;
    }
    return last || (state.vols[0] && state.vols[0].vol) || 1;
  }

  function volTitle(vol) {
    for (var i = 0; i < state.vols.length; i += 1) {
      if (state.vols[i].vol === vol) return state.vols[i].title || '';
    }
    return '';
  }

  /* ---------------- 卡片渲染 ---------------- */

  function unitNo(u) {
    if (u.level === 'section') {
      return u.chapter_no + '.' + u.section_no;
    }
    if (u.level === 'subsection') {
      var parts = String(u.subsection_id || u.key || '').split('.');
      if (parts.length < 4) return '';
      return parts.slice(-3).map(function (x) {
        var n = Number(x);
        return isNaN(n) ? x : String(n);
      }).join('.');
    }
    return '';
  }

  function cardHTML(u) {
    var a = state.answers[u.key];
    var st = a && a.verdict ? a.verdict : 'pending';
    var L = labels();
    var customChanged = st === 'custom' && a.custom_title && a.custom_title !== u.title;
    var titleText = customChanged ? a.custom_title : u.title || '';
    var no = (u.level === 'section' && ui.view === 'group') ? '' : unitNo(u);
    var parts = [];

    parts.push('<article class="card" data-key="' + esc(u.key) + '" data-status="' + esc(st) +
      '" data-level="' + esc(u.level || 'subsection') + '">');
    parts.push('<h3 class="card-title">' + (no ? '<span class="card-no">' + esc(no) + '</span>' : '') +
      esc(titleText) + '</h3>');
    if (customChanged) {
      parts.push('<p class="card-old">原题：' + esc(u.title) + '</p>');
    }
    if (u.thesis) {
      parts.push('<p class="card-thesis">' + esc(u.thesis) + '</p>');
    }
    parts.push('<div class="card-meta">');
    if (u.source_count != null) {
      parts.push('<span class="badge">来源 ' + esc(u.source_count) + '</span>');
    }
    if (u.flag_machine) parts.push('<span class="badge warn">机判曾 FAIL</span>');
    if (u.flag_human) parts.push('<span class="badge warn">人判曾 FAIL</span>');
    if (st === 'ok') parts.push('<span class="badge status-ok" aria-label="已通过">✓</span>');
    if (st === 'reroll') parts.push('<span class="badge status-reroll">' + esc(L.reroll) + '</span>');
    if (st === 'custom') parts.push('<span class="badge status-custom">' + esc(L.custom) + '</span>');
    if (st !== 'pending') {
      parts.push('<button type="button" class="badge clear-btn" data-act="clear" data-key="' +
        esc(u.key) + '">清除作答</button>');
    }
    parts.push('</div>');

    parts.push('<div class="pills">');
    ['ok', 'reroll', 'custom'].forEach(function (v) {
      parts.push('<button type="button" class="pill" data-act="verdict" data-v="' + v +
        '" data-key="' + esc(u.key) + '" aria-pressed="' + (st === v ? 'true' : 'false') + '"' +
        (v === 'ok' ? ' aria-label="通过（维持原题）" title="通过"' : '') + '>' +
        ICONS[v] + (v === 'ok' ? '' : '<span>' + esc(L[v]) + '</span>') + '</button>');
    });
    parts.push('</div>');

    if (st === 'reroll') {
      var tags0 = (a && a.tags) || [];
      if (tags0.length || (a && a.merge_target)) {
        parts.push('<div class="tag-badges">' + tags0.map(function (t) {
          return '<span class="badge tag">' + esc(tagLabel(t)) + '</span>';
        }).join('') + (a && a.merge_target
          ? '<span class="badge tag">合并→' + esc(mergeLabel(a.merge_target)) + '</span>' : '') + '</div>');
      }
    }
    if (ui.tagging === u.key && st === 'reroll') {
      var selTags = (a && a.tags) || [];
      parts.push('<div class="tagbar" data-key="' + esc(u.key) + '">');
      parts.push('<div class="tag-chips">');
      TAG_DEFS.forEach(function (t) {
        var on = selTags.indexOf(t.id) >= 0;
        parts.push('<button type="button" class="chip' + (on ? ' on' : '') + '" data-act="tag" data-tag="' +
          t.id + '" data-key="' + esc(u.key) + '" aria-pressed="' + on + '">' + t.label + '</button>');
      });
      parts.push('</div>');
      if (selTags.indexOf('merge') >= 0) {
        parts.push('<div class="tag-merge"><span>合并到</span>');
        [['prev', '上一条'], ['next', '下一条'], ['parent', '本节题']].forEach(function (m) {
          var on = a && a.merge_target === m[0];
          parts.push('<button type="button" class="chip' + (on ? ' on' : '') +
            '" data-act="merge-target" data-merge="' + m[0] + '" data-key="' + esc(u.key) +
            '" aria-pressed="' + on + '">' + m[1] + '</button>');
        });
        parts.push('</div>');
      }
      parts.push('<div class="tag-actions"><label><input type="checkbox" data-act="tag-quick"' +
        (state.quickTags ? ' checked' : '') + '> 连续沿用</label>');
      parts.push('<button type="button" data-act="suggest" data-key="' + esc(u.key) +
        '">获取建议</button>');
      parts.push('<button type="button" class="primary" data-act="tag-save" data-key="' + esc(u.key) +
        '">完成</button></div>');
      parts.push('</div>');
    }
    if (st === 'reroll' && state.suggest[u.key]) {
      parts.push('<div class="suggest-wait" data-key="' + esc(u.key) + '">' +
        '<span class="suggest-dot" aria-hidden="true"></span>' +
        '<span>已提交给 LLM 会话，等待返回建议… 已等 <span class="suggest-elapsed">0 秒</span></span>' +
        '<button type="button" data-act="suggest-cancel" data-key="' + esc(u.key) + '">取消</button></div>');
    }

    var prefill = st === 'custom' && a.custom_title ? a.custom_title : (u.title || '');
    parts.push('<div class="inline-box" data-box="custom" ' + (ui.editing === u.key ? '' : 'hidden') + '>');
    parts.push('<label>自定义题名（1–120 字）</label>');
    parts.push('<textarea class="ct-input" maxlength="120" rows="2">' + esc(prefill) + '</textarea>');
    parts.push('<div class="inline-meta"><span class="ct-count"></span><span class="ct-err err"></span></div>');
    parts.push('<button type="button" class="note-toggle" data-act="note-toggle">备注（可选，≤500 字）</button>');
    parts.push('<div data-box="note" hidden><textarea class="note-input" maxlength="500" rows="2">' +
      esc((a && a.note) || '') + '</textarea></div>');
    parts.push('<div class="inline-actions">');
    parts.push('<button type="button" data-act="custom-cancel" data-key="' + esc(u.key) + '">取消</button>');
    parts.push('<button type="button" class="primary" data-act="custom-save" data-key="' + esc(u.key) +
      '">保存</button>');
    parts.push('</div></div>');

    var cands = state.candidates[u.key];
    if (st === 'reroll' && cands && cands.length) {
      parts.push('<div class="cand-box">');
      parts.push('<p class="cand-old">旧题：' + esc(u.title) + '</p>');
      cands.forEach(function (c, i) {
        var cid = c.candidate_id != null ? c.candidate_id : i;
        parts.push('<div class="cand-item">');
        parts.push('<p class="cand-title">' + esc(c.new_title) + '</p>');
        if (c.rationale) parts.push('<p class="cand-why">' + esc(c.rationale) + '</p>');
        if (c.source) parts.push('<p class="cand-src">' + esc(c.source) + '</p>');
        parts.push('<div class="cand-actions">');
        parts.push('<button type="button" data-act="cand-adopt" data-key="' + esc(u.key) +
          '" data-cid="' + esc(cid) + '">采纳</button>');
        parts.push('<button type="button" data-act="cand-edit" data-key="' + esc(u.key) +
          '" data-cid="' + esc(cid) + '">改写后采纳</button>');
        parts.push('</div></div>');
      });
      parts.push('<div class="cand-actions">');
      parts.push('<button type="button" data-act="cand-keep" data-key="' + esc(u.key) + '">保留旧题</button>');
      parts.push('<button type="button" data-act="cand-reroll" data-key="' + esc(u.key) + '">再次重拟</button>');
      parts.push('</div>');
      parts.push('</div>');
    }

    parts.push('</article>');
    return parts.join('');
  }

  /* ---------------- 分组视图 ---------------- */

  function pctOf(done, total) {
    return total > 0 ? Math.round(done * 100 / total) : 0;
  }

  function statText(done, total) {
    return done + '/' + total + ' · ' + pctOf(done, total) + '%';
  }

  function foldCaret(open) {
    return '<svg class="fold-caret" viewBox="0 0 24 24" aria-hidden="true"><path d="' +
      (open ? 'M6 9l6 6 6-6' : 'M9 6l6 6-6 6') + '"/></svg>';
  }

  function foldState(kind, key, dflt) {
    var v = state.fold[kind][key];
    if (v === 1) return true;
    if (v === 0) return false;
    return !!dflt;
  }

  function setFold(kind, key, val) {
    state.fold[kind][key] = val ? 1 : 0;
    saveState();
  }

  function renderGroup() {
    var root = $('#view-group');
    if (!state.manifest) {
      if (!root.innerHTML) root.innerHTML = '<p class="loading">正在载入…</p>';
      return;
    }
    if (!state.unitsLoaded) {
      root.innerHTML = '<p class="loading">' +
        (state.unitsError ? '载入失败：' + esc(state.unitsError) : '正在载入条目…') + '</p>';
      return;
    }
    var volList;
    if (ui.all) {
      volList = state.vols.map(function (v) {
        return v.vol;
      });
    } else {
      if (!ui.vol) ui.vol = pickVol();
      volList = [ui.vol];
    }

    var html = [];
    html.push('<div class="vol-head">');
    html.push('<select class="vol-select" id="vol-select" aria-label="选择卷">');
    html.push('<option value="all"' + (ui.all ? ' selected' : '') + '>全部卷</option>');
    state.vols.forEach(function (v) {
      html.push('<option value="' + v.vol + '"' + (!ui.all && v.vol === ui.vol ? ' selected' : '') +
        '>第 ' + v.vol + ' 卷</option>');
    });
    html.push('</select>');
    if (ui.all) {
      var doneAll = state.units.filter(function (u) {
        return statusOf(u.key) !== 'pending';
      }).length;
      html.push('<span class="vol-name">全部 ' + volList.length + ' 卷</span>');
      html.push('<span class="spacer"></span><span class="vol-stat">' +
        statText(doneAll, state.units.length) + '</span>');
    } else {
      var volUnits = state.units.filter(function (u) {
        return u.vol === ui.vol;
      });
      var volDone = volUnits.filter(function (u) {
        return statusOf(u.key) !== 'pending';
      }).length;
      html.push('<span class="vol-name">' + esc(volTitle(ui.vol)) + '</span>');
      html.push('<span class="spacer"></span><span class="vol-stat">' +
        statText(volDone, volUnits.length) + '</span>');
    }
    html.push('</div>');

    var shown = 0;
    volList.forEach(function (vno) {
      var res = volBlockHTML(vno);
      shown += res.shown;
      if (res.html) html.push(res.html);
    });

    if (shown === 0 && ui.filter !== 'all') {
      html.push('<p class="loading">没有符合当前筛选的条目。</p>');
    }
    root.innerHTML = html.join('');
    refreshCounters(root);
  }

  function volBlockHTML(vol) {
    var all = state.units.filter(function (u) {
      return u.vol === vol;
    });
    if (!all.length) return { html: '', shown: 0 };
    var volDone = all.filter(function (u) {
      return statusOf(u.key) !== 'pending';
    }).length;
    var withHead = ui.all;
    var open = !withHead || !foldState('vols', 'v' + vol, true);
    var parts = [];
    if (withHead) {
      parts.push('<section class="vol-block" data-vol="' + vol + '">');
      parts.push('<button type="button" class="vol-block-head" data-act="fold-vol" data-vol="' + vol +
        '" aria-expanded="' + (open ? 'true' : 'false') + '">' + foldCaret(open) +
        '<span class="vol-block-title">第 ' + vol + ' 卷 · ' + esc(volTitle(vol)) + '</span>' +
        '<span class="vol-stat">' + statText(volDone, all.length) + '</span></button>');
    }
    var shown = 0;
    if (!open) {
      shown = all.filter(passFilter).length;
      if (withHead) parts.push('</section>');
      return { html: parts.join(''), shown: shown };
    }

    var subs = [];
    all.forEach(function (u) {
      if (u.level === 'subsection') subs.push(u);
    });
    var chapOrder = [];
    var chapMap = {};
    subs.forEach(function (u) {
      var cn = u.chapter_no;
      if (!chapMap[cn]) {
        chapMap[cn] = { no: cn, sections: {}, order: [] };
        chapOrder.push(cn);
      }
      var sn = u.section_no == null ? 0 : u.section_no;
      if (!chapMap[cn].sections[sn]) {
        chapMap[cn].sections[sn] = [];
        chapMap[cn].order.push(sn);
      }
      chapMap[cn].sections[sn].push(u);
    });
    chapOrder.sort(function (a, b) {
      return a - b;
    });

    var unitIndex = {};
    all.forEach(function (u) {
      if (u.level !== 'subsection') {
        unitIndex[u.level + ':' + u.chapter_no + ':' + (u.section_no || 0)] = u;
      }
    });

    var body = [];
    chapOrder.forEach(function (cn) {
      var chap = chapMap[cn];
      var chapterUnit = unitIndex['chapter:' + cn + ':0'];
      var chapUnits = chapterUnit ? [chapterUnit] : [];
      chap.order.forEach(function (sn) {
        chapUnits = chapUnits.concat(chap.sections[sn]);
      });
      var chapDone = chapUnits.filter(function (u) {
        return statusOf(u.key) !== 'pending';
      }).length;
      var chapFiltered = chapUnits.filter(passFilter);

      if (ui.filter !== 'all' && chapFiltered.length === 0) return;
      shown += chapFiltered.length;

      var chapOpen = !foldState('chapters', 'v' + vol + 'c' + cn, false);
      body.push('<div class="chapter-block">');
      body.push('<button type="button" class="chapter-head" data-act="fold-chapter" data-vol="' + vol +
        '" data-chapter="' + cn + '" aria-expanded="' + (chapOpen ? 'true' : 'false') + '">' +
        foldCaret(chapOpen) +
        '<span class="status-dot' + (chapDone === chapUnits.length ? ' is-ok' : '') + '"></span>' +
        '<span class="ch-title">第 ' + cn + ' 章</span>' +
        '<span class="ch-stat">' + statText(chapDone, chapUnits.length) + '</span></button>');
      if (chapOpen) {
        if (chapterUnit && (ui.filter === 'all' || passFilter(chapterUnit))) {
          body.push(cardHTML(chapterUnit));
        }
        chap.order.forEach(function (sn) {
          var units = chap.sections[sn];
          var sectionUnit = sn === 0 ? null : unitIndex['section:' + cn + ':' + sn];
          var list = units.filter(passFilter);
          if (ui.filter !== 'all' && list.length === 0 && !(sectionUnit && passFilter(sectionUnit))) return;
          var seqAll = (sectionUnit ? [sectionUnit] : []).concat(units);
          var done = seqAll.filter(function (u) {
            return statusOf(u.key) !== 'pending';
          }).length;
          var pending = seqAll.length - done;
          var secOpen = !foldState('sections', 'v' + vol + 'c' + cn + 's' + sn, false);
          body.push('<div class="section-block">');
          body.push('<div class="section-head">');
          body.push('<button type="button" class="section-fold" data-act="fold-section" data-vol="' +
            vol + '" data-chapter="' + cn + '" data-section="' + sn + '" aria-expanded="' +
            (secOpen ? 'true' : 'false') + '">' + foldCaret(secOpen) +
            '<span class="status-dot' + (done === seqAll.length ? ' is-ok' : done > 0 ? ' is-partial' : '') + '"></span>' +
            '<span class="sec-title">' + (sn === 0 ? '（无节）' : cn + '.' + sn + ' 节') + '</span>' +
            '<span class="sec-stat">' + statText(done, seqAll.length) + '</span></button>');
          body.push('<button type="button" class="sec-pass" data-act="section" data-vol="' + vol +
            '" data-chapter="' + cn + '" data-section="' + sn + '"' + (pending ? '' : ' disabled') +
            '>整节通过</button>');
          body.push('</div>');
          if (secOpen) {
            if (sectionUnit && (ui.filter === 'all' || passFilter(sectionUnit))) {
              body.push(cardHTML(sectionUnit));
            }
            list.forEach(function (u) {
              body.push(cardHTML(u));
            });
          }
          body.push('</div>');
        });
      }
      body.push('</div>');
    });

    if (withHead) {
      parts.push('<div class="vol-block-body">' + body.join('') + '</div>');
      parts.push('</section>');
      return { html: parts.join(''), shown: shown };
    }
    return { html: body.join(''), shown: shown };
  }

  function refreshCounters(root) {
    $$('.inline-box', root).forEach(function (box) {
      var ta = $('.ct-input', box);
      var cnt = $('.ct-count', box);
      if (ta && cnt) cnt.textContent = ta.value.length + ' / 120';
    });
  }

  /* ---------------- 单卡视图 ---------------- */

  function singleList() {
    return state.units.filter(function (u) {
      return passFilter(u);
    });
  }

  function renderSingle() {
    var root = $('#view-single');
    if (!state.unitsLoaded) {
      root.innerHTML = '<p class="loading">正在载入条目…</p>';
      return;
    }
    var list = singleList();
    if (!list.length) {
      root.innerHTML = '<p class="loading">没有符合条件的条目。</p>';
      return;
    }
    if (ui.singleIdx >= list.length) ui.singleIdx = list.length - 1;
    if (ui.singleIdx < 0) ui.singleIdx = 0;
    var u = list[ui.singleIdx];
    var crumbs = '第 ' + u.vol + ' 卷';
    if (u.chapter_no != null) crumbs += ' · 第 ' + u.chapter_no + ' 章';
    if (u.section_no != null) crumbs += ' · 第 ' + u.section_no + ' 节';
    var html = [];
    html.push('<div class="single-wrap">');
    html.push('<p class="crumbs">' + esc(crumbs) + '</p>');
    html.push('<div class="single-card">' + cardHTML(u) + '</div>');
    html.push('<div class="single-nav">');
    html.push('<button type="button" data-act="single-prev"' + (ui.singleIdx === 0 ? ' disabled' : '') +
      '>上一条</button>');
    html.push('<button type="button" data-act="single-next"' +
      (ui.singleIdx >= list.length - 1 ? ' disabled' : '') + '>下一条</button>');
    html.push('</div>');
    html.push('<p class="counter">' + (ui.singleIdx + 1) + ' / ' + list.length + '</p>');
    html.push('</div>');
    root.innerHTML = html.join('');
    refreshCounters(root);
  }

  function renderActive() {
    if (ui.view === 'group') {
      $('#view-single').hidden = true;
      $('#view-group').hidden = false;
      renderGroup();
    } else {
      $('#view-group').hidden = true;
      $('#view-single').hidden = false;
      renderSingle();
    }
    renderProgress();
  }

  /* ---------------- 作答动作 ---------------- */

  function unitByKey(key) {
    for (var i = 0; i < state.units.length; i += 1) {
      if (state.units[i].key === key) return state.units[i];
    }
    return null;
  }

  function activeRoot() {
    return ui.view === 'group' ? $('#view-group') : $('#view-single');
  }

  function toggleTag(key, tag) {
    var a = state.answers[key];
    if (!a || a.verdict !== 'reroll') return;
    var tags = (a.tags || []).slice();
    var idx = tags.indexOf(tag);
    if (idx >= 0) tags.splice(idx, 1); else tags.push(tag);
    applyAnswer(key, 'reroll', null, a.note, { tags: tags, merge_target: a.merge_target || '' });
    saveState();
    renderActive();
  }

  function setMergeTarget(key, target) {
    var a = state.answers[key];
    if (!a || a.verdict !== 'reroll') return;
    applyAnswer(key, 'reroll', null, a.note,
      { tags: (a.tags || []).slice(), merge_target: target });
    saveState();
    renderActive();
  }

  function onVerdict(key, v) {
    var u = unitByKey(key);
    if (!u) return;
    setCursor(u);

    if (v === 'custom') {
      var cur = statusOf(key);
      var a = state.answers[key];
      ui.editing = key;
      renderActive();
      var box = $('.card[data-key="' + key + '"] .inline-box[data-box="custom"]', activeRoot());
      if (box) {
        box.hidden = false;
        var ta = $('.ct-input', box);
        if (ta) {
          if (cur !== 'custom' || !a || !a.custom_title) ta.value = u.title || '';
          ta.focus();
          ta.setSelectionRange(ta.value.length, ta.value.length);
        }
      }
      return;
    }

    if (v === 'reroll') {
      var a0 = state.answers[key];
      var keepTags = (a0 && a0.verdict === 'reroll' && (a0.tags || []).length)
        ? a0.tags.slice() : state.lastTags.slice();
      if (state.quickTags && ui.tagging !== key) {
        var snapQ = snapshot([key]);
        applyAnswer(key, 'reroll', null, null,
          { tags: keepTags, merge_target: (a0 && a0.merge_target) || '' });
        pushUndo('将“' + (u.title || key) + '”改为重拟（沿用标签）', snapQ);
        renderActive();
        showToast('已重拟（' + tagLabels(keepTags) + '）', undoLast, true);
        return;
      }
      var snapR = snapshot([key]);
      ui.editing = null;
      ui.tagging = key;
      applyAnswer(key, 'reroll', null, null,
        { tags: keepTags, merge_target: (a0 && a0.merge_target) || '' });
      pushUndo('将“' + (u.title || key) + '”改为重拟', snapR);
      renderActive();
      return;
    }

    var snap = snapshot([key]);
    var wasPending = statusOf(key) === 'pending';
    applyAnswer(key, v, null, null);
    pushUndo('将“' + (u.title || key) + '”改为' + labels()[v] + (wasPending ? '（原为待审）' : ''), snap);
    ui.editing = null;
    renderActive();
    showToast('已标记为' + labels()[v], undoLast, true);
  }

  function onClear(key) {
    var u = unitByKey(key);
    var snap = snapshot([key]);
    if (!removeAnswer(key)) return;
    pushUndo('清除“' + ((u && u.title) || key) + '”的作答', snap);
    renderActive();
    showToast('已清除作答，回到待审', undoLast, true);
  }

  function onSectionPass(vol, chapter, section) {
    var sectionUnit = state.units.filter(function (u) {
      return u.level === 'section' && u.vol === vol && u.chapter_no === chapter &&
        (u.section_no == null ? 0 : u.section_no) === section;
    })[0];
    var units = state.units.filter(function (u) {
      return u.level === 'subsection' && u.vol === vol && u.chapter_no === chapter &&
        (u.section_no == null ? 0 : u.section_no) === section && statusOf(u.key) === 'pending';
    });
    if (sectionUnit && statusOf(sectionUnit.key) === 'pending') units.unshift(sectionUnit);
    if (!units.length) {
      showToast('本节没有待审条目');
      return;
    }
    var keys = units.map(function (u) {
      return u.key;
    });
    openSheet('整节通过', function (body) {
      body.innerHTML = '<p class="hint">第 ' + chapter + ' 章第 ' + section + ' 节共有待审 ' +
        keys.length + ' 条，将全部标记为“' + esc(labels().ok) + '”。章节级不提供一键通过。</p>' +
        '<div class="sheet-actions"><button type="button" id="sec-cancel">取消</button>' +
        '<button type="button" class="primary" id="sec-ok">确认通过 ' + keys.length + ' 条</button></div>';
      $('#sec-cancel').addEventListener('click', closeSheet);
      $('#sec-ok').addEventListener('click', function () {
        var snap = snapshot(keys);
        keys.forEach(function (k) {
          applyAnswer(k, 'ok', null, null);
        });
        pushUndo('整节通过 ' + keys.length + ' 条（第 ' + chapter + ' 章第 ' + section + ' 节）', snap);
        closeSheet();
        renderActive();
        showToast('整节通过 ' + keys.length + ' 条', undoLast, true);
      });
    });
  }

  function saveCustom(key, titleText, noteText) {
    var u = unitByKey(key);
    var t = String(titleText || '').trim();
    if (t.length < 1 || t.length > 120) return false;
    var snap = snapshot([key]);
    applyAnswer(key, 'custom', t, noteText);
    pushUndo('自定义“' + ((u && u.title) || key) + '”为“' + t + '”', snap);
    ui.editing = null;
    renderActive();
    showToast('已保存自定义题名', undoLast, true);
    return true;
  }

  /* ---------------- 弹层 ---------------- */

  function openSheet(title, build) {
    $('#sheet-title').textContent = title;
    var body = $('#sheet-body');
    body.innerHTML = '';
    build(body);
    $('#sheet-backdrop').hidden = false;
  }

  function closeSheet() {
    $('#sheet-backdrop').hidden = true;
    $('#sheet-body').innerHTML = '';
  }

  /* ---------------- Toast ---------------- */

  function showToast(msg, undoFn, withUndo) {
    $('#toast-msg').textContent = msg;
    var btn = $('#toast-undo');
    if (withUndo && undoFn) {
      btn.hidden = false;
      btn.onclick = function () {
        hideToast();
        undoFn();
      };
    } else {
      btn.hidden = true;
      btn.onclick = null;
    }
    $('#toast').classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(hideToast, 5000);
  }

  function hideToast() {
    $('#toast').classList.remove('show');
    clearTimeout(toastTimer);
  }

  /* ---------------- 外观 ---------------- */

  function applyChrome() {
    document.documentElement.setAttribute('data-theme', state.theme);
    document.documentElement.setAttribute('data-fs', String(state.fontSize));
    var meta = $('#meta-theme');
    if (meta) meta.setAttribute('content', state.theme === 'light' ? '#f2f7f2' : '#000000');
    $('#btn-theme').textContent = state.theme === 'dark' ? '日间' : '夜间';
    $('#btn-font').textContent = '字号 ' + ['小', '中', '大'][state.fontSize - 1];
  }

  function toggleTheme() {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    applyChrome();
    saveState();
  }

  function cycleFont() {
    state.fontSize = state.fontSize >= 3 ? 1 : state.fontSize + 1;
    applyChrome();
    saveState();
  }

  /* ---------------- 统计 ---------------- */

  function volOfKey(key) {
    if (state.volIndex && state.volIndex.has(key)) return state.volIndex.get(key);
    var m = /^[Vv](\d+)/.exec(key);
    return m ? Number(m[1]) : null;
  }

  function speedPerMinute() {
    if (!state.sessionStart || !state.sessionCount) return 0;
    var minutes = (Date.now() - state.sessionStart) / 60000;
    if (minutes <= 0) return 0;
    return state.sessionCount / minutes;
  }

  function openStats() {
    var total = scopeTotal();
    var done = answeredCount();
    var remain = Math.max(0, total - done);
    var speed = speedPerMinute();
    var eta = speed > 0 ? remain / speed : null;
    var today = state.todayCount.date === todayStr() ? state.todayCount.count : 0;
    var goal = state.dailyGoal || 500;
    var volCounts = {};
    Object.keys(state.answers).forEach(function (k) {
      var v = volOfKey(k);
      if (v == null) return;
      volCounts[v] = (volCounts[v] || 0) + 1;
    });

    openSheet('统计', function (body) {
      var html = [];
      html.push('<div class="stat-grid">');
      html.push('<div class="stat-cell"><span class="k">已答</span><span class="v">' + done + '</span></div>');
      html.push('<div class="stat-cell"><span class="k">剩余</span><span class="v">' + remain + '</span></div>');
      html.push('<div class="stat-cell"><span class="k">速度（条/分钟）</span><span class="v">' +
        (speed ? speed.toFixed(1) : '—') + '</span></div>');
      html.push('<div class="stat-cell"><span class="k">剩余估算</span><span class="v">' +
        (eta == null ? '—' : Math.round(eta) + ' 分') + '</span></div>');
      html.push('<div class="stat-cell"><span class="k">今日已答</span><span class="v">' + today + '</span></div>');
      html.push('<div class="stat-cell"><span class="k">每日目标</span><span class="v">' + goal + '</span></div>');
      html.push('</div>');

      html.push('<div class="field"><label>每日目标（条）</label><input type="number" id="goal-input" min="1" max="5000" value="' +
        goal + '"></div>');
      var todayPct = goal > 0 ? Math.min(100, Math.round((today / goal) * 100)) : 0;
      html.push('<div class="volbar"><span>今日</span><div class="track"><div class="fill" style="width:' +
        todayPct + '%"></div></div><span>' + todayPct + '%</span></div>');

      html.push('<h3 style="font-size:14px;margin:14px 0 8px">按卷进度</h3>');
      state.vols.forEach(function (v) {
        var count = volCounts[v.vol] || 0;
        var vt = v.units || 0;
        var pct = vt ? Math.round((count / vt) * 100) : 0;
        html.push('<div class="volbar"><span>第 ' + v.vol + ' 卷</span><div class="track"><div class="fill" style="width:' +
          pct + '%"></div></div><span>' + count + '/' + vt + '</span></div>');
      });
      body.innerHTML = html.join('');
      var input = $('#goal-input', body);
      if (input) {
        input.addEventListener('change', function () {
          var n = parseInt(input.value, 10);
          if (!n || n < 1) return;
          state.dailyGoal = n;
          saveState();
          postConfig({ daily_goal: n }).catch(function () {});
          showToast('每日目标已改为 ' + n);
        });
      }
    });
  }

  function postConfig(patch) {
    var cfg = Object.assign({}, state.config || {}, patch);
    return apiSend('POST', '/api/config', { config: cfg }).then(function (r) {
      state.config = r && r.config ? r.config : cfg;
      saveState();
    });
  }

  /* ---------------- 配置上传 ---------------- */

  function openConfig() {
    openSheet('配置', function (body) {
      var cfgText = JSON.stringify(state.config || {}, null, 2);
      var scopeCount = state.scope && typeof state.scope.effective === 'number'
        ? state.scope.effective
        : scopeTotal();
      var html = [];
      html.push('<p class="hint">当前作用域 ' + scopeCount + ' 条（原 ' + originalTotal() + '）</p>');
      html.push('<div class="field"><label>参数配置 JSON（vol_start / vol_end / daily_goal / theme / font_size / labels / only_flagged）</label>');
      html.push('<textarea id="cfg-text" rows="7">' + esc(cfgText) + '</textarea>');
      html.push('<input type="file" id="cfg-file" accept=".json,application/json">');
      html.push('</div>');
      html.push('<div class="field"><label>审阅清单 JSON（{"unit_keys":[...]}）</label>');
      html.push('<textarea id="scope-text" rows="4" placeholder="{&quot;unit_keys&quot;:[]}"></textarea>');
      html.push('<input type="file" id="scope-file" accept=".json,application/json">');
      html.push('</div>');
      html.push('<div class="sheet-actions">');
      html.push('<button type="button" class="primary" id="cfg-save">上传参数配置</button>');
      html.push('<button type="button" class="primary" id="scope-save">上传审阅清单</button>');
      html.push('<button type="button" id="scope-reset">恢复全量（卷段与清单）</button>');
      html.push('<button type="button" id="cfg-export">导出配置</button>');
      html.push('</div>');
      body.innerHTML = html.join('');

      function readFile(file, cb) {
        var fr = new FileReader();
        fr.onload = function () {
          cb(String(fr.result || ''));
        };
        fr.readAsText(file, 'utf-8');
      }

      $('#cfg-file', body).addEventListener('change', function (e) {
        var f = e.target.files && e.target.files[0];
        if (!f) return;
        readFile(f, function (text) {
          $('#cfg-text', body).value = text;
        });
      });
      $('#scope-file', body).addEventListener('change', function (e) {
        var f = e.target.files && e.target.files[0];
        if (!f) return;
        readFile(f, function (text) {
          $('#scope-text', body).value = text;
        });
      });
      $('#cfg-save', body).addEventListener('click', function () {
        var obj;
        try {
          obj = JSON.parse($('#cfg-text', body).value);
        } catch (err) {
          showToast('参数配置不是合法 JSON');
          return;
        }
        apiSend('POST', '/api/config', { config: obj })
          .then(function (r) {
            state.config = r && r.config ? r.config : obj;
            if (typeof obj.daily_goal === 'number' && obj.daily_goal > 0) state.dailyGoal = obj.daily_goal;
            saveState();
            applyChrome();
            closeSheet();
            showToast('参数配置已上传');
            reloadAll();
          })
          .catch(function (e) {
            showToast('上传失败：' + e.message);
          });
      });
      $('#scope-save', body).addEventListener('click', function () {
        var obj;
        try {
          obj = JSON.parse($('#scope-text', body).value);
        } catch (err) {
          showToast('审阅清单不是合法 JSON');
          return;
        }
        var keys = Array.isArray(obj) ? obj : obj.unit_keys;
        if (!Array.isArray(keys)) {
          showToast('缺少 unit_keys 数组');
          return;
        }
        apiSend('POST', '/api/scope', { unit_keys: keys })
          .then(function () {
            closeSheet();
            showToast('审阅清单已上传：' + keys.length + ' 条');
            reloadAll();
          })
          .catch(function (e) {
            showToast('上传失败：' + e.message);
          });
      });
      $('#scope-reset', body).addEventListener('click', function () {
        apiSend('POST', '/api/config', { config: { vol_start: 1, vol_end: 75, only_flagged: false } })
          .then(function () {
            return apiSend('POST', '/api/scope', { unit_keys: [] });
          })
          .then(function () {
            closeSheet();
            showToast('已恢复全量作用域（卷段 1–75、清空清单）');
            reloadAll();
          })
          .catch(function (e) {
            showToast('操作失败：' + e.message);
          });
      });
      $('#cfg-export', body).addEventListener('click', function () {
        downloadFile('/api/config/export');
      });
    });
  }

  function reloadAll() {
    state.units = [];
    state.volIndex = null;
    state.unitsLoaded = false;
    state.unitsLoading = false;
    state.unitsError = null;
    loadAll();
  }

  function downloadFile(url) {
    var a = document.createElement('a');
    a.href = url;
    a.rel = 'noopener';
    a.download = '';
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
      a.remove();
    }, 0);
  }

  /* ---------------- 导出 / 归档 / 导入 ---------------- */

  function openExport() {
    openSheet('导出', function (body) {
      var html = [];
      html.push('<p class="hint">导出全部作答；回写清单按落账格式输出。</p>');
      html.push('<div class="sheet-actions">');
      html.push('<button type="button" id="exp-json">导出 JSON</button>');
      html.push('<button type="button" id="exp-tsv">导出 TSV</button>');
      html.push('<button type="button" id="exp-rw">导出回写清单</button>');
      html.push('<button type="button" class="primary" id="exp-archive">收工归档</button>');
      html.push('</div>');
      html.push('<div class="field" style="margin-top:14px"><label>导入 JSON 恢复</label>');
      html.push('<input type="file" id="imp-file" accept=".json,application/json"></div>');
      html.push('<div class="field"><button type="button" id="exp-cfg">导出配置</button></div>');
      body.innerHTML = html.join('');

      $('#exp-json', body).addEventListener('click', function () {
        downloadFile('/api/export?fmt=json');
      });
      $('#exp-tsv', body).addEventListener('click', function () {
        downloadFile('/api/export?fmt=tsv');
      });
      $('#exp-rw', body).addEventListener('click', function () {
        downloadFile('/api/export?fmt=rewrite');
      });
      $('#exp-cfg', body).addEventListener('click', function () {
        downloadFile('/api/config/export');
      });
      $('#exp-archive', body).addEventListener('click', function () {
        apiSend('POST', '/api/archive', {})
          .then(function (r) {
            showToast('已归档 ' + ((r && r.count) || 0) + ' 条至 ' + ((r && r.dir) || ''));
          })
          .catch(function (e) {
            showToast('归档失败：' + e.message);
          });
      });
      $('#imp-file', body).addEventListener('change', function (e) {
        var f = e.target.files && e.target.files[0];
        if (!f) return;
        var fr = new FileReader();
        fr.onload = function () {
          var obj;
          try {
            obj = JSON.parse(String(fr.result || ''));
          } catch (err) {
            showToast('导入文件不是合法 JSON');
            return;
          }
          var answers = obj && obj.answers ? obj.answers : obj;
          if (!answers || typeof answers !== 'object') {
            showToast('导入文件缺少 answers');
            return;
          }
          apiSend('POST', '/api/import', { answers: answers })
            .then(function () {
              Object.keys(answers).forEach(function (k) {
                var a = answers[k];
                if (!a || !a.verdict) return;
                if (!state.answers[k] || newerAnswer(a, state.answers[k])) {
                  state.answers[k] = cloneAnswer(a);
                }
              });
              saveState();
              renderActive();
              closeSheet();
              showToast('已导入 ' + Object.keys(answers).length + ' 条');
            })
            .catch(function (err) {
              showToast('导入失败：' + err.message);
            });
        };
        fr.readAsText(f, 'utf-8');
      });
    });
  }

  /* ---------------- 定位 / 筛选 ---------------- */

  function openGoto() {
    openSheet('定位', function (body) {
      var current = ui.vol || pickVol();
      var html = [];
      html.push('<div class="field"><label>卷</label><select id="goto-vol">');
      state.vols.forEach(function (v) {
        html.push('<option value="' + v.vol + '"' + (v.vol === current ? ' selected' : '') + '>第 ' +
          v.vol + ' 卷 ' + esc(v.title || '') + '</option>');
      });
      html.push('</select></div>');
      html.push('<div class="field"><label>章</label><select id="goto-chap"></select></div>');
      html.push('<div class="field"><label>节</label><select id="goto-sec"></select></div>');
      html.push('<div class="sheet-actions"><button type="button" class="primary" id="goto-go">跳转</button></div>');
      body.innerHTML = html.join('');

      function fillChaps() {
        var vol = Number($('#goto-vol', body).value);
        var chaps = state.units.filter(function (u) {
          return u.level === 'chapter' && u.vol === vol;
        });
        chaps.sort(function (a, b) {
          return a.chapter_no - b.chapter_no;
        });
        var opt = ['<option value="">全部章</option>'];
        chaps.forEach(function (c) {
          opt.push('<option value="' + c.chapter_no + '">第 ' + c.chapter_no + ' 章 ' +
            esc(c.title || '') + '</option>');
        });
        $('#goto-chap', body).innerHTML = opt.join('');
        fillSecs();
      }

      function fillSecs() {
        var vol = Number($('#goto-vol', body).value);
        var chap = $('#goto-chap', body).value;
        var secs = state.units.filter(function (u) {
          return u.level === 'section' && u.vol === vol && (!chap || String(u.chapter_no) === chap);
        });
        secs.sort(function (a, b) {
          return a.chapter_no - b.chapter_no || a.section_no - b.section_no;
        });
        var opt = ['<option value="">全部节</option>'];
        secs.forEach(function (s) {
          opt.push('<option value="' + s.chapter_no + ':' + s.section_no + '">第 ' + s.chapter_no +
            ' 章第 ' + s.section_no + ' 节 ' + esc(s.title || '') + '</option>');
        });
        $('#goto-sec', body).innerHTML = opt.join('');
      }

      $('#goto-vol', body).addEventListener('change', function () {
        ensureVolUnits(Number($('#goto-vol', body).value), fillChaps);
        fillChaps();
      });
      $('#goto-chap', body).addEventListener('change', fillSecs);
      $('#goto-go', body).addEventListener('click', function () {
        var vol = Number($('#goto-vol', body).value);
        var chap = $('#goto-chap', body).value;
        var sec = $('#goto-sec', body).value;
        closeSheet();
        ui.vol = vol;
        ui.all = false;
        if (ui.view !== 'group') setView('group');

        function jump() {
          var target = null;
          if (sec) {
            var pair = sec.split(':');
            var heads = $$('.section-head', $('#view-group'));
            for (var i = 0; i < heads.length; i += 1) {
              var btn = heads[i].querySelector('.sec-pass');
              if (btn && Number(btn.dataset.chapter) === Number(pair[0]) &&
                Number(btn.dataset.section) === Number(pair[1])) {
                target = heads[i];
                break;
              }
            }
          } else if (chap) {
            var chs = $$('.chapter-head', $('#view-group'));
            for (var j = 0; j < chs.length; j += 1) {
              var chTitle = chs[j].querySelector('.ch-title');
              if (chTitle && chTitle.textContent.indexOf('第 ' + chap + ' 章') === 0) {
                target = chs[j];
                break;
              }
            }
          }
          if (target) target.scrollIntoView({ block: 'start', behavior: 'smooth' });
          else window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        ensureVolUnits(vol, function () {
          renderGroup();
          jump();
        });
      });

      ensureVolUnits(current, fillChaps);
      fillChaps();
    });
  }

  function openFilter() {
    openSheet('筛选', function (body) {
      var opts = [
        ['all', '全部'],
        ['pending', '待审'],
        ['changed', '已改'],
        ['ok', '已通过']
      ];
      var html = ['<div class="opt-list">'];
      opts.forEach(function (o) {
        html.push('<button type="button" data-filter="' + o[0] + '" aria-pressed="' +
          (ui.filter === o[0] ? 'true' : 'false') + '">' + o[1] + '</button>');
      });
      html.push('</div>');
      body.innerHTML = html.join('');
      $$('[data-filter]', body).forEach(function (b) {
        b.addEventListener('click', function () {
          ui.filter = b.dataset.filter;
          $('#btn-filter').textContent = '筛选：' + b.textContent;
          ui.singleIdx = 0;
          closeSheet();
          renderActive();
        });
      });
    });
  }

  function resumeLast() {
    if (!state.cursor || state.cursor.key == null) {
      showToast('还没有作答记录');
      return;
    }
    ui.vol = state.cursor.vol || pickVol();
    ui.all = false;
    ui.filter = 'all';
    $('#btn-filter').textContent = '筛选：全部';
    if (ui.view !== 'group') setView('group');
    else renderGroup();
    var el = $('.card[data-key="' + state.cursor.key + '"]', $('#view-group'));
    if (el) el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    else window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function setView(v) {
    ui.view = v;
    $('#btn-view').textContent = v === 'group' ? '单卡模式' : '分组模式';
    $('#btn-view').setAttribute('aria-pressed', v === 'single' ? 'true' : 'false');
    if (v === 'single') {
      var list = singleList();
      var idx = 0;
      if (state.cursor && state.cursor.key) {
        for (var i = 0; i < list.length; i += 1) {
          if (list[i].key === state.cursor.key) {
            idx = i;
            break;
          }
        }
      }
      ui.singleIdx = idx;
    }
    renderActive();
  }

  /* ---------------- 实时建议（本会话轮询） ---------------- */

  var suggestPollers = {};

  function stopSuggestPoll(key) {
    if (suggestPollers[key]) {
      clearInterval(suggestPollers[key]);
      delete suggestPollers[key];
    }
  }

  function pollSuggest(key, rid) {
    stopSuggestPoll(key);
    suggestPollers[key] = setInterval(function () {
      if (document.hidden) return;
      var st = state.suggest[key];
      if (!st) {
        stopSuggestPoll(key);
        return;
      }
      var elapsed = Math.round((Date.now() - st.started) / 1000);
      var box = $('.suggest-wait[data-key="' + key + '"]');
      var label = box ? $('.suggest-elapsed', box) : null;
      if (label) label.textContent = elapsed + ' 秒';
      if (elapsed > 300) {
        stopSuggestPoll(key);
        delete state.suggest[key];
        renderActive();
        showToast('等待建议超时（5 分钟）：请在本会话说“处理”后重试');
        return;
      }
      apiGet('/api/suggest?id=' + encodeURIComponent(rid)).then(function (d) {
        if (!d || d.status === 'pending') return;
        stopSuggestPoll(key);
        delete state.suggest[key];
        if (d.status === 'ready' && d.candidates && d.candidates.length) {
          state.candidates[key] = d.candidates;
          showToast('已收到 ' + d.candidates.length + ' 条建议', null, true);
        } else {
          showToast('建议生成失败：' + (d.error || '未知错误'));
        }
        renderActive();
      }).catch(function () {});
    }, 1500);
  }

  function requestSuggest(key) {
    var u = unitByKey(key);
    var a = state.answers[key];
    if (!u || !a || a.verdict !== 'reroll') {
      showToast('请先选择“重拟”');
      return;
    }
    apiSend('POST', '/api/suggest', {
      unit_key: key,
      tags: (a.tags || []).slice(),
      merge_target: a.merge_target || ''
    }).then(function (res) {
      if (!res || !res.id) throw new Error('入队失败');
      state.suggest[key] = { id: res.id, started: Date.now() };
      ui.tagging = null;
      renderActive();
      pollSuggest(key, res.id);
      showToast('已提交，等待会话返回建议');
    }).catch(function (err) {
      showToast('提交失败：' + (err.message || err));
    });
  }

  function resumeSuggest() {
    apiGet('/api/suggest?pending=1').then(function (d) {
      var list = (d && d.pending) || [];
      if (!list.length) return;
      list.slice(0, 10).forEach(function (item) {
        state.suggest[item.unit_key] = {
          id: item.id,
          started: Date.parse(item.created_at) || Date.now()
        };
        pollSuggest(item.unit_key, item.id);
      });
      renderActive();
    }).catch(function () {});
  }

  /* ---------------- 事件委托 ---------------- */

  function onCardClick(ev) {
    var btn = ev.target.closest('[data-act]');
    if (!btn) return;
    var act = btn.dataset.act;
    var key = btn.dataset.key;

    if (act === 'fold-vol') {
      var fv = 'v' + btn.dataset.vol;
      setFold('vols', fv, !foldState('vols', fv, ui.all));
      renderGroup();
      return;
    }
    if (act === 'fold-chapter') {
      var fc = 'v' + btn.dataset.vol + 'c' + btn.dataset.chapter;
      setFold('chapters', fc, !foldState('chapters', fc, false));
      renderGroup();
      return;
    }
    if (act === 'fold-section') {
      var fs = 'v' + btn.dataset.vol + 'c' + btn.dataset.chapter + 's' + btn.dataset.section;
      setFold('sections', fs, !foldState('sections', fs, false));
      renderGroup();
      return;
    }

    if (act === 'verdict') {
      onVerdict(key, btn.dataset.v);
      return;
    }
    if (act === 'tag') {
      toggleTag(key, btn.dataset.tag);
      return;
    }
    if (act === 'merge-target') {
      setMergeTarget(key, btn.dataset.merge);
      return;
    }
    if (act === 'tag-save') {
      ui.tagging = null;
      renderActive();
      return;
    }
    if (act === 'suggest') {
      requestSuggest(key);
      return;
    }
    if (act === 'suggest-cancel') {
      stopSuggestPoll(key);
      delete state.suggest[key];
      renderActive();
      return;
    }
    if (act === 'tag-quick') {
      state.quickTags = !!btn.checked;
      saveState();
      showToast(state.quickTags
        ? '已开启连续沿用：之后点“重拟”一键沿用当前标签'
        : '已关闭连续沿用');
      return;
    }
    if (act === 'clear') {
      onClear(key);
      return;
    }
    if (act === 'section') {
      onSectionPass(Number(btn.dataset.vol), Number(btn.dataset.chapter), Number(btn.dataset.section));
      return;
    }
    if (act === 'custom-cancel') {
      ui.editing = null;
      renderActive();
      return;
    }
    if (act === 'custom-save') {
      var card = btn.closest('.card');
      var ta = $('.ct-input', card);
      var note = $('.note-input', card);
      if (!saveCustom(key, ta ? ta.value : '', note ? note.value : '')) {
        var err = $('.ct-err', card);
        if (err) err.textContent = '题名须为 1–120 字';
      }
      return;
    }
    if (act === 'note-toggle') {
      var box = $('[data-box="note"]', btn.closest('.inline-box'));
      if (box) box.hidden = !box.hidden;
      return;
    }
    if (act === 'cand-adopt') {
      adoptCandidate(key, btn.dataset.cid, false);
      return;
    }
    if (act === 'cand-edit') {
      adoptCandidate(key, btn.dataset.cid, true);
      return;
    }
    if (act === 'cand-keep') {
      var snapK = snapshot([key]);
      applyAnswer(key, 'ok', null, null);
      pushUndo('保留旧题：' + key, snapK);
      renderActive();
      showToast('已保留旧题', undoLast, true);
      return;
    }
    if (act === 'cand-reroll') {
      var snapR = snapshot([key]);
      applyAnswer(key, 'reroll', null, '再次重拟');
      pushUndo('再次重拟：' + key, snapR);
      renderActive();
      showToast('已标记再次重拟', undoLast, true);
      return;
    }
    if (act === 'single-prev' || act === 'single-next') {
      var list = singleList();
      var step = act === 'single-prev' ? -1 : 1;
      ui.singleIdx = Math.min(list.length - 1, Math.max(0, ui.singleIdx + step));
      if (list[ui.singleIdx]) setCursor(list[ui.singleIdx]);
      saveState();
      renderSingle();
      window.scrollTo({ top: 0 });
    }
  }

  function adoptCandidate(key, cid, editFirst) {
    var u = unitByKey(key);
    var cands = state.candidates[key] || [];
    var cand = null;
    for (var i = 0; i < cands.length; i += 1) {
      var c = cands[i];
      if (String(c.candidate_id != null ? c.candidate_id : i) === String(cid)) {
        cand = c;
        break;
      }
    }
    if (!cand) {
      showToast('候选已失效');
      return;
    }
    if (editFirst) {
      ui.editing = key;
      renderActive();
      var card = $('.card[data-key="' + key + '"]', activeRoot());
      if (card) {
        var box = $('.inline-box[data-box="custom"]', card);
        if (box) box.hidden = false;
        var ta = $('.ct-input', card);
        if (ta) {
          ta.value = cand.new_title;
          ta.focus();
        }
      }
      showToast('可改写候选题名后点“保存”');
      return;
    }
    var snap = snapshot([key]);
    applyAnswer(key, 'custom', cand.new_title, null);
    pushUndo('采纳候选“' + cand.new_title + '”', snap);
    renderActive();
    showToast('已采纳候选', undoLast, true);
    if (u) setCursor(u);
  }

  /* ---------------- 沉浸模式 ---------------- */

  function enterImmersive() {
    $('#start-overlay').hidden = true;
    var el = document.documentElement;
    var req = el.requestFullscreen || el.webkitRequestFullscreen;
    if (!req) {
      fallbackStatusBar('当前浏览器不支持全屏，已使用同色状态栏模式');
      return;
    }
    Promise.resolve(req.call(el))
      .then(function () {
        $('#btn-exit-fs').hidden = false;
      })
      .catch(function () {
        fallbackStatusBar('全屏被拒绝，已使用同色状态栏模式');
      });
  }

  function fallbackStatusBar(msg) {
    document.documentElement.classList.add('no-fs');
    showToast(msg);
  }

  function exitImmersive() {
    if (document.fullscreenElement && document.exitFullscreen) {
      document.exitFullscreen().catch(function () {});
    } else if (document.webkitFullscreenElement && document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    }
    $('#btn-exit-fs').hidden = true;
  }

  /* ---------------- 启动 ---------------- */

  function syncTopOffset() {
    var tb = $('#topbar');
    if (!tb) return;
    var h = Math.round(tb.getBoundingClientRect().height);
    document.documentElement.style.setProperty('--top-h', h + 'px');
  }

  function bind() {
    $('#btn-theme').addEventListener('click', toggleTheme);
    $('#btn-font').addEventListener('click', cycleFont);
    $('#btn-view').addEventListener('click', function () {
      setView(ui.view === 'group' ? 'single' : 'group');
    });
    $('#btn-filter').addEventListener('click', openFilter);
    $('#btn-goto').addEventListener('click', openGoto);
    $('#btn-resume').addEventListener('click', resumeLast);
    $('#btn-stats').addEventListener('click', openStats);
    $('#btn-config').addEventListener('click', openConfig);
    $('#btn-export').addEventListener('click', openExport);
    $('#btn-exit-fs').addEventListener('click', exitImmersive);
    $('#sheet-close').addEventListener('click', closeSheet);
    $('#sheet-backdrop').addEventListener('click', function (e) {
      if (e.target === $('#sheet-backdrop')) closeSheet();
    });
    $('#btn-start').addEventListener('click', enterImmersive);
    $('#btn-start-plain').addEventListener('click', function () {
      $('#start-overlay').hidden = true;
    });

    $('#view-group').addEventListener('click', onCardClick);
    $('#view-single').addEventListener('click', onCardClick);

    $('#view-group').addEventListener('input', function (e) {
      if (e.target.classList.contains('ct-input')) {
        var box = e.target.closest('.inline-box');
        var cnt = $('.ct-count', box);
        if (cnt) cnt.textContent = e.target.value.length + ' / 120';
        var err = $('.ct-err', box);
        if (err) err.textContent = '';
      }
    });

    $('#view-group').addEventListener('change', function (e) {
      if (e.target.id === 'vol-select') {
        if (e.target.value === 'all') {
          ui.all = true;
          renderGroup();
          ensureAllVols(renderGroup);
        } else {
          ui.all = false;
          ui.vol = Number(e.target.value);
          ensureVolUnits(ui.vol, renderGroup);
        }
      }
    });

    document.addEventListener('fullscreenchange', function () {
      $('#btn-exit-fs').hidden = !document.fullscreenElement;
    });

    document.addEventListener('visibilitychange', function () {
      if (!document.hidden && (sync.dirty.size || sync.pendingPut || sync.pendingDeletes.size)) {
        flush();
      }
    });

    window.addEventListener('online', function () {
      flush();
    });
  }

  function init() {
    loadLocal();
    if (state.todayCount.date !== todayStr()) {
      state.todayCount = { date: todayStr(), count: 0 };
    }
    if (state.config === null) state.config = {};
    applyChrome();
    bind();
    syncTopOffset();
    if (window.ResizeObserver) {
      new ResizeObserver(syncTopOffset).observe($('#topbar'));
    } else {
      window.addEventListener('resize', syncTopOffset);
    }
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('./sw.js').catch(function () {});
      navigator.serviceWorker.ready.then(function () {
        var tries = 0;
        (function warm() {
          // 首访时首个请求发在 SW claim 之前，不落缓存；须等 controller 就绪
          if ((!navigator.serviceWorker.controller || !ui.vol) && tries < 80) {
            tries += 1;
            setTimeout(warm, 250);
            return;
          }
          if (!ui.vol) return;
          // 预热当前卷与答案接口，保证断网刷新仍可渲染并合并
          apiGet('/api/answers').catch(function () {});
          apiGet('/api/units?vol=' + ui.vol).catch(function () {});
        })();
      }).catch(function () {});
      navigator.serviceWorker.addEventListener('controllerchange', function () {
        if (ui.vol) apiGet('/api/units?vol=' + ui.vol).catch(function () {});
      });
    }
    loadAll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
