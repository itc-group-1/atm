
from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):

    return render(request, 'bootstrap.html')