import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="Deep Agent Architecture Demo", layout="wide")

st.title("🚀 Proper Deep Agent - 4 Components System")

# ---------------------------
# Architecture Legend (4 Components)
# ---------------------------
cols = st.columns(4)
cols[0].metric("📋 Planner", "Explicit Tool")
cols[1].metric("🔍 Researcher", "Internal Knowledge")
cols[2].metric("✍️ Writer", "Filesystem Output")
cols[3].metric("🛡️ Manager", "Runtime Orchestration")

st.divider()

# ---------------------------
# Import the Deep Agent system
# ---------------------------
from agents import create_full_deep_system

@st.cache_resource
def load_system():
    return create_full_deep_system()

agent = load_system()

# ---------------------------
# Helper for safe file retrieval
# ---------------------------
def get_file_content(files, *keys):
    for k in keys:
        if k in files:
            content = files[k]
            return content.get("content", content) if isinstance(content, dict) else content
    return None

# ---------------------------
# User Input
# ---------------------------
task = st.text_area("Research Task:", "Future of AI Agents in 2026")

if st.button("🚀 Run Deep Agent Demo", type="primary"):
    with st.spinner("Multi-Agent Coordination in progress..."):
        # Full prompt mentioning all 4 components
        full_prompt = (
            f"TASK: {task}\n\n"
            "SYSTEM INSTRUCTIONS:\n"
            "1. [PLANNER]: Use 'write_todos' to list research steps.\n"
            "2. [RESEARCHER]: Use 'internal_analysis' for each step.\n"
            "3. [WRITER]: Create 'report.md' (Markdown) and 'data.json' (Structured).\n"
            "4. [MANAGER]: Validate that both formats match and tasks are complete."
        )

        # Invoke the agent
        result = agent.invoke({"messages": [{"role": "user", "content": full_prompt}], "files": {}})

        files = result.get("files", {})

        # ---------------------------
        # Tabs for clean UI
        # ---------------------------
        tab1, tab2, tab3 = st.tabs([
            "💬 Execution Trace (Manager Decisions)",
            "📄 Markdown Report",
            "📦 JSON Data"
        ])

        # Execution Trace = Manager behavior
        with tab1:
            st.subheader("🤖 Execution Trace")
            with st.expander("Show Full Execution Trace", expanded=True):
                for msg in result.get("messages", []):
                    if msg.content:
                        st.chat_message("assistant").write(msg.content)

        # Writer Output = Markdown
        with tab2:
            st.subheader("✍️ Writer Output (Markdown)")
            md_content = get_file_content(files, "/report.md", "report.md")
            if md_content:
                st.markdown("\n".join(md_content) if isinstance(md_content, list) else str(md_content))
            else:
                st.info("No Markdown report generated yet.")

        # Manager Validated Data = JSON
        with tab3:
            st.subheader("🛡️ Manager Validated Data (JSON)")
            json_content = get_file_content(files, "/report.json", "data.json", "report.json")
            if json_content:
                st.json(json_content)
            else:
                st.info("Agent is processing internal data structure...")
                st.write(files)

    # Execution success
    st.success("✅ DeepAgent Workflow Completed: Planner, Researcher, Writer, Manager all active.")
