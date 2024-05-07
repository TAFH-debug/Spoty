<script>
  import Header from "./components/header.svelte";
  export let data;
</script>
<Header />

<div class="trends_container">
  {@html data.data.message}
</div>