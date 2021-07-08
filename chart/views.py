from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Chart

# Create your views here.

def chart_view(request):
    files = Chart.objects.all()

    return render(request,"chart.html",{
        "file":files,

    })

