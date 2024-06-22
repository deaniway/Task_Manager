from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from apps.labels.models import Label
from core.mixins import CustomLoginRequired


class LabelListView(CustomLoginRequired, ListView):
    model = Label
    template_name = 'labels/list.html'
    context_object_name = 'labels'


class LabelCreateView(CustomLoginRequired, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_list')
    success_message = _("The label has been successfully created")


class LabelUpdateView(CustomLoginRequired, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels_list')
    success_message = _("The label has been successfully updated")


class LabelDeleteView(CustomLoginRequired, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_list')
    success_message = _('The label has been successfully deleted')

    def post(self, request, *args, **kwargs):
        if self.get_object().tasks.exists():
            messages.error(
                self.request,
                _('Unable to delete a label because it is being used'))
            return redirect('labels_list')
        return super().post(request, *args, **kwargs)
