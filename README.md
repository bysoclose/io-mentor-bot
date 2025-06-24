# 🧠 AI Hack Mentor Bot

> An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity.

## 🚀 What is AI Hack Mentor Bot?

AI Hack Mentor Bot is an open-source assistant designed to summarize and analyze complex content (like documentation, research, or articles). It's built using the IO.net AI Agent infrastructure and runs on Llama 3-70B Instruct model.

Ideal for:
- Developers participating in hackathons
- Summarizing technical docs
- Mentoring teammates with dense information

## 💡 How It Works

The bot:
1. Accepts a large input (text, document, etc.)
2. Sends the objective to IO.net agent (via API)
3. Uses a powerful AI model to extract key insights
4. Prints a structured summary

## 🛠️ Tech Stack

- Python 3.12
- [IO.net AI Agents API](https://ai.io.net/ai/agents)
- Llama-3.3-70B-Instruct model
- Asyncio & Requests

## 🔧 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/bysoclose/io-mentor-bot.git
   cd io-mentor-bot
