import customtkinter as ctk
import asyncio
from dotenv import load_dotenv
import os
from PIL import Image
from customtkinter import CTkImage
from iointel import Agent, Workflow
import nest_asyncio
from datetime import datetime

nest_asyncio.apply()

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

def copy_to_clipboard(text):
    app.clipboard_clear()
    app.clipboard_append(text)
    ctk.CTkMessagebox(title="Copied", message=f"'{text}' copied to clipboard!")

def on_click_copy(event, text_widget):
    text = text_widget.get("1.0", "end").strip()
    copy_to_clipboard(text)

async def update_loading_time():
    # This coroutine updates loading_label with elapsed seconds during loading
    global loading_start_time
    while loading_label.cget("text").startswith("⏳ Loading"):
        elapsed = int((datetime.now() - loading_start_time).total_seconds())
        loading_label.configure(text=f"⏳ Loading... {elapsed}s")
        await asyncio.sleep(1)
    loading_label.configure(text="")  # Clear when done

async def process_user_input(user_input):
    global loading_start_time
    loading_start_time = datetime.now()
    loading_label.configure(text="⏳ Loading... 0s")
    submit_btn.configure(state="disabled")

    # Start coroutine to update loading time display
    asyncio.create_task(update_loading_time())

    try:
        result = await run_workflow(user_input)
    except Exception as e:
        result = f"Error: {str(e)}"

    output_textbox.configure(state="normal")
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", result)
    output_textbox.configure(state="disabled")

    chat_textbox.configure(state="normal")
    chat_textbox.insert("end", f"You: {user_input}\nAgent: {result}\n\n")
    chat_textbox.configure(state="disabled")

    input_entry.delete(0, "end")

    loading_label.configure(text="")
    submit_btn.configure(state="normal")

def on_submit():
    user_input = input_entry.get().strip()
    if not user_input:
        return
    output_textbox.configure(state="normal")
    output_textbox.delete("1.0", "end")
    asyncio.create_task(process_user_input(user_input))

def clear_chat_history():
    chat_textbox.configure(state="normal")
    chat_textbox.delete("1.0", "end")
    chat_textbox.configure(state="disabled")

def update_datetime_label():
    now = datetime.now()
    datetime_label.configure(text=now.strftime("%Y-%m-%d %H:%M:%S"))
    app.after(1000, update_datetime_label)  # Update every 1 second

app = ctk.CTk()
app.title("IO.NET Assistant")
app.geometry("720x820")

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

# DateTime label at top-right corner
datetime_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=12))
datetime_label.place(relx=0.95, rely=0.02, anchor="ne")
update_datetime_label()

input_entry = ctk.CTkEntry(app, placeholder_text="Write your question...", width=680)
input_entry.pack(pady=10)

submit_btn = ctk.CTkButton(app, text="SEND", command=on_submit)
submit_btn.pack(pady=5)

loading_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14, weight="bold"), text_color="orange")
loading_label.pack(pady=5)

chat_textbox = ctk.CTkTextbox(app, width=680, height=150)
chat_textbox.pack(pady=10)
chat_textbox.configure(state="disabled")

output_textbox = ctk.CTkTextbox(app, width=680, height=300, wrap="word")
output_textbox.pack(pady=10)
output_textbox.configure(state="disabled")

# Clear chat history button
clear_chat_btn = ctk.CTkButton(app, text="Clear Chat History", command=clear_chat_history)
clear_chat_btn.pack(pady=5)

# Links label
link_label = ctk.CTkLabel(app, text="Links (Click to copy):", font=ctk.CTkFont(size=14, weight="bold"))
link_label.pack(pady=(20,5))

# Github link text
github_text = ctk.CTkTextbox(app, width=680, height=25)
github_text.insert("0.0", "https://github.com/bysoclose/io-mentor-bot")
github_text.configure(state="disabled")
github_text.pack(pady=5)
github_text.bind("<Button-1>", lambda e: on_click_copy(e, github_text))

# Discord link text
discord_text = ctk.CTkTextbox(app, width=680, height=25)
discord_text.insert("0.0", "https://discord.gg/cXN3WghNhG")
discord_text.configure(state="disabled")
discord_text.pack(pady=5)
discord_text.bind("<Button-1>", lambda e: on_click_copy(e, discord_text))

# Twitter link text
twitter_text = ctk.CTkTextbox(app, width=680, height=25)
twitter_text.insert("0.0", "https://twitter.com/bilal_ibanoglu")
twitter_text.configure(state="disabled")
twitter_text.pack(pady=5)
twitter_text.bind("<Button-1>", lambda e: on_click_copy(e, twitter_text))

# Asyncio and Tkinter integration (run main loop)
async def main_loop():
    while True:
        app.update()
        await asyncio.sleep(0.01)

asyncio.run(main_loop())
