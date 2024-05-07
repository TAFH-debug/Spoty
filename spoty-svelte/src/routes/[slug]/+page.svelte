<script>
  import Header from "../components/header.svelte";
  export let data;
</script>
<Header />

<div class="container">
    <img src={data.post.image} class="image" alt=""/>
    <div>
      <div class="title">{data.post.title}</div>
      <div class="author">{data.post.author}</div>
    </div>
</div>

<style>
  .container {
    background-color: black;
    display: flex;
    justify-content: row;
    align-items: center;

  }

  .image {
    margin: 40px 20px 40px 40px;
    border-radius: 5px;
    width: 20%;
    aspect-ratio: 1;
  }

  .author {
    margin: 10px 20px;
    font-size: 20px;
    color: rgb(135, 135, 135);
  }

  .title {
    margin: 10px 20px;
    font-weight: bolder;
    font-size: 70px;
    color: white;
  }
</style>
