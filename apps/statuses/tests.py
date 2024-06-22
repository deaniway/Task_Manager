from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import reverse
from apps.statuses.models import Status
from core.tests import StatusTestCase


class StatusListViewTests(StatusTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('statuses_list')

    def test_status_list_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/list.html')
        self.assertContains(response, 'Test status')


class StatusCreateViewTests(StatusTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('status_create')
        cls.data = {'name': 'New Status'}

    def test_status_create_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/create.html')

    def test_status_create_view_post(self):
        self.login()
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertTrue(Status.objects.filter(name='New Status').exists())


class StatusUpdateViewTests(StatusTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('status_update', kwargs={'pk': cls.test_status.pk})
        cls.data = {'name': 'Updated Status'}

    def test_status_update_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/update.html')

    def test_status_update_view_post(self):
        self.login()
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse('statuses_list'))
        self.test_status.refresh_from_db()
        self.assertEqual(self.test_status.name, 'Updated Status')


class StatusDeleteViewTests(StatusTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('status_delete', kwargs={'pk': cls.test_status.pk})
        cls.url_list = reverse('statuses_list')

    def test_status_delete_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/delete.html')

    def test_status_delete_view_post(self):
        self.login()
        response = self.client.post(self.url)
        self.assertRedirects(response, self.url_list)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=self.test_status.pk)

    def test_status_delete_view_get_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, settings.LOGIN_URL)

    def test_status_delete_view_post_not_logged_in(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, settings.LOGIN_URL)
        self.assertTrue(Status.objects.filter(pk=self.test_status.pk).exists())
