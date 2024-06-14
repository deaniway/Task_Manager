from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.utils.translation import gettext as _

User = get_user_model()


class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.logged_user_data = {'username': 'albert_einstein', 'password': 'qwer1234qwer1234'}
        cls.logged_user = User.objects.create_user(**cls.logged_user_data)

    def login(self):
        self.client.login(**self.logged_user_data)


class TestUserListView(BaseTestCase):
    def setUp(self):
        self.url = reverse('user_list')

    def test_user_list_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/list.html')


class TestUserCreateView(BaseTestCase):
    def setUp(self):
        self.url = reverse('user_create')

    def test_user_create_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

    def test_user_create_view_post(self):
        user_data = {
            'username': 'isaac_newton',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'isaac@example.com'
        }
        response = self.client.post(self.url, user_data)
        self.assertRedirects(response, reverse('login'), status_code=302)

        # Проверяем, что сообщение об успешной регистрации добавлено в контекст
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(_("The user has been successfully registered") in str(message) for message in messages))


class TestUserUpdateView(BaseTestCase):
    def setUp(self):
        self.url = reverse('user_update', args=[self.logged_user.pk])
        self.login()

    def test_user_update_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')


class TestUserDeleteView(BaseTestCase):
    def setUp(self):
        self.url = reverse('user_delete', args=[self.logged_user.pk])
        self.login()

    def test_user_delete_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')

    def test_user_delete_view_post(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('user_list'), status_code=302)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(_("User successfully deleted") in str(message) for message in messages))
        self.assertFalse(User.objects.filter(pk=self.logged_user.pk).exists())


class TestPermissionDenied(BaseTestCase):
    def setUp(self):
        self.other_user = User.objects.create_user(username='nikola_tesla', password='testpassword123')
        self.update_url = reverse('user_update', args=[self.other_user.pk])
        self.delete_url = reverse('user_delete', args=[self.other_user.pk])
        self.login()

    def test_permission_denied_update(self):
        response = self.client.get(self.update_url)
        self.assertRedirects(response, reverse('user_list'), status_code=302)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any(_("You do not have permission to modify another user.") in str(message) for message in messages))

    def test_permission_denied_delete(self):
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, reverse('user_list'), status_code=302)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any(_("You do not have permission to modify another user.") in str(message) for message in messages))
