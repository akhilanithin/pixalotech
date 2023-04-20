from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)    
   
