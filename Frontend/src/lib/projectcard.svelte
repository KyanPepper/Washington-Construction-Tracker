<script lang="ts">
  import '../app.css';
  const url: string = '';
  const img: string = 'src/lib/Logo.png';
  const price: string = '40 Billion - 50 Billion';
  const description: string = 'this is the project of the ...';
  const name: string = 'Worm project';
  const timeline: string = '2089 - 2024';
</script>


<div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
  <a href="{url}">
      <img class="rounded-t-lg" src="{img}"  />
  </a>
  <div class="p-5">
      <a href="#">
          <h6 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{name}</h6>
      </a>
      <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{description}</p>
      <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{price}</p>
      <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{timeline}</p>
  </div>
</div>
