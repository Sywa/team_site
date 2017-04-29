from django.shortcuts import render
import datetime
import json
import requests
import hashlib
import urllib
import logging

from django.conf import settings
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.views.generic import View, TemplateView


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class Portfolio(TemplateView):
    def get(self, request):
        return HttpResponse("Here's the text of the Web page.")