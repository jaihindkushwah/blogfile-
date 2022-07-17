from django.db import models
from datetime import datetime
# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=50)
    created_time=models.DateTimeField(default=datetime.now,blank=False)
    body = models.CharField(max_length=50000)

