from django.urls import path
from . import views
from .views import TestimonyListView

urlpatterns = [
    
    path('', views.project_list_view, name='project_list'),
    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path('projects/add/', views.add_project, name='add_project'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/', TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),

   
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/project/add/', views.create_project, name='create_project'),
    path('dashboard/tech-stack/add/', views.create_tech_stack, name='create_tech_stack'),


    path('dashboard/project/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('dashboard/project/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('dashboard/tech-stack/<int:pk>/edit/', views.edit_tech_stack, name='edit_tech_stack'),
    path('dashboard/tech-stack/<int:pk>/delete/', views.delete_tech_stack, name='delete_tech_stack'),
]