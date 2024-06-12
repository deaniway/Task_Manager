from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import reverse
from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status


class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        cls.status = Status.objects.create(name='Test status')
        cls.test_label = Label.objects.create(name='Test label')
        cls.test_task = Task.objects.create(
            name='Test task',
            description='Test description',
            creator=cls.user,
            status=cls.status
        )
        cls.test_task.labels.add(cls.test_label)

    def login(self):
        self.client.login(username='testuser', password='testpassword')


class LabelListViewTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('labels_list')

    def test_label_list_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/list.html')
        self.assertContains(response, 'Test label')


class LabelCreateViewTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('label_create')
        cls.data = {'name': 'New Label'}

    def test_label_create_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/create.html')

    def test_label_create_view_post(self):
        self.login()
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse('labels_list'))
        self.assertTrue(Label.objects.filter(name='New Label').exists())


class LabelUpdateViewTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('label_update', kwargs={'pk': cls.test_label.pk})
        cls.data = {'name': 'Updated Label'}

    def test_label_update_view_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/update.html')

    def test_label_update_view_post(self):
        self.login()
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse('labels_list'))
        self.test_label.refresh_from_db()
        self.assertEqual(self.test_label.name, 'Updated Label')


class LabelDeleteViewTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('label_delete', kwargs={'pk': cls.test_label.pk})
        cls.url_list = reverse('labels_list')

    def test_label_delete_view_post_with_task(self):
        self.login()
        response = self.client.post(self.url)
        self.assertRedirects(response, self.url_list)
        self.assertTrue(Label.objects.filter(pk=self.test_label.pk).exists())

    def test_label_delete_view_post(self):
        self.test_task.labels.remove(self.test_label)
        self.login()
        response = self.client.post(self.url)
        self.assertRedirects(response, self.url_list)
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(pk=self.test_label.pk)
