from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_priorities),
    path('<uuid:priorityID>/', views.priority),
]
