# 🧠 AI Hack Mentor Bot

> An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity. Built for the **Launch IO Hackathon**! 🚀

---

## 🎯 What is AI Hack Mentor Bot?

**AI Hack Mentor Bot** is an open-source, multi-language AI assistant designed to summarize and analyze complex content like documentation, research papers, or articles. Powered by the **IO.net AI Agent infrastructure** and the **Llama-3.3-70B-Instruct** model, it’s your go-to tool for hackathons and technical tasks.

### Ideal for:
- 🏆 Developers crushing it at hackathons
- 📝 Summarizing dense technical documentation
- 🤝 Mentoring teammates with clear insights

---

## ✨ Features

- 🌍 **Multi-language Support**: Switch between English (🇬🇧), Turkish (🇹🇷), and German (🇩🇪) with flag icons
- 📚 **Text Summarization**: Condenses long texts into concise summaries with key points
- 💡 **Smart Agent System**: Detects and suggests the right agent (e.g., Translation, Summary) for your task
- 🔗 **IO.net Integration**: Connects to the [IO Intelligence API](https://intelligence.io.solutions/)
- 🧑‍💻 **Powerful AI**: Uses `Llama-3.3-70B-Instruct` for accurate results
- ✅ **Async Execution**: Efficient performance with `asyncio`
- 🇹🇷 **Turkish Character Support**: Handles characters like `ş`, `ğ`, `ı` flawlessly
- 📱 **Social Media Links**: Copy GitHub, Discord, and Twitter links with a click
- 🖼️ **Sleek UI**: PyQt5-powered interface with agent and flag icons
- 🛠️ **Modular Code**: Organized into `utils.py`, `agents_config.py`, and `workflow.py`

---

## 📸 Preview

![AI Hack Mentor Bot UI](https://github.com/user-attachments/assets/1da30007-b5a3-4fdc-8d1e-9e0f8e343b45)

🎥 Watch the demo: [AI Hack Mentor Bot Video](https://github.com/user-attachments/assets/e7c8c6b7-8b6c-4e47-b8d7-ee9377b00503)

---

## 💡 How It Works

1. 📥 Input text or documents via the PyQt5 interface
2. 🤖 Select an agent (e.g., Summary, Translation) or let the bot suggest one
3. 🔗 Send the task to IO.net’s AI agents via API
4. 📤 Receive a structured summary or analysis in your chosen language

---

## 🛠️ Tech Stack

- 🐍 **Python 3.12**
- 🎨 **PyQt5**: For the user-friendly interface
- 🌐 **IO.net AI Agents API**: Powers the backend
- 🧠 **Llama-3.3-70B-Instruct**: For intelligent processing
- ⚡️ **Asyncio & Requests**: For efficient API calls
- 📦 **python-dotenv**: For secure API key management
- 🔄 **nest-asyncio**: For async compatibility
- 🧩 **iointel**: Custom library for IO.net integration

---

## 🔧 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bysoclose/io-mentor-bot.git
   cd io-mentor-bot
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/WSL
   .\venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **🔐 Set up API key**:
   - Go to [IO Intelligence](https://intelligence.io.solutions), log in, and generate an API key.
   - Create a `.env` file in the project root:
     ```bash
     echo "OPENAI_API_KEY=io-v2-xxxxxxxxxxxxxxxxxxxxxxxx" > .env
     ```

5. **▶️ Run the bot**:
   ```bash
   python io_mentor_bot.py
   ```

---

## 📄 Example Output

**Input**:
```
The global electric vehicle (EV) market has a rich history... From early inventions in the 1800s to Tesla's modern breakthroughs...
```

**Output**:
```
Summary: The EV market evolved from 1800s inventions to modern Tesla innovations.
Key Points: Early EV inventions, Tesla's impact.
```

---

## 📁 Project Structure

```
io-mentor-bot/
├── io_mentor_bot.py        # Main script with PyQt5 UI
├── utils.py                # Helper functions (e.g., fix_turkish_chars)
├── agents_config.py        # Agent configurations and translations
├── workflow.py             # Async task execution
├── icons/                  # Flag and agent icons (uk.png, tr.png, etc.)
├── .env                    # API key (git ignored)
├── .gitignore              # Excludes Zone.Identifier, debug.log, etc.
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! 🚀
- Fork the repo and submit a pull request.
- Report issues or suggest features on [GitHub Issues](https://github.com/bysoclose/io-mentor-bot/issues).

---

## 🌟 Credits

Made with ❤️ by [Bilal İbanoğlu](https://github.com/bysoclose) for the **Launch IO Hackathon**.  
Powered by [IO.net Intelligence API](https://intelligence.io.solutions/).

### Connect with me:
- 📂 [GitHub](https://github.com/bysoclose/io-mentor-bot)
- 💬 [Discord](https://discord.gg/cXN3WghNhG)
- 🐦 [Twitter/X](https://twitter.com/bilal_ibanoglu)
