from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import UserUpdateView


urlpatterns = [
    path('about/', views.about_view, name='users-about'),
    path('register/', views.register_view, name="users-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='users-logout'),
    #     path('logout/', views.logout_view, name='users-logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password-reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    # UIDB64 and Token are what Django looks for to confirm the user
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('<int:pk>/update', login_required(UserUpdateView.as_view()),
         name='user-update'),
]
