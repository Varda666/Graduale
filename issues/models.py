from django.db import models


class Project(models.Model):
    project_name = models.TextField(
        max_length=700, verbose_name='суть проекта'
    )
    owner = models.ForeignKey(
        to='users.User', to_field='email',
        verbose_name='владелец проекта', on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class Issue(models.Model):
    PARAM_TERM_CHOISES = [
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('working days', 'working days'),
        ('calendar days', 'calendar days'),
        ('weeks', 'weeks'),
        ('months', 'months'),
    ]
    STATUS_CHOISES = [
        ('new', 'new'),
        ('in progress', 'in progress'),
        ('suspended', 'suspended'),
        ('cancelled', 'cancelled'),
        ('done', 'done'),
    ]
    issue_name = models.TextField(
        max_length=700, verbose_name='суть задачи'
    )
    owner = models.ForeignKey(
        to='users.User', to_field='email',
        verbose_name='постановщик задачи', on_delete=models.DO_NOTHING,
        related_name='owned_issues',
    )
    issue_executor = models.ForeignKey(
        to='users.User', to_field='email', default=None, null=True,
        verbose_name='исполнитель', on_delete=models.DO_NOTHING,
        related_name='executed_issues'
    )
    param_term_of_execution = models.CharField(
        choices=PARAM_TERM_CHOISES, max_length=150,
        verbose_name='параметр времени выполнения'
    )
    term_of_execution = models.IntegerField(
        verbose_name='время выполнения'
    )
    project_name = models.ForeignKey(
        to='Project', default=None,
        verbose_name='название проекта', on_delete=models.DO_NOTHING
    )
    status = models.CharField(
        choices=STATUS_CHOISES, max_length=150,
        verbose_name='переодичность'
    )
    is_public = models.BooleanField(default=False, verbose_name='публичность')
    is_critical = models.BooleanField(default=False, verbose_name='публичность')

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


