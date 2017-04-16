from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .views import IndexView
from django.conf import settings

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home_view'),
]