const cacheName = 'cache-v1';
const resourcesToPrecache = [
'/',
'index.html',
'pred.html'
];

self.addEventListener('install',event =>{
    console.log('Install event');
    event.waitUntil(
        caches.open(cacheName)
        .then(caches => {
            return caches.addAll(resourcesToPrecache);
        })
    );
});

self.addEventListener('activate',event =>{
    console.log('activate event!');
});

self.addEventListener('fetch',event=>{
    event.respondWith(caches.match(event.request)
    .then(cachedResponse =>{
        return cachedResponse || fetch(event.request)
    })
    );
});