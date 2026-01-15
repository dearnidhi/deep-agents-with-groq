# 🧠 Deep Agents Architecture – 4 Component System

This project demonstrates a **proper Deep Agent architecture** built using  
**DeepAgents + LangChain + Groq (LLaMA 3.3) + Streamlit**.

It is designed to clearly show how a real Deep Agent works internally,
not just a fake “agent” wrapper.

---

## 🚀 What is a Deep Agent?

A Deep Agent is an AI system that:
- **Plans** before acting
- **Executes tasks step by step**
- **Uses tools when needed**
- **Writes structured outputs**
- **Is orchestrated by an internal manager**

This project shows all of that in a clean, observable way.

---

## 🧩 4 Core Components Explained

### 1️⃣ Planner  
📋 Uses an explicit planning tool to decide steps before execution.

Implemented via:
- `write_todos` tool

---

### 2️⃣ Researcher  
🔍 Performs analysis for each planned step using internal knowledge.

Implemented via:
- `internal_analysis` tool

---

### 3️⃣ Writer  
✍️ Produces final outputs into files:
- `report.md` (Markdown)
- `data.json` (Structured JSON)

This shows **file-based memory & persistence**.

---

### 4️⃣ Manager  
🛡️ The most important part.

- Handles planning → execution → synthesis loop
- Routes tools correctly
- Maintains file consistency
- Orders messages and execution trace

⚠️ **Important:**  
The Manager is **NOT manually coded**.  
It is handled internally by `create_deep_agent()` from DeepAgents.

The UI simply **visualizes the Manager’s behavior** via execution logs.

---


---

## 🖥️ UI Features

The Streamlit UI shows:
- 📋 Component legend (Planner, Researcher, Writer, Manager)
- 💬 Execution Trace (Manager decisions)
- 📄 Markdown Report (Writer output)
- 📦 JSON Data (Manager-validated structured output)

---


---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Create .env file

GROQ_API_KEY=your_groq_api_key_here
3️⃣ Run the app

streamlit run main.py

🧠 Tech Stack
DeepAgents
LangChain
Groq (LLaMA 3.3 70B)
Streamlit
Python

🎯 Use Cases
Learning Deep Agent architecture

Understanding Planner / Researcher / Writer / Manager roles

Building real multi-step AI agents

Educational demos & YouTube tutorials

✅ Key Takeaway
This project proves that:

A Deep Agent is not just a prompt

The Manager is internal, not imaginary

Proper agents require planning, tools, memory, and orchestration

⭐ If this helped you
Give the repo a ⭐ and share it with others learning AI Agents.

<p align="center">
  <a href="https://youtu.be/MvDyDOPPxPA">
    <img src="https://img.youtube.com/vi/MvDyDOPPxPA/maxresdefault.jpg" alt="Deep Agents Demo" />
  </a>
</p>

<p align="center">
  <b>▶ Click the image to watch the full demo</b>
</p>


---




