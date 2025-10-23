import streamlit as st
import PyPDF2
import google.generativeai as genai

st.title("📄 PDF Q&A Chatbot (Gemini)")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
question = st.text_input("Ask a question about the PDF:")

if st.button("Ask"):
    if not api_key or not pdf_file or not question:
        st.warning("Please provide API Key, upload a PDF, and ask a question.")
    else:
        genai.configure(api_key=api_key)

        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"Answer the question based on this PDF content:\n\n{text}\n\nQuestion: {question}"

        response = model.generate_content(prompt)
        st.write("### 💬 Answer:")
        st.write(response.text)
