# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Orders
# Create your views here.
def staffpage(request):
    data = Orders.objects.all()
    stu = {
        "order_id": data
}
    return render(request, 'staffpage/staffpage.html', stu)
