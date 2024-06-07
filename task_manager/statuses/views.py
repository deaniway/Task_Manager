from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.mixins import CustomLoginRequired
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses.models import Status


class StatusListView(CustomLoginRequired, ListView):
    model = Status
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'


class StatusCreateView(CustomLoginRequired, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("The status has been successfully created")


class StatusUpdateView(CustomLoginRequired, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("The status has been successfully updated")


class StatuesDeleteView(CustomLoginRequired,SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("The status has been successfully deleted")

