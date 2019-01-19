from django.db import models
from django.urls import reverse

from apps.base import mixins


class Contact(mixins.CreationDateMixin):
    sender_name = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('contact:contact_detail', kwargs={'pk': self.pk})
