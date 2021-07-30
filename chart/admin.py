from django.contrib import admin
from .models import Chart

# Register your models here.
class ChartAdmin(admin.ModelAdmin):
    list_display = ('heading','content','percentage')
    
admin.site.register(Chart, ChartAdmin)