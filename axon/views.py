from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext, loader

def index(request):
    return render_to_response('index.html')
