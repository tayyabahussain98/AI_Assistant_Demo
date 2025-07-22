# 💬 AI Assistant Demo (Gemini + Streamlit)

This is a simple AI assistant built using **Gemini 2.5 Flash API** and deployed using **Streamlit**. It allows users to input questions and receive intelligent, real-time answers.

---

## 🌟 Features

- ✅ Gemini-powered assistant (Google's latest AI)
- ✅ Clean, simple UI (built with Streamlit)
- ✅ Instant answers to user questions
- ✅ Secure API key management via Streamlit secrets

---

## 🖥️ Live Demo

🔗 [Click here to try the live assistant](https://aiassistantdemo-tayyaba98.streamlit.app/)

> Replace with your actual deployed link.

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/tayyabahussain98/AI_Assistant_Demo.git
cd ai-assistant-demo
```
### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key
Create a file at this path:

```bash
.streamlit/secrets.toml
```
Paste your Gemini API key:

```bash
GEMINI_API_KEY = "your_actual_api_key_here"
```
Never share your actual key in public repos.

### 4. Run the App

```bash
streamlit run main.py
```
