# 📌 PDF Q&A with Gemini (Google AI)

A simple and fast PDF Question Answering app powered by **Google Gemini 2.0 Flash**, built with **Python + Streamlit**.  
This app allows you to upload a PDF, extract the content, and ask any question related to the document.

---

## 🚀 Features

- ✅ Upload PDF and extract text
- ✅ Ask questions based on document context (PDF Q&A)
- ✅ Powered by **Gemini 2.0 Flash**
- ✅ Clean and simple UI with Streamlit
- ✅ Fast response and lightweight
- ✅ Customizable for future features
- ✅ Ready to deploy on **HuggingFace Spaces**

---

## 🧱 Tech Stack

| Component | Technology |
|-----------|------------|
| AI Model  | Gemini 2.0 Flash |
| Backend   | Python |
| UI        | Streamlit |
| PDF Parser| PyPDF2 |

---

## 📌 Project Structure
pdf-qa-gemini/
│
├─ app/
│ └─ main.py
│
├─ requirements.txt
└─ README.md


---

## 🧪 Local Development

### 1. Create virtual environment (optional)
```bash
python -m venv venv
source venv/Scripts/activate   # Windows

2. Install dependencies
pip install -r requirements.txt

3. Add your Gemini API key

Create a .env file:

GEMINI_API_KEY=YOUR_API_KEY_HERE

4. Run the app
streamlit run app/main.py

🌐 Deploy to HuggingFace

Upload project to HF Space

Select Python + Streamlit

Make sure requirements.txt exists

HF will auto-run app/main.py

🛠 Customization & Future Development (Roadmap)
Feature	Status
PDF Q&A	✅ Done
Support Multiple PDFs	⏳ Next
Add Memory / Chat History	⏳ Next
Support for images inside PDF	⏳ Next
Model switch (Gemini / OpenAI / Local LLM)	⏳ Next
Export Q&A to PDF	⏳ Next
Multi-language support	⏳ Next

This project is designed to be fully customizable, so additional features can be added easily based on client needs.

👨‍💻 Author

Created by Rizki Firmansyah
GitHub: https://github.com/abirizki

📄 License

MIT License
