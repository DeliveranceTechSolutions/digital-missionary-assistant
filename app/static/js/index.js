document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-form").addEventListener("submit", (event) => {
        event.preventDefault();

        let usr = document.getElementById("login-username");
        let pwd = document.getElementById("login-password");

        const dest = "http://localhost:8000/login"
        const data = {
            usrn: usr,
            pdrd: pwd
        }

        handleOnSubmit(dest, data)
        .then((response) => {
            console.log(response);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    });
});

async function handleOnSubmit(url, payload) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    return await response.json();
}