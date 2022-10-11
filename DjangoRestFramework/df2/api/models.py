from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    address=models.CharField(max_length=100)

    
