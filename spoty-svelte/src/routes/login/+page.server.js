export const actions = {
    default: async ({ request, cookies }) => {
        const form = await request.formData();
        const username = form.get('username');
        const password = form.get('password');
        cookies.set("username", username, { path: "/" });
        cookies.set("password", password, { path: "/" });
    }
}