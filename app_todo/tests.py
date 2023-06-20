from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from app_todo.models import Task


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Test_1', password='hello!123')

    def test_login_user(self):
        response = self.client.post('/login/', data={'username': 'Test_1', 'password': 'hello!123'})
        self.assertEqual(response.status_code, 302)

    def test_logout_user(self):
        self.client.login(username='Test_1', password='hello!123')
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        self.client.logout()
        response = self.client.post('/register/', data={'username': 'Username', 'email': 'username@yandex.ru',
                                                        'password1': 'hello!1234', 'password2': 'hello!1234'})
        self.assertEqual(response.status_code, 302)


class TaskTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Test',
            password='111',
        )

    def test_homepage_for_not_auth_user(self):
        response = self.client.get('/')
        self.assertEqual(response.url, '/login')

    def test_homepage_for_auth_user(self):
        self.client.login(username='Test', password='111')
        response = self.client.get('/')
        self.assertEqual(response.url, '/tasks')

    def test_create_task_status(self):
        self.client.login(username='Test', password='111')
        response = self.client.post('/tasks', data={'name': 'hello world'})
        self.assertEqual(response.status_code, 301)

    def test_create_task(self):
        self.client.login(username='Test', password='111')
        self.client.post('/tasks/', data={'name': 'hello world'})
        self.assertTrue(Task.objects.filter(name='hello world').exists(), "Task didnt add!")

    def test_delete_task(self):
        self.client.login(username='Test', password='111')
        self.client.post('/tasks/', data={'name': 'hello world'})
        task_id = Task.objects.filter(name='hello world').get().id
        self.client.get(f'/tasks/{task_id}/delete/')
        self.assertFalse(Task.objects.filter(name='hello world').exists(), "Task didnt delete!")
