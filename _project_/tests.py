from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.logged_user_data = {'username': 'way', 'password': '1234qwertertyr1'}
        cls.logged_user = get_user_model().objects.create_user(**cls.logged_user_data)

    def login(self):
        self.client.login(**self.logged_user_data)


class TestIndexTemplateView(BaseTestCase):
    def setUp(self):
        self.url = reverse('index')
        self.login()

    def test_index_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class TestUserLoginView(BaseTestCase):
    def setUp(self):
        self.url = reverse('login')
        self.login()

    def test_user_login_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_user_login_view_post(self):
        self.client.logout()
        response = self.client.post(self.url, self.logged_user_data)
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(int(self.client.session['_auth_user_id']), self.logged_user.pk)


class TestUserLogoutView(BaseTestCase):
    def setUp(self):
        self.url = reverse('logout')
        self.login()

    def test_user_logout_view_post(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('index'))


class TestNotFoundPage(TestCase):
    def test_not_found_page(self):
        response = self.client.get('/not-founded-page/')
        self.assertEqual(response.status_code, 404)
