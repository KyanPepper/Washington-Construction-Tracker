<script>
    import NavBar from "$lib/NavBar.svelte";
    import '../app.css';
    import Page from "./+page.svelte";
    </script>
  <header>
  <NavBar>
    </NavBar>
  </header>

  <slot></slot>



<style global lang="postcss">
	:global(body) {
		background-color:  #f2f2f2;
	}
</style>