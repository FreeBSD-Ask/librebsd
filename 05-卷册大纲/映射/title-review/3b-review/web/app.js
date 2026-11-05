'use strict';

const state = {
  manifest: null,
  config: null,
  scope: null,
  answers: {},
  vol: null,
  chapter: '',
  units: [],
  chapters: [],
  search: '',
  visible: 80,
  customTarget: null,
};

const dom = {};
const cardMap = new Map();
let toastTimer = null;
let searchTimer = null;

function $(selector, root = document) {
  return root.querySelector(selector);
}

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined && text !== null) node.textContent = String(text);
  return node;
}

async function api(path, options = {}) {
  const init = { method: options.method || 'GET', headers: {} };
  if (options.body !== undefined) {
    init.headers['Content-Type'] = 'application/json';
    init.body = JSON.stringify(options.body);
  }
  const response = await fetch(path, init);
  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch (err) {
      data = null;
    }
  }
  if (!response.ok) {
    const detail = data && (data.detail || data.error) ? data.detail || data.error : `HTTP ${response.status}`;
    const error = new Error(detail);
    error.status = response.status;
    error.payload = data;
    throw error;
  }
  return data;
}

function toast(message, isError = false) {
  dom.toast.textContent = message;
  dom.toast.classList.toggle('is-error', Boolean(isError));
  dom.toast.classList.add('is-visible');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => dom.toast.classList.remove('is-visible'), isError ? 4200 : 2000);
}

