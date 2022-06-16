
from django.urls import path
from expenses import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('add_expences', views.addExpence, name="add_expences")
    
]
