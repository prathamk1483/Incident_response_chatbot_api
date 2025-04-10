
# 🛡️ AI-Powered Cybersecurity Chatbot

This chatbot takes the **type of cybersecurity incident** as input and uses the **Google Gemini API** to advise administrators on how to mitigate or respond to the threat.

---

## 🚀 Features

- ⚡ FastAPI-powered backend
- 🤖 Uses Google Gemini 1.5/2 API
- 📘 Simple input: just specify the attack type
- 🧠 Returns concise mitigation strategies
- 🔒 Designed for system admins and cybersecurity response teams

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
fastapi==0.110.0
uvicorn==0.29.0
google-generativeai==0.3.2
python-dotenv==1.0.1
```

---

## 🔑 API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and generate your API key.
2. Create a `.env` file in your project root directory.
3. Add your key like this:

```
GEMINI_API_KEY=your_google_api_key_here
```

---

## ▶️ Run the Chatbot

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

> Replace `main` with your Python file name (without `.py`) if needed.

---

## 💬 How to Chat

You can interact with the chatbot by sending a `POST` request to the `/chat` endpoint.

### Example (PowerShell):

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/chat" -Method POST `
  -Body (@{type="Phishing attack"} | ConvertTo-Json) `
  -ContentType "application/json"
```

---

## 🎯 Supported Incident Types

Try inputs like:

- Phishing attack  
- DDoS attack  
- SQL injection  
- Ransomware  
- Insider threat  
- Zero-day exploit  
- Malware infection  
- Cross-site scripting (XSS)

---

## ❗ Troubleshooting

- **400 API key not valid**: Check if `.env` file exists and `GEMINI_API_KEY` is correct.
- **No/partial response**: Gemini streams responses in chunks; ensure you're printing `chunk.text` fully.
- **ImportError**: Make sure you have `google-generativeai==0.3.2` installed.

---

## 📁 Folder Structure

```
/chatbot
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Google Gemini API](https://ai.google.dev/)
