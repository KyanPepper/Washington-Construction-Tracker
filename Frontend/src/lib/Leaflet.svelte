<script>
    import { onMount, onDestroy } from 'svelte';
    import { browser } from '$app/environment';

    /**
   * @type {string | HTMLElement}
   */
    let mapElement;
    /**
   * @type {import("leaflet").Map | import("leaflet").LayerGroup<any>}
   */
    let map;

	
    onMount(async () => {
        if(browser) {
            const leaflet = await import('leaflet');
			//bounds at washinton
           const washingtonBounds = leaflet.latLngBounds(
				leaflet.latLng(44, -125.5),
                leaflet.latLng(49.5, -116.0) 
            );
			map = leaflet.map(mapElement, {
                maxBounds: washingtonBounds, 
                maxBoundsViscosity: 1.0,      
				minZoom:2
            }).setView([47.7511, -120.7401], 7);
            leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            leaflet.marker([47.5, -122.09]).addTo(map)
                .bindPopup('Kyles house.')
                .openPopup();
        }
    });

    onDestroy(async () => {
        if(map) {
            console.log('Unloading Leaflet map.');
            map.remove();
        }
    });
</script>


<main>
    <div bind:this={mapElement}></div>
</main>

<style>
    @import 'leaflet/dist/leaflet.css';
    main div {
        height: 800px;
    }
</style>