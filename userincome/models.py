from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddIncome(models.Model):
    income_amount= models.FloatField()
    date= models.DateTimeField()
    income_desc= models.TextField()
    owner= models.ForeignKey(to=User, on_delete=models.CASCADE)
    income_source= models.CharField(max_length=255)

    def __str__(self):
        return self.income_source

    # class Meta:
    #     ordering: ['-date']
    
    # class Source(models.Model):
    #     name= models.CharField(max_length=256)

