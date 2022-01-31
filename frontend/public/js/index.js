frontendUrl = "http://localhost:3000"
apiUrl = "http://localhost:5000"
isAuth = false

function displayContent() {
    if (isAuth) {
        window.location.replace(frontendUrl + "/home.html");
    }
    else {
        window.location.replace(frontendUrl + "/login.html");
    }
}

function displayPlots() {
    
}

function register() {
    username = document.getElementById("form3Example1c");
    potId = document.getElementById("form3Example3c");
    pass = document.getElementById("form3Example4c");

    postData = {
        "password": userName,
        "username": pass
    }

    fetch(apiUrl + "/auth/register", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`${reponse.status}`)
            }
            return response.json()
        })
        .then(data => {
            isAuth = true;
        })
        .catch(error => {
            authCard = document.createElement('div');
            authCard.className = 'card';
            authResponse = document.createElement('div');
            authResponse.className = 'card-body';
            authMsg = document.createElement('p');
            authCard.appendChild(authResponse);
            authResponse.appendChild(authMsg);
            authMsg.innerText = "Invalid username or password";
            authMsg.className = 'text-warning';
            form = document.getElementById("signupForm");
            form.appendChild(authCard);

            console.log(error);
        });
}

function login() {
    username = document.getElementById("form3Example3");
    pass = document.getElementById("form3Example4");

    postData = {
        "password": userName,
        "username": pass
    }

    fetch(apiUrl + "/auth/login", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`${reponse.status}`)
            }
            return response.json()
        })
        .then(data => {
            isAuth = true;
        })
        .catch(error => {
            authCard = document.createElement('div');
            authCard.className = 'card';
            authResponse = document.createElement('div');
            authResponse.className = 'card-body';
            authMsg = document.createElement('p');
            authCard.appendChild(authResponse);
            authResponse.appendChild(authMsg);
            authMsg.innerText = "Wrong username or password";
            authMsg.className = 'text-warning';
            form = document.getElementById("loginForm");
            form.appendChild(authCard);

            console.log(error)
        });
}

function logout() {
    fetch(apiUrl + "/auth/login")
        .then(response => {
            if (!response.ok) {
                throw new Error(`${reponse.status}`)
            }
            return response.json()
        })
        .then(data => {
            isAuth = false;
        })
        .catch(error => {
            console.log(error);
        });
}

function forceWater(value) {
    postData = {
        "value": value
    }
}

function setCharacteristics(humidity, temperature) {
    postData = {
        "ideal_humidity": humidity,
        "ideal_temperature": temperature
    }
}

function setHumidity(value) {
    postData = {
        "value": value
    }
}

function setTemperature(degrees) {
    postData = {
        "degrees": degrees
    }
}