function localDateKey(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function shorten(text, limit) {
  const value = String(text || '');
  return value.length > limit ? `${value.slice(0, limit)}…` : value;
}

function labelFor(verdict) {
  if (!state.config || !state.config.labels) return verdict;
  return state.config.labels[verdict] || verdict;
}

function levelLabel(level) {
  return level === 'chapter' ? '章' : level === 'section' ? '节' : '小节';
}

function applyConfig(config) {
  state.config = config;
  const root = document.documentElement;
  root.dataset.theme = config.theme;
  root.dataset.size = config.font_size;
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.setAttribute('content', config.theme === 'day' ? '#f4efe4' : '#000000');
  if (dom.flagToggle) dom.flagToggle.checked = Boolean(config.only_flagged);
}

function renderMeter() {
  if (!state.config || !state.manifest) return;
  const answers = Object.values(state.answers);
  const counts = { ok: 0, reroll: 0, custom: 0 };
  const todayKey = localDateKey(new Date());
  let today = 0;
  for (const answer of answers) {
    if (counts[answer.verdict] !== undefined) counts[answer.verdict] += 1;
    if (answer.updated_at) {
      const when = new Date(answer.updated_at);
      if (!Number.isNaN(when.getTime()) && localDateKey(when) === todayKey) today += 1;
    }
  }
  const goal = state.config.daily_goal;
  const effective = state.manifest.scope.effective;
  dom.answerStats.textContent = `已答 ${answers.length} / ${effective}`;
  dom.verdictStats.textContent = `${labelFor('ok')} ${counts.ok} · ${labelFor('reroll')} ${counts.reroll} · ${labelFor('custom')} ${counts.custom}`;
  dom.dailyStats.textContent = `今日 ${today} / ${goal}`;
  const percent = Math.min(100, Math.round((today / goal) * 100));
  dom.dailyBar.style.width = `${percent}%`;
  dom.meterBar.setAttribute('aria-valuenow', String(percent));
}

function renderScopeSummary() {
  if (!state.manifest || !state.config) return;
  const manifest = state.manifest;
  if (manifest.scope.active) {
    dom.scopeSummary.textContent = `定制范围 · ${manifest.scope.configured} 单元（共 ${manifest.totals.units}）`;
  } else {
    dom.scopeSummary.textContent = `第 ${state.config.vol_start}–${state.config.vol_end} 卷 · ${manifest.scope.effective} 单元`;
  }
}

function buildVolSelect() {
  dom.volSelect.replaceChildren();
  for (const vol of state.manifest.vols) {
    const option = document.createElement('option');
    option.value = String(vol.vol);
    option.textContent = `第 ${vol.vol} 卷 · ${shorten(vol.title, 16)}`;
    option.title = vol.title;
    dom.volSelect.appendChild(option);
  }
}

function initialVol() {
  const scope = state.scope;
  if (scope && Array.isArray(scope.unit_keys) && scope.unit_keys.length) {
    const match = /^V(\d{2})\./.exec(scope.unit_keys[0]);
    if (match) return Number(match[1]);
  }
  const start = state.config ? state.config.vol_start : 1;
  const end = state.config ? state.config.vol_end : 75;
  return Math.min(Math.max(start, 1), Math.max(end, 1));
}

function deriveChapters(units) {
  const map = new Map();
  for (const unit of units) {
    if (unit.level === 'chapter') {
      map.set(unit.chapter_no, unit.title);
    } else if (!map.has(unit.chapter_no)) {
      map.set(unit.chapter_no, `第 ${unit.chapter_no} 章`);
    }
  }
  return Array.from(map.entries())
    .sort((left, right) => left[0] - right[0])
    .map(([no, title]) => ({ no, title }));
}

function buildChapterSelect() {
  dom.chapterSelect.replaceChildren();
  dom.chapterSelect.appendChild(new Option('全部', ''));
  for (const chapter of state.chapters) {
    const option = new Option(`第 ${chapter.no} 章 · ${shorten(chapter.title, 16)}`, String(chapter.no));
    option.title = chapter.title;
    dom.chapterSelect.appendChild(option);
  }
  dom.chapterSelect.value = state.chapter;
}

function filteredUnits() {
  let units = state.units;
  if (state.chapter !== '') {
    const chapterNo = Number(state.chapter);
    units = units.filter((unit) => unit.chapter_no === chapterNo);
  }
  const query = state.search.trim().toLowerCase();
  if (query) {
    units = units.filter((unit) => {
      const haystack = `${unit.title || ''} ${unit.thesis || ''}`.toLowerCase();
      return haystack.includes(query);
    });
  }
  return units;
}

function buildCard(unit) {
  const answer = state.answers[unit.key];
  const card = el('article', `unit unit-${unit.level}`);
  card.dataset.key = unit.key;
  card.setAttribute('role', 'listitem');

  const head = el('div', 'unit-head');
  head.appendChild(el('span', 'level-badge', levelLabel(unit.level)));
  head.appendChild(el('span', 'unit-key', unit.key));
  if (unit.flag_machine) head.appendChild(el('span', 'flag flag-machine', '机判'));
  if (unit.flag_human) head.appendChild(el('span', 'flag flag-human', '人判'));
  if (answer) head.appendChild(el('span', 'answered-chip', labelFor(answer.verdict)));
  card.appendChild(head);

  const title = el('h2', 'unit-title', unit.title);
  card.appendChild(title);

  if (unit.level === 'subsection' && unit.thesis) {
    card.appendChild(el('p', 'unit-thesis', unit.thesis));
  }

  const meta = el('div', 'unit-meta');
  if (unit.level === 'subsection' && unit.source_count !== null && unit.source_count !== undefined) {
    meta.appendChild(el('span', '', `史料 ${unit.source_count}`));
  }
  meta.appendChild(el('span', '', `序 ${unit.order}`));
  if (unit.level === 'subsection' && unit.section_no !== null) {
    meta.appendChild(el('span', '', `${unit.chapter_no}.${unit.section_no}`));
  }
  card.appendChild(meta);

  if (answer && answer.verdict === 'custom' && answer.custom_title) {
    const line = el('p', 'custom-line');
    line.appendChild(el('span', 'tag', '自定义'));
    line.appendChild(document.createTextNode(answer.custom_title));
    card.appendChild(line);
  }
  if (answer && answer.note) {
    card.appendChild(el('p', 'note-line', `备注：${answer.note}`));
  }

  const actions = el('div', 'verdict-row');
  for (const verdict of ['ok', 'reroll', 'custom']) {
    const button = el('button', 'verdict-btn', labelFor(verdict));
    button.type = 'button';
    button.dataset.verdict = verdict;
    if (answer && answer.verdict === verdict) button.classList.add('is-active');
    button.setAttribute('aria-pressed', answer && answer.verdict === verdict ? 'true' : 'false');
    button.addEventListener('click', () => setVerdict(unit, verdict));
    actions.appendChild(button);
  }
  if (answer) {
    const clear = el('button', 'clear-btn', '清除');
    clear.type = 'button';
    clear.addEventListener('click', () => clearAnswer(unit.key));
    actions.appendChild(clear);
  } else {
    actions.appendChild(el('span'));
  }
  card.appendChild(actions);

  return card;
}

function render() {
  const units = filteredUnits();
  dom.unitList.replaceChildren();
  cardMap.clear();
  for (const unit of units.slice(0, state.visible)) {
    const card = buildCard(unit);
    dom.unitList.appendChild(card);
    cardMap.set(unit.key, card);
  }
  dom.empty.hidden = units.length > 0;
  if (units.length === 0) {
    if (state.search || state.chapter !== '') {
      dom.emptyText.textContent = '没有符合当前筛选的单元。';
    } else if (state.config && state.config.only_flagged) {
      dom.emptyText.textContent = '本卷没有带机判或人判标记的单元。';
    } else {
      dom.emptyText.textContent = '本卷没有单元。';
    }
  }
  dom.loadMore.hidden = units.length <= state.visible;
}

function refreshCard(key) {
  const oldCard = cardMap.get(key);
  const unit = state.units.find((item) => item.key === key);
  if (!oldCard || !unit) return;
  const fresh = buildCard(unit);
  oldCard.replaceWith(fresh);
  cardMap.set(key, fresh);
}

function answerPayload(verdict, customTitle, note) {
  return {
    verdict,
    custom_title: customTitle || '',
    note: note || '',
    updated_at: new Date().toISOString(),
  };
}

async function saveAnswer(key, payload) {
  try {
    await api('/api/answers', { method: 'PUT', body: { answers: { [key]: payload } } });
    state.answers[key] = payload;
    refreshCard(key);
    renderMeter();
    toast(`${labelFor(payload.verdict)} · ${key}`);
    return true;
  } catch (error) {
    toast(error.message, true);
    return false;
  }
}

async function setVerdict(unit, verdict) {
  if (verdict === 'custom') {
    openCustom(unit);
    return;
  }
  const existing = state.answers[unit.key];
  const note = existing ? existing.note : '';
  await saveAnswer(unit.key, answerPayload(verdict, '', note));
}

async function clearAnswer(key) {
  try {
    await api(`/api/answers?key=${encodeURIComponent(key)}`, { method: 'DELETE' });
    delete state.answers[key];
    refreshCard(key);
    renderMeter();
    toast(`已清除 · ${key}`);
  } catch (error) {
    toast(error.message, true);
  }
}

function openCustom(unit) {
  state.customTarget = unit;
  const existing = state.answers[unit.key];
  dom.customOrigin.textContent = `${unit.key} · ${unit.title}`;
  dom.customTitle.value = existing && existing.custom_title ? existing.custom_title : unit.title;
  dom.customNote.value = existing ? existing.note : '';
  dom.customDialog.showModal();
  dom.customTitle.focus();
  dom.customTitle.select();
}

async function saveCustom() {
  if (!state.customTarget) return;
  const title = dom.customTitle.value.trim();
  if (!title) {
    toast('请填写新题名', true);
    return;
  }
  const ok = await saveAnswer(
    state.customTarget.key,
    answerPayload('custom', title, dom.customNote.value.trim()),
  );
  if (ok) {
    dom.customDialog.close();
    state.customTarget = null;
  }
}

async function loadVol(vol) {
  state.vol = vol;
  state.chapter = '';
  state.search = '';
  state.visible = 80;
  dom.searchInput.value = '';
  dom.volSelect.value = String(vol);
  try {
    const data = await api(`/api/units?vol=${vol}`);
    state.units = data.units || [];
    state.chapters = deriveChapters(state.units);
    buildChapterSelect();
    render();
  } catch (error) {
    state.units = [];
    state.chapters = [];
    buildChapterSelect();
    render();
    toast(error.message, true);
  }
}

async function refreshMetrics() {
  const [configResponse, manifest] = await Promise.all([api('/api/config'), api('/api/manifest')]);
  state.config = configResponse.config;
  state.scope = configResponse.scope;
  state.manifest = manifest;
  applyConfig(state.config);
  renderScopeSummary();
  renderMeter();
}

function openSettings() {
  const config = state.config;
  dom.cfgVolStart.value = config.vol_start;
  dom.cfgVolEnd.value = config.vol_end;
  dom.cfgDailyGoal.value = config.daily_goal;
  dom.cfgTheme.value = config.theme;
  dom.cfgFontSize.value = config.font_size;
  dom.cfgLabelOk.value = config.labels.ok;
  dom.cfgLabelReroll.value = config.labels.reroll;
  dom.cfgLabelCustom.value = config.labels.custom;
  dom.cfgOnlyFlagged.checked = config.only_flagged;
  dom.settingsDialog.showModal();
}

async function saveSettings() {
  const config = {
    vol_start: Number(dom.cfgVolStart.value),
    vol_end: Number(dom.cfgVolEnd.value),
    daily_goal: Number(dom.cfgDailyGoal.value),
    theme: dom.cfgTheme.value,
    font_size: dom.cfgFontSize.value,
    labels: {
      ok: dom.cfgLabelOk.value.trim(),
      reroll: dom.cfgLabelReroll.value.trim(),
      custom: dom.cfgLabelCustom.value.trim(),
    },
    only_flagged: dom.cfgOnlyFlagged.checked,
  };
  if (!Number.isInteger(config.vol_start) || config.vol_start < 1 || config.vol_start > 75) {
    toast('起始卷须为 1–75 的整数', true);
    return;
  }
  if (!Number.isInteger(config.vol_end) || config.vol_end < 1 || config.vol_end > 75) {
    toast('结束卷须为 1–75 的整数', true);
    return;
  }
  if (config.vol_start > config.vol_end) {
    toast('起始卷不得大于结束卷', true);
    return;
  }
  if (!Number.isInteger(config.daily_goal) || config.daily_goal < 1 || config.daily_goal > 5000) {
    toast('每日目标须为 1–5000 的整数', true);
    return;
  }
  for (const key of ['ok', 'reroll', 'custom']) {
    const value = config.labels[key];
    if (value.length < 1 || value.length > 8) {
      toast('按钮文字须为 1–8 字', true);
      return;
    }
  }
  try {
    const response = await api('/api/config', { method: 'POST', body: { config } });
    applyConfig(response.config);
    await refreshMetrics();
    const target = state.manifest.scope.active ? state.vol : Math.min(Math.max(state.vol, config.vol_start), config.vol_end);
    await loadVol(target);
    dom.settingsDialog.close();
    toast('设置已保存');
  } catch (error) {
    toast(error.message, true);
  }
}

function updateScopeText() {
  if (!state.scope || !state.manifest) return;
  if (Array.isArray(state.scope.unit_keys) && state.scope.unit_keys.length) {
    dom.scopeCurrent.textContent = `当前为定制范围：${state.scope.unit_keys.length} 个单元。`;
  } else {
    dom.scopeCurrent.textContent = `当前为全量：按设置的卷段（第 ${state.config.vol_start}–${state.config.vol_end} 卷），有效 ${state.manifest.scope.effective} 个单元。`;
  }
}

function openScope() {
  updateScopeText();
  dom.scopeDialog.showModal();
}

async function applyScope(unitKeys) {
  try {
    const response = await api('/api/scope', { method: 'POST', body: { unit_keys: unitKeys } });
    await refreshMetrics();
    updateScopeText();
    let target = state.vol;
    if (response.count && unitKeys.length) {
      const match = /^V(\d{2})\./.exec(unitKeys[0]);
      if (match) target = Number(match[1]);
    } else {
      target = Math.min(Math.max(state.vol, state.config.vol_start), state.config.vol_end);
    }
    await loadVol(target);
    dom.scopeDialog.close();
    toast(response.count ? `已锁定 ${response.count} 个单元` : '已恢复全量范围');
  } catch (error) {
    toast(error.message, true);
  }
}

function scopeVolKeys() {
  return state.units.filter((unit) => unit.vol === state.vol).map((unit) => unit.key);
}

function scopeChapterKeys() {
  if (state.chapter === '') return [];
  const chapterNo = Number(state.chapter);
  return state.units.filter((unit) => unit.chapter_no === chapterNo).map((unit) => unit.key);
}

async function archiveSnapshot() {
  try {
    const response = await api('/api/archive', { method: 'POST', body: {} });
    toast(`已归档 ${response.count} 条：${response.dir}`);
  } catch (error) {
    toast(error.message, true);
  }
}

async function importAnswers(file) {
  if (!file) return;
  try {
    const text = await file.text();
    const parsed = JSON.parse(text);
    const answers = parsed && parsed.answers ? parsed.answers : parsed;
    if (!answers || typeof answers !== 'object' || Array.isArray(answers)) {
      throw new Error('文件中缺少 answers 对象');
    }
    const response = await api('/api/import', { method: 'POST', body: { answers } });
    const latest = await api('/api/answers');
    state.answers = latest.answers || {};
    render();
    renderMeter();
    toast(`导入完成：合并 ${response.merged} 条，现共 ${response.count} 条`);
  } catch (error) {
    toast(error.message, true);
  } finally {
    dom.importFile.value = '';
  }
}

function bindEvents() {
  dom.volSelect.addEventListener('change', () => loadVol(Number(dom.volSelect.value)));
  dom.chapterSelect.addEventListener('change', () => {
    state.chapter = dom.chapterSelect.value;
    state.visible = 80;
    render();
  });
  dom.searchInput.addEventListener('input', () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.search = dom.searchInput.value.trim();
      state.visible = 80;
      render();
    }, 140);
  });
  dom.flagToggle.addEventListener('change', async () => {
    try {
      const response = await api('/api/config', {
        method: 'POST',
        body: { config: { only_flagged: dom.flagToggle.checked } },
      });
      applyConfig(response.config);
      await refreshMetrics();
      await loadVol(state.vol);
    } catch (error) {
      dom.flagToggle.checked = Boolean(state.config && state.config.only_flagged);
      toast(error.message, true);
    }
  });
  dom.loadMore.addEventListener('click', () => {
    const units = filteredUnits();
    const start = state.visible;
    state.visible += 80;
    for (const unit of units.slice(start, state.visible)) {
      const card = buildCard(unit);
      dom.unitList.appendChild(card);
      cardMap.set(unit.key, card);
    }
    dom.loadMore.hidden = units.length <= state.visible;
  });

  dom.openSettings.addEventListener('click', openSettings);
  dom.openScope.addEventListener('click', openScope);
  dom.saveSettings.addEventListener('click', saveSettings);
  dom.saveCustom.addEventListener('click', saveCustom);
  dom.archiveButton.addEventListener('click', archiveSnapshot);
  dom.dockArchive.addEventListener('click', archiveSnapshot);

  dom.scopeAll.addEventListener('click', () => applyScope([]));
  dom.scopeVol.addEventListener('click', () => {
    const keys = scopeVolKeys();
    if (!keys.length) {
      toast('当前卷没有可见单元', true);
      return;
    }
    applyScope(keys);
  });
  dom.scopeChapter.addEventListener('click', () => {
    const keys = scopeChapterKeys();
    if (!keys.length) {
      toast('请先选择章，且当前章没有可见单元', true);
      return;
    }
    applyScope(keys);
  });

  dom.importFile.addEventListener('change', () => importAnswers(dom.importFile.files[0]));

  for (const button of document.querySelectorAll('[data-close]')) {
    button.addEventListener('click', () => button.closest('dialog').close());
  }
  for (const dialog of document.querySelectorAll('dialog')) {
    dialog.addEventListener('click', (event) => {
      if (event.target === dialog) dialog.close();
    });
  }
}

