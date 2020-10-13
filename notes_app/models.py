from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active = models.BooleanField(default=True)
    tags = models.CharField(blank=True, max_length=100)
