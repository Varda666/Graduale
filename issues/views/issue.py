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

