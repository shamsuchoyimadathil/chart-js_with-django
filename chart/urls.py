from chart import views
from django.urls import path

urlpatterns = [
    path("",views.chart_view,name="chart-view")
]
