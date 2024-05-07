from django.core.management.base import BaseCommand
from django.conf import settings

from telebot import TeleBot


bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


class Command(BaseCommand):

   def send_message(self, *args, **kwargs):
        bot.send_message(
            chat_id=kwargs.get['chat_id'],
            text=kwargs.get['text']
        )


