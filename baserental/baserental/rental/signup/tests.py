# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
# Create your tests here.
from django.contrib.auth import get_user_model

from django.test import Client, TestCase

class TestLoggedUser(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.user = User.objects.create_user('test_user', 'user@test.net', 'secret')
        self.user.save()
        self.client.login(username='test_user', password='secret')
    
    def tearDown(self):
        self.user.delete()
    
    def test_logged_user_get_homepage(self):
        response = self.client.get(reverse('/'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_logged_user_get_settings(self):
        response = self.client.get(reverse('/settings/'), follow=True)
        self.assertEqual(response.status_code, 200)

class TestcaseUserBackend(object):
    def authenticate(self, testcase_user=None):
        return testcase_user
    
    def test_get_user(self, user_id):
        User = get_user_model()
        return User.objects.get(pk=user_id)
