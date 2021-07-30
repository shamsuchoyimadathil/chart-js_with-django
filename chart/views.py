from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView

# Create your views here.

from . models import Chart
from . forms import ChartForm , ChartForm1


def chart_continue_view(request):
    
    files = Chart.objects.all()
    if request.method == "POST":
        form = ChartForm1(request.POST)

        if form.is_valid():
            heading = request.session.get('heading')
            form_data = form.cleaned_data
            c = Chart(heading=heading, content=form_data['content'], percentage=form_data['percentage'])
            c.save()
            return HttpResponseRedirect(reverse('chart-continue-view'))
    else:
        form = ChartForm1()

    return render(request,"chart.html",{
        "file":files,
        "form":form,
    })


def chart_view(request):
    print('chart_view', request)
    files = Chart.objects.all()

    if request.method == "POST":
        form = ChartForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['heading'] = form.cleaned_data['heading']

            return HttpResponseRedirect(reverse('chart-continue-view'))

    else:
        form = ChartForm()

    return render(request,"chart.html",{
        "file":files,
        "form":form,
    })


def delete_all_data(request):
    dlt = Chart.objects.all().delete()
    request.session['heading'] = None
    return HttpResponseRedirect("/")
