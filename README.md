# Agentic Workflow using LangGraph

## Project Objective

This project implements an **Agentic Workflow** using LangGraph that:
- Takes a user query.
- Breaks it into subtasks (PlanAgent).
- Solves tasks (ToolAgent).
- Validates/refines outputs (ReflectionAgent).
- Uses iterative feedback loops for reliability.

---

##  High-Level Architecture

**Plan Agent (Planner)**  
Splits the input query into smaller subtasks using LLM (`phi3:mini` model via Ollama).

**Tool Agent**  
Processes each subtask using simple tools:
- Math evaluation (`eval()`)
- Default text response for non-math queries.

**Reflection Agent**  
Validates each task result:
- If valid: accepts.
- If invalid: refines and retries.

**LangGraph Workflow**  
Manages:
- State transitions.
- Task iteration.
- Feedback loops.

**UI**  
Built with Streamlit for interactive user input & visualization.

---

## ⚙ Setup Instructions

### 🖥 Python Version
- Python 3.12.x

###Required Packages

Create `requirements.txt` with:

```txt
langgraph
streamlit
langchain
langchain_ollama
ollama
