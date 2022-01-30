let criterion = "nameAsc";

function createSortedTbody(providersList) {
    if (criterion === "nameAsc") {
        providersList.sort((a, b) => {
            if (a.title.toLowerCase() < b.title.toLowerCase())
                return -1;
            else if (a.title.toLowerCase() > b.title.toLowerCase())
                return 1;
            return 0;
        });
    }
    else if (criterion === "nameDesc") {
        providersList.sort((a, b) => {
            if (a.title.toLowerCase() > b.title.toLowerCase())
                return -1;
            else if (a.title.toLowerCase() < b.title.toLowerCase())
                return 1;
            return 0;;
        });
    }
    else if (criterion === "priceAsc") {
        providersList.sort((a, b) => {
            return a.price - b.price;
        });
    }
    else if (criterion === "priceDesc") {
        providersList.sort((a, b) => {
            return b.price - a.price;
        });
    }

    return createTbody(providersList);
}

function createSortButton(column, providersList, table) {
    let sortButton = createElement('button', { 'className': 'btn shadow-none', 'style': 'background-color:transparent'});
    sortButton.appendChild(createElement('i', { 'className': 'fa fa-fw fa-sort' }));

    sortButton.addEventListener('click', () => {
        if (criterion.indexOf(column) !== -1) {
            if (criterion === column + 'Asc')
                criterion = column + 'Desc';
            else
                criterion = column + 'Asc';
        }
        else {
            criterion = column + 'Asc';
        }
        
        table.replaceChild(createSortedTbody(providersList), table.lastChild);
    });

    return sortButton;
}