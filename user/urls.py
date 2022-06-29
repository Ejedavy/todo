from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_user_profile),
    path('edit/', views.edit_user_profile),
]
