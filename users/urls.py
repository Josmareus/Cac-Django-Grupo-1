from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import (
    permission_required,
    login_required,
    user_passes_test,
)
from . import views


urlpatterns=[
    path('sign-up/',views.sign_up, name="Registrar Usuario"),
    path(r"login/", LoginView.as_view(), name="auth_login"),
    path('logout/', LogoutView.as_view(next_page='auth_login'), name='auth_logout'),
]