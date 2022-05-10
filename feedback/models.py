from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    feedback = models.CharField(max_length=1000)
    score = models.IntegerField()
