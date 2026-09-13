from django.urls import path
from .views import donation_page

urlpatterns = [
    path('<int:project_id>/', donation_page, name='donation_page'),
]