from django.conf import settings
from django.db import models

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    pub_date = models.DateField(null=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
