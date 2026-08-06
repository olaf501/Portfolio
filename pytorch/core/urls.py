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
]