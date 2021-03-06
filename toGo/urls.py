from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project/', views.createProject, name="create_project"),
    path('update_project/<str:pk>/', views.updateProject, name="update_project"),
    path('delete_project/<str:pk>/', views.deleteProject, name="delete_project")
]