from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .views import IndexView
from django.conf import settings

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home_view'),
    # url(r'^$', Portfolio.as_view(), name='portfolio_view'),
    # url(r'^$', Team.as_view(), name='team_view'),
    # url(r'^$', Sources.as_view(), name='sources_view'),
    # url(r'^$', About.as_view(), name='about_view'),
    # url(r'^$', Contact.as_view(), name='contact_view'),
]