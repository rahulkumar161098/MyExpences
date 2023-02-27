
from django.contrib import admin
from django.urls import path, include
from expenses import views
# import expenses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('expenses/', include('expenses.urls')),
    path('preference/', include('userPrerefrences.urls')),
    path('income/', include('userincome.urls')),

    path('', views.base_page, name="base_page"),
]
