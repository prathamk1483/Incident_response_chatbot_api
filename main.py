# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import re

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def remove_html_except_strong(text):
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    return text


class IncidentRequest(BaseModel):
    type: str

@app.post("/chat")
async def chat(req: IncidentRequest):
    try:
        prompt = f"""
You're a cybersecurity assistant helping system administrators.
Given the following type of security incident, precisely explain standard ways to mitigate or respond to it. Keep response fairly short.You should professionally response to common questions similar to hi 
,hello ,etc. Apart from that do not respond to query which is not related to cybersecurity.

Incident type: {req.type}
"""
        response = model.generate_content(prompt)
        return {"response": remove_html_except_strong(response.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
