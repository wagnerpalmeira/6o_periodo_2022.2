from django.db import models

class Tag(models.Model):
    titulo = models.CharField(max_length=50)