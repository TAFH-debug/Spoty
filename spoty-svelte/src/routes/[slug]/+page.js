export async function load({ params, fetch }) {
    const album = params.slug;
    const post = {
        "title": album,
        "author": "Imagine Dragons",
        "image": "https://source.unsplash.com/random/200x200?sig=1"
    }
    return { post }
}