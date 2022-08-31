from django.db import models

class Plugins(models.Model):
  name = models.CharField(max_length=255)
  version = models.CharField(max_length=255)