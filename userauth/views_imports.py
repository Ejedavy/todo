from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from bot import Bot
from rest_framework.response import Response
from .serializers import *
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from django.contrib.auth import login,authenticate
from knox.models import AuthToken
from confirmation_token import token_generator
import uuid
from django.core.cache import cache