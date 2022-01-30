function createTableContainer(providersList) {
    let tableContainer = createElement('div', {});
    let table = createElement('table', { 'className': 'table' });
    let thead = createElement('thead', {});
    let tbody = createSortedTbody(providersList);

    let nameTable = createElement('th', { 'className': 'align-middle', 'scope': 'col', 'innerText': 'Name' });
    let priceTable = createElement('th', { 'className': 'align-middle', 'scope': 'col', 'innerText': 'Price per month' });

    thead.appendChild(createElement('th', { 'className': 'align-middle', 'scope': 'col', 'innerText': '#' }));
    thead.appendChild(nameTable);
    thead.appendChild(priceTable);
    thead.appendChild(createElement('th', { 'className': 'align-middle', 'scope': 'col', 'innerText': 'More details' }));

    table.appendChild(thead);
    table.appendChild(tbody);
    tableContainer.appendChild(table);

    nameTable.appendChild(createSortButton('name', providersList, table));
    priceTable.appendChild(createSortButton('price', providersList, table));

    return tableContainer;
}

function createTbody(providersList) {
    let tbody = createElement('tbody', {});
    let idx = 1;

    providersList.forEach(el => {
        let tr = createElement('tr', {});

        tr.appendChild(createElement('th', { 'scope': 'col', 'innerText': idx }));

        let td1 = createElement('td', {});
        let i = createElement('i', { 'className': 'fas fa-external-link-alt' });
        let p = createElement('a', { 'innerText': '\u00a0' + el.title, 'href': el.link });
        td1.appendChild(i);
        td1.appendChild(p);

        let td2 = createElement('td', {});
        td2.appendChild(createElement('h6', { 'innerText': el.price + '$' }));

        let td3 = createElement('td', {});
        let button = createElement('button', {
            'type': 'button', 'className': 'btn btn-secondary btn-sm',
            'innerText': 'Show more details', 'style': 'width:15vh'
        });
        button.addEventListener('click', () => {
            displayDetails(el);
        });

        td3.appendChild(button);

        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);

        tbody.appendChild(tr);

        ++idx;
    });

    return tbody;
}