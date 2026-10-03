from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import user_passes_test

from .models import Project, PersonalInformation, Testimony, Inquiry, TechStack
from .forms import ProjectForm, TestimonyForm, InquiryForm, SuperuserLoginForm, TechStackForm



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




class AdminLoginView(LoginView):
    template_name = 'Core/login.html'
    authentication_form = SuperuserLoginForm


def superuser_required(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(superuser_required, login_url='login')
def dashboard(request):
    projects = Project.objects.all()
    tech_stacks = TechStack.objects.all()
    return render(request, 'Core/dashboard.html', {
        'projects': projects,
        'tech_stacks': tech_stacks
    })


@user_passes_test(superuser_required, login_url='login')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'Core/add_project.html', {'form': form})


@user_passes_test(superuser_required, login_url='login')
def create_tech_stack(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TechStackForm()
    return render(request, 'Core/add_tech_stack.html', {'form': form})



@user_passes_test(superuser_required, login_url='login')
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'Core/add_project.html', {'form': form, 'is_edit': True})

@user_passes_test(superuser_required, login_url='login')
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'Core/confirm_delete.html', {'object': project, 'type': 'Project'})


@user_passes_test(superuser_required, login_url='login')
def edit_tech_stack(request, pk):
    stack = get_object_or_404(TechStack, pk=pk)
    if request.method == 'POST':
        form = TechStackForm(request.POST, instance=stack)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TechStackForm(instance=stack)
    return render(request, 'Core/add_tech_stack.html', {'form': form, 'is_edit': True})

@user_passes_test(superuser_required, login_url='login')
def delete_tech_stack(request, pk):
    stack = get_object_or_404(TechStack, pk=pk)
    if request.method == 'POST':
        stack.delete()
        return redirect('dashboard')
    return render(request, 'Core/confirm_delete.html', {'object': stack, 'type': 'Tech Stack'})