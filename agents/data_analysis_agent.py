from autogen import AssistantAgent
from utils.query_builder import QueryBuilder
from utils.data_loader import AzureDataExplorerClient
from utils.config_loader import load_config  # Import config loader

azure_client = AzureDataExplorerClient()
query_builder = QueryBuilder()

# Load Azure OpenAI configuration
config = load_config()
azure_openai_config = config["azure_openai"]

# Tool 1: 执行普通查询
def query_data(kql_query: str):
    """
    Execute a KQL query and return the result.
    """
    try:
        result = azure_client.query(kql_query)
        return result
    except Exception as e:
        return {"error": str(e)}

# Tool 2: 执行预定义查询
def execute_predefined_query(query_name: str, **kwargs):
    """
    Dynamically build and execute a query based on predefined templates.
    """
    try:
        query_text = query_builder.build_query(query_name, **kwargs)
        result = azure_client.query(query_text)
        return result
    except Exception as e:
        return {"error": str(e)}

# Tool 3: 查询表结构信息
def get_table_info(table_name: str = ""):
    """
    Get the structure of a table, including its columns.
    """
    try:
        return azure_client.query(f".show table {table_name} schema as json")
    except Exception as e:
        return {"error": str(e)}

# ✨ 定义 Functions 列表
functions = [
    {
        "name": "query_data",
        "description": "Use KQL to query product usage data.",
        "parameters": {
            "type": "object",
            "properties": {
                "kql_query": {
                    "type": "string",
                    "description": "The full KQL query statement to execute."
                }
            },
            "required": ["kql_query"]
        },
        "function": query_data
    },
    {
        "name": "get_table_info",
        "description": "Retrieve the structure and columns of a specified table.",
        "parameters": {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Name of the table to inspect. Optional."
                }
            },
            "required": []
        },
        "function": get_table_info
    },
    {
        "name": "execute_predefined_query",
        "description": "Execute a query from the predefined knowledge base with dynamic parameters.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_name": {
                    "type": "string",
                    "description": "The name of the predefined query template to use."
                },
                # 注意：如果你的 query_builder 支持动态参数，这里可以补充更多字段
            },
            "required": ["query_name"]
        },
        "function": execute_predefined_query
    }
]

# ✅ 创建 Data Analysis Agent
data_analysis_agent = AssistantAgent(
    name="DataAnalysisAgent",
    system_message=(
        "You are a professional data analysis expert, skilled in analyzing product usage through KQL queries. "
        "You have access to several tools:\n"
        "- `query_data`: Run arbitrary KQL queries.\n"
        "- `get_table_info`: Retrieve database table structure.\n"
        "- `execute_predefined_query`: Use predefined query templates.\n"
        "Use these tools appropriately to solve user problems efficiently. "
        "If a query result is empty, analyze possible causes and suggest improvements."
    ),
    llm_config={
        "endpoint": azure_openai_config["endpoint"],
        "deployment_name": azure_openai_config["deployment_name"],
        "api_version": azure_openai_config["api_version"],
        "api_key": azure_openai_config["api_key"],
        "temperature": 0.2
    },
    functions=functions  # <<< 注意这里是 functions
)