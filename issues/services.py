import json
from datetime import datetime, timedelta

from django.db.models import Q
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule

from config import settings
from issues.models import Issue

schedule, created = IntervalSchedule.objects.get_or_create(
     every=3,
     period=IntervalSchedule.DAYS,
)

PeriodicTask.objects.create(
     interval=schedule,
     name='Напоминание о важных задачах',
     task='issues.management.commands.bot',
     # chat_id=settings.MY_CHAT_ID,
     # text=Issue.objects.filter(Q(is_critical=True)).values('issue_name'),
     kwargs=json.dumps(
          {
               'be_careful': True,
               'chat_id': settings.MY_CHAT_ID,
               'text': Issue.objects.filter(Q(is_critical=True)).values('issue_name'),
          }
     ),
     expires=datetime.utcnow() + timedelta(minutes=3)
)
