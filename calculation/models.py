from django.db import models


# Create your models here.
class File(models.Model):
    original = models.FileField(blank=False, null=False)
    impulse = models.FileField(blank=False, null=False)
    result = models.FileField(blank=False, null=False)
