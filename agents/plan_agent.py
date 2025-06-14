from langchain_ollama import ChatOllama

# Load phi3:mini model via Ollama
llm = ChatOllama(model="phi3:mini")

def plan_agent(query):
    """
    Break down the user query into smaller subtasks.
    """
    prompt = f"""
    Break down the following user query into smaller subtasks as a numbered list.

    Query: {query}

    Subtasks:
    """
    response = llm.invoke(prompt)
    output = response.content.strip()

    lines = output.splitlines()
    subtasks = []
    for line in lines:
        if line.strip() == "":
            continue
        if ":" in line:
            _, subtask = line.split(":", 1)
            subtask = subtask.strip()
        else:
            subtask = line.strip()
        if subtask:
            subtasks.append(subtask)
    return subtasks
