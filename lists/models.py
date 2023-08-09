"""
Definition of models.
"""

from email.policy import default
from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.TextField(default="")

class List(models.Model):
    id = models.AutoField(primary_key=True)