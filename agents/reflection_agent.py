from langchain_ollama import ChatOllama

# Load phi3:mini model via Ollama
llm = ChatOllama(model="phi3:mini")

def reflection_agent(task, result):
    """
    Evaluate result and return feedback.
    """
    prompt = f"""
    Task: {task}
    Result: {result}

    If this result is sufficient, say exactly: ACCEPTED
    Otherwise, briefly suggest ONE improvement.
    """
    response = llm.invoke(prompt)
    feedback = response.content.strip()

    if "ACCEPTED" in feedback.upper():
        return "ACCEPTED"
    return feedback
