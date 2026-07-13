# 🤖 AI Chatbot

A simple, friendly AI chatbot built with **Streamlit** and **Mistral AI**, featuring a persistent chat interface with a touch of humor and sarcasm baked into its personality.

---

## ✨ Features

- 💬 Clean, chat-style UI powered by Streamlit's native chat components
- 🧠 Powered by Mistral's `mistral-small-2506` model via LangChain
- 😄 Custom personality — friendly, humorous, and lightly sarcastic, with emojis in every reply
- 🗂️ Maintains conversation history within a session
- 🛑 Type `0` to end the chat session
- 🖥️ Two ways to run it — a web-based Streamlit UI or a lightweight local terminal version

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [LangChain](https://www.langchain.com/) — LLM orchestration
- [langchain-mistralai](https://pypi.org/project/langchain-mistralai/) — Mistral AI integration
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

---

## 📋 Requirements

- Python 3.9+
- A [Mistral AI](https://console.mistral.ai/) API key

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit python-dotenv langchain-core langchain-mistralai
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   MISTRAL_API_KEY=your_api_key_here
   ```

   > ⚠️ **Important:** The `.env` file is **not included** in this repo — you need to create it yourself and add your **own** Mistral AI API key. Get one from [console.mistral.ai](https://console.mistral.ai/). Without a valid key, the chatbot will not be able to connect to the model.

---

## 🚀 Usage

You can run the chatbot in two ways:

### Option 1: Web UI (Streamlit)

```bash
streamlit run chatbotUI.py
```

This opens the chatbot in your default browser at `http://localhost:8501`, with a full chat-style interface.

### Option 2: Local terminal version

```bash
python chatbot.py
```

This runs the bot directly in your terminal — handy for quick local testing without launching a browser.

In both versions, type `0` at any time to end the session.

---

## 📂 Project Structure

```
├── chatbotUI.py       # Streamlit web app version
├── chatbot.py          # Local terminal version, for running the bot without a browser
├── .env                # Environment variables (not committed to version control)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 📦 requirements.txt

```
streamlit
python-dotenv
langchain-core
langchain-mistralai
```

---

## ⚠️ Known Issues

- `response.text` is used to extract the AI's reply. In some versions of `langchain-core`, `AIMessage.text` is a **method**, not an attribute. If you encounter errors or unexpected output, replace it with `response.content`, which is the standard way to access message text in LangChain.

---

## 🔒 Notes on Security

- Never commit your `.env` file or expose your `MISTRAL_API_KEY` publicly.
- Add `.env` to your `.gitignore` file.

---

## 📄 License

This project is open source and available for personal and educational use.
