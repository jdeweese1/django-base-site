from django.db import models


class IsHiddenMixin(models.Model):
    is_hidden = models.BooleanField(default=False)

    class Meta(object):
        abstract = True
