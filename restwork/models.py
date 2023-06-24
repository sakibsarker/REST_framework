from django.db import models

# Create your models here.
class Advocate(models.Model):
    username=models.CharField(max_length=10)
    bio=models.TextField(max_length=1000)
    def __str__(self):
        return self.username