<script>
    export let data;
</script>


<div class="trends_container">
  <div class="trends_title">
    Current trends and new albums
  </div>
	{#each data.trends as trend}
    <div class="trend" on:click={window.location.href = "/albums?id=" + trend.id}>
      <img src={trend.image} alt="">
      <div class="title">{trend.title}</div>
      <div class="author">{trend.author}</div>
    </div>
	{/each}
</div>

<style>
    * {
      margin: 0;
      padding: 0;
    }

    .trends_title {
      background-color: black;
      width: 100%;
      color: white;
      padding: 50px 50px 0 50px;
      text-align: center;

      font-family: CircularSpTitle, sans-serif;
      font-weight: bold;
      font-size: 30px;
    }

    .trends_container {
      background-color: black;
      width: 100%;
      display: flex;
      height: 100%;
      flex-wrap: wrap;
      justify-content: center;
    }
  
    .trend {
      /* background-color: rgb(58, 58, 58); */
      border-radius: 10px;
      width: 17%;
      height: 300px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 20px;
      padding: 20px;
      transition: all 0.3s;
    }
  
    .trend:hover {
      cursor: pointer;
      background-color: rgb(17, 17, 17);
    }
  
    .trend * {
      margin: 5px;
    }
  
    .trend img {
      border-radius: 5px;
      width: 80%;
      aspect-ratio: 1;
    }
  
    .trend .author {
      color: rgb(135, 135, 135);
    }
  
    .trend .title {
      color: white;
    }
  
  </style>