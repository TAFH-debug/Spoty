export async function load({ fetch, url }) {
    const id = url.searchParams.get('id');
    const res = await fetch("http://127.0.0.1:8000/api/get_messages", {
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
    return { 
        messages: data,
        post: {
            image: "",
            title: "Demons",
            author: "Imagine Dragons"
        }
    }
}