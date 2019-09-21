"""Import django module and models"""
from django.shortcuts import render

def home(request):
    """Home Page"""
    return render(request, 'pages/index.html')

def project(request):
    """request page"""
    return render(request, 'pages/index.html')