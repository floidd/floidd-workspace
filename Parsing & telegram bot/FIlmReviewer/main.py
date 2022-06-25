import Messages
import telebot
import Parsing

bot = telebot.TeleBot(token='token')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, Messages.startMessage)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.from_user.id, Messages.helpMessage, parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def start_message(message):
    try:
        filmname, review, actors, genres, duration = Parsing.get_result('Parsing'+'\\' + message.text.lower() + '.csv')
        text = f"<b>{filmname}</b>\n<b>Жанр:</b>{genres[1:-1]}\n\n" \
               f"{review[:-10]}\n\n" \
               f"<b>Главные актеры - </b>{actors[1:-1]}\n" \
               f"<b>Продолжительность - </b>{duration}"
        bot.send_photo(message.from_user.id, open('Parsing\Poster.png', 'rb'))
        if len(text) > 4096:
            for x in range(0, len(text), 4096):
                bot.send_message(message.from_user.id, text[x:x+4096], parse_mode="HTML")
        else:
            bot.send_message(message.from_user.id, text, parse_mode="HTML")
    except FileNotFoundError:
        bot.send_message(message.from_user.id, Messages.errorMessage, parse_mode="HTML")


bot.infinity_polling()
