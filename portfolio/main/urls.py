from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("project/<int:project_id>/", views.project, name="project"),
    path('projects/', views.projects, name="projects"),
]