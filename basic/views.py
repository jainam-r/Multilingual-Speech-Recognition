from django.shortcuts import render
import os
from mysite import settings
from django.http import HttpResponse
# Create your views here.
def index(request):
    try:
        with open(os.path.join(settings.REACT_APP_DIR,'build','index.html')) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        return HttpReponse(
            'Not working',
            status=501,
        )