from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus

# Create your views here.

def base(request):

    bus = Bus.objects.all()

    print(bus)

    context = {
        "data": bus
    }

    return render(request,"base/index.html",context)