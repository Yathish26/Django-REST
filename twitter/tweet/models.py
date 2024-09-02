from django.db import models

class Tweet(models.Model):
    username = models.CharField(max_length=20)
    Tweet = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.username