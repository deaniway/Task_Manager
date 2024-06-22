from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('created'),
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated'),
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
