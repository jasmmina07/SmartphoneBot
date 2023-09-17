from pprint import pprint
from db import DB
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler

db_py=DB("data.json")
TOKEN="6662177620:AAH-dEI7vGQWh-v3_piDLmm0qRnxptBqF2U"

def shop(update:Update, context:CallbackContext):
    data=db.get_tables()
    return data

def start(update:Update, context:CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id

    Shop=InlineKeyboardButton(text="🛍 Shop",callback_data="Shop")
    Cart=InlineKeyboardButton(text="📦 Cart",callback_data="Cart")
    Contact=InlineKeyboardButton(text="📞 Contact",callback_data="Contact")
    About=InlineKeyboardButton(text="📝 About",callback_data="About")

    keyboard=InlineKeyboardMarkup([[Shop,Cart],[Contact,About]])


    bot.sendMessage(chat_id,text="Welcome to smartphone bot",reply_markup=keyboard)
def main(update:Update,context:CallbackContext):
    bot=context.bot
    
    query=update.callback_query
    data=query.data
    chat_id = query.message.chat.id
    brand='Apple'

    if data=="Shop":
        db_py.data_shop(query)
    if str(data) in db_py.get_phone():
        db_py.products(data,query)
        brand=str(data)
    if data=="back":
        db_py.data_back_shop(query)
    if data=="back_brands":
        db_py.data_shop(query)
    if str(data).isdigit():
        photo,text=(db_py.phone_photo(brand,str(data)))
        bot.sendPhoto(chat_id,photo,caption=text)
        
    

updater=Updater(token=TOKEN)
db=updater.dispatcher

db.add_handler(CommandHandler("start",start))
db.add_handler(CallbackQueryHandler(main))

updater.start_polling()
updater.idle()