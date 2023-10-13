import telegram
import os 
from flask import Flask, request

TOKEN="6683059977:AAGFDLPV6W8GmlMtnkuFSfSOuphU_bXt0Ww"
bot = telegram.Bot(TOKEN)

url = "https://jasmina07.pythonanywhere.com/webhook/"

# print(bot.delete_webhook())
print(bot.set_webhook(url))

print(bot.get_webhook_info())