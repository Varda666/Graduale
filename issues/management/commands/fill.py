from django.core.management import BaseCommand

from issues.models import Issue, Project
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user1, _ = User.objects.get_or_create(email='ivan1@mail.ru', defaults={
            'name': 'Ivan',
            'is_superuser': False,
            'is_staff': True,
            'is_active': True
             })

        user2, _ = User.objects.get_or_create(email='vladimir1@mail.ru', defaults={
            'name': 'Vladimir',
            'is_superuser': False,
            'is_staff': True,
            'is_active': True
        })

        user3, _ = User.objects.get_or_create(email='aleks1@mail.ru', defaults={
            'name': 'Aleks',
            'is_superuser': False,
            'is_staff': True,
            'is_active': True
        })

        # project_list1 = [
        #     {
        #         'project_name': 'Аренда',
        #         'owner': user1,
        #      },
        #     {
        #         'project_name': 'Поставка',
        #         'owner': user2,
        #     }
        # ]


        issues_list1 = [
            {
                'owner': user1,
                 'issue_name': 'Проверить договор аренды',
                 'issue_executor': user2,
                 'param_term_of_execution': 'working days',
                 'term_of_execution': 2,
                 'project_name': Project.objects.get(pk=1),
                 'status': 'new',
                 'is_public': True,
                 'is_critical': False,
            },
            {
                 'owner': user2,
                 'issue_name': 'Проверить договор поставки',
                 'issue_executor': user2,
                 'param_term_of_execution': 'working days',
                 'term_of_execution': 1,
                 'project_name': Project.objects.get(pk=2),
                 'status': 'in progress',
                 'is_public': True,
                 'is_critical': True,
             },
            {
                'owner': user3,
                'issue_name': 'Проверить товар',
                'issue_executor': user1,
                'param_term_of_execution': 'hours',
                'term_of_execution': 5,
                'project_name': Project.objects.get(pk=2),
                'status': 'new',
                'is_public': True,
                'is_critical': False,

             },
        ]

        issues_for_create = []
        for item in issues_list1:
            issues_for_create.append(Issue(**item))
        Issue.objects.all().delete()
        Issue.objects.bulk_create(issues_for_create)


