from django.contrib.auth import get_user_model
from django.test import TestCase
from apps.statuses.models import Status
from apps.tasks.models import Task
from apps.labels.models import Label
from django.shortcuts import reverse


class LoggedUserAndTestDataTaskMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.logged_user_data = {'username': 'testuser', 'password': 'testpassword234'}
        cls.logged_user = get_user_model().objects.create_user(**cls.logged_user_data)

    def login(self):
        self.client.login(**self.logged_user_data)


"""
class TaskTestCase(UserTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()  # Вызов метода setUpTestData из базового класса
        cls.test_status = Status.objects.create(name='Test status')
        cls.other_user = get_user_model().objects.create_user(username='otheruser',
                                                              password='otherpassword234')
        cls.test_task = Task.objects.create(
            name='Test task',
            description='Test description',
            status=cls.test_status,
            creator=cls.other_user
        )
        cls.url_detail = reverse('task_detail', kwargs={'pk': cls.test_task.pk})
        cls.url_list = reverse('tasks_list')
        cls.url_create = reverse('task_create')
        cls.url_update = reverse('task_update', kwargs={'pk': cls.test_task.pk})
        cls.url_delete = reverse('task_delete', kwargs={'pk': cls.test_task.pk})
"""


class StatusTestCase(LoggedUserAndTestDataTaskMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.test_status = Status.objects.create(name='Test status')

    def login(self):
        self.client.login(**self.logged_user_data)


class TaskTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser',
                                                        password='testpassword'
                                                        )
        cls.test_status = Status.objects.create(name='Test status')
        cls.other_user = get_user_model().objects.create(username='otheruser',
                                                         password='otherpassword'
                                                         )
        cls.test_task = Task.objects.create(
            name='Test task',
            description='Test description',
            status=cls.test_status,
            creator=cls.other_user
        )
        cls.url_detail = reverse('task_detail', kwargs={'pk': cls.test_task.pk})
        cls.url_list = reverse('tasks_list')
        cls.url_create = reverse('task_create')
        cls.url_update = reverse('task_update', kwargs={'pk': cls.test_task.pk})
        cls.url_delete = reverse('task_delete', kwargs={'pk': cls.test_task.pk})


class LabelTestCase(LoggedUserAndTestDataTaskMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.status = Status.objects.create(name='Test status')
        cls.test_label = Label.objects.create(name='Test label')
        cls.test_task = Task.objects.create(
            name='Test task',
            description='Test description',
            creator=cls.logged_user,
            status=cls.status
        )
        cls.test_task.labels.add(cls.test_label)
