import telebot

bot = telebot.TeleBot('6247380430:AAGaesmfelvkrt0_oGcRtr6GIGhtnAoavdM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Начнём', parse_mode = 'Markdown')

    @bot.message_handler(commands=['Стихотворение'])
    def main(message):
        bot.send_message(message.chat.id,
                         'Ёлочка, ты ёлочка.\n Елка просто диво,\n Посмотрите сами,\n Как она красива', parse_mode = 'Markdown')

@bot.message_handler(commands=['Предсказание'])
def main(message):
        bot.send_message(message.chat.id, 'Сегодня у тебя все получится!', parse_mode = 'Markdown')


bot.infinity_polling()