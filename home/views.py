# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie

from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string


def index(request):

    return render_to_response('home/index.html', {}, context_instance=RequestContext(request))