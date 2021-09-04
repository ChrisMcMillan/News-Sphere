from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

app_name = 'members'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', views.PasswordEditView.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile/', views.ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),
]