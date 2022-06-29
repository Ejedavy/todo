from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_lists),
    path('<uuid:listID>/', views.list_),
]
