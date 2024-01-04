<script>
  // @ts-nocheck

  import Projectcard from "$lib/projectcard.svelte";
  // @ts-ignore
  {
    import("./+page").PageData;
  }
  export let data;
 let  rProjects = data.randomProjects

</script>

<div class="bg-gradient-to-b from-orange-400 to-yellow-300 py-6">
  <h1 class="text-xl md:text-2xl lg:text-3xl font-bold text-center text-white">
    Washington Construction Projects
  </h1>
  <p
    class="text-sm md:text-base text-center mt-2 font-semibold text-white opacity-75"
  >
    Explore Washington's Latest Developments
  </p>
</div>


  
<div class="flex justify-between pt-4 pb-4 flex-wrap">
  {#each rProjects as project, index (project.id)}
    <Projectcard
      class="w-full sm:w-1/3 bg-white rounded-lg shadow-md p-2 mt-2 project-card"
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
    ></Projectcard>
  {/each}
</div>

  

