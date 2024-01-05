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

  // Function to truncate text to first 5 words followed by '...'
  function truncateText(text: string): string {
    const words = text.split(' ');
    if (words.length > 5) {
      return words.slice(0, 5).join(' ') + '...';
    }
    return text;
  }
  function nullCounty(text: string | null): string {
  if (text === null || text.toLowerCase().includes('null')) {
    return '';
  }
  return text as string;
}

</script>
<div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 flex flex-col w-full">
  <div class="h-48 overflow-hidden rounded-t-lg">
    <img class="h-full w-full object-cover" src={img} alt={name} />
  </div>

  <div class="flex-grow p-5 flex flex-col justify-between">
    <div class="flex flex-col h-full">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{name}</h5>
      <h6 class="mb-2 font-normal text-gray-700 dark:text-gray-400">{nullCounty(county)}</h6>
      <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Estimated Cost: {truncateText(price)}</p>
      <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Timeline: {truncateText(timeline)}</p>
      <div class="flex-grow"></div> 
    </div>
    
    <a href={`projectpage/${id}`} class="px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
      Project Overview
    </a>
  </div>
</div>
