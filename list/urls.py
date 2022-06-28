from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_lists),
    path('<uuid:listID>/', views.view_list),
    path('<uuid:listID>/edit/', views.edit_list),
    path('<uuid:listID>/delete/', views.delete_list),
]
