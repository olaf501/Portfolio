from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Project, PersonalInformation, Testimony, Inquiry
from .forms import ProjectForm, TestimonyForm, InquiryForm


def project_list_view(request):
    projects = Project.objects.all()
    personal_info = PersonalInformation.objects.first()
    context = {
        'projects': projects,
        'personal_info': personal_info
    }
    return render(request, 'Core/home.html', context)


def project_detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project
    }
    return render(request, 'Core/detail.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'Core/add_project.html', {'form': form})


def contact_view(request):
    success = False
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = InquiryForm()
    else:
        form = InquiryForm()
    return render(request, 'Core/contact.html', {'form': form, 'success': success})


def add_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'Core/add_testimony.html', {'form': form})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'Core/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-created_at']


def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'Core/testimony_detail.html', {'testimony': testimony})