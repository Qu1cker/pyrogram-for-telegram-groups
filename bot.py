from pyrogram import Client, filters
import roll
import postgres
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

bot = Client(
    "aboba",
    api_id=15757718,
    api_hash="f98906c4d2e3d37de4e8373ba28b6be4",
    bot_token="5238095432:AAHLwu4xn3t3rZWbuq9TKrOaj0UWSPOcjA8"
)


@bot.on_message(filters.command('start'))
def start_message(bot, message):
    bot.send_message(message.chat.id, "hey, I'm a bot")


@bot.on_message(filters.command('roll'))
def start_message(bot, message):
    number = roll.random_number(0, 100)
    bot.send_message(message.chat.id, f"Случайное число - {number}")


@bot.on_message(filters.command('coinflip'))
def start_message(bot, message):
    number = roll.random_number(1, 2)
    if number == 1:
        bot.send_message(message.chat.id, "Орел")
    else:
        bot.send_message(message.chat.id, "Решка")


@bot.on_message(filters.command('question'))
def start_message(bot, message):
    row1 = postgres.question_get(1)
    row = row1[0]
    question = row[1]
    answer = row[2]
    incorrect_answer = row[3]
    incorrect_answer2 = row[4]
    incorrect_answer3 = row[5]
    all_answers = [answer,
                   incorrect_answer,
                   incorrect_answer2,
                   incorrect_answer3
                   ]
    # a1 = ReplyKeyboardMarkup(incorrect_answer, one_time_keyboard=True, resize_keyboard=True)
    # a2 = ReplyKeyboardMarkup(answer, one_time_keyboard=True, resize_keyboard=True)
    reply_markup = ReplyKeyboardMarkup(all_answers)
    message.reply(
        text=question,
        reply_markup=reply_markup,
    )


print("------- bot is working -------")
bot.run()
