# 🛍️ ShopBot: Building an E-commerce Chatbot with Python and OpenAI

ShopBot is a conversational AI assistant built using **Python**, **OpenAI GPT**, and **Streamlit**. It enhances online fashion shopping by guiding users through product browsing, information lookup, and checkout – all through a sleek chat interface.

---

## 📑 Table of Contents

- [🧠 Introduction](#-introduction)  
- [🚀 Getting Started](#-getting-started)  
- [⚙️ How ShopBot Works](#️-how-shopbot-works)  
- [💬 Chat with ShopBot](#-chat-with-shopbot)  
- [🛠️ Tech Stack](#️-tech-stack)  
- [🧩 Features](#-features)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)

---

## 🧠 Introduction

ShopBot is your AI-powered shopping assistant built to:

- Engage with customers using a natural chat interface  
- Recommend products based on user preferences  
- Guide users through product listings and checkout  
- Offer helpful, polite, and intelligent responses  

This project demonstrates how large language models can be customized for real-world tasks like e-commerce using the OpenAI API.

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.8+
- OpenAI Python SDK
- Streamlit
- pandas (for product table handling)

🔑 Setup
1.Place your OpenAI API key inside a file called Key.txt:
OPENAI_API_KEY=your_key_here

2.Run the chatbot:
streamlit run app.py

## ⚙️ How ShopBot Works
ShopBot uses OpenAI’s gpt-3.5-turbo model to interpret customer queries and recommend relevant products from your catalog.

The catalog is passed to the AI as structured Markdown, allowing ShopBot to understand and refer to actual items during conversations.

🔄 Main Flow:
📦 Load product list and initialize system context

💬 Capture user input via Streamlit’s chat interface

🧠 Send messages to OpenAI Chat Completions API

🤖 Display dynamic, friendly responses in real time

💬 Chat with ShopBot
Here’s a quick demo of how you can interact:

Copy code:
User: Hi, I’m looking for something elegant for a wedding.
ShopBot: Great choice! You may love our Elegant Evening Gown, available in Black, Navy Blue, and Burgundy...
✅ ShopBot understands natural language
✅ Recommends products based on category, price, color, etc.
✅ Makes online shopping smooth, friendly, and helpful

🛠️ Tech Stack
💬 OpenAI GPT-3.5 Turbo – for conversational intelligence

🖥️ Streamlit – for real-time chat interface

🐍 Python – scripting and integration

🗂️ Markdown & CSV – to manage product data

🧑🏻‍💻 VS Code - Recommended IDE for editing and testing

🎨 Custom CSS (optional) – to style the chatbot

🧩 Features
🛍️ Intelligent product recommendations

💬 Friendly and helpful conversation style

🧠 Context-aware responses using LLM

📁 Easily updatable product catalog

💡 Beginner-friendly Python codebase

🤝 Contributing
Pull requests are welcome! If you have suggestions for improvements, features, or bug fixes, feel free to open an issue.

🪪 License
This project is licensed under the MIT License.

📸 Preview
Made with ❤️ using Python, Streamlit & OpenAI
Let me know if you'd like to add a [preview GIF](f), [code badge section](f), or tips for deploying it to [Streamlit Cloud](f)!
