<script>
// @ts-nocheck

  import Projectcard from "$lib/projectcard.svelte";
  import { onMount } from "svelte";

  export let data;
  let rProjects = data.randomProjects;
  let selectedCounty = "All"; 

  const filterProjects = () => {
    if (selectedCounty === "All") {
      rProjects = data.randomProjects;
    } else {
      rProjects = data.randomProjects.filter((/** @type {{ county: string; }} */ project) => project.county === selectedCounty);
    }
  };

  const handleCountyChange = (/** @type {string} */ county) => {
    selectedCounty = county;
    filterProjects();
  };

 
  onMount(() => {
    filterProjects();
  });
</script>

<nav class="bg-white shadow-md flex justify-center items-center p-4 mx-auto max-w-screen-lg font-sans">
  <div class="flex items-center space-x-6">
    <a on:click={() => handleCountyChange("King")} class="text-black hover:text-blue-500 transition duration-300 ease-in-out">King County</a>
    <a on:click={() => handleCountyChange("Snohomish")} class="text-black hover:text-blue-500 transition duration-300 ease-in-out">Snohomish County</a>
    <a on:click={() => handleCountyChange("Spokane")} class="text-black hover:text-blue-500 transition duration-300 ease-in-out">Spokane County</a>
    <a on:click={() => handleCountyChange("Other")} class="text-black hover:text-blue-500 transition duration-300 ease-in-out">Other</a>
    <a on:click={() => handleCountyChange("All")} class="text-black hover:text-blue-500 transition duration-300 ease-in-out">All</a>
  </div>
</nav>

<div class="mx-auto max-w-screen-lg w-full">
  <div class="grid gap-4 sm:grid-cols-2 md:grid-cols-3 justify-center pt-4 pb-4">
    {#each rProjects as project, index (project.id)}
      <Projectcard
        class="bg-white rounded-lg shadow-md p-2 mb-2 mt-2"
        price={project.price}
        description={project.description}
        name={project.name}
        img={project.img}
        url={project.url}
        timeline={project.timeline}
        location={project.location}
        lon={project.lon}
        lat={project.lat}
        county={project.county}
        id={project.id}
      ></Projectcard>
    {/each}
  </div>
</div>
