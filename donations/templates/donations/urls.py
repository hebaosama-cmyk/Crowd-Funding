from django.urls import path
from .views import donation_page

urlpatterns = [
    path('', donation_page, name='donation_page'),
]