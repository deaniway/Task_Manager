from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from apps.tasks.models import Task
from core.tests import TaskTestCase


class TaskDetailViewTests(TaskTestCase):

    def test_task_detail_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)

    def test_task_detail_view_get_not_logged_in(self):
        response = self.client.get(self.url_detail)
        self.assertRedirects(response, settings.LOGIN_URL)


class TaskFilterViewTests(TaskTestCase):

    def test_task_filter_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['tasks']), Task.objects.all())

    def test_task_filter_view_get_not_logged_in(self):
        response = self.client.get(self.url_list)
        self.assertRedirects(response, settings.LOGIN_URL)


class TaskCreateViewTests(TaskTestCase):

    def test_task_create_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_create)
        self.assertEqual(response.status_code, 200)

    def test_task_create_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'name': 'New task',
            'description': 'New description',
            'status': self.test_status.pk
        }
        response = self.client.post(self.url_create, data)
        self.assertRedirects(response, self.url_list)
        self.assertTrue(Task.objects.filter(name='New task').exists())

    def test_task_create_view_get_not_logged_in(self):
        response = self.client.get(self.url_create)
        self.assertRedirects(response, settings.LOGIN_URL)

    def test_task_create_view_post_not_logged_in(self):
        data = {
            'name': 'New task',
            'description': 'New description',
            'status': self.test_status.pk
        }
        response = self.client.post(self.url_create, data)
        self.assertRedirects(response, settings.LOGIN_URL)
        self.assertFalse(Task.objects.filter(name='New task').exists())


class TaskUpdateViewTests(TaskTestCase):

    def test_task_update_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_update)
        self.assertEqual(response.status_code, 200)

    def test_task_update_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'name': 'Updated task',
            'description': 'Updated description',
            'status': self.test_status.pk
        }
        response = self.client.post(self.url_update, data)
        self.assertRedirects(response, self.url_list)
        self.test_task.refresh_from_db()
        self.assertEqual(self.test_task.name, 'Updated task')
        self.assertEqual(self.test_task.description, 'Updated description')

    def test_task_update_view_get_not_logged_in(self):
        response = self.client.get(self.url_update)
        self.assertRedirects(response, settings.LOGIN_URL)

    def test_task_update_view_post_not_logged_in(self):
        data = {
            'name': 'Updated task',
            'description': 'Updated description',
            'status': self.test_status.pk
        }
        response = self.client.post(self.url_update, data)
        self.assertRedirects(response, settings.LOGIN_URL)
        self.test_task.refresh_from_db()
        self.assertNotEqual(self.test_task.name, 'Updated task')


class TaskDeleteViewTests(TaskTestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        # Создаем задачу, которую может удалить testuser
        cls.user_created_task = Task.objects.create(
            name='User Created Task',
            description='Task created by testuser',
            status=cls.test_status,
            creator=cls.user
        )
        cls.url_delete_user_task = reverse('task_delete', kwargs={'pk': cls.user_created_task.pk})
        cls.url_delete_other_task = reverse('task_delete', kwargs={'pk': cls.test_task.pk})

    def test_task_delete_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url_delete_user_task)
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url_delete_user_task)
        self.assertRedirects(response, self.url_list)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(pk=self.user_created_task.pk)

    def test_task_delete_view_post_other_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url_delete_other_task)
        self.assertRedirects(response, self.url_list)
        self.assertTrue(
            Task.objects.filter(pk=self.test_task.pk).exists(),
            'Task should not be deleted by another user'
        )

    def test_task_delete_view_get_not_logged_in(self):
        response = self.client.get(self.url_delete_user_task)
        self.assertRedirects(response, settings.LOGIN_URL)

    def test_task_delete_view_post_not_logged_in(self):
        response = self.client.post(self.url_delete_user_task)
        self.assertRedirects(response, settings.LOGIN_URL)
        self.assertTrue(Task.objects.filter(pk=self.user_created_task.pk).exists())
