from .serializers_imports import *


class BotLinkSerializer(serializers.Serializer):
    link = serializers.URLField(required=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField()
    token = serializers.CharField(max_length=150, read_only=True)

    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["email", "nickname", "telegram_link", 'telegram_userID', "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
