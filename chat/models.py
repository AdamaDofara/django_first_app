from datetime import datetime
from django.db import models

from client.models import Client

# Create your models here.
class Message(models.Model):
    value = models.CharField(max_length=1000)
    date_creation = models.DateTimeField(default=datetime.now, blank=True)
    client = models.ForeignKey(Client, null=True,on_delete=models.SET_NULL)