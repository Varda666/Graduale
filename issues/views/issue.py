from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, UpdateAPIView,
                                     RetrieveAPIView, DestroyAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated

from issues.models import Project, Issue
from issues.permissions import IsModerator, IsOwner
from issues.serializers.issue import IssueSerializer, ProjectSerializer
from users.models import User
from users.serializers import UserSerializer


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class ProjectRetrieveView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class ProjectDestroyView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class IssueCreateView(CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]


class IssueUpdateView(UpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class IssueRetrieveView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class IssueDestroyView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class IssueListView(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]


class ImportantIssueListView(ListAPIView):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.filter(Q(is_critical=True) & Q(status='new') | Q(status='in progress'))
        return queryset


class ImportantIssueNewListView(ListAPIView):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = []
        new_issues = Issue.objects.filter(
            Q(status='new') | Q(status='suspended')
        )
        in_progress_issues = Issue.objects.filter(
            Q(status='in progress')
        )
        for new_issue in new_issues:
            for in_progress_issue in in_progress_issues:
                if new_issue.project_name == in_progress_issue.project_name:
                    queryset.append(new_issue)
                else:
                    pass

        return queryset


class ImportantIssueNewRetrieveView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]


class ImportantIssueNewExecutorListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        issue_pk = self.kwargs['pk']
        issue = Issue.objects.get(id=issue_pk)
        project_id = issue.project_name
        queryset = []
        user_with_min_workload = User.objects.annotate(num_tasks=Count('executed_issues')).order_by('num_tasks').first()
        num_issues_user_with_min_workload = user_with_min_workload.executed_issues.count()
        user_from_same_project = User.objects.annotate(num_tasks=Count('executed_issues', filter=Q(executed_issues__project_name=project_id))).order_by('-num_tasks').first()
        num_issues_user_from_same_project = user_from_same_project.executed_issues.count()
        if num_issues_user_from_same_project - num_issues_user_with_min_workload > 2:
            queryset.append(user_with_min_workload)
        else:
            queryset.append(user_with_min_workload)
            queryset.append(user_from_same_project)
        return queryset



