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

  function truncateText(text: string): string {
    const words = text.split(' ');
    if (words.length > 5) {
      return words.slice(0, 5).join(' ') + '...';
    }
    return text;
  }
</script>

<div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700" style="height: 450px;">
  <img class="rounded-t-lg h-48 w-full object-cover" src={img} alt={name} />

  <div class="p-5 h-full flex flex-col justify-between">
    <div>
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{name}</h5>
      <h6 class="mb-2 font-normal text-gray-700 dark:text-gray-400">{county}</h6>
      <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Estimated Cost: {truncateText(price)}</p>
      <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Timeline: {truncateText(timeline)}</p>
    </div>
    
    <a href="#" class="inline-flex items-center justify-center w-full px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mt-2">
      Project Overview
    </a>
  </div>
</div>


