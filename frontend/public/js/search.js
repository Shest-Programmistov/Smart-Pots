const resultCardId = '05db71bd-4e9e-4a4e-ad6f-ebf99b3538c1';
const resultErrorId = '05db71bd-4e9e-4a4e-ad6f-ebf99b3538c1';

function enableSearch(typeProvider) {
    const searchButton = document.getElementById('search-button');
    searchButton.addEventListener('click', () => {
        performSearch(typeProvider);
    });
}

function performSearch(typeProvider) {
    let text = document.getElementById('search').value;

    if (text == '') {
        filterData([], '');
        return;
    }

    url = "http://" + ip + ":" + port + "/" + typeProvider

    fetch(url).then(resposne => {
        resposne.json().then(data => {
            filterData(data, text);
        })
    });
}

function filterData(data, text) {
    answer = []

    Object.keys(data).forEach(k => {
        data[k].forEach(el => {
            if (el.title.toLowerCase().indexOf(text.toLowerCase()) !== -1)
                answer.push(el);
        });        
    });

    let uniqueAnswer = [];
    let uniqueTitles = new Set();
    answer.forEach(el => {
        if (!uniqueTitles.has(el.title)) {
            uniqueTitles.add(el.title);
            uniqueAnswer.push(el);
        }
    });

    displayResults(uniqueAnswer, text);
}

function displayResults(answer, text) {
    if (answer.length > 0) {
        let title = document.getElementById('resultModalLongTitle');
        title.innerText = `Results for '${text}'`;

        let modalLocations = document.getElementById('resultModalLocations');
        while (modalLocations.firstChild)
            modalLocations.removeChild(modalLocations.firstChild);

        modalLocations.appendChild(createTableContainer(answer));

        $('#resultModal').modal('show');
    }
    else {
        let title = document.getElementById('errorModalLongTitle');

        title.innerText = `No results found for '${text}'`;
        if (text == '')
            title.innerText = 'Please enter some keywords!';

        $('#errorModal').modal('show');
    }
}