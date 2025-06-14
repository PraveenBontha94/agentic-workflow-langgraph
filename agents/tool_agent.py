# agents/tool_agent.py

from agents.tools import tool_router

def tool_agent(task):
    result = tool_router(task)
    print(f"Tool Agent Task: {task}\nResult: {result}")
    return result
