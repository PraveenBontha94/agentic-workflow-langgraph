import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from workflow.langgraph_workflow import build_langgraph_workflow

st.set_page_config(page_title="Agentic Workflow", page_icon="🧠", layout="wide")

st.title("Agentic Workflow using LangGraph")

query = st.text_input(" Enter your query:")

if query:
    st.info(" Initializing graph...", icon="")
    graph, initializer = build_langgraph_workflow()
    state = initializer(query)

    st.info("Generating plan...")
    with st.expander("Generated Plan"):
        for idx, subtask in enumerate(state["plan"]):
            st.write(f"**Step {idx+1}:** {subtask}")

    st.success(" Starting graph stream...")
    for update in graph.stream(state):
        for key, value in update.items():
            state[key] = value

    st.success("Graph execution completed successfully!")
    st.header(" Final Completed Tasks:")
    for task, result in state['completed']:
        st.markdown(f"""
        <div style="background-color:#1E1E1E;padding:15px;border-radius:10px;margin-bottom:10px;">
            <b style="color:#00BFFF;">Task:</b> {task}<br>
            <b style="color:#7CFC00;">Result:</b> {result}
        </div>
        """, unsafe_allow_html=True)
