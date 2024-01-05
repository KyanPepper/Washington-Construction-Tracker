<script>
     import Projectpage from "$lib/projectpage.svelte";
  {
    // @ts-ignore
    import("./+page").PageData;
  }
  export let data;
 // @ts-ignore
 let project = data.project
console.log(project)
console.log('\n thei')
</script>

<div>
  <Projectpage   price={project[0].price}
  description={project[0].description}
  name={project[0].name}
  img={project[0].img}
  url={project[0].url}
  timeline={project[0].timeline}
  location={project[0].location}
  lon={project[0].lon}
  lat={project[0].lat}
  county={project[0].county}
  id={project[0].id} ></Projectpage>
</div>
