from django.conf.urls import re_path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'contact'

urlpatterns = (
    re_path(r'^$', views.ContactFormView.as_view(), name='site_contact'),
    re_path(r'^list/$', login_required(views.ContactListView.as_view()), name='contact_list'),
    re_path(r'^(?P<pk>[\d]+)/$', login_required(views.ContactDetailView.as_view()), name='contact_detail'),
    re_path(r'^submitted', views.contact_submitted, name='contact_submitted')
)
