from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.username