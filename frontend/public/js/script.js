const ip = 'localhost'
const port = '3000'

const displayableProvider = {
    'ded_serv': 'Dedicated Server',
    'low_end_vps': 'Low End VPS',
    'vds': 'VDS',
    'vpn': 'VPN',
    'vps': 'VPS'
};

function renderInfo(typeProvider) {
    url = "http://" + ip + ":" + port + "/" + typeProvider
    let search = document.getElementById('search');
    if (search !== null) {
        search.value = "";
        search.placeholder = 'Search for ' + displayableProvider[typeProvider] + ' providers';
    }

    fetch(url).then(resposne => {
        resposne.json().then(data => {
            appendDataToDOM(data);
        })
    });
}

function createElement(_tag, options) {
    let retVal = document.createElement(_tag);
    Object.keys(options).forEach(op => {
        retVal[op] = options[op];
    });
    return retVal;
}

function appendDataToDOM(data) {
    let container = document.getElementById('cards-container');

    let loader = document.getElementById('loader');
    loader.parentNode.removeChild(loader);

    Object.keys(data).forEach(k => {
        container.appendChild(createCard(k, data[k]));
    })
}

function createCard(region, providersList) {
    let card = createElement('div', { 'className': 'card m-4', 'style': 'width: 100vh' });
    card.appendChild(createCardHeader(region, providersList.length));
    card.appendChild(createCardBody(region, providersList));
    return card;
}

function createCardHeader(region, noProviders) {
    let cardHeader = createElement('div', { 'className': 'card-header d-flex justify-content-sm-between' });

    let regionName = createElement('h1', { 'className': 'text-center', 'innerText': region , 'style': 'margin-left: 5vh;' });
    cardHeader.appendChild(regionName);

    let tempDiv = createElement('div', { 'style': 'margin-right: 5vh;' });
    tempDiv.appendChild(createCollapseButton(region.split(' ').join('')));
    tempDiv.appendChild(createElement('br', {}));

    let text = noProviders + ' providers';
    if (noProviders == 1)
        text = '1 provider';

    tempDiv.appendChild(createElement('small', { 'innerText': text }));
    cardHeader.appendChild(tempDiv);

    return cardHeader;
}

function createCardBody(region, providersList) {
    let cardBody = createElement('div', { 'className': 'card-body' });
    cardBody.appendChild(createTableContainer(providersList));

    let retVal = createElement('div', { 'id': 'collapse' + region.split(' ').join(''), 'className': 'collapse' });
    retVal.appendChild(cardBody);

    return retVal;
}