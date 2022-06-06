from pyexpat import model
from django.db import models

# Create your models here.


class Gameuser(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    PhoneNumber=models.CharField(max_length=10)
    Password=models.CharField(max_length=20)
    DateofBirth=models.DateField()


    def __str__(self):
        return self.Name
    
    