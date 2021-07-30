from django.db import models

# Create your models here.

class Chart(models.Model):
    heading = models.CharField( default="", max_length=50)
    content = models.CharField(max_length=100)
    percentage = models.CharField(default="",max_length=50)
    def __str__(self):
        return f"{self.content}"


class Chart1(models.Model):
    content = models.CharField(max_length=100)
    percentage = models.CharField(default="",max_length=50)
    def __str__(self):
        return f"{self.content}"

