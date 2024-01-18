<script>
  // @ts-nocheck

  import { onMount, onDestroy } from "svelte";
  import { browser } from "$app/environment";

  /**
   * @type {string | HTMLElement}
   */
  let mapElement;
  /**
   * @type {import("leaflet").Map | import("leaflet").LayerGroup<any>}
   */
  let mapProjects;
  let map;

  onMount(async () => {
    if (browser) {
      try {
        const response = await fetch("http://127.0.0.1:5000/getmap");
        if (!response.ok) {
          throw new Error(`Failed to fetch data: ${response.status}`);
        }
        mapProjects = await response.json();
        console.log(mapProjects);
      } catch (error) {
        console.error("Error fetching map projects:", error);
      }

      // @ts-ignore
      const leaflet = await import("leaflet");
      //bounds at washinton
      const washingtonBounds = leaflet.latLngBounds(
        leaflet.latLng(44, -125.5),
        leaflet.latLng(49.5, -116.0)
      );
      map = leaflet
        .map(mapElement, {
          maxBounds: washingtonBounds,
          maxBoundsViscosity: 1.0,
          minZoom: 2,
        })
        .setView([47.7511, -120.7401], 7);
      leaflet
        .tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution:
            '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        })
        .addTo(map);

      for (let i = 0; i < mapProjects.length; i++) {
        leaflet.marker([mapProjects[i].lat, mapProjects[i].lon]).addTo(map)
          .bindPopup(`<div>
            <a href="projectpage/${mapProjects[i].id}">
            <h3>${mapProjects[i].name}</h3>
            <img src="${mapProjects[i].img}" style="width: 100%; height: auto;">
            </a>
          </div>`);
      }
    }
  });

  onDestroy(async () => {
    if (map) {
      console.log("Unloading Leaflet map.");
      map.remove();
    }
  });
</script>

<main>
  <div bind:this={mapElement}></div>
</main>

<style>
  @import "leaflet/dist/leaflet.css";
  main div {
    height: 800px;
  }
</style>
