from django.db import models

class Workers(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    work_category = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name