from django.contrib import admin
from userPrerefrences.models import UserPreferences

# Register your models here.
class UserPreferencesViews(admin.ModelAdmin):
    list_display= ['id','user', 'currency']
admin.site.register(UserPreferences, UserPreferencesViews)
