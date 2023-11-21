document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-form").addEventListener("submit", (event) => {
        event.preventDefault();

        let usr = document.getElementById("login-username").value;
        let pwd = document.getElementById("login-password").value;

        const dest = "http://localhost:8000/api/login"
        const data = {
            usrn: usr,
            pdrd: pwd,
        }
        console.log(JSON.stringify(data))
        handleOnSubmit(dest, JSON.stringify(data))
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