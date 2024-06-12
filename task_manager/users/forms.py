from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username',]

    '''def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance.username == username:
            return username
        return username'''
