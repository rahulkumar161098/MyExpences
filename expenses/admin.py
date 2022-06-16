from django.contrib import admin
from expenses.models import User, AddExpence

# Register your models here.

class AddExpencesView(admin.ModelAdmin):
    list_display=['date', 'amount']
    
admin.site.register(AddExpence, AddExpencesView)
