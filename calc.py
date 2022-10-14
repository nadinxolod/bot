from telegram import Bot, Update
from telegram.ext import  CommandHandler, ConversationHandler

INPUT_RAC , INPUT_COMPLEX , END_CALC, INIT_CALC, CALC = range(5)


def init_calc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Это Мистер Калькуляторик!\n '
                                                      'С какими чиселками вы хотите работать??\n '
                                                      'Если с рациональными - введите "1"\n'
                                                      ' Если с комплексными - введите "2"')
    return CALC

def calc(update, context):
    number = update.message.text
    if number == "1":
        context.bot.send_message(update.effective_chat.id, 'Введите выражение: \n (Пример: 1 + 3)')
        return INPUT_RAC
    elif number == "2":
        context.bot.send_message(update.effective_chat.id, 'Введите комплесное выражение: \n (Пример: 1+4j + 2+3j)')
        return  INPUT_COMPLEX


def rac_calc(update, context):
   example = update.message.text
   example1 = example.split()

   if "+" in example1:
        context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} + {int(example1[2])} = {int(example1[0])+ int(example1[2])} ')
   elif "-" in example1:
        context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} - {int(example1[2])} = {int(example1[0])- int(example1[2])} ')
   elif "*" in example1:
       context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} * {int(example1[2])} = {int(example1[0])* int(example1[2])} ')
   elif "/" in example1:
       context.bot.send_message(update.effective_chat.id, f'{int(example1[0])} / {int(example1[2])} = {int(example1[0]) / int(example1[2])} ')
   context.bot.send_message(update.effective_chat.id,
                            'Если вы хотите выйти из калькулятора, напишите exit\n А если хотите продолжить нажмите любую кнопку!')
   return END_CALC

def complex_calc(update, context):
    number1 = update.message.text
    number1_1 = number1.split()
    if  "+" in number1_1:
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} +{complex(number1_1[2])} = {complex(number1_1[0])+ complex(number1_1[2])} ')
    elif  "-" in number1_1:
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} - {complex(number1_1[2])} = {complex(number1_1[0]) - complex(number1_1[2])} ')
    elif  "*" in number1_1:
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} * {complex(number1_1[2])} = {complex(number1_1[0]) * complex(number1_1[2])} ')
    elif  "/" in number1_1:
        numb = complex(number1_1[0])/ complex(number1_1[2])
        context.bot.send_message(update.effective_chat.id, f' {complex(number1_1[0])} / {complex(number1_1[2])} = {complex(round(numb.real, 2),round(numb.imag, 2))}')
    context.bot.send_message(update.effective_chat.id, 'Если вы хотите выйти из калькулятора, напишите exit')
    return END_CALC

def end_calc(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, 'выход из калькулятора')
    return ConversationHandler.END