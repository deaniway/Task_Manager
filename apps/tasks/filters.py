from django_filters import FilterSet
from django_filters.filters import BooleanFilter, ModelChoiceFilter
from django.forms import CheckboxInput
from django.utils.translation import gettext as _
from apps.tasks.models import Task
from apps.labels.models import Label


class TaskFilter(FilterSet):

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),  # cвсе метки
        field_name='labels',  # для фильтрации по метке
        label=_('Label'),
    )

    tasks = BooleanFilter(
        widget=CheckboxInput,  # чекбокс для фильтрации
        field_name='creator',  # поля модели Task для фильтрации
        method='filter_tasks',  # фунционал фильтра
        label=_('Only your own tasks'),
    )

    def filter_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'tasks']  # тут все поля фильтров
