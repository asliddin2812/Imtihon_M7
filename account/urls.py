from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    register_user,
    login_user,
    logout_user,
    PasswordResetAPIView
)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/password-reset/', PasswordResetAPIView.as_view(), name='api_password_reset'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
