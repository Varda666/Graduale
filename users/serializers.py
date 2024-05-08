from django.db.models import Count, Q
from rest_framework import serializers

from issues.models import Issue
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)
    executed_issues = serializers.IntegerField


    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'executed_issues')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        return user

    def get_executed_issues(self):
        executed_issues = User.objects.annotate(
            num_issues=Count(
                'executed_issues',
                filter=Q(executed_issues__status='new') | Q(executed_issues__status='in progress'),
            )
        )
        return executed_issues.issue_name





