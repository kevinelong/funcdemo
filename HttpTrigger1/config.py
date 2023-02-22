import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://clvrclvr.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'yXcR8zS6fRLP6egav0k5I0INuxTAow0JxhcKkXSAbt4Q14XrsYCEGhoZZEA1nEtBchJOh2wLD0l7ACDbD0vvmA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}