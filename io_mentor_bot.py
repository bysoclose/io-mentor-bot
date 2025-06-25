import customtkinter as ctk
import asyncio
from dotenv import load_dotenv
import os
from PIL import Image
from customtkinter import CTkImage
from iointel import Agent, Workflow

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

agent = Agent(
    name="Super Agent",
    instructions="You are an assistant specialized in doing anything.",
    model="meta-llama/Llama-3.3-70B-Instruct",
    api_key=api_key,
    base_url="https://api.intelligence.io.solutions/api/v1"
)

async def run_workflow(user_input):
    workflow = Workflow(objective=user_input, client_mode=False)
    result = await workflow.custom(
        name="custom-task",
        objective="continue summarizing",
        instructions="Focus on previous history",
        agents=[agent]
    ).run_tasks()
    return result["results"]["custom-task"]

def on_submit():
    user_input = input_entry.get()
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", "⏳ Loading...\n")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(run_workflow(user_input))
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", result)
    # Add to chat history
    chat_textbox.configure(state="normal")
    chat_textbox.insert("end", f"You: {user_input}\nAgent: {result}\n\n")
    chat_textbox.configure(state="disabled")
    input_entry.delete(0, "end")

def copy_to_clipboard(text):
    app.clipboard_clear()
    app.clipboard_append(text)
    ctk.CTkMessagebox(title="Copied", message=f"'{text}' copied to clipboard!")

def on_click_copy(event, text_widget):
    text = text_widget.get("1.0", "end").strip()
    copy_to_clipboard(text)

app = ctk.CTk()
app.title("IO.NET Assistant")
app.geometry("700x700")

# Logo
try:
    image = Image.open("io_logo.png")
    image = image.resize((120, 40))
    logo_img = CTkImage(light_image=image, dark_image=image, size=(120,40))
    logo_label = ctk.CTkLabel(app, image=logo_img, text="")
    logo_label.pack(pady=10)
except Exception:
    logo_label = ctk.CTkLabel(app, text="IO.NET Assistant", font=ctk.CTkFont(size=20, weight="bold"))
    logo_label.pack(pady=10)

input_entry = ctk.CTkEntry(app, placeholder_text="Write your question...", width=600)
input_entry.pack(pady=10)

submit_btn = ctk.CTkButton(app, text="SEND", command=on_submit)
submit_btn.pack(pady=5)

chat_textbox = ctk.CTkTextbox(app, width=650, height=150)
chat_textbox.pack(pady=10)
chat_textbox.configure(state="disabled")

output_textbox = ctk.CTkTextbox(app, width=650, height=200)
output_textbox.pack(pady=10)
output_textbox.configure(state="disabled")

# Links label
link_label = ctk.CTkLabel(app, text="Links (Click to copy):", font=ctk.CTkFont(size=14, weight="bold"))
link_label.pack(pady=(20,5))

# Github link text
github_text = ctk.CTkTextbox(app, width=650, height=25)
github_text.insert("0.0", "https://github.com/bysoclose/io-mentor-bot")
github_text.configure(state="disabled")
github_text.pack(pady=5)
github_text.bind("<Button-1>", lambda e: on_click_copy(e, github_text))

# Discord link text
discord_text = ctk.CTkTextbox(app, width=650, height=25)
discord_text.insert("0.0", "https://discord.gg/cXN3WghNhG")
discord_text.configure(state="disabled")
discord_text.pack(pady=5)
discord_text.bind("<Button-1>", lambda e: on_click_copy(e, discord_text))

# Twitter link text
twitter_text = ctk.CTkTextbox(app, width=650, height=25)
twitter_text.insert("0.0", "https://twitter.com/bilal_ibanoglu")
twitter_text.configure(state="disabled")
twitter_text.pack(pady=5)
twitter_text.bind("<Button-1>", lambda e: on_click_copy(e, twitter_text))

# Asyncio and Tkinter integration
async def main_loop():
    while True:
        app.update()
        await asyncio.sleep(0.01)

asyncio.run(main_loop())
