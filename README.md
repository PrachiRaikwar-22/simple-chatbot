# 🤖 Simple AI Chatbot | LLM-Powered Conversational App

A lightweight conversational AI application built with **Python, Streamlit, LangChain, and Groq**. The chatbot enables users to interact with a Large Language Model (LLM) through a clean web interface, demonstrating the fundamentals of LLM integration, prompt engineering, and conversational context management.

## ✨ Key Features

- **Interactive Chat Interface:** Communicate with the AI through a simple, user-friendly web application.
- **LLM Integration:** Generate responses using a language model accessed through the Groq API.
- **Conversation History:** Maintain previous messages and provide conversational context to the model.
- **Prompt Management:** Use LangChain prompt templates to structure model interactions.
- **Real-Time Interaction:** Display AI responses directly in the Streamlit application.
- **Secure Configuration:** Keep API credentials separate from source code using environment variables.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| LangChain | LLM integration and prompt management |
| Groq API | Access to a supported language model |

## 🏗️ How It Works

1. The user enters a message through the Streamlit chat interface.
2. The application collects relevant conversation history.
3. LangChain prepares the messages and sends them to the configured language model through Groq.
4. The model generates a response.
5. The application displays the response and updates the conversation history.

## 📁 Project Structure

```text
simple-chatbot/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── .gitignore          # Excluded files and secrets
└── README.md           # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python installed on your system
- A Groq API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/PrachiRaikwar-22/simple-chatbot.git
cd simple-chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Set the `GROQ_API_KEY` environment variable to your own API key. You can obtain one through the [Groq Console](https://console.groq.com/).

Never commit API keys or files containing secrets to GitHub.

### 5. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to start chatting.

## 🧠 Key Learnings

Through this project, I explored:

- Integrating LLM APIs into Python applications.
- Using LangChain for model initialization and prompt management.
- Passing conversation history as context for generating responses.
- Building interactive AI applications using Streamlit.
- Managing Python dependencies and API credentials securely.

## 🔮 Future Enhancements

- Add more robust error handling and API failure recovery.
- Support configurable models and generation parameters.
- Improve conversation management and the user interface.
- Deploy the application for public access.

## 👩‍💻 Author

**Prachi Raikwar**  

- GitHub: [@PrachiRaikwar-22](https://github.com/PrachiRaikwar-22)

---

*Built to explore the practical foundations of conversational AI and LLM-powered application development.*