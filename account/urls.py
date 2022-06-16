

from django.urls import path
from account import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register"),
    path('home', views.user_dashboard, name="home"),
    path('login', views.user_login, name="user_log"),
    path('logged_out', views.logged_out, name="user_logged_out"),
    # path('userlog', views.index, name='userlog')
]
