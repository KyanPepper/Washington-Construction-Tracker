<script>
  import Projectpage from "$lib/projectpage.svelte";
  {
    // @ts-ignore
    import("./+page").PageData;
  }
  export let data;
  // @ts-ignore
  let project = data.project;
</script>

<div>
  <Projectpage
    price={project[0].price}
    description={project[0].description}
    name={project[0].name}
    img={project[0].img}
    url={project[0].url}
    timeline={project[0].timeline}
    location={project[0].location}
    county={project[0].county}
  ></Projectpage>
</div>
