from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.view_boards),
    path('<uuid:boardID>/', views.view_board),
    path('<uuid:boardID>/edit/', views.edit_board),
    path('<uuid:boardID>/delete/', views.delete_board),
]
