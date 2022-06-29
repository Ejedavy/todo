from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

