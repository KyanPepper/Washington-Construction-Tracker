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
  
  