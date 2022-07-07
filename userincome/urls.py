
from django.urls import path
from userincome import views

urlpatterns = [
    path('my_income', views.income_index, name="user_income_index"),
    path('edit_my_income/<int:id>', views.income_edit, name="edit_income"),
    path('delete_income/<int:id>', views.del_income, name="delete_income")
    
]
