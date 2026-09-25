🤖 AI Assistant

A simple LLM-powered chatbot built with Python, Streamlit, and Groq using the OpenAI-compatible API.

The project provides a clean, ChatGPT-style interface and maintains conversation history during the active session.

✨ Features

💬 ChatGPT-style chat interface

🧠 Conversation memory during the current session

⚡ Fast responses powered by Groq

🤖 Uses openai/gpt-oss-120b

🎨 Custom dark UI built with Streamlit

🔐 API key stored securely in .env

📦 Dependency management with Pipenv

🛠️ Tech Stack

Python

Streamlit

Groq API

OpenAI Python SDK

Pipenv

python-dotenv

📁 Project Structure

ai-engineer/
│
├── app.py              # Streamlit UI
├── chat_bot.py         # LLM / Groq integration
├── .env                # API key (not committed)
├── .gitignore
├── Pipfile
└── README.md

🚀 Getting Started

1. Clone the repository

git clone https://github.com/your-username/your-repository.git
cd your-repository

2. Install dependencies

Make sure Python and Pipenv are installed.

pipenv install

3. Add your Groq API key

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key

Never commit your .env file or expose your API key publicly.

4. Run the application

pipenv run streamlit run app.py

Streamlit will provide a local URL, usually:

http://localhost:8501

Open it in your browser.

💡 How It Works

The application has two main parts:

User
  ↓
Streamlit UI
  ↓
app.py
  ↓
chat_bot.py
  ↓
Groq API
  ↓
GPT-OSS 120B
  ↓
AI Response
  ↓
Streamlit UI

app.py handles the interface and conversation history, while chat_bot.py handles communication with the LLM.

🔑 Environment Variables

The project expects:

GROQ_API_KEY=your_groq_api_key

The key is loaded with python-dotenv and passed to the OpenAI Python client configured for Groq's OpenAI-compatible endpoint.

📌 Notes

This project is intended as a learning project for exploring:

LLM APIs

Prompt and message handling

Conversation state

Streamlit app development

AI application architecture

🔮 Future Improvements

Possible next steps include:

Streaming responses

Persistent chat history

PDF upload and RAG

Vector database integration

Tool calling

User authentication

Database integration

Deployment with Docker

📄 License

This project is available for educational and personal use.