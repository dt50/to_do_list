from telegram import Bot

from telegram import Update

from telegram.ext import Updater

from telegram.ext import MessageHandler

from telegram.ext import Filters

import os 

def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'Noname'
	text = update.effective_message.text
	reply_text = f'Hello, {name}\n\n Вы написали: {text}'
	bot.send_message(
		chat_id = update.effective_message.chat_id,
		text = reply_text,)

def main():
	'''bot = Bot(
					token = os.environ['TOKEN'],
					base_url = "https://telegg.ru/orig/bot"
				)'''
	updater = Updater(
		token = os.environ['TOKEN'],
		base_url = "https://telegg.ru/orig/bot",
	)

	handler = MessageHandler(Filters.all, message_handler)
	updater.dispatcher.add_handler(handler)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()