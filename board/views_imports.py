from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Board
from .serializers import BoardSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404