from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView

from . models import Chart
from . forms import ChartForm , ChartForm1

# Create your views here.

def chart_view(request):
    files = Chart.objects.all()

    if request.method == "POST":
        form = ChartForm1(request.POST)
       # print(form)
        if form.is_valid():
            clean_data = Chart()
            #clean_data.heading = form.cleaned_data["heading"]
            #clean_data.content = form.cleaned_data["content"]
            #clean_data.percentage = form.cleaned_data["percentage"]
            clean_data.save()

            form = ChartForm1()
            return render(request, "chart.html",{
                "file":files,
                "form":form,})
            #return HttpResponseRedirect('/')
    else:
        form = ChartForm()
        #delete_all = Chart.objects.all().delete()

    return render(request,"chart.html",{
        "file":files,
        "form":form,
        #"delete":delete_all
    })

# class Delete_data(DeleteView ,pk=p):
#     model = Chart
#     success_url ="/"

def delete_all_data(request):
    dlt = Chart.objects.all().delete()
    return HttpResponseRedirect("/")
