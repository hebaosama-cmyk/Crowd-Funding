from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('<int:project_id>/', views.project_details, name='project_details'),
]