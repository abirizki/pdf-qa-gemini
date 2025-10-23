# 📄 AI PDF Q&A Chatbot — Gemini Flash (Streamlit)

This is an **AI-powered PDF Question & Answer Web App** built using **Gemini Flash**, **Python**, and **Streamlit**.  
The app allows users to **upload a PDF, ask questions, and get instant AI-generated answers** based on the document's content.

This project is part of my **freelance portfolio** — designed for real business use cases on **Upwork & Fiverr**, such as internal document search, knowledge bots, compliance documents, manuals, handbooks, SOPs, and more.

---

## 🚀 Features

| Feature | Status |
|---------|---------|
| Upload any PDF | ✅ |
| Ask natural language questions about content | ✅ |
| Gemini Flash LLM responses | ✅ |
| Streamlit UI, runs in browser | ✅ |
| Fast inference | ✅ |

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|------------|
| **LLM Model** | Gemini Flash |
| **Language** | Python |
| **UI Framework** | Streamlit |
| **Document Parser** | PyPDF2 |

---

## 📌 Use Cases (for Clients)

This app can be used for:

- 📌 Company SOP / Policy Q&A
- 📌 Legal document Q&A
- 📌 Handbook & Training manuals
- 📌 Research papers summarization
- 📌 Proposal, report, or technical document Q&A
- 📌 Mini RAG system for internal teams

🔑 API Key

Generate a free Gemini API Key here:
https://aistudio.google.com/apikey

Input the key into the app when prompted.

📌 How It Works

Upload your PDF

Ask any question in natural language

The app reads and extracts PDF content

Gemini Flash processes your question

The answer is displayed instantly

📌 Demo Status

✅ Local Streamlit Demo working

🌍 Optional deployment (coming soon):

Streamlit Cloud / Railway / HuggingFace

📌 Roadmap (Next Upgrades)

 Vector DB (ChromaDB / FAISS) for longer PDFs

 Web UI styling (Tailwind / Bootstrap)

 Web deployment for public demo

 Web search + multi-PDF support

🧑‍💻 Author

Rizki Firmansyah — AI Automation Developer
GitHub: https://github.com/abirizki

---

## 🛠️ Installation (Local Setup)

```bash
pip install -r requirements.txt
streamlit run app/main.py
