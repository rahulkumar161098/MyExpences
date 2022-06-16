
from django.urls import path
from userPrerefrences import views

urlpatterns = [
    path('preference', views.preferences, name="preference")
]
