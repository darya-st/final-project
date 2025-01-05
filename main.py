from init_bot import bot
import telebot

class UserState(telebot.handler_backends.StatesGroup):
    new_quest = telebot.handler_backends.State()
    num_quest = telebot.handler_backends.State()
    variants = telebot.handler_backends.State()


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = ("/get_question - ответить на вопрос\n"
            "/my_statistic - моя статистика\n"
            "/total_statistic - общая статистика\n"
            "/add_question - добавить вопрос\n"
            "/delete_question - удалить вопрос")
    bot.send_message(message.from_user.id, text=f"Привет, {message.from_user.first_name}!\n"
                                                f"Выберите действие:\n"
                                                f"{text}", parse_mode='HTML')


@bot.message_handler(commands=['add_question'])
def create_quiz(message: telebot.types.Message):
    bot.send_message(message.from_user.id, text="Введите свой вопрос...", parse_mode='HTML')
    bot.set_state(message.from_user.id, UserState.new_quest, message.chat.id)

bot.infinity_polling()