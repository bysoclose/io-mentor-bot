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

message_history = []  # Mesaj geçmişi (kullanıcı ve agent mesajları)

async def run_workflow(user_input):
    workflow = Workflow(objective=user_input, client_mode=False)
    result = await workflow.custom(
        name="custom-task",
        objective="continue summarizing",
        instructions="Focus on previous history",
        agents=[agent]
    ).run_tasks()
    return result["results"]["custom-task"]

def update_chat_history():
    chat_textbox.configure(state="normal")
    chat_textbox.delete("1.0", "end")
    for speaker, msg in message_history:
        prefix = "Sen: " if speaker == "user" else "Agent: "
        chat_textbox.insert("end", prefix + msg + "\n\n")
    chat_textbox.configure(state="disabled")

def on_submit():
    user_input = input_entry.get().strip()
    if not user_input:
        return
    
    # Mesajı geçmişe ekle ve göster
    message_history.append(("user", user_input))
    update_chat_history()
    
    # Butonu ve giriş kutusunu devre dışı bırak
    submit_btn.configure(state="disabled")
    input_entry.configure(state="disabled")
    
    output_textbox.configure(state="normal")
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", "⏳ LOADING...\n")
    output_textbox.configure(state="disabled")
    
    # Asenkron çağrıyı event loop ile yap
    asyncio.create_task(handle_agent_response(user_input))

async def handle_agent_response(user_input):
    result = await run_workflow(user_input)
    message_history.append(("agent", result))
    update_chat_history()

    output_textbox.configure(state="normal")
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", result)
    output_textbox.configure(state="disabled")
    
    # Buton ve giriş kutusunu tekrar aktif et
    submit_btn.configure(state="normal")
    input_entry.configure(state="normal")
    input_entry.delete(0, 'end')

# Ana pencere
app = ctk.CTk()
app.title("IO.NET Assistant")
app.geometry("700x600")

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

# Giriş kutusu
input_entry = ctk.CTkEntry(app, placeholder_text="Write your question...", width=500)
input_entry.pack(pady=10)

# Gönder butonu
submit_btn = ctk.CTkButton(app, text="SEND", command=on_submit)
submit_btn.pack(pady=5)

# Geçmiş mesajlar textbox (salt okunur)
chat_textbox = ctk.CTkTextbox(app, width=650, height=200)
chat_textbox.pack(pady=10)
chat_textbox.configure(state="disabled")

# Yanıt kutusu (tek mesaj gösteriyor)
output_textbox = ctk.CTkTextbox(app, width=650, height=300)  # Yüksekliği 150'den 300'e çıkardım
output_textbox.pack(pady=10, fill="both", expand=True)     # fill ve expand ile esnek boyutlanma
output_textbox.configure(state="disabled")


# Asyncio ve Tkinter entegrasyonu için:
async def main_loop():
    while True:
        app.update()
        await asyncio.sleep(0.01)

asyncio.run(main_loop())
