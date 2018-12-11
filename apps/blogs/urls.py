from django.conf.urls import re_path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'blogs'

# Includes
urlpatterns = (
    re_path(r'^$', views.BlogIndex.as_view(), name='blog_index'),
    re_path(r'^(?P<pk>[\d]+)/$', views.BlogDetailView.as_view(), name='blog_detail'),
    re_path(r'^(?P<pk>[\d]+)/edit/$', login_required(views.BlogUpdateView.as_view()), name='blog_edit'),
    re_path(r'^create/$', login_required(views.BlogCreateView.as_view()), name='blog_create'),
    re_path(r'^list/$', login_required(views.BlogListView.as_view()), name='blog_list'),

)
