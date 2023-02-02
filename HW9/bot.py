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
    list = text.split()
    new_list = []
    for word in list:
        if 'абв' not in word: new_list.append(word)
    text = ' '.join(map(str, new_list))
    context.bot.send_message(update.effective_chat.id, text)


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, delete_abv)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)

updater.start_polling()
updater.idle()