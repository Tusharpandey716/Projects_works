from django.http import HttpResponse
from django.shortcuts import render
#from other_app.views import Home

# Create your views here.
def home(request):
    return HttpResponse("hello to songs section")