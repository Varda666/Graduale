from django.urls import path
from django.contrib import admin

from issues.views.issue import (IssueListView, IssueRetrieveView, IssueDestroyView,
                                IssueCreateView, IssueUpdateView, ProjectListView,
                                ProjectDestroyView, ProjectUpdateView, ProjectRetrieveView,
                                ProjectCreateView, ImportantIssueListView, ImportantIssueNewListView,
                                ImportantIssueNewRetrieveView,
                                ImportantIssueNewExecutorListView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectRetrieveView.as_view(), name='project_detail'),
    path('projects/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/delete/<int:pk>/', ProjectDestroyView.as_view(), name='project_delete'),
    path('', IssueListView.as_view(), name='issue_list'),
    path('important/', ImportantIssueListView.as_view(), name='important_issue_list'),
    path('important/new/', ImportantIssueNewListView.as_view(), name='important_issue_list'),
    path('important/new/<int:pk>/', ImportantIssueNewRetrieveView.as_view(), name='important_issue_detail'),
    path('important/new/<int:pk>/executors', ImportantIssueNewExecutorListView.as_view(), name='important_issue_detail_executors'),
    path('<int:pk>/', IssueRetrieveView.as_view(), name='issue_detail'),
    path('update/<int:pk>/', IssueUpdateView.as_view(), name='issue_update'),
    path('create/', IssueCreateView.as_view(), name='issue_create'),
    path('delete/<int:pk>/', IssueDestroyView.as_view(), name='issue_delete'),
]