async function init() {
  dom.volSelect = $('#vol-select');
  dom.chapterSelect = $('#chapter-select');
  dom.searchInput = $('#search-input');
  dom.flagToggle = $('#flag-toggle');
  dom.loadMore = $('#load-more');
  dom.unitList = $('#unit-list');
  dom.empty = $('#empty');
  dom.emptyText = $('#empty-text');
  dom.answerStats = $('#answer-stats');
  dom.verdictStats = $('#verdict-stats');
  dom.dailyStats = $('#daily-stats');
  dom.dailyBar = $('#daily-bar');
  dom.meterBar = $('.meter-bar');
  dom.scopeSummary = $('#scope-summary');
  dom.toast = $('#toast');
  dom.openSettings = $('#open-settings');
  dom.openScope = $('#open-scope');
  dom.settingsDialog = $('#settings-dialog');
  dom.scopeDialog = $('#scope-dialog');
  dom.customDialog = $('#custom-dialog');
  dom.customOrigin = $('#custom-origin');
  dom.customTitle = $('#custom-title');
  dom.customNote = $('#custom-note');
  dom.saveCustom = $('#save-custom');
  dom.cfgVolStart = $('#cfg-vol-start');
  dom.cfgVolEnd = $('#cfg-vol-end');
  dom.cfgDailyGoal = $('#cfg-daily-goal');
  dom.cfgTheme = $('#cfg-theme');
  dom.cfgFontSize = $('#cfg-font-size');
  dom.cfgLabelOk = $('#cfg-label-ok');
  dom.cfgLabelReroll = $('#cfg-label-reroll');
  dom.cfgLabelCustom = $('#cfg-label-custom');
  dom.cfgOnlyFlagged = $('#cfg-only-flagged');
  dom.saveSettings = $('#save-settings');
  dom.scopeCurrent = $('#scope-current');
  dom.scopeAll = $('#scope-all');
  dom.scopeVol = $('#scope-vol');
  dom.scopeChapter = $('#scope-chapter');
  dom.archiveButton = $('#settings-archive');
  dom.dockArchive = $('#dock-archive');
  dom.importFile = $('#import-file');

  bindEvents();

  try {
    const [manifest, configResponse, answersResponse] = await Promise.all([
      api('/api/manifest'),
      api('/api/config'),
      api('/api/answers'),
    ]);
    state.manifest = manifest;
    state.scope = configResponse.scope;
    state.answers = answersResponse.answers || {};
    applyConfig(configResponse.config);
    buildVolSelect();
    renderScopeSummary();
    renderMeter();
    await loadVol(initialVol());
  } catch (error) {
    toast(`载入失败：${error.message}`, true);
  }

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').catch(() => {});
    });
  }
}

document.addEventListener('DOMContentLoaded', init);
