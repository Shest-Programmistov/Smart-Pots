function constructErrorCard(msg) {
    errorCard = document.createElement('div');
    errorCard.className = 'card';
    errorCard.id = 'error-card';
    authResponse = document.createElement('div');
    authResponse.className = 'card-body';
    authMsg = document.createElement('p');
    errorCard.appendChild(authResponse);
    authResponse.appendChild(authMsg);
    authMsg.innerText = msg;
    authMsg.className = 'text-warning';
    return errorCard;
}

async function register() {
    username = document.getElementById("form3Example1c").value;
    pass = document.getElementById("form3Example4c").value;

    ok = await callRegister(username, pass);
    errorCard = document.getElementById("error-card");

    if (ok) {
        if (errorCard !== null)
            errorCard.parentNode.removeChild(errorCard);
        window.location.replace(apiUrl);
    }
    else {
        if (errorCard === null) {
            errorCard = constructErrorCard("Invalid username or password");
            form = document.getElementById("signupForm");
            form.appendChild(errorCard);
        }
    }
}

async function login() {
    username = document.getElementById("form3Example3").value;
    pass = document.getElementById("form3Example4").value;

    ok = await callLogin(username, pass);
    errorCard = document.getElementById("error-card");

    if (ok) {
        if (errorCard !== null)
            errorCard.parentNode.removeChild(errorCard);
        window.location.replace(apiUrl);
    }
    else {
        if (errorCard === null) {
            errorCard = constructErrorCard("Wrong username or password");
            form = document.getElementById("loginForm");
            form.appendChild(errorCard);
        }
    }
}

async function logout() {
    await fetch("/auth/logout");
    window.location.replace(apiUrl + '/login');
}

async function forceWater() {
    waterAmount = (document.getElementById("water").value);
    ok = callForceWater(Number(waterAmount));
    if (ok && waterAmount != '')
        alert("Force water was successfull");
    else
        alert("Can't force water - invalid fields");
}

async function setCharacteristics() {
    idealHum = (document.getElementById('idealHumidity').value);
    idealTemp = (document.getElementById('idealTemp').value);

    ok = callSetCharacteristic(Number(idealHum), Number(idealTemp));
    if (ok && idealHum != '' && idealTemp != '')
        alert("Set characteristics successfully");
    else
        alert("Can't set characteristics - invalid fields");
}

async function setHumidity() {
    humidity = (document.getElementById('humidity').value);

    ok = callSetHumidity(Number(humidity));
    if (ok && humidity != '')
        alert("Set humidity successfully");
    else
        alert("Can't set humidity - invalid fields");

    console.log(ok);
    console.log(humidity);
}

async function setTemperature() {
    tempereture = (document.getElementById('temp').value);

    ok = callSetTemperature(Number(tempereture));
    if (ok && tempereture != '')
        alert("Set temperature successfully");
    else
        alert("Can't set temperature - invalid fields");
}