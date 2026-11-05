/* 3B 标题审定 · Service Worker（shell 预缓存；数据接口网络优先） */
'use strict';

const CACHE_NAME = '3b-review-v7-20261106';
let apiOfflineUntil = 0;
const SHELL = [
  './',
  './index.html',
  './app.css',
  './app.js',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './fonts/LXGWWenKaiScreen-subset.woff2',
  './fonts/OFL.txt',
  './api/manifest',
  './api/config',
  './api/scope'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      Promise.all(
        SHELL.map((url) =>
          cache.add(new Request(url, { cache: 'reload' })).catch(() => null)
        )
      )
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  let url;
  try {
    url = new URL(req.url);
  } catch (e) {
    return;
  }
  if (url.origin !== self.location.origin) return;

  const isApi = url.pathname.indexOf('/api/') !== -1;

  if (isApi) {
    const isAnswers = url.pathname.indexOf('/api/answers') !== -1;
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      const cached = await cache.match(req);
      // 刚失败过：30 s 内直接走缓存，避免 75 卷逐卷空等
      if (Date.now() < apiOfflineUntil) {
        if (cached) return cached;
        throw new Error('offline');
      }
      if (!cached) {
        const fresh = await fetch(req);
        cache.put(req, fresh.clone()).catch(() => {});
        return fresh;
      }
      if (isAnswers) {
        // 答案：网络优先（1.2 s 上限），失败回缓存，避免断网时长时间空等
        try {
          const fresh = await Promise.race([
            fetch(req),
            new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 1200))
          ]);
          cache.put(req, fresh.clone()).catch(() => {});
          return fresh;
        } catch (e) {
          apiOfflineUntil = Date.now() + 30000;
          return cached;
        }
      }
      // 参数可能随作用域变化：网络优先（1.2 s 上限），失败回缓存
      try {
        const fresh = await Promise.race([
          fetch(req),
          new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 1200))
        ]);
        cache.put(req, fresh.clone()).catch(() => {});
        return fresh;
      } catch (e) {
        apiOfflineUntil = Date.now() + 30000;
        return cached;
      }
    })());
    return;
  }

  event.respondWith(
    caches.match(req).then((hit) => {
      if (hit) return hit;
      return fetch(req)
        .then((res) => {
          if (res && res.status === 200 && res.type === 'basic') {
            const copy = res.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, copy)).catch(() => {});
          }
          return res;
        })
        .catch(() =>
          req.mode === 'navigate' ? caches.match('./index.html') : Promise.reject(new Error('offline'))
        );
    })
  );
});
