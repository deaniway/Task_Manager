from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from core.mixins import CustomLoginRequired
from django.contrib.messages.views import SuccessMessageMixin
from apps.statuses.models import Status


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
    fields = ['name']
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("The status has been successfully updated")


class StatuesDeleteView(CustomLoginRequired, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("The status has been successfully deleted")

    def post(self, request, *args, **kwargs):
        if self.get_object().tasks.exists():
            messages.error(
                self.request,
                _('Unable to delete a status because it is being used'))
            return redirect('statuses_list')
        return super().post(request, *args, **kwargs)
