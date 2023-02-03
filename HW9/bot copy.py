from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token1 = "YOUR TOKEN"
bot = Bot(token = token1)
updater = Updater(token = token1)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! Отправь мне текст, и я удалю из него все слова, содержащие "абв".:)')

def delete_abv(update, context):
    text = update.message.text
    text = text.split()
    lst = list(filter(lambda word: 'абв' not in word.lower(), text))
    lst = ' '.join(lst)
    context.bot.send_message(update.effective_chat.id, lst)


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, delete_abv)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)

updater.start_polling()
updater.idle()