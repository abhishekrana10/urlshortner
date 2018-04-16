from django.urls import path, re_path

from . import views

app_name = "short_url"
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^(?P<code>[\w]{8})/$', views.page_redirect, name='page_redirect' )
]