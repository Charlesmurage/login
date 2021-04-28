# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required

# Create your views here.
@allowed_users(allowed_roles=['work'])
def plan(request):
    return render(request,'paygate.html')