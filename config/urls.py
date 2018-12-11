from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from apps.base.views import AboutView, IndexView, NameChange, http_404, http_500
from apps.contact.views import ContactFormView

urlpatterns = []

# Debug/Development URLs
if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/doc/', include('django.contrib.admindocs.urls')),
    ]
admin.autodiscover()

# Includes
urlpatterns += [
    path(r'admin/', admin.site.urls),
]

# Project Urls
urlpatterns += [
    path('', IndexView.as_view(), name='site_index'),
    path('500/', http_500),
    path('404/', http_404),
    path('accounts/name/', NameChange.as_view(), name='account_change_name'),
    path('accounts/', include('allauth.urls')),
    url('about/', AboutView.as_view(), name='site_about'),
    re_path(r'^contact/', include('apps.contact.urls', namespace='contact')),
    re_path(r'^blog/', include('apps.blogs.urls', namespace='blogs')),

]
