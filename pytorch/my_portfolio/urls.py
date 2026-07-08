from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.admin_site.urls if hasattr(admin.site, 'admin_site') else admin.site.urls),
    # The home page displaying project names and personal info
    path('', views.project_list_view, name='project_list'),
    # The detail page path using dynamic integer matching for project IDs
    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),
]