from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ProfileDetailsView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView
)

app_name = "track"

urlpatterns = [
    path('', login_required(ProfileDetailsView.as_view()), name='track-home'),
    path('about/', views.about_view, name='track-about'),
    path('about/for-learner/', views.for_learner_view, name='track-for-learner'),
    path('project/create/', login_required(ProjectCreateView.as_view()),
         name='track-project-create'),
    path('project/<str:slug>', views.project_details_view,
         name='track-project-details'),
    path('project/<str:slug>/update', login_required(ProjectUpdateView.as_view()),
         name='track-project-update'),
    path('project/<str:slug>/delete/', login_required(ProjectDeleteView.as_view()),
         name='track-project-delete'),
    path('project/<str:slug>/issue/create/', views.issue_create_view,
         name='track-issue-create'),
    path('issue/<str:slug>/details/', views.issue_details_view,
         name='track-issue-details'),
    path('issue/<str:slug>/update/', views.issue_update_view,
         name='track-issue-update'),
    path('issue/<str:slug>/delete/', views.issue_delete_view,
         name='track-issue-delete'),
]
