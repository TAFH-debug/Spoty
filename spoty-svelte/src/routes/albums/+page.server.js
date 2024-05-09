export async function load({ url, fetch, cookies }) {
    const id = url.searchParams.get('id');
    const res = await fetch("http://127.0.0.1:8000/api/get_reviews", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            album_id: parseInt(id)
        })
    });


    const data = await res.json();

    const username = cookies.get("username");
    const password = cookies.get("password");
    return {
        reviews: data.reviews,
        album: data.album,
        username,
        password
    };
}