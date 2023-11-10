#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6979831417:AAHcXEzXKWyKlvGUti1cU7Py-TIpMy5DjoE'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Связаться со мной")
	item3 = types.KeyboardButton("😋 Жамкни на меня")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет тебе от Антера, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/unterweg2/cv')
		elif message.text == '😋 Связаться со мной':
			bot.send_message(message.chat.id, 'flaeronalex25@yandex.ru')
		elif message.text == '😋 Жамкни на меня':
			bot.send_message(message.chat.id, 'Хорошего тебе настроения:)')
		else:
			bot.send_message(message.chat.id, 'Я тест-бот, пока что я не знаю что тебе ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
