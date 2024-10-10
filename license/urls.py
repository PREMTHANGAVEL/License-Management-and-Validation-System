from django.urls import path
from . import views

urlpatterns = [
    path('validate/', views.validate_license, name='validate_license'),
    path('activate/', views.activate_license, name='activate_license'),
]
