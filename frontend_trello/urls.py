"""frontend_trello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# SWAGGER CONFIGURATION
schema_view = get_schema_view(
   openapi.Info(
      title="Dave's ToDo Project",
      default_version='v1',
      description="""THIS IS A TODO APP.
      
      Here a user is notified via his/her favorite social media
      
      The user can create priority groups and configure the notifications and later assign these priorities to tasks.
      
      The general structure of the platform is Boards, which contains lists and then lists contains the tasks """,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="d.edje@innopolis.university"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('auth/', include('userauth.urls')),
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
    path('list/', include('list.urls')),
    path('item/', include('item.urls')),
    path('schedule/', include('schedule.urls')),
    path('priorities/', include('priorities.urls')),
]
