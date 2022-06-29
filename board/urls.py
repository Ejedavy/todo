from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.view_boards),
    path('<uuid:boardID>/', views.board),
    path('create/', views.board_create),
]
