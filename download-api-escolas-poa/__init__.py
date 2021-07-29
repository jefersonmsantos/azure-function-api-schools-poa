import logging

import azure.functions as func
from azure.storage.blob import BlockBlobService
from datetime import datetime
import requests
from io import BytesIO, StringIO
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    azure_account_name = os.environ['account_name']
    azure_account_key = os.environ['account_key']

    block_blob_service = BlockBlobService(account_name=azure_account_name,account_key = azure_account_key)

    url = ' https://dadosabertos.poa.br/api/3/action/datastore_search?resource_id=5579bc8e-1e47-47ef-a06e-9f08da28dec8'
    
    with requests.get(url, stream=True) as r:
        today = datetime.today().strftime('%Y-%m-%d')
        block_blob_service.create_blob_from_stream('download-area','ESCOLAS/POA/'+'cadastro_escoalas_'+today+'.json',BytesIO(r.content))


    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
