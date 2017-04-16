from django.shortcuts import render
import datetime
import json
import requests
import hashlib
import urllib
import logging

from django.conf import settings
from django.http import HttpResponsePermanentRedirect
#from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, TemplateView
#from cover_images.models import CoverImage
#from inventory.models import FeaturedBoat
#from destinations.models import DestinationAlias, AliasSerializer
from django.contrib.gis.geoip import GeoIP


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
