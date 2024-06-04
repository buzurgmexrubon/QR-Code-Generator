import os

import pyqrcode
import telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TOKEN")

bot = telebot.TeleBot(API_KEY)


def generate_qr(link):
    url = pyqrcode.create(link)

    url.png("myqr.png", scale=6)


def delete_qr():
    if os.path.exists("myqr.png"):
        os.remove("myqr.png")


# TBD
# def handle_message(update, context):
#     user_first_name = update.message.chat.first_name
#     user_last_name = update.message.chat.last_name
#     username = update.message.chat.username
#     update.message.reply_text(
#         f"Hey👋 {user_first_name} {user_last_name} aka @{username} welcome to the Open-Bot type: /help to explore options."
#     )
#
#


# This Decorator handle's the message with and /start
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(
        message,
        "Welcome to Open-Bot Powered by Open-Source and Developed by @thisiskanishkP",
    )
    bot.send_photo(chat_id=message.chat.id, photo=open("images/octocat.png", "rb"))


# This Decorator helps in handling the message with /help
@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.reply_to(
        message,
        """\
    The Following Commands can we user

     /start - to say welcome message
     /help - to get help
     /qr <link of data> - to generate qr code
    """,
    )


# This Decorator helps in handling the message with /qr
@bot.message_handler(commands=["qr"])
def handle_qr(message):
    chat_id = message.chat.id
    text = message.text
    link = text[4::]
    try:
        generate_qr(link=link)
        bot.send_photo(chat_id=chat_id, photo=open("myqr.png", "rb"))
        delete_qr()
    except:
        bot.reply_to(message, f"QR of this {link} can't be generated")
        delete_qr()


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # bot.reply_to(message, message.text)
    chat_id = message.chat.id
    text = message.text
    try:
        generate_qr(link=text)
        bot.send_photo(chat_id=chat_id, photo=open("myqr.png", "rb"))
        delete_qr()
    except:
        bot.reply_to(message, f"QR of this {text} can't be generated")
        delete_qr()


bot.infinity_polling()
