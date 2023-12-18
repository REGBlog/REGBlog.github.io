importScripts(
    'https://storage.googleapis.com/workbox-cdn/releases/6.4.1/workbox-sw.js'
  );

const { registerRoute } = workbox.routing;
const { precacheAndRoute } = workbox.precaching;

registerRoute(
    /\. (?:css|js)$/,
    new workbox.strategies.StaleWhileRevalidate({
        "cacheName": 'assests',
        plugins: [
            new workbox.expiration.ExpirationPlugin({
                maxEntries: 1000,
                maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
            }),
        ],
    })
);

registerRoute(
    /\.(?:png|jpg|gif)$/,
    new workbox.strategies.CacheFirst({
        "cacheName": 'images',
        plugins: [
            new workbox.expiration.ExpirationPlugin({
                maxEntries: 60, // 60 Files
                maxAgeSeconds: 30 * 24 * 60 *60, // 30 Days
            }),
        ],
    })
);

precacheAndRoute([
    { url: '/index.html', revision: '383676' },
    { url: '/404.html', revision: '383676' },
]);

caches.keys().then(function(names) {
    for (let name of names)
        caches.delete(name);
});


