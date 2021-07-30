from chart import views
from django.urls import path

urlpatterns = [
    path("",views.chart_view,name="chart-view"),
    path("continue",views.chart_continue_view,name="chart-continue-view"),
    path("delete-all",views.delete_all_data,name="deleteall")
]

