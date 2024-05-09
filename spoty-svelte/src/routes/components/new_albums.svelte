<script>
    export let data;
</script>

<div class="albums_container">
	{#each data.albums as album}
    <div class="album" on:click={window.location.href = "/albums?id=" + album.id}>
      <img src={album.image} alt="">
      <div>
        <div class="title">{album.title}</div>
        <div class="author">{album.author}</div>
      </div>
    </div>
	{/each}
</div>

<style>
  * {
    margin: 0;
    padding: 0;
  }

  .albums_container {
    background-color: black;
    width: 100%;
    display: flex;
    height: 100%;
    flex-wrap: wrap;
  }

  .album {
    border-radius: 10px;
    width: 25%;
    height: 150px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin: 20px;
    padding: 20px;
    transition: all 0.3s;
  }

  .album:hover {
    cursor: pointer;
    background-color: rgb(17, 17, 17);
  }

  .album * {
    margin: 5px;
  }

  .album img {
    border-radius: 5px;
    width: 30%;
    aspect-ratio: 1;
  }

  .album .author {
    color: rgb(135, 135, 135);
  }

  .album .title {
    color: white;
  }

</style>