
from rest_framework.generics import (CreateAPIView, UpdateAPIView,
                                     RetrieveAPIView, DestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Count, Q
from users.models import User
from issues.permissions import IsOwner, IsModerator
from users.serializers import UserSerializer
from rest_framework.response import Response


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.annotate(
            num_issues=Count(
                'executed_issues',
                filter=Q(executed_issues__status='new') | Q(executed_issues__status='in progress'),

            )
        ).order_by('-num_issues')
        return queryset
