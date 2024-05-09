<script>
  import Header from "../components/header.svelte";
  export let data;
</script>

<Header />

<div class="container">
    <form class="form" action="/register" method="POST">
        <label for="username">Username</label>
        <input id="username" name="username"/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password"/>
        <button>Send</button>
    </form>
</div>

<style>
    .container {
        display: flex;
        background-color: black;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }

    .form {
        background-color: rgb(18, 18, 18);
        color: white;
        padding: 20px;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .form input {
        background-color: rgb(28, 28, 28);
        color: white;
        outline: none;
        text-decoration: none;
        border: none;
        border-radius: 10px;
        font-size: 20px;
        margin: 10px;
        padding: 10px;
    }

    .form label {
        color: white;
    }

    .form button {
        background-color: rgb(28, 28, 28);
        color: white;
        border: none;
        border-radius: 10px;
        margin: 20px;
        padding: 20px;
    }
    
    .form button:hover {
        background-color: rgb(44, 44, 44);
        cursor: pointer;
    }
</style>