from django.db import models

# Create your models here.
class events (models.Model):
    title = models.CharField(max_length=32)
    value = models.IntegerField()