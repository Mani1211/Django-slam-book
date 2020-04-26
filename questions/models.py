from django.db import models

# Create your models here.


class Questions(models.Model):

    name  = models.CharField(max_length=255)
    number = models.BigIntegerField()
    advice = models.CharField(max_length=255)
    positive = models.CharField(max_length=255)
    weakness = models.CharField(max_length=255)
    like = models.CharField(max_length=255)
    words = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
   
    def __str__(self):
        return self.name