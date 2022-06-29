from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        extra_kwargs = {
            'created_by': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_at': {'read_only': True},
        }

