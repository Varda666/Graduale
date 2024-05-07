from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, UpdateAPIView,
                                     RetrieveAPIView, DestroyAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated

from issues.models import Project, Issue
from issues.permissions import IsModerator, IsOwner
from issues.serializers.issue import IssueSerializer, ProjectSerializer


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated]


class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class ProjectRetrieveView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated,
                          #IsModerator | IsOwner | IsOwnerOrPublic]


class ProjectDestroyView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class IssueCreateView(CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    #permission_classes = [IsAuthenticated]


class IssueUpdateView(UpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class IssueRetrieveView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    #permission_classes = [IsAuthenticated,
                          #IsModerator | IsOwner | IsOwnerOrPublic]


class IssueDestroyView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    #permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class IssueListView(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]

class ImportantIssueListView(ListAPIView):
    serializer_class = IssueSerializer
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        queryset = Issue.objects.filter(Q(is_critical=True) & Q(status='new') | Q(status='suspended'))
        return queryset


class ImportantIssueNewListView(ListAPIView):
    serializer_class = IssueSerializer
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

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
