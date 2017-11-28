from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Fmenu(models.Model):
    name = models.CharField(max_length=1000)
    desc = models.TextField()
    price = models.IntegerField()
    calories = models.IntegerField()
    #add imagefield
    #food_image = models.CharField(255)

    def __str__(self):
        return str(self.name)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','name')
