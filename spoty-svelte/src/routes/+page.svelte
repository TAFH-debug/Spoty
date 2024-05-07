<script>
  import Header from "./components/header.svelte";
  import NewAlbums from "./components/new_albums.svelte";
  import Trends from "./components/trends.svelte";
  export let data;
</script>
<Header />
<Trends data={data}/>
<NewAlbums data={data}/>
