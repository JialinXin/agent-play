from autogen import UserProxyAgent

user_proxy_agent = UserProxyAgent(
    name="UserProxyAgent",
    system_message="You are a user proxy agent, skilled in understanding user needs and preferences.",
    code_execution_config={
        "work_dir": "generated_code", # execute code in the specified directory
        "use_docker": False, # do not use docker for code execution in local environment
    }  
)
