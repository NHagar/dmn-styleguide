# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from .models import Entry
from django.db import models

class EntryAdmin(admin.ModelAdmin):
    list_display=('term',)
    search_fields=('term',)
    ordering = ('term',)


admin.site.register(Entry, EntryAdmin)
# Register your models here.
