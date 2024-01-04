<script lang="ts">
  import "../app.css";
  export let id: number;
  export let lat: number;
  export let lon: number;
  export let img: string;
  export let price: string;
  export let description: string;
  export let name: string;
  export let timeline: string;
  export let county: string;
</script>

<div
  class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
>
 
    <img class="rounded-t-lg" src={img} />
 
  <div class="p-5">
    
      <h5
        class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
      >
        {name}
      </h5>
    
    <h6 class="mb-2 font-normal text-gray-700 dark:text-gray-400">{county}</h6>
    <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">
      Estimated Cost: {price}
    </p>
    <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">
      Timeline: {timeline}
    </p>
    <a
      href=""
      class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      Project Overview
    </a>
  </div>
</div>
