<script lang="ts">
  import '../app.css';
  const id: string = '4';
  const img: string = 'src/lib/Logo.png';
  const price: string = '40 Billion - 50 Billion';
  const description: string = 'this is the project of the ...';
  const name: string = 'Worm project';
  const timeline: string = '2089 - 2024';
  const county: string = 'Snohomish County'
</script>


<div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
  <a href="/id">
      <img class="rounded-t-lg" src="{img}"  />
  </a>
  <div class="p-5">
      <a href="#">
          <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{name}</h5>
      </a>
      <h6 class="mb-2 font-normal text-gray-700 dark:text-gray-400">{county}</h6>
      <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Estimated Cost: {price}</p>
      <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Timeline: {timeline}</p>
  </div>
</div>
