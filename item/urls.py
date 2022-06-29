from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_items),
    path('<uuid:itemID>/', views.item),
    path('create/', views.item_create),
]
