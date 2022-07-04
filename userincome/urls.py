
from django.urls import path
from userincome import views

urlpatterns = [
    path('my_income', views.income_index, name="user_income_index"),
    path('edit_my_income', views.income_edit, name="edit_income")
    
]
