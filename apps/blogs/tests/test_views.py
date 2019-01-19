import datetime
from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from apps.base.tests.test_base import BaseTest


class BlogTest(BaseTest):
    def setUp(self):
        super().setUp()
        future_date = timezone.now() + timedelta(days=3)
        hidden_blog = self.mommy.make('blogs.Blog', title='First_blog', is_hidden=True)
        visible_blog = self.mommy.make('blogs.Blog', title='Second blog', is_hidden=False)
        future_blog = self.mommy.make('blogs.Blog', title='Future blog', is_hidden=False, pub_date=future_date)


class TestBlogList(BlogTest):

    def setUp(self):
        super().setUp()
        self.url = reverse('blogs:blog_list')

    def test_visible_blogs(self):
        import ipdb; ipdb.set_trace()
        resp = self.client.get(self.url)
