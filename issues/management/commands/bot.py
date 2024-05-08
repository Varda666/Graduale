from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import Bot


bot = Bot(token=settings.TELEGRAM_BOT_API_KEY)


class Command(BaseCommand):

   def handle(self, *args, **kwargs):
       bot.send_message(
            chat_id=kwargs.get('chat_id'),
            text=kwargs.get('text')
        )


