from django.db import models

class Category(models.Model):
    titulo = models.CharField(max_length=50)
