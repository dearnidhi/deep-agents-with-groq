import os
from typing import List
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from deepagents import create_deep_agent
# ==========================================
# COMPONENT 1: PLANNER & RESEARCHER TOOLS
# ==========================================
@tool
def write_todos(tasks: List[str]) -> str:
    """
    PLANNER COMPONENT:
    This tool is used by the Planner to create a step-by-step 
    roadmap for the entire research process.
    """
    return "✅ PLAN CREATED: " + ", ".join(tasks)

@tool
def internal_analysis(query: str) -> str:
    """
    RESEARCHER COMPONENT:
    This tool is used by the Researcher to perform deep analysis 
    on specific topics using the model's internal knowledge.
    """
    return f"🔍 Analysis for '{query}' completed."

def create_full_deep_system():
    # Model configuration
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )
    # ==========================================
    # COMPONENT 3 & 4: WRITER & MANAGER LOGIC
    # ==========================================
    # create_deep_agent internally uses a 'Manager' to orchestrate
    # and a 'Writer' to format the final filesystem output.
    return create_deep_agent(llm, [write_todos, internal_analysis])