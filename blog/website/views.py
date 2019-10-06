"""Import django module and models"""
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CommentForm
from .models import Project, Comment

def home(request):
    """Home Page"""
    return render(request, 'pages/index.html')

def addProject(request):
    """Page to create a new project"""
    return render(request, 'pages/index.html')

def addComment(request):
    """Page process to add a comment"""
    if request.method == 'POST':
        form = request.POST
        project = Project.objects.get(number=form['number'])
        comment = Comment.objects.create(user=request.user,
                               content=form['content'],
                               project=project)
        try:
            return redirect('project', project_number=project.number)
        except:
            return redirect('home')
    return redirect('home')

def project(request, project_number):
    """Page that display the project"""
    number = project_number
    form = CommentForm
    try:
        project = Project.objects.get(number=number)
        form = CommentForm
        context = {'project' : project, 'form' : form }
    except Project.DoesNotExist:
        raise Http404()
    return render(request, 'pages/project.html', context)

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

def deleteComment(request):
    """Page process to delete a comment"""
    if request.method == 'POST':
        comment = Comment.objects.get(pk=request.POST['comment_id'])
        if comment.user == request.user:
            comment.delete()
            return HttpResponse('Comment deleted')
    return HttpResponse('Error')
        

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

def mentions(request):
    """Page to legals mentions"""
    return render(request, 'pages/mentions.html')

def contact(request):
    """Page to contact"""
    return render(request, 'pages/contact.html')

def handler404(request, exception):
    """Error page 404"""
    return render(request, 'errors/error404.html', status=404)

def handler500(request):
    """Error page 500"""
    return render(request, 'errors/error500.html')