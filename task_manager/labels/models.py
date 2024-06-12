from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Label(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
        unique=True,
    )

    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('created'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
