from .tag import Tag
from .category import Category
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag)
    categoria = models.ForeignKey(Category, on_delete=models.PROTECT)
