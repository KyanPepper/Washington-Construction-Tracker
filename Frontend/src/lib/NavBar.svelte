<script>
  import "../app.css";
</script>

<nav class="bg-gray-800">
  <div
    class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
  >
    <div class="flex flex-shrink-0 items-center">
      <img class="h-8 w-auto" src="\src\lib\Logo.png" alt="WCPLOGO" />
    </div>
    <div class=" flex space-x-4">
      <a
        href="/"
        class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium"
        >Home</a
      >
      <a
        href="/projects"
        class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium"
        >Projects</a
      >
      <a
        href="/map"
        class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium"
        >Map</a
      >
      <a
        href="/about"
        class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium"
        >About</a
      >
    </div>
  </div>
</nav>

<slot />
