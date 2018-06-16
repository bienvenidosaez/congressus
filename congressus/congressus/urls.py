"""congressus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('window/', include('windows.urls')),
    path('access/', include('access.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('report/', include('dashboard.urls_report')),
    path('invs/', include('invs.urls')),
    path('', include('tickets.urls')),
]

if 'theme' in settings.INSTALLED_APPS:
    urlpatterns += path('custom/', include('theme.urls')),

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('debug/', include(debug_toolbar.urls)),
        path('silk/', include('silk.urls', namespace='silk'))
    ]
