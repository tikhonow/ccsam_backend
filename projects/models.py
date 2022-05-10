from django.db import models
import os
from PIL import Image
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


def image_folder(instance, filename):
    req = get_current_user()
    return '/'.join(['avatars', req.username, filename])


def project_folder(instance, filename):
    req = get_current_user()
    return '/'.join(['projects', req.username, filename])


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_folder)
    file = models.FileField(blank=True, upload_to=project_folder)

    def __str__(self):
        return  self.name