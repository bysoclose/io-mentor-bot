	mport requests

API_KEY = "io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6ImVjNjRlYWY5LWFhM2YtNDJhNi05NzM4LTI3NzY2ZTU1NWUwMCIsImV4cCI6NDkwNDM3Njc0OX0.H7YqxBIsoiI3rByKh094CjXNlybHcwhWOFTbTvLzYVMGd7lDBZkXL_jW8Lq1fHOcAeIEsl502muZhUQWZL5Kkw"
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
