# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Car

# Create your views here.

def homepage(request):
    data = Car.objects.all()
    stu = {
        "car_id": data
    }
    return render(request, 'homepage/homepage.html', stu)
