from django.contrib import admin

from issues.models import Issue, Project


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'issue_name', 'owner', 'issue_executor', 'param_term_of_execution',
        'term_of_execution', 'project_name', 'status', 'is_public'
    )
    list_filter = (
        'issue_name', 'owner', 'issue_executor', 'param_term_of_execution',
        'term_of_execution', 'project_name', 'status', 'is_public'
    )
    search_fields = (
        'issue_name', 'owner', 'issue_executor', 'param_term_of_execution',
        'term_of_execution', 'project_name', 'status', 'is_public'
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('owner', 'project_name')
    list_filter = ('owner', 'project_name')
    search_fields = ('owner', 'project_name')
# Register your models here.
