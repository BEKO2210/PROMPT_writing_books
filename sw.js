// Service Worker – Prompt Engineering Meistern PWA
const CACHE_NAME = 'pe-meistern-v2.1.0';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon.svg',
  './icon-192.png',
  './icon-512.png',
  './band-01/index.html',
  './band-02/index.html',
  './band-03/index.html',
  './band-04/index.html',
  './band-05/index.html',
  './band-06/index.html',
  './band-07/index.html',
  './band-08/index.html',
  './band-09/index.html',
  './band-10/index.html',
  './band-bonus/index.html',
  './version.json'
];

// Install: cache all core assets
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(ASSETS);
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(names) {
      return Promise.all(
        names.filter(function(n) { return n !== CACHE_NAME; })
             .map(function(n) { return caches.delete(n); })
      );
    })
  );
  self.clients.claim();
});

// Fetch: network first, fallback to cache
self.addEventListener('fetch', function(e) {
  // Skip non-GET and cross-origin
  if (e.request.method !== 'GET') return;
  if (!e.request.url.startsWith(self.location.origin)) return;

  e.respondWith(
    fetch(e.request).then(function(response) {
      // Cache successful responses
      if (response.ok) {
        var clone = response.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(e.request, clone);
        });
      }
      return response;
    }).catch(function() {
      return caches.match(e.request);
    })
  );
});

// Listen for version check messages
self.addEventListener('message', function(e) {
  if (e.data && e.data.type === 'CHECK_VERSION') {
    fetch('./version.json?t=' + Date.now())
      .then(function(r) { return r.json(); })
      .then(function(data) {
        self.clients.matchAll().then(function(clients) {
          clients.forEach(function(client) {
            client.postMessage({ type: 'VERSION_INFO', payload: data });
          });
        });
      })
      .catch(function() {});
  }
});
