import telebot;
bot = telebot.TeleBot('925333719:AAGkxg1P6RArMuoVbRjIElGfht_3FvZB16I');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Hello, how can I help you? :)")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write 'Hello'!")
    else: 
        bot.send_message(message.from_user.id, "I don't understand you :(. Write /help.")

bot.polling(none_stop=True, interval=0)