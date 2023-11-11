<script>
    import NavBar from "$lib/NavBar.svelte";
    import '../app.css';
    import Page from "./+page.svelte";
    </script>
  <header>
  <NavBar>
    </NavBar>
  </header>
<div>
  <slot></slot>
</div>


<style global lang="postcss">
	:global(body) {
		background-color:  #E5E5E5;
	}
</style>