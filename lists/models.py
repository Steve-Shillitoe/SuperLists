"""
Definition of models.
"""

from email.policy import default
from django.db import models

# Create your models here.
class List(models.Model):
    pass
    #id = models.AutoField(primary_key=True)


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.SET_DEFAULT)

