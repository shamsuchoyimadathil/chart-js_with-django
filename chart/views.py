from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def chart_view(request):
    return HttpResponse("<h1>it's working</h1>")