from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
class UserView(admin.ModelAdmin):
  list_display=('id', 'username')

# admin.site.register(User, UserView)
