apiUrl = "http://localhost:5000"

async function callRegister(username, password) {
    const postData = {
        "password": password,
        "username": username
    }

    const response = await fetch(apiUrl + "/auth/register", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}

async function callLogin(username, password) {
    const postData = {
        "password": password,
        "username": username
    }

    const response = await fetch(apiUrl + "/auth/login", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    console.log(response);

    return response.ok;
}

async function callLogout() {
    const response = await fetch(apiUrl + "/auth/logout");
    return response.ok;
}

async function callSetCharacteristic(humidity, tempereture) {
    const postData = {
        "ideal_humidity": humidity,
        "ideal_temperature": tempereture
    }

    const response = await fetch(apiUrl + "/characteristics/set", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}

async function callSetHumidity(value) {
    const postData = {
        "value": value,
    }

    const response = await fetch(apiUrl + "/humidity/set", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}

async function callSetTemperature(degrees) {
    const postData = {
        "degrees": degrees,
    }

    const response = await fetch(apiUrl + "/temperature/set", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}

async function callForceWater(value) {
    const postData = {
        "value": value,
    }

    const response = await fetch(apiUrl + "/tforce_water", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}

async function callPlots() {
    const response1 = await fetch(apiUrl + "/plot");
    const response2 = await fetch(apiUrl + "/plot_humidity");
    const response3 = await fetch(apiUrl + "/plot_temperature");

    if (!response1.ok || !response2.ok || !response3.ok) 
        return null;

    return {
        "quantities": response1.json(),
        "humidity": response2.json(),
        "temperature": response3.json()
    }
}