from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

app_name = 'members'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', views.PasswordEditView.as_view(template_name='registration/change_password.html')),
]