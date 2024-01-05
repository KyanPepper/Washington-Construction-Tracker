<script>
     import Projectcard from "$lib/projectcard.svelte";
  
  {
    // @ts-ignore
    import("./+page").PageData;
  }
  export let data;
 // @ts-ignore
 let project = data.project
console.log(project)
</script>