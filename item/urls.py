from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_items),
    path('<uuid:itemID>/', views.view_item),
    path('<uuid:itemID>/edit/', views.edit_item),
    path('<uuid:itemID>/delete/', views.delete_item),
]
