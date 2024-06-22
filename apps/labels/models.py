from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel

"""
class Label(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
        unique=True,
    )

    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Created'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
"""


class Label(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
        unique=True,
    )

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
