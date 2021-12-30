from django.db import models

# Create your models here.
# In this case we will have title, technology, description, imagepath
# Project(title="", description="", technology="", imagepath="")
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=40)
    imagepath = models.CharField(max_length=100)
