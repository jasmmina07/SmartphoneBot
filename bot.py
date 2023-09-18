from pprint import pprint
from db import DB
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
import os

db_py=DB("data.json")

TOKEN=os.environ['TOKEN']

def start(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id

    Shop=InlineKeyboardButton(text="🛍 Shop",callback_data="Shop")
    Cart=InlineKeyboardButton(text="📦 Cart",callback_data="Cart")
    Contact=InlineKeyboardButton(text="📞 Contact",callback_data="Contact")
    About=InlineKeyboardButton(text="📝 About",callback_data="About")

    keyboard=InlineKeyboardMarkup([[Shop,Cart],[Contact,About]])


    bot.sendMessage(chat_id,text="Welcome to smartphone bot",reply_markup=keyboard)

def main_menu(update: Update, context: CallbackContext):
    query = update.callback_query

    Shop=InlineKeyboardButton(text="🛍 Shop",callback_data="Shop")
    Cart=InlineKeyboardButton(text="📦 Cart",callback_data="Cart")
    Contact=InlineKeyboardButton(text="📞 Contact",callback_data="Contact")
    About=InlineKeyboardButton(text="📝 About",callback_data="About")

    keyboard=InlineKeyboardMarkup([[Shop,Cart],[Contact,About]])
    query.edit_message_text(text="Smartphone shop",reply_markup=keyboard)

def product(update: Update, context: CallbackContext):
    query = update.callback_query
    
    buttons = []
    for name in db_py.get_tables():
        button = InlineKeyboardButton(text=name,callback_data=f"products_{name}")
        buttons.append([button])
    back = InlineKeyboardButton(text="⬅️ back",callback_data="main_menu")
    buttons.append([back])
    keyboard=InlineKeyboardMarkup(buttons)
    query.edit_message_text(text="Choose a brand",reply_markup=keyboard)

def products(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    text, brand = data.split('_')
    data = db_py.get_phone_list(brand)

    buttons=[]
    for i in data[:10]:
        button=InlineKeyboardButton(text=i['name'],callback_data=f"phone_{brand}_{i.doc_id}")
        buttons.append([button])

    back = InlineKeyboardButton(text="⬅️ back",callback_data="Shop")
    buttons.append([back])
    keyboard=InlineKeyboardMarkup(buttons)
    query.edit_message_text(text=brand,reply_markup=keyboard)

def phone(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat.id
    bot = context.bot
    data = query.data
    text, brand, doc_id = data.split('_')
    phone = db_py.get_phone(brand, doc_id)

    text=f"name: {phone['name']}\nprice: {phone['price']} $\ncolor: {phone['color']} "
    
    bot.sendPhoto(chat_id, phone['img_url'], caption=text)
    query.answer("Done!")

updater=Updater(token=TOKEN)
dp=updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CallbackQueryHandler(product, pattern="Shop"))
dp.add_handler(CallbackQueryHandler(products, pattern="products"))
dp.add_handler(CallbackQueryHandler(phone, pattern="phone"))
dp.add_handler(CallbackQueryHandler(main_menu, pattern="main_menu"))
# dp.add_handler(CallbackQueryHandler(main))

updater.start_polling()
updater.idle()