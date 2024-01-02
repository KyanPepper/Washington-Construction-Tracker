<script lang="ts">
    import '../app.css';
    const id: string = '4';
    const img: string = 'src/lib/Logo.png';
    const price: string = '40 Billion - 50 Billion';
    const description: string = 'this is the project of the blah blah blah blah blah blah blah blah blah blah ';
    const name: string = 'Worm project';
    const timeline: string = '2089 - 2024';
    const url: string = 'github.com/kyanpepper'
    const lat: GLfloat = 120
    const lon: GLfloat = -88
    const county: string = 'Snohomish County'
  </script>
  
<div class="mx-auto max-w-7xl px-4 pb-4 pt-10 sm:px-6 lg:flex lg:items-start lg:justify-center lg:gap-x-8 lg:px-0 lg:pb-4 lg:pt-16">
    <!-- Image Section -->
    <div class="lg:w-2/5 lg:pr-6">
        <div class="aspect-h-2 aspect-w-3 overflow-hidden rounded-lg">
            <img src="{img}"  class="h-full w-full object-cover object-center">
        </div>
    </div>

    <!-- Quick Information Section -->
    <div class="lg:w-3/5 lg:pl-6 lg:text-lg">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">{name}</h1>
        <p class="text-4xl tracking-tight text-gray-900">Area: {county}</p>
        <p class="text-4xl tracking-tight text-gray-900">Timeline: {timeline}</p>
        <p class="text-4xl tracking-tight text-gray-900">Estimated Cost: {price}</p>

        <!-- See on map -->
     
        <button class="mt-8 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-4 text-lg font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">View On Map</button>
    </div>
</div>

<div class="max-w-7xl">
    <div class="text-2xl font-bold mb-4 text-gray-900">Details</div>
    <div class="text-gray-700">
        <p class="mb-4">{description}</p>
        <p>See Full Documentation - {url}</p>
    </div>
</div>
