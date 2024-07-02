from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext
from django.utils.translation import gettext as _


class CustomLoginRequired(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, gettext('You are not logged in! Please log in.'))
        return redirect(reverse('login'))


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
