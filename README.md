🧠 AI Hack Mentor Bot

An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity. Built for the Launch IO Hackathon! 🚀


🎯 What is AI Hack Mentor Bot?
AI Hack Mentor Bot is an open-source, multi-language AI assistant designed to summarize and analyze complex content like documentation, research papers, or articles. Powered by the IO.net AI Agent infrastructure and the Llama-3.3-70B-Instruct model, it’s your go-to tool for hackathons and technical tasks.
Ideal for:

🏆 Developers crushing it at hackathons
📝 Summarizing dense technical documentation
🤝 Mentoring teammates with clear insights


✨ Features

🌍 Multi-language Support: Switch between English (🇬🇧), Turkish (🇹🇷), and German (🇩🇪) with flag icons
📚 Text Summarization: Condenses long texts into concise summaries with key points
💡 Smart Agent System: Detects and suggests the right agent (e.g., Translation, Summary) for your task
🔗 IO.net Integration: Connects to the IO Intelligence API
🧑‍💻 Powerful AI: Uses Llama-3.3-70B-Instruct for accurate results
✅ Async Execution: Efficient performance with asyncio
🇹🇷 Turkish Character Support: Handles characters like ş, ğ, ı flawlessly
📱 Social Media Links: Copy GitHub, Discord, and Twitter links with a click
🖼️ Sleek UI: PyQt5-powered interface with agent and flag icons
🛠️ Modular Code: Organized into utils.py, agents_config.py, and workflow.py


📸 Preview

🎥 Watch the demo: AI Hack Mentor Bot Video

💡 How It Works

📥 Input text or documents via the PyQt5 interface
🤖 Select an agent (e.g., Summary, Translation) or let the bot suggest one
🔗 Send the task to IO.net’s AI agents via API
📤 Receive a structured summary or analysis in your chosen language


🛠️ Tech Stack

🐍 Python 3.12
🎨 PyQt5: For the user-friendly interface
🌐 IO.net AI Agents API: Powers the backend
🧠 Llama-3.3-70B-Instruct: For intelligent processing
⚡️ Asyncio & Requests: For efficient API calls
📦 python-dotenv: For secure API key management
🔄 nest-asyncio: For async compatibility
🧩 iointel: Custom library for IO.net integration


🔧 How to Run

Clone the repository:
git clone https://github.com/bysoclose/io-mentor-bot.git
cd io-mentor-bot


Create a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate  # Linux/WSL
.\venv\Scripts\activate   # Windows


Install dependencies:
pip install -r requirements.txt


🔐 Set up API key:

Go to IO Intelligence, log in, and generate an API key.
Create a .env file in the project root:echo "OPENAI_API_KEY=io-v2-xxxxxxxxxxxxxxxxxxxxxxxx" > .env




▶️ Run the bot:
python io_mentor_bot.py




📄 Example Output
Input:
The global electric vehicle (EV) market has a rich history... From early inventions in the 1800s to Tesla's modern breakthroughs...

Output:
Summary: The EV market evolved from 1800s inventions to modern Tesla innovations.
Key Points: Early EV inventions, Tesla's impact.


📁 Project Structure
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


🪪 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! 🚀

Fork the repo and submit a pull request.
Report issues or suggest features on GitHub Issues.


🌟 Credits
Made with ❤️ by Bilal İbanoğlu for the Launch IO Hackathon.Powered by IO.net Intelligence API.
Connect with me:

📂 GitHub
💬 Discord
🐦 Twitter/X
