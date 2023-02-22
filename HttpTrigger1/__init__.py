import azure.cosmos.documents as documents
import azure.functions as func
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import os
import json
import uuid

HOST = os.environ.get('ACCOUNT_HOST', 'https://clvrclvr.documents.azure.com:443/')
MASTER_KEY = os.environ.get('ACCOUNT_KEY', 'yXcR8zS6fRLP6egav0k5I0INuxTAow0JxhcKkXSAbt4Q14XrsYCEGhoZZEA1nEtBchJOh2wLD0l7ACDbD0vvmA==')
DATABASE_ID = os.environ.get('COSMOS_DATABASE', 'contacts')
CONTAINER_ID = os.environ.get('COSMOS_CONTAINER', 'contact_container')

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # DB SETUP
        client = cosmos_client.CosmosClient(
            HOST, 
            {'masterKey': MASTER_KEY}, 
            user_agent="CosmosDBPythonQuickstart", 
            user_agent_overwrite=True
        )
        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)
                
        # ACTION
        data = json.loads(req.params.get('data'))
        data["id"] = str(uuid.uuid4())
        container.create_item(body=data)

        # RESPONSE
        items = list(container.read_all_items(max_item_count=1000))
        return func.HttpResponse(json.dumps(items, indent=4), mimetype="application/json")
    
    ## ERROR HANDLING
    except exceptions.CosmosHttpResponseError as e:
        return func.HttpResponse('{"error":"' + e.message + '"}', status_code=201)
