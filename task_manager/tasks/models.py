from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone
from task_manager.statuses.models import Status


class Task(models.Model):

    name = models.CharField(_('name'), max_length=256, unique=True)

    description = models.TextField(_('description'), blank=True)

    creator = models.ForeignKey(get_user_model(),
                                on_delete=models.PROTECT,
                                verbose_name=_('creator'),
                                related_name='create_tasks'
                                )

    executor = models.ForeignKey(get_user_model(),
                                 on_delete=models.PROTECT,
                                 verbose_name=_('executor'),
                                 related_name='executor_tasks',
                                 blank=True,  # может быть пустым (или нет)
                                 null=True  # значение null может быть в бд
                                 )

    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,  # сносим 1 статус
                               verbose_name=_('status'),
                               related_name='tasks'
                               )

    created_at = models.DateTimeField(_('created'), default=timezone.now)  # ?default=timezone.now

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
