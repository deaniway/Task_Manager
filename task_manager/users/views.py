from django.urls import reverse_lazy  # Для отложенного вычисления URL-адресов
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Классовые представления
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from task_manager.mixins import CustomLoginRequired
from task_manager.users.forms import UserForm

User = get_user_model()  # Получаем юзера


class LoginRequiredAndUserSelfCheckMixin(CustomLoginRequired, UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            messages.error(
                self.request,
                _('You do not have permission to modify another user.'))
            return redirect('user_list')


# Отображение
class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'


# Создание
class UserCreateView(CreateView):
    model = User()
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')  # отложенное определение URL-адреса до момента его фактического использования.
    success_message = _("The user has been successfully registered")  # The user has been successfully registered


# Редактирование
class UserUpdateView(LoginRequiredAndUserSelfCheckMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_list')  # Перенаправление
    success_message = _("User successfully updated")  # Флешка и перевод строки через '_'

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid!")
        print("Response status code:", response.status_code)
        return response


# Удаление
class UserDeleteView(LoginRequiredAndUserSelfCheckMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')  # Перенаправление
    success_message = _("User successfully deleted")
