from azure.identity import AzureCliCredential
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from utils.config_loader import load_config

class AzureDataExplorerClient:
    def __init__(self):
        config = load_config()
        azure_config = config.get("azure_data_explorer", {})
        
        cluster = azure_config.get("cluster")
        database = azure_config.get("database")
        
        if not all([cluster, database]):
            raise ValueError("Missing configuration for Azure Data Explorer, please check config.yaml")
        
        credential = AzureCliCredential()
        kcsb = KustoConnectionStringBuilder.with_azure_token_credential(
            cluster, credential
        )
        self.client = KustoClient(kcsb)
        self.database = azure_config.get("database")

    def query(self, kql_query: str):
        if not kql_query.strip():
            raise ValueError("Argument 'kql_query' cannot be empty.")
        response = self.client.execute(self.database, kql_query)
        rows = []
        for row in response.primary_results[0]:
            rows.append(dict(row))
        return rows
