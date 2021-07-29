## Azure Function - API call to download data from Schools in Porto Alegre
This is a Azure function developed to access a provided API and download data from schools in Porto Alegre, RS, Brazil. The downloaded data is saved in json format in an Azure Storage Account.

The link for the API is https://dadosabertos.poa.br/api/3/action/datastore_search?resource_id=5579bc8e-1e47-47ef-a06e-9f08da28dec8

The main code for the Azure Function is inside 'download-api-escolas-poa' folder, in __init__.py file.