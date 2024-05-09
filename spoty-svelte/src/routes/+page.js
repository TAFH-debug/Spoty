export const load = async ({ fetch }) => {
    const res = await fetch("http://127.0.0.1:8000/api/trends");
    const data = await res.json();
    return data;
}