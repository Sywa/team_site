from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .views import IndexView, Portfolio
from django.conf import settings

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home_view'),
    url(r'^portfolio', TemplateView.as_view(template_name="portfolio.html"), name='portfolio_view'),
    url(r'^contact', TemplateView.as_view(template_name="contact.html"), name='contact_view'),
    url(r'^about', TemplateView.as_view(template_name="about.html"), name='about_view'),
    url(r'^team', TemplateView.as_view(template_name="team.html"), name='team_view'),
    url(r'^sources', TemplateView.as_view(template_name="sources.html"), name='sources_view'),
]