from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    return HttpResponse('<h1 style="color:blue;background-color:black">Hello world</h1> <h2 style="color:red">HACKER</h2> <br> <h2 style="color:green">HACKER</h2>')