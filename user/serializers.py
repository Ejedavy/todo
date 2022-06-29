from .serializers_imports import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
        extra_kwargs = {
            'password': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'is_superuser': {'read_only': True},
            "groups": {'read_only': True},
            "user_permissions": {'read_only': True}
        }
