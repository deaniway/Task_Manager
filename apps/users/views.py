from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from core.mixins import LoginRequiredAndUserSelfCheckMixin
from apps.users.forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin


# Отображение
class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'
    context_object_name = 'users'


# Создание
class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')  # отложенное определение URL-адреса
    success_message = _("The user has been successfully registered")


# Редактирование
class UserUpdateView(LoginRequiredAndUserSelfCheckMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_list')  # Перенаправление
    success_message = _("User successfully updated")  # Флешка и перевод строки через '_'


# Удаление
class UserDeleteView(LoginRequiredAndUserSelfCheckMixin, SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')  # Перенаправление
    success_message = _("User successfully deleted")
