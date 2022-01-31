
function displayPlots() {
    
}

async function register() {
    username = document.getElementById("form3Example1c");
    pass = document.getElementById("form3Example4c");

    const ok = await callRegister(username, pass);
    authCard = document.getElementById("error-card");

    if (ok) {
        if (authCard !== null)
            authCard.parentNode.removeChild(authCard);
        window.location.replace(apiUrl);
    }
    else {
        if (authCard === null) {
            authCard = document.createElement('div');
            authCard.className = 'card';
            authCard.id = 'error-card';
            authResponse = document.createElement('div');
            authResponse.className = 'card-body';
            authMsg = document.createElement('p');
            authCard.appendChild(authResponse);
            authResponse.appendChild(authMsg);
            authMsg.innerText = "Invalid username or password";
            authMsg.className = 'text-warning';
            form = document.getElementById("signupForm");
            form.appendChild(authCard);
        }
    }
}

async function login() {
    username = document.getElementById("form3Example3");
    pass = document.getElementById("form3Example4");

    const ok = await callLogin(username, pass);
    authCard = document.getElementById("error-card");

    if (ok) {
        if (authCard !== null)
            authCard.parentNode.removeChild(authCard);
        window.location.replace(apiUrl);
    }
    else {
        if (authCard === null) {
            authCard = document.createElement('div');
            authCard.className = 'card';
            authCard.id = 'error-card';
            authResponse = document.createElement('div');
            authResponse.className = 'card-body';
            authMsg = document.createElement('p');
            authCard.appendChild(authResponse);
            authResponse.appendChild(authMsg);
            authMsg.innerText = "Wrong username or password";
            authMsg.className = 'text-warning';
            form = document.getElementById("loginForm");
            form.appendChild(authCard);
        }
    }
}

async function logout() {
    callLogout();
    window.location.replace(apiUrl);
}

async function forceWater(value) {
    
}

async function setCharacteristics(humidity, temperature) {
   
}

async function setHumidity(value) {
    
}

async function setTemperature(degrees) {
    
}