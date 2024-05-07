<nav class="header">
    <a class="logo" href="/">S p o t y</a>
</nav>

<style>
.header {
    width: 100%;
    background: rgb(29, 29, 29);
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.header * {
    padding: 10px;
    margin: 10px;
}

.logo {
    font-weight: bolder;
    font-family: 'Arial', sans-serif;
    font-size: 40px;
    color: white;

    background-size: 200% 100%;
    transition: background-position 1s ease-in;
    
}

.logo:hover {
    transform: none;
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