from django.shortcuts import render, redirect
from .models import Message
from openai import OpenAI
import os
from dotenv import load_dotenv
from telegram import Bot
from django.contrib.auth.decorators import login_required
from authentication.models import Customer_user

def index(request):
    return render(request, "main/main.html")



def edit_message_via_GPT(text):
#     load_dotenv()
#     api_key = os.getenv("GPT_api_key")
#     client = OpenAI(api_key)
#     response = client.chat.completions.create(
#         model =  "gpt-4",
#   messages = [
#     {
#       "role": "system",
#       "content": "You are a helpful assistant. Please rewrite my message in a formal/business style."
#     },
#     {
#       "role": "user",
#       "content": text
#     }
#     ]
#     )
    
#     return response['choices'][0]['message']['content']
    return text + " edited"


@login_required
async def send_message(request):

    if request.method == "POST":
        text = request.POST["message"]

        edited = edit_message_via_GPT(text)

        await Message.objects.acreate(original_text = text, edited_text = edited, owner = request.user)

        return redirect("history")
    return render(request, "main/send_message.html")

@login_required
async def send_to_telegram(request):
    if request.method == "POST":
    
        text = request.POST["message"]
        edited_message = edit_message_via_GPT(text)
        load_dotenv()
        api_token = os.getenv("telegram_bot_api")
        chat_id = os.getenv("telegram_chat_id")
        bot = Bot(api_token)
        await Message.objects.acreate(original_text = text, edited_text = edited_message, owner = request.user)
        await bot.send_message(chat_id, f"Message from {request.user}: {edited_message}")
        
        return redirect("history")
    return render(request, "main/send_message.html")


@login_required
def history(request):
    message = Message.objects.filter(owner = request.user)
    return render(request, "main/history.html", {"messages":message})
