from rest_framework import serializers

from issues.models import Issue, Project
from issues.validators import valid_term_of_execution


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):
    term_of_execution = serializers.IntegerField(validators=[valid_term_of_execution])


    def validate_issue_name(self, data):
        list_of_forbidden_words = ['голова', 'нога', 'рука']
        for word in list_of_forbidden_words:
            if word in data['issue_name']:
                raise serializers.ValidationError(
                    f"Название не может содержать слово {word}"
                )
        else:
            return data

    class Meta:
        model = Issue
        fields = "__all__"


