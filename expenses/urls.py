
from django.urls import path
from expenses import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('add_expences', views.addExpence, name="add_expences"),
    path('edit_expense/<int:pk>', views.edit_expense, name="edit_expense"),
    path('delete_expense/<int:pk>', views. delete_expense, name="delete_expense"),
    path('expence_summary', views.categoty_summary_data, name="expence_summary")
    
]
