from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "6000845921:AAG705zxRffEn6RSOIMiHBvQ15AvDFhNRXM"
bot = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Введите выражение: ')

def calc(update: Update, context: CallbackContext):
    expression = update.message.text
    expr_list = GetStepsLst(expression)
    oper_count = GetOperationsCount(expr_list)
    res_list = expr_list[:]
    for _ in range(oper_count): 
        res_list = OperProcess(res_list)
    context.bot.send_message(update.effective_chat.id, f'{expression} = {res_list[0]}')
    log(res_list[0], update, context)
    
def GetStepsLst(inData):
    res = ''
    for el in inData:
        if el.isdigit(): 
            res += el
        else: res += f' {el} '
    res = res.split()
    for i in range(len(res)):
        if res[i].isdigit(): res[i] = int(res[i])
    return res

def GetOperationsCount(lstIn):
    count = 0
    for el in lstIn:
        if type(el) == str: count += 1
    return count

def OperProcess(lstIn):
    lstWork = lstIn[:]
    if ('/' in lstWork) or ('*' in lstWork):
        for i in range(len(lstWork)):
            if (lstWork[i] == '/'):
                temp = lstWork[i - 1]/lstWork[i + 1]
                del lstWork[i-1 : i+2]
                lstWork.insert(i - 1, temp)
                break
            elif (lstWork[i] == '*'):
                temp = lstWork[i - 1] * lstWork[i + 1]
                del lstWork[i-1 : i+2]
                lstWork.insert(i - 1, temp)
                break
    else:
        for i in range(len(lstWork)):
            if (lstWork[i] == '-'):
                temp = lstWork[i - 1] - lstWork[i + 1]
                del lstWork[i-1 : i+2]
                lstWork.insert(i - 1, temp)
                break
            elif (lstWork[i] == '+'):
                temp = lstWork[i - 1] + lstWork[i + 1]
                del lstWork[i-1 : i+2]
                lstWork.insert(i - 1, temp)
                break
    return lstWork

def log(result, update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {result}\n')
    file.close()


start_handler = CommandHandler('start', start)
calc_handler = MessageHandler(Filters.text, calc)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(calc_handler)

updater.start_polling()
updater.idle()