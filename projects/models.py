from django.db import models

# Create your models here.

class Projects(models.Model):   
    title = models.CharField(max_length=255)
    rute = models.CharField(max_length=255)
    users = models.CharField(max_length=40)
    keys = models.CharField(max_length=20)
    creat_at = models.DateTimeField(auto_now_add=True)