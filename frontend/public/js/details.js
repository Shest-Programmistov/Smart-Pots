function displayDetails(providerObj) {
    let modalTitle = document.getElementById('infoModalLongTitle');
    modalTitle.innerText = providerObj.title;

    let modalDesc = document.getElementById('infoModalDesc');
    modalDesc.innerText = providerObj.info;
    if (modalDesc.innerText == '') 
        modalDesc.innerText = 'N/A';

    let modalCompany = document.getElementById('infoModalCompany');
    modalCompany.innerText = providerObj.company;

    let modalLocations = document.getElementById('infoModalLocations');
    while (modalLocations.firstChild)
        modalLocations.removeChild(modalLocations.firstChild);

    providerObj.locations.forEach(el => {
        let listItem = createElement('li', {'className': 'list-group-item', 'innerText': el});
        modalLocations.appendChild(listItem);       
    });

    $('#resultModal').modal('hide');
    $('#errorModal').modal('hide');
    $('#infoModal').modal('show');
}