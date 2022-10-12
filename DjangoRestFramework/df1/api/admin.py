from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)

class stuAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','address']
    
    

