from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate
from django.conf import settings

from bot.models import UserTg
from task.models import Task

import telebot
import configparser
import os
from . import helper


class Command(BaseCommand):
    help = 'Telegram-Bot'

    def handle(self, *args, **options):

        config = configparser.ConfigParser()
        config.read(os.path.join(settings.BASE_DIR, '.conf'))

        api_key = config['TELEGRAM']['api_key']
        bot = telebot.TeleBot(api_key)

        @bot.message_handler(commands=['authenticate'])
        def login(message):
            msg = bot.send_message(
                message.chat.id,
                'Вы еще не ввели логин и пароль\nВведите данные через пробел'
            )
            bot.register_next_step_handler(msg, auth)

        def auth(message):
            text = str(message.text).split(' ')
            log_conditionals = {
                'email': text[0],
                'password': text[1]
            }

            obj, flag = UserTg.objects.get_or_create(
                external_id=message.chat.id,
                defaults={
                    'user_name': message.from_user.username,
                }
            )

            if flag or obj.user is None:
                user = authenticate(email=log_conditionals['email'], password=log_conditionals['password'])
                if user is not None:
                    obj.user = user
                    obj.save()
                    bot.send_message(
                        message.chat.id,
                        f'Successfully authorization\nHi {message.from_user.username}\nUsername on website {obj.user})'
                    )
                else:
                    bot.send_message(
                        message.chat.id,
                        f'Error, your login or password is incorrect'
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    'You are already logging in bot'
                )

        @bot.message_handler(commands=['logout'])
        def logout(message):
            try:
                user = UserTg.objects.get(external_id=message.chat.id)
            except UserTg.DoesNotExist:
                bot.send_message(
                    message.chat.id,
                    'Вы еще не вошли в систему что бы из нее выходить'
                )
            else:
                user.user = None
                user.user_name = None
                user.save()
                bot.send_message(
                    message.chat.id,
                    'Вы успешно вышли из своей записи. Ждем вас!'
                )

        @bot.message_handler(commands=['task_list'])
        def task_list(message):
            user_tg = UserTg.objects.get(external_id=message.chat.id)
            if user_tg:
                user = user_tg.user
                tasks = Task.objects.all().filter(user=user).order_by('date')
                for task in tasks:
                    bot.send_message(
                        message.chat.id,
                        f'Task: {task.title}\nTag: {task.tag}\nTime: {task.date}\nComplete: {task.completed}'
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    'You are not logged into Telegram bot\nwrite /authenticate after email and password'
                )

        bot.polling(none_stop=True)
