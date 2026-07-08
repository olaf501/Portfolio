from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation

def project_list_view(request):
    # Fetch all projects from the database
    projects = Project.objects.all()
    # Fetch your personal information profile row
    personal_info = PersonalInformation.objects.first()
    
    context = {
        'projects': projects,
        'personal_info': personal_info
    }
    return render(request, 'Core/home.html', context)

def project_detail_view(request, project_id):
    # Fetch the precise project or return a 404 error if it's missing
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project': project
    }
    return render(request, 'Core/detail.html', context)