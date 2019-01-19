from django.urls import reverse

from model_mommy import mommy

from apps.base.tests.test_base import BaseTest


class BaseTestContact(BaseTest):
    def setUp(self):
        super().setUp()
        self.contact = mommy.make('contact.Contact')


class TestContact(BaseTestContact):

    def test_url(self):
        expected_url = reverse('contact:contact_detail', kwargs={'pk': self.contact.pk})
        actual_url = self.contact.get_absolute_url()
        self.assertEqual(expected_url, actual_url)
