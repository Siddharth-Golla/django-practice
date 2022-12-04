from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskList.as_view(), name="tasks"),
    path("task/<int:pk>", views.TaskDetail.as_view(), name='task'),
    path("task-create/", views.TaskCreate.as_view(), name="task-create"),
    path("task-edit/<int:pk>", views.TaskEdit.as_view(), name="task-edit"),
    path("task-delete/<int:pk>", views.TaskDelete.as_view(), name="task-delete"),
]