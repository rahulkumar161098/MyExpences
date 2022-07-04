from django.contrib import admin
from userincome.models import AddIncome

# Register your models here.
class AddIncomeView(admin.ModelAdmin):
    list_display=['date', 'income_amount']
    
admin.site.register(AddIncome, AddIncomeView)