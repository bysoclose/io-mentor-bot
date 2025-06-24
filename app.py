	mport requests

api_key = os.environ["OPENAI_API_KEY"]  # .env ya da sistem değişkeninden gelsin
AGENT_ID = "SENIN_AGENT_IDIN"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {"role": "user", "content": "Hackathona nasıl katılırım?"}
    ],
    "agent_id": AGENT_ID
}

response = requests.post("https://api.io.net/v1/agent-chat", headers=headers, json=data)
print("Yanıt:", response.json())
