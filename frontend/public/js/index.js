authUser = false;
url = "http://localhost:3000"

function displayContent() {
    if (authUser) {
        window.location.replace(url + "/home.html");
    }
    else {
        window.location.replace(url + "/login.html");
    }
}