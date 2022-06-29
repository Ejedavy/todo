from django.urls import path, include
from . import views

urlpatterns = [
    path('getbot/', views.get_bot_link),
    path('login/', views.logIn),
    path('signup/', views.signup),
    path('activate_account/<int:code>/', views.activate_account)
]
