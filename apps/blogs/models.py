from datetime import datetime

from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from apps.base import mixins

# Create your models here.


class Blog(mixins.IsHiddenMixin, mixins.CreationDateMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    pub_date = models.DateField(null=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_hidden = models.BooleanField(default=False)

    class Meta(object):
        verbose_name = "Blog"

    def get_absolute_url(self):
        slug = self.title.lower().replace(' ', '-')
        return reverse('blogs:blog_detail_slug', kwargs={'slug': slug, 'pk': self.pk})

    @property
    def is_visible(self):
        return self.pub_date < datetime.date(datetime.now()) and self.is_hidden is False

    def __str__(self):
        return self.title

    @staticmethod
    def get_model_verbose_name(cls=None):
        return "Blog"
