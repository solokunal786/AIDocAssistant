import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🔍 Auto-pick first text-capable model
models = genai.list_models()
model_name = None

for m in models:
    if "generateContent" in m.supported_generation_methods:
        model_name = m.name
        break

model = genai.GenerativeModel(model_name)

def ask_ai(document_text, question):
    prompt = f"""
You are a helpful document assistant.

Document:
{document_text}

Question:
{question}
"""
    response = model.generate_content(prompt)
    return response.text
