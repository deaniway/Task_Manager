from task_manager.tasks.models import Task
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from task_manager.tasks.filters import TaskFilter
from task_manager.mixins import CustomLoginRequired
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect


class TaskFilterView(CustomLoginRequired, FilterView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskDetailView(CustomLoginRequired, DetailView):
    model = Task
    template_name = 'tasks/detail.html'


class TaskCreateView(CustomLoginRequired,SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'labels', 'executor']
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _("The task has been created")

    # для назначения создателя
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequired, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'labels', 'executor']
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _("The task has been successfully updated")


class TaskDeleteView(CustomLoginRequired, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _("The task has been successfully deleted")

    def check_task_creator(self):
        if self.get_object().creator != self.request.user:
            messages.error(
                self.request,
                _('Only the author of the task can delete it'))
            return False
        return True

    def get(self, request, *args, **kwargs):
        if not self.check_task_creator():
            return redirect('tasks_list')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.check_task_creator():
            return redirect('tasks_list')
        return super().post(request, *args, **kwargs)
