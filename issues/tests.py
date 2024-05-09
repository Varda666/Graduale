from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from issues.models import Issue, Project
from users.models import User


class ModelCreateTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@mail.com',
            name='TestName',
            position='TestPosition',
            is_staff=True,
            is_active=True,
        )
        self.user.set_password('123qwe')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.project = Project.objects.create(
            project_name='Аренда',
            owner=self.user,
        )
        self.issue = Issue.objects.create(
            owner=self.user,
            issue_name='Проверить товар',
            issue_executor=self.user,
            param_term_of_execution='hours',
            term_of_execution=5,
            project_name=self.project,
            status='new',
            is_public=True,
            is_critical=False,
        )

    def test_get_list_issues(self):
        response = self.client.get(
            reverse('issues:issue_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {"count": 1,
                 "next": None,
                 "previous": None,
                 "results": [
                     {
                         "id": 1,
                         "term_of_execution": 2,
                         "issue_name": "Проверить договор аренды",
                         "param_term_of_execution": "working days",
                         "status": "new",
                         "is_public": True,
                         "is_critical": False,
                         "owner": "ivan1@mail.ru",
                         "issue_executor": "vladimir1@mail.ru",
                         "project_name": 1
                     },
                 ]
                 },
            ]
        )

    def test_project_create(self):
        data = {
            'id': 1,
            'owner': User.objects.get(email='test@mail.com'),
            "project_name": "Поставка",

        }
        response = self.client.post(
            reverse('issues:project_create'),
            data=data,
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Project.objects.all().count(),
            2
        )

    def test_issue_update(self):
        data = {
            'issue_name': 'Проверить товар Проверить товар'
        }
        responce = self.client.put(
            reverse(
                'issues:issue_update',
                kwargs={'pk': self.issue.pk}),
            data=data,
            format='json'
        )
        self.assertEquals(
            Issue.objects.get(pk=self.issue.pk).issue_name,
            'Проверить товар'
        )

    def test_issue_delete(self):
        response = self.client.delete(
            reverse('issues:issue_delete', kwargs={'pk': self.issue.id})
        )
        self.assertEqual(response.status_code, 204)
        self.assertEquals(
            Issue.objects.all().count(),
            0
        )
