export const load = async ({ fetch }) => {
    return {
        trends: [
          {
            title: "Eyes closed",
            author: "Imagine Dragons",
            image: "https://source.unsplash.com/random/200x200?sig=1"
          },
          {
            title: "Eyes closed",
            author: "Imagine Dragons",
            image: "https://source.unsplash.com/random/200x200?sig=1"
          },
          {
            title: "Eyes closed",
            author: "Imagine Dragons",
            image: "https://source.unsplash.com/random/200x200?sig=1"
          },
          {
            title: "Eyes closed",
            author: "Imagine Dragons",
            image: "https://source.unsplash.com/random/200x200?sig=1"
          }
        ],
        albums: [
          {
            title: "Human",
            author: "One Republic",
            image: "https://source.unsplash.com/random/200x200?sig=2"
          },
          {
            title: "Human",
            author: "One Republic",
            image: "https://source.unsplash.com/random/200x200?sig=2"
          },
          {
            title: "Human",
            author: "One Republic",
            image: "https://source.unsplash.com/random/200x200?sig=2"
          },
          {
            title: "Human",
            author: "One Republic",
            image: "https://source.unsplash.com/random/200x200?sig=2"
          }
        ]
    };
    const res = await fetch("http://127.0.0.1:8000/api/trends");
    const data = await res.json();
    return { data }
}