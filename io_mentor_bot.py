from dotenv import load_dotenv
import os
import asyncio
from iointel import Agent, Workflow

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
# Doğrudan API anahtarını gir (güvenli değilse ortam değişkeni kullan)
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
