from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'edit/<int:id>/',
        views.edit_internship,
        name='edit_internship'
    ),

    path(
        'delete/<int:id>/',
        views.delete_internship,
        name='delete_internship'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),
]