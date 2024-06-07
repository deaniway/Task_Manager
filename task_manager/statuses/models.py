from django.db import models
from django.utils.translation import gettext_lazy
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=gettext_lazy('name'),
    )

    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=gettext_lazy('created'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = gettext_lazy('Status')
        verbose_name_plural = gettext_lazy('Statuses')
