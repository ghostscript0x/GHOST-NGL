// Basic service worker for PWA
self.addEventListener('install', () => {
  console.log('Service worker installing...');
});

self.addEventListener('activate', () => {
  console.log('Service worker activating...');
});

self.addEventListener('fetch', (event) => {
  // Cache static assets if needed, but for now, just pass through
  event.respondWith(fetch(event.request));
});

