#!/usr/bin/env python
#encoding:utf-8
from django.http import Http404
from django.shortcuts import render_to_response, RequestContext


def index(request):
    return render_to_response(
                'admin_main.html'
            )
