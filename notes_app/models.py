from django.db import models

# Create your models here.
class ClassName(models.Model):
    first_name =  models.CharField(max_length=30)
    second_name =  models.CharField(max_length=30)
