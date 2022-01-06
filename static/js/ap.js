self.addEventListener('install',event =>{
    console.log('Install event');
    event.waitUntil(
        caches.open(cacheName)
        .then(caches => {
            return caches.addAll(resourcesToPrecache);
        })
    );
});