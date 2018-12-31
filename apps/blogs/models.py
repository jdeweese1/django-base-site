from django.conf import settings
from django.db import models

from apps.base import mixins

# Create your models here.


class Blog(mixins.IsHiddenMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    pub_date = models.DateField(null=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_hidden = models.BooleanField(default=False)
