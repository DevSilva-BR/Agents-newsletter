import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    text = ""
    send_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(send_msg, send_welcome)

caminho = "src/post.md"
def send_post(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        result = file.read()
    bot.send_message(message.chat.id, result, parse_mode="Markdown")

cam = send_post(caminho)

bot.infinity_polling()