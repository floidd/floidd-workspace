import Messages
import telebot
import database

bot = telebot.TeleBot(token='Ваш токен')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, Messages.startMessage)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, Messages.helpMessage, parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def send_film(message):
    if message.text.lower() == 'фильм':
        filmname, review, actors, genres, duration = database.processing(database.get_film())
        text = f"<b>{filmname}</b>\n<b>Жанр: </b>{genres}\n\n" \
               f"{review}\n\n" \
               f"<b>Главные актеры - </b>{actors}\n" \
               f"<b>Продолжительность - </b>{duration}"
        bot.send_photo(message.from_user.id, open('Poster.png', 'rb'))
        if len(text) > 4096:
            for x in range(0, len(text), 4096):
                bot.send_message(message.from_user.id, text[x:x+4096], parse_mode="HTML")
        else:
            bot.send_message(message.from_user.id, text, parse_mode="HTML")
    else:
        bot.send_message(message.from_user.id, Messages.errorMessage)


bot.infinity_polling()
