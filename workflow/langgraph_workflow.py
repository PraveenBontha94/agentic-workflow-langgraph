from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Tuple
from agents.plan_agent import plan_agent
from agents.tool_agent import tool_agent
from agents.reflection_agent import reflection_agent

class WorkflowState(TypedDict):
    query: str
    plan: List[str]
    completed: List[Tuple[str, str]]
    pending: List[str]
    results: dict

def initialize_state(query):
    plan = plan_agent(query)
    return {
        "query": query,
        "plan": plan,
        "completed": [],
        "pending": plan,
        "results": {}
    }

def tool_node(state):
    if not state["pending"]:
        return state

    task = state['pending'][0]
    result = tool_agent(task)
    new_completed = state['completed'] + [(task, result)]
    new_results = state['results'].copy()
    new_results[task] = result

    return {
        "completed": new_completed,
        "plan": state['plan'],
        "pending": state['pending'],
        "query": state['query'],
        "results": new_results
    }

def reflection_node(state):
    if not state["pending"]:
        return state

    task = state["pending"][0]
    result = state["results"].get(task)
    feedback = reflection_agent(task, result)

    if "ACCEPTED" in feedback.upper():
        return {
            "completed": state["completed"] + [(task, result)],
            "plan": state["plan"],
            "pending": state["pending"][1:],
            "query": state["query"],
            "results": state["results"]
        }
    else:
        return {
            "completed": state["completed"],
            "plan": state["plan"],
            "pending": state["pending"][1:] + [feedback],
            "query": state["query"],
            "results": state["results"]
        }

def build_langgraph_workflow():
    graph = StateGraph(WorkflowState)
    graph.add_node("Tool", tool_node)
    graph.add_node("Reflection", reflection_node)
    graph.set_entry_point("Tool")
    graph.add_edge("Tool", "Reflection")
    graph.add_conditional_edges(
        "Reflection",
        lambda state: "DONE" if not state['pending'] else "CONTINUE",
        {
            "DONE": END,
            "CONTINUE": "Tool"
        }
    )
    return graph.compile(), initialize_state
