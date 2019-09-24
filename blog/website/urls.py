from django.urls import path, include
from . import views
from django.conf.urls import handler500, handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('connection', views.connection, name='connection'),
    path('logout', views.disconnect, name='logout'),
    path('add-project', views.add_project, name='add_project'),
    path('project/<int:project_number>', views.project, name='project'),
]