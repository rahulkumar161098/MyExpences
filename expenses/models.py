
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddExpence(models.Model):
    amount= models.FloatField()
    date= models.DateTimeField()
    description= models.TextField()
    owner= models.ForeignKey(to=User, on_delete=models.CASCADE)
    category= models.CharField(max_length=255)

    def __str__(self):
        return self.category

    # class Meta:
    #     ordering: ['-date']
    
    class Category(models.Model):
        name= models.CharField(max_length=256)
