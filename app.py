import streamlit as st
from pdf_utils import extract_text_from_pdf
from ai_utils import ask_ai

st.set_page_config(page_title="AI Doc Assistant", layout="wide")

st.title("📄 AI Document Assistant")
st.write("Upload a PDF and ask questions based on its content.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading PDF..."):
        document_text = extract_text_from_pdf(uploaded_file)

    if document_text.strip() == "":
        st.error("PDF text extract nahi ho pa raha. Scan PDF ho sakta hai.")
    else:
        st.success("PDF loaded successfully ✅")

        question = st.text_input("Ask a question about this document")

        if question:
            with st.spinner("AI is thinking... 🤖"):
                answer = ask_ai(document_text, question)

            st.subheader("Answer")
            st.write(answer)
