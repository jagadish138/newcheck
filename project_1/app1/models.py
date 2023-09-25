from django.db import models

# Create your models here.

class logIn(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class login_Register(models.Model):
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    mobile = models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    
    def __str__(self):
        return self.father
    


