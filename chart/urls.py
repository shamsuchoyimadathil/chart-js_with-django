from chart import views
from django.urls import path

urlpatterns = [
    path("",views.chart_view,name="chart-view"),
    path("delete-all",views.delete_all_data,name="deleteall")
    # path("delete-all/<slug:pk>/",views.Delete_data.as_view(),name="deleteall")
]

