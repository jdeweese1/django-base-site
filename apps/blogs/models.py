from datetime import datetime

from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from apps.base import mixins

# Create your models here.


class Blog(mixins.IsHiddenMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    pub_date = models.DateField(null=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_hidden = models.BooleanField(default=False)

    def get_absolute_url(self):
        slug = self.title.lower().replace(' ', '-')
        return reverse('blogs:blog_detail_slug', kwargs={'slug': slug, 'pk': self.pk})

    @property
    def is_visible(self):
        return self.pub_date < datetime.date(datetime.now()) and self.is_hidden is False
