# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entry(models.Model):
    term = models.CharField(max_length=500)
    definition = models.TextField()
    source = models.CharField(max_length=5, choices=[('AP', 'AP'), ('DMN', 'DMN')])
