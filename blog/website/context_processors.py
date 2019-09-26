from .models import Project

def get_projects(request):
    projects = Project.objects.all().order_by('number')
    return {'projects' : projects}
