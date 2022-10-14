from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint
from  calc import  calc, rac_calc, end_calc, init_calc, complex_calc
bot = Bot(token='5768450077:AAEvHE5gKam4uPkPS7W80AWf4HAeHKDtHkM')
updater = Updater(token='5768450077:AAEvHE5gKam4uPkPS7W80AWf4HAeHKDtHkM')
dispatcher = updater.dispatcher
global board
board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]

STEP_PL, STEP_BOT, END_GAME = range(3)


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f'Привет, сыграем в игру? Если да, напиши /start_game.\n Для вызова калькулятора введите /init_calc \n Для выхода нажми /cansel')

def start_game(update, context):
    global board
    board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
    context.bot.send_message(update.effective_chat.id, 'Начальное поле "Крестики-нолики": ')
    for i in board:
        context.bot.send_message(update.effective_chat.id, i)
    context.bot.send_message(update.effective_chat.id, f'Введите строку и столбец через пробел: ')
    return STEP_PL


def take_pos_player(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ход игрока')
    rows_colms = update.message.text
    array = rows_colms.split(" ")
    ar = []
    for i in array:
        ar.append(int(i))
    global board
    try:
        if board[ar[0]][ar[1]] == '*' and board[ar[0]][ar[1]] != "X":
            board[ar[0]][ar[1]] = "0"
    except:
        context.bot.send_message(update.effective_chat.id, "Числа слишком большое! Введите в пределах от 0 до 2")
        rows_colms = update.message.text
        array = rows_colms.split(" ")
        ar = []
        for i in array:
            ar.append(int(i))

    for i in board:
        context.bot.send_message(update.effective_chat.id, i)
    context.bot.send_message(update.effective_chat.id, "Введите любую строку для следующего хода!")
    if win(board):
        context.bot.send_message(update.effective_chat.id, 'Выиграл ты')
        context.bot.send_message(update.effective_chat.id, 'Для завершения игры введите любую цифру')
        return END_GAME
    else:
        return STEP_BOT


def take_pos_bot(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ход бота')
    global board
    row = randint(0, 2)
    colms = randint(0, 2)
    if board[row][colms] not in "X0":
        board[row][colms] = "X"
        for i in board:
            context.bot.send_message(update.effective_chat.id, i)
        context.bot.send_message(update.effective_chat.id, "Введите в пределах от 0 до 2")
        if win(board):
            context.bot.send_message(update.effective_chat.id, 'Выиграла я')
            context.bot.send_message(update.effective_chat.id, 'Для завершения игры введите любую цифру')
            return END_GAME
        else:
            return STEP_PL
    else:
        context.bot.send_message(update.effective_chat.id, "Клетка уже занята")
        return STEP_BOT


def win(arr):
    if arr[0][0] == arr[1][0] == arr[2][0] == "X":
        return True
    elif arr[0][1] == arr[1][1] == arr[2][1] == "X":
        return True
    elif arr[0][2] == arr[1][2] == arr[2][2] == "X":
        return True
    elif arr[0][0] == arr[0][1] == arr[0][2] == "X":
        return True
    elif arr[1][0] == arr[1][1] == arr[1][2] == "X":
        return True
    elif arr[2][0] == arr[2][1] == arr[2][2] == "X":
        return True
    elif arr[0][0] == arr[1][1] == arr[2][2] == "X":
        return True
    elif arr[0][2] == arr[1][1] == arr[2][0] == "X":
        return True

    if arr[0][0] == arr[1][0] == arr[2][0] == "0":
        return True
    elif arr[0][1] == arr[1][1] == arr[2][1] == "0":
        return True
    elif arr[0][2] == arr[1][2] == arr[2][2] == "0":
        return True
    elif arr[0][0] == arr[0][1] == arr[0][2] == "0":
        return True
    elif arr[1][0] == arr[1][1] == arr[1][2] == "0":
        return True
    elif arr[2][0] == arr[2][1] == arr[2][2] == "0":
        return True
    elif arr[0][0] == arr[1][1] == arr[2][2] == "0":
        return True
    elif arr[0][2] == arr[1][1] == arr[2][0] == "0":
        return True

    else:
        False


def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.'
    )
    return ConversationHandler.END


def end_game(update, context):
    context.bot.send_message(update.effective_chat.id, 'GAME OVER')
    return ConversationHandler.END


INPUT_RAC , INPUT_COMPLEX , END_CALC, INIT_CALC, CALC = range(5)
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start_game', start_game)],
    states={
        STEP_PL: [MessageHandler(Filters.text, take_pos_player)],
        STEP_BOT: [MessageHandler(Filters.text, take_pos_bot)],
        END_GAME: [MessageHandler(Filters.text, end_game)]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
dispatcher.add_handler(conv_handler)


conv2_handler = ConversationHandler(
    entry_points=[CommandHandler('init_calc', init_calc)],
    states={
        CALC: [MessageHandler(Filters.text, calc)],
        INPUT_RAC: [MessageHandler(Filters.text, rac_calc)],
        INPUT_COMPLEX: [MessageHandler(Filters.text, complex_calc)],
        END_CALC: [MessageHandler(Filters.text, end_calc)]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
dispatcher.add_handler(conv2_handler)



start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()  # ctrl + c