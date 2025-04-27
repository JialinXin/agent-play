# AIAgent AutoGen

AIAgent AutoGen is a Python-based project designed to provide intelligent data analysis capabilities using Azure OpenAI and Azure Data Explorer. It enables users to execute KQL queries, retrieve table structures, and perform predefined queries dynamically.

## Features

- **Azure OpenAI Integration**: Leverages Azure OpenAI for natural language processing and intelligent agent capabilities.
- **Azure Data Explorer Integration**: Executes KQL queries and retrieves data from Azure Data Explorer.
- **Dynamic Query Execution**: Supports predefined query templates with dynamic parameters.
- **Customizable Agent**: Includes a configurable assistant agent for data analysis tasks.

## Prerequisites

- Python 3.8 or higher
- Azure OpenAI resource with a deployed model (e.g., GPT-4)
- Azure Data Explorer cluster and database
- API keys and endpoint for Azure OpenAI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/AIAgent_AutoGen.git
   cd AIAgent_AutoGen
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the application:
   - Update the `config/config.yaml` file with your Azure OpenAI and Azure Data Explorer settings.

## Configuration

The configuration file is located at `config/config.yaml`. Below is an example:

```yaml
azure_openai:
  endpoint: "https://your-azure-openai-endpoint.openai.azure.com/"
  deployment_name: "gpt-4-deployment"
  api_version: "2023-03-15-preview"
  api_key: "your-azure-openai-api-key"

azure_data_explorer:
  cluster: "https://your-cluster.kusto.windows.net"
  database: "your-database"

agent_settings:
  max_round: 10

logging:
  level: INFO
```

## Usage

1. **Run the Agent**:
   Execute the main script to start the data analysis agent:
   ```bash
   python agents/data_analysis_agent.py
   ```

2. **Available Tools**:
   - `query_data`: Execute arbitrary KQL queries.
   - `get_table_info`: Retrieve table structure and columns.
   - `execute_predefined_query`: Run predefined queries with dynamic parameters.

3. **Customizing the Agent**:
   Modify the `data_analysis_agent.py` file to adjust the agent's behavior or add new tools.

## Project Structure

```
AIAgent_AutoGen/
├── agents/
│   └── data_analysis_agent.py   # Main agent implementation
├── config/
│   └── config.yaml              # Configuration file
├── utils/
│   ├── config_loader.py         # Configuration loader
│   ├── query_builder.py         # Query builder utility
│   └── data_loader.py           # Azure Data Explorer client
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## Notes

- Ensure your Azure OpenAI resource has the correct `deployment_name` configured.
- Validate your configuration using the `config_loader.py` utility.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
