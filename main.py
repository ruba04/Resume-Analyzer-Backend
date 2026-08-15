from fastapi import FastAPI, UploadFile, Form
from resume_parser import extract_text_from_pdf
from gemini import ask_gemini
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173" , "https://chatbot-seven-olive-68.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

resume_text = ""

@app.post("/upload")
async def upload_resume(file: UploadFile):
    global resume_text
    resume_text = extract_text_from_pdf(file.file)
    return {"message": "Resume uploaded successfully"}

@app.post("/chat")
async def chat(query: str = Form(...)):
    prompt = f"""
    You are a professional resume analyzer.Answer in **plain text only**, without Markdown, headers (##), bullets, or numbering.


    Resume:
    {resume_text}

    Question:
    {query}
    """
    answer = ask_gemini(prompt)
    return {"reply": answer}
