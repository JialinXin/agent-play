from autogen import GroupChat, GroupChatManager
from agents.user_proxy_agent import user_proxy_agent
from agents.data_analysis_agent import data_analysis_agent

def create_pm_workflow():
    # Create a GroupChat instance with the agents
    groupchat = GroupChat(
        agents=[
            user_proxy_agent,
            data_analysis_agent
            #competitor_analysis_agent,
            #strategy_advisor_agent
        ],
        messages=[],
        max_round=10
    )

    manager = GroupChatManager(
        groupchat=groupchat,
        llm_config={"temperature": 0.2, "model": "gpt-4"}
    )
    return manager
