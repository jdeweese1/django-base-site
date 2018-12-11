from django.db import models
from django.utils import timezone


class Contact(models.Model):
    sender_name = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
