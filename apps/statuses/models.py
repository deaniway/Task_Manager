from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Status(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
