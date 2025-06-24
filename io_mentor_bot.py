from iointel import Agent, Workflow
import asyncio

# Doğrudan API anahtarını gir (güvenli değilse ortam değişkeni kullan)
api_key = "io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6ImVjNjRlYWY5LWFhM2YtNDJhNi05NzM4LTI3NzY2ZTU1NWUwMCIsImV4cCI6NDkwNDM3Njc0OX0.H7YqxBIsoiI3rByKh094CjXNlybHcwhWOFTbTvLzYVMGd7lDBZkXL_jW8Lq1fHOcAeIEsl502muZhUQWZL5Kkw"  # ← Buraya kendi IO API anahtarını yaz

text = """The global electric vehicle (EV) market is witnessing exponential growth..."""

agent = Agent(
    name="Super Agent",
    instructions="You are an assistant specialized in doing anything.",
    model="meta-llama/Llama-3.3-70B-Instruct",
    api_key=api_key,
    base_url="https://api.intelligence.io.solutions/api/v1"
)

workflow = Workflow(objective=text, client_mode=False)

async def run_workflow():
    result = await workflow.custom(
        name="custom-task",
        objective="continue summarizing",
        instructions="Focus on previous history",
        agents=[agent]
    ).run_tasks()
    return result["results"]

results = asyncio.run(run_workflow())
print(results)
