# 🚀 Simple LangChain Chatbot with Groq

A simple, interactive AI chatbot built using **Streamlit, LangChain, and Groq**. It allows users to interact with Large Language Models (LLMs), maintain conversational context, switch between AI models, and receive responses in real time through streaming.

This project demonstrates the fundamentals of LangChain, including prompt templates, conversation history, LLM integration, and output parsing.

## ✨ Features

- **Conversational AI:** Interact with an AI assistant that remembers previous messages within the session.
- **Multiple Models:** Switch between available Groq models.
- **Real-Time Streaming:** Receive AI responses as they are generated.
- **Chat History:** Maintains conversation history using Streamlit session state.
- **New Chat:** Start a fresh conversation.
- **Clear Chat:** Clear existing conversation history.
- **Interactive Interface:** Clean Streamlit UI with a sidebar for model selection and suggested prompts.

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Streamlit** – Interactive web interface
- **LangChain** – LLM orchestration and prompt management
- **Groq API** – Fast LLM inference
- **ChatGroq** – Integration with Groq-hosted models
- **python-dotenv** – Environment variable management

## 📂 Project Structure

```text
Simple-LangChain-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Simple-LangChain-Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd Simple-LangChain-Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

All required Python packages and dependencies are listed in the `requirements.txt` file.

Install them using:

```bash
pip install -r requirements.txt
```

### 5. Configure Groq API Key

Get your API key from [Groq Console](https://console.groq.com/keys).

Create a `.env` file in the root directory and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Note:** Keep your API key private. Never upload your `.env` file to GitHub.

### 6. Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The chatbot will open in your default web browser.

## 🧠 LangChain Concepts Implemented

This project explores the following LangChain concepts:

**1. ChatGroq**

Connects the application to Groq-hosted language models.

**2. ChatPromptTemplate**

Defines the structure of messages sent to the LLM, including system instructions, conversation history, and the current user question.

**3. MessagesPlaceholder**

Dynamically inserts previous conversation messages into the prompt to maintain conversational context.

**4. HumanMessage & AIMessage**

Represent user messages and AI-generated responses in the conversation history.

**5. LCEL (LangChain Expression Language)**

Connects different LangChain components using the pipe operator.

```python
chain = prompt | llm | StrOutputParser()
```

**6. StrOutputParser**

Converts the language model output into a string.

**7. Streaming**

Uses `chain.stream()` to generate and display responses incrementally.

**8. Streamlit Session State**

Maintains conversation history across Streamlit application reruns.

**9. Cache Resource**

Uses `@st.cache_resource` to reuse the initialized LangChain chain instead of recreating it on every rerun.

## 🖥️ Application Preview

Add your application screenshot to the repository and display it here:

```markdown
![Chatbot Preview](assets/chatbot-preview.png)
```

## 🔮 Future Improvements

- Add persistent chat history using a database.
- Support PDF document uploads and question answering.
- Add conversation export functionality.
- Introduce customizable system prompts.
- Improve error handling and API status feedback.

## 👩‍💻 Author

**Prachi Raikwar**

B.Tech CSE (AI & ML) Student

- GitHub: [PrachiRaikwar-22](https://github.com/PrachiRaikwar-22)
- LinkedIn: [Prachi Raikwar](https://www.linkedin.com/in/prachi-raikwar-911526330/)

---

⭐ If you find this project useful, consider giving it a star!

*Built to explore the practical foundations of conversational AI and LLM-powered application development.*
