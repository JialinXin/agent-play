import yaml

def load_config(path="config/config.yaml"):
    with open(path, "r") as file:
        config = yaml.safe_load(file)
    
    # Validate configuration parameters
    if not config.get("azure_openai"):
        raise ValueError("Missing 'azure_openai' configuration.")
    if not config["azure_openai"].get("endpoint"):
        raise ValueError("Missing 'endpoint' in 'azure_openai' configuration.")
    if not config["azure_openai"].get("deployment_name"):
        raise ValueError("Missing 'deployment_name' in 'azure_openai' configuration.")
    if not config["azure_openai"].get("api_version"):
        raise ValueError("Missing 'api_version' in 'azure_openai' configuration.")
    if not config["azure_openai"].get("api_key"):
        raise ValueError("Missing 'api_key' in 'azure_openai' configuration.")
    
    return config
