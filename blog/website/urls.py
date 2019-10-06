from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('connection', views.connection, name='connection'),
    path('logout', views.disconnect, name='logout'),
    path('add-project', views.addProject, name='add_project'),
    path('project/<int:project_number>', views.project, name='project'),
    path('mentions', views.mentions, name='mentions'),
    path('contact', views.contact, name='contact'),
    path('delete-comment', views.deleteComment, name='delete_comment'),
    path('add-comment', views.addComment, name='add_comment'),
]