<script lang="ts">
    import '../app.css';
  export let img: string;
  export let price: string;
  export let description: string;
  export let name: string;
  export let timeline: string;
  export let county: string;
  export let url : string;
  export let location:string;
  function nullValue(text: string | null): string {
  if (text === null || text.toLowerCase().includes('null')) {
    return '';
  }
  return text as string;
}
  </script>
  
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:flex lg:items-start lg:gap-x-8 lg:px-0 lg:pb-4 lg:pt-16">
    <!-- Image Section -->
    <div class="lg:w-2/5 lg:pr-6 lg:pl-2">
        <div class="h-72 lg:h-50 overflow-hidden rounded-lg">
            <img src="{img}" alt="{name}" class="w-full h-full object-cover object-center">
        </div>
    </div>

    <!-- Quick Information Section -->
    <div class="lg:w-3/5 lg:pl-6 lg:pr-2">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">{name}</h1>
        <p class="text-xl lg:text-2xl tracking-tight text-gray-900">{nullValue(county)}</p>
        <p class="text-xl lg:text-2xl tracking-tight text-gray-900">{nullValue(location)}</p>
        <p class="text-xl lg:text-2xl tracking-tight text-gray-900">Timeline: {timeline}</p>
        <p class="text-xl lg:text-2xl tracking-tight text-gray-900">Estimated Cost: {price}</p>

        <!-- See on map -->
        <a href="{url}">
        <button class="mt-2 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-4 text-lg font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">View Documentation</button>
      </a>
    </div>
</div>

<div class="max-w-7xl mx-auto px-4">
    <div class="text-2xl font-bold text-gray-900">Details</div>
    <div class="text-gray-700">
        <p class="mb-4">{description}</p>
    </div>
</div>

