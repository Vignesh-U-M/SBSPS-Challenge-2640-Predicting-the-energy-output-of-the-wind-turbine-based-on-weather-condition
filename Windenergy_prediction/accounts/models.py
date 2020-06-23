from django.db import models

# Create your models here.

class user_details(models.Model):
    Name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)


