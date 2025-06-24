# 🧠 AI Hack Mentor Bot

> An intelligent assistant powered by IO.net's LLM agents to help developers navigate complex information with clarity.

## 🚀 What is AI Hack Mentor Bot?

AI Hack Mentor Bot is an open-source assistant designed to summarize and analyze complex content (like documentation, research, or articles). It's built using the IO.net AI Agent infrastructure and runs on Llama 3-70B Instruct model.

Ideal for:
- Developers participating in hackathons
- Summarizing technical docs
- Mentoring teammates with dense information

## 🚀 Features

- 📚 Summarize long technical texts and documents  
- 💡 Continue and elaborate on topics using LLMs  
- 🔗 Connects to [IO Intelligence API](https://intelligence.io.solutions/)  
- 🧑‍💻 Uses powerful models like `Llama-3-70B-Instruct`  
- ✅ Async support for efficient performance

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


Create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate


Install the required dependencies:
pip install -r requirements.txt


🔐 API Key Setup
This project requires an IO.net API key.
     1.Go to https://intelligence.io.solutions and log in.
     2.Generate your API key.
     3.Create a .env file in the project root with the following content:

Code : OPENAI_API_KEY=io-v2-xxxxxxxxxxxxxxxxxxxxxxxx

▶️ Usage
To run the mentor bot:
python io_mentor_bot.py



📄 Example Output
The global electric vehicle (EV) market has a rich history...
From early inventions in the 1800s to Tesla's modern breakthroughs...


📁 Project Structure

io-mentor-bot/
├── io_mentor_bot.py        # Main script to execute tasks
├── app.py                  # Flask API (optional use)
├── .env                    # API key (excluded from Git)
├── .gitignore              # Git exclusions
└── requirements.txt        # Dependencies


🪪 License
This project is open-source and licensed under the MIT License.


🤝 Contributing
Contributions, issues, and feature requests are welcome.
Feel free to open a pull request or submit an issue.


🌍 Credits
Made with ❤️ bysoclosee (BİLAL İBANOĞLU)
Powered by IO.net Intelligence API
Discord : Bilalibanoğlu
x :Bilal_ibanoglu

