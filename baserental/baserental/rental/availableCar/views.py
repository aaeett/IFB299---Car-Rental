# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Car

# Create your views here.

def availableCar(request):
    data = Car.objects.all()
    stu = {
        "car_id": data
    }
    return render(request, 'availableCar/avaiCar.html', stu)

