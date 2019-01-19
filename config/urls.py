from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path

from allauth.account.views import LoginView

from apps.base.views import AboutView, DashboardView, IndexView, NameChange, PortfolioView, http_404, http_500

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
    path('accounts/signup', LoginView.as_view(), name='redirected_signup'),
    url('about/', AboutView.as_view(), name='site_about'),  # Redirected signup to sign in bc I don't want just anyone to be able to make an account
    re_path(r'^contact/', include('apps.contact.urls', namespace='contact')),
    re_path(r'^blog/', include('apps.blogs.urls', namespace='blogs')),
    re_path(r'^portfolio/', PortfolioView.as_view(), name='portfolio_index'),
    re_path(r'^dashboard/', login_required(DashboardView.as_view()), name='dashboard')

]
