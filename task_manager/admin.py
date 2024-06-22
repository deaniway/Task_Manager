from django.contrib import admin
from apps.labels.models import Label
from apps.tasks.models import Task
from apps.statuses.models import Status

admin.site.register(Label)
admin.site.register(Task)
admin.site.register(Status)
