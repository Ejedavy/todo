from django.urls import path, include
from knox.views import LogoutView, LogoutAllView

from . import views


urlpatterns = [
    path('getbot/', views.get_bot_link),
    path('login/', views.logIn),
    path('logout/', LogoutView.as_view()),
    path('logout_all/', LogoutAllView.as_view()),
    path('signup/', views.signup),
    path('activate_account/<int:code>/', views.activate_account)
]
