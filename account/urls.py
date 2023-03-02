

from django.urls import path
from account import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register"),
    path('home', views.user_dashboard, name="home"),
    path('login', views.user_login, name="user_log"),
    path('logged_out', views.logged_out, name="user_logged_out"),
    path('user_details', views.user_details, name="user_details"),
    path('edit_user_details/<int:id>', views.edit_user_details, name="edit_user_details"),
    path('user_service', views.user_service, name='user_service'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"), 
    path('', views.index_page, name="index_page")
    # path('userlog', views.index, name='userlog')
]

    