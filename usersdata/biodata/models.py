from django.db import models

class Biodata(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name