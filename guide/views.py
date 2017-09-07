# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import operator
import json
import itertools

from django.shortcuts import render
from django.http import HttpResponse

from models import Entry

# Create your views here.
def full(request):
    entry_list = list(Entry.objects.all())
    get_key = operator.attrgetter('term')
    entry_list.sort(key = lambda s: get_key(s).lower(), reverse = False)
    return render(request, 'guide/full.html', {'entry_list': entry_list})

def search(request):
    entry_list = list(Entry.objects.all())
    get_key = operator.attrgetter('term')
    entry_list.sort(key = lambda s: get_key(s).lower(), reverse = False)
    return render(request, 'guide/search.html', {'entry_list': entry_list})
