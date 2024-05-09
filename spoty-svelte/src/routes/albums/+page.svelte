<script>
  import Header from "../components/header.svelte";
  export let data;
  
  function send() {
    var inp = document.getElementById("content");
    var inp2 = document.getElementById("score");
    const content = inp.value;
    const score = inp2.value;
    const urlParams = new URLSearchParams(window.location.search);
    const album_id = urlParams.get('id');

    const arr = document.cookie.split(";");
    let cookies = {};
    for (let i = 0; i < arr.length; i++) {
        let a = arr[i].split("=")[0];
        let b = arr[i].split("=")[1];
        cookies[a.trim()] = b;
    }

    const body = JSON.stringify({
            album_id: parseInt(album_id),
            content: content,
            username: data.username,
            password: data.password,
            score: parseInt(score)
    });

    fetch("http://127.0.0.1:8000/api/create_review/", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: body
    })
  }
</script>
<Header />

<div class="container">
    <img src={data.album.image} class="image" alt=""/>
    <div>
      <div class="title">{data.album.title}</div>
      <div class="author">{data.album.author}</div>
    </div>
</div>

<div class="send_title">Send your review on this song!</div>
<div class="send">
  <input class="send_content" type="text" id="content"/>
  <input class="send_score" type="number" id="score" min="1" max="10"/>
  <button on:click={send}>Send</button>
</div>

<div class="reviews_title">Other reviews</div>
<div class="reviews_container">
  {#each data.reviews as review}
  <div class="review" style={"border-color: rgb(" + ((10 - review.score) * 255  / 10) + ", " + ((review.score) * 255 / 10) + ", 0)"}>
    <div>
      <div class="review_title">{review.username}</div>
      <div class="review_content">{review.content}</div>
    </div>
    <div class="review_score">Score: {review.score}/10</div> 
  </div>
  {/each}
</div>


<style>
  .reviews_title {
    text-align: center;
    background-color: black;
    color: white;
    font-size: 30px;
  }

  .reviews_container {
    width: 100%;
    background-color: black;
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
  }

  .send * {
    padding: 20px;
    margin: 20px;
  }

  .send_title {
    text-align: center;
    background-color: black;
    color: white;  
  }

  .send {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: column;
    background-color: black;
    color: white;
  }

  .send_content {
    background-color: rgb(28, 28, 28);
    color: white;
    outline: none;
    text-decoration: none;
    border: none;
    border-radius: 10px;
    font-size: 20px;
  }

  .send_score {
    background-color: black;
    color: white;
    outline: none;
    text-decoration: none;
    border: none;
    font-size: 20px; 
  }

  .send button {
    background-color: rgb(28, 28, 28);
    color: white;
    border: none;
    border-radius: 10px;
  }

  .send button:hover {
    background-color: rgb(44, 44, 44);
    cursor: pointer;
  }

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

  .review {
    margin: 10px;
    border-style: solid;
    border-radius: 10px;
    width: 50%;
    background-color: black;
    padding: 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .review_title {
    color: white;
    font-weight: bolder;
    font-size: 30px;
  }

  .review_content {
    color: white;
    font-size: 20px;
  }

  .review_score {
    color: white;
    font-size: 20px;
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
