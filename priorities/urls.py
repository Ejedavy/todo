from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_priorities),
    path('<uuid:priorityID>/', views.view_priority),
    path('<uuid:priorityID>/edit/', views.edit_priority),
    path('<uuid:priorityID>/delete/', views.delete_priority),
]
