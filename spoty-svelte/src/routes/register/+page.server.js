export const actions = {
    default: async ({ request, cookies, fetch }) => {
        const form = await request.formData();
        const username = form.get('username');
        const password = form.get('password');
        const body = {
            "username": username,
            "password": password
        };
        console.log(body);
        fetch(
            "http://127.0.0.1:8000/api/register",
            {
                method: "POST",
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            }
        )
        cookies.set("username", username, { path: "/" });
        cookies.set("password", password, { path: "/" });
    }
}