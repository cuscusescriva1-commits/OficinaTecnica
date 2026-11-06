const VERSION = 'oficina-tecnica-v3.0';
const FILES = ['./', './index.html', './manifest.webmanifest', './icon-180.png', './icon-192.png', './icon-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET' || !r.url.startsWith(self.location.origin)) return;
  e.respondWith(fetch(r).then(res => {
    const copy = res.clone();
    if (res.ok) caches.open(VERSION).then(c => c.put(r, copy));
    return res;
  }).catch(() => caches.match(r).then(m => m || caches.match('./index.html'))));
});
