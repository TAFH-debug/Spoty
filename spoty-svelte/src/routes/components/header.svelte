<nav class="header">
    <img class="logo" src="src/lib/images/logo.svg" alt=""/>
    <a class="name" href="/">Spoty</a>
    <a href="/login">Login</a>
    <a href="/register">Register</a>
    <input class="search"/>
</nav>

<style>
.header {
    width: 100%;
    background: rgb(16, 16, 16);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.header * {
    padding: 10px;
    margin: 10px;
}

.logo {
    width: 80px;
    height: 80px;
    float: left;
}

.search {
    margin: 10px 20px;
    background-color: rgb(37, 37, 37);
    border: none;
    outline: none;
    font-size: 20px;
    color: white;
    border-radius: 10px;
    width: 30%;
}

.name {
    font-weight: bolder;
    font-family: 'Arial', sans-serif;
    font-size: 40px;
    color: white;
    letter-spacing: 10px;
    background-size: 200% 100%;
    transition: all 0.5s ease-in-out;
}

.name:hover {
    transform: none;
    letter-spacing: 20px;
}

a {
    text-decoration: none;
    outline: none;
    color: white;
    font-family: 'Arial', Courier, monospace;
    font-size: 1.7vw;
    transition: all 0.25s ease-in-out;
}

a:hover {
    transform: translate(10%);
}
</style>