from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.


class Patente(models.Model):
    id=IntegerField(primary_key=True)
    pat=CharField(max_length=7, null=False)
