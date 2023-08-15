from django.db import models


# Create your models here.
class AboutMe(models.Model):
    description = models.TextField()
    image = models.CharField(max_length=100)
