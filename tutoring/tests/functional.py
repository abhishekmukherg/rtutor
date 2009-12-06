from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

import tutoring.models

class ScrapeTest(TestCase):

    def __init__(self, *args, **kwargs):
        super(ScrapeTest, self).__init__(*args, **kwargs)
        self.url = reverse('tutoring.views.scrape')

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user('foo', 'bar@baz.com', 'foo')
        self.user.user_permissions = [
                Permission.objects.get(codename='add_subject'),
                Permission.objects.get(codename='add_course'),
                Permission.objects.get(codename='add_courselisting'),
        ]
        self.user.save()

        self.superuser = User.objects.create_user('bar', 'foo@baz.com', 'foo')
        self.superuser.is_superuser = True
        self.superuser.save()

    def test_unauthenticated_get_form(self):
        response = self.client.get(self.url)
        self.assertRedirects(response,
                settings.LOGIN_URL + '?next=' + self.url,
                status_code=302)

    def test_authenticated_get_form(self):
        self.assert_(self.client.login(username='foo', password='foo'))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_superuser_authenticated_get_form(self):
        self.assert_(self.client.login(username='bar', password='foo'))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_superuser_bad_url(self):
        self.assert_(self.client.login(username='bar', password='foo'))
        response = self.client.post(self.url, {'url': 'hello_world'})
        self.assertFormError(response, 'form', 'url', u'Enter a valid URL.')

    def test_superuser_bad_url(self):
        self.assert_(self.client.login(username='bar', password='foo'))
        response = self.client.post(self.url, {'url': 'hello_world'})
        self.assertFormError(response, 'form', 'url', u'Enter a valid URL.')

