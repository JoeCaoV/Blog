"""Import django module and models"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    """Home Page"""
    return render(request, 'pages/index.html')

def add_project(request):
    """Page to create a new project"""
    return render(request, 'pages/index.html')
def project(request):
    """request page"""
    return render(request, 'pages/index.html')

def registration(request):
    """Page to create an account"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'pages/registration.html', context)

def connection(request):
    """page to log in"""
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context['error'] = 'Le mot de passe & le pseudo ne correspondent pas.'
        except:
            context['error'] = 'Le mot de passe & le pseudo ne correspondent pas.'

    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, 'pages/connection.html', context)

def disconnect(request):
    """page to log out"""
    logout(request)
    return redirect('home')