apiUrl = "http://127.0.0.1:5000"

async function callRegister(username, password) {
    const postData = {
        "password": password,
        "username": username
    }

    const response = await fetch("/auth/register", {
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

    const response = await fetch("/auth/login", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}

async function callSetCharacteristic(humidity, tempereture) {
    const postData = {
        "ideal_humidity": humidity,
        "ideal_temperature": tempereture
    }

    const response = await fetch("/characteristics/set", {
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

    const response = await fetch("/humidity/set", {
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

    const response = await fetch("/temperature/set", {
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

    const response = await fetch("/force_water", {
        method: "POST",
        body: JSON.stringify(postData),
        headers: {
            "Content-Type": "application/json"
        }
    });

    return response.ok;
}