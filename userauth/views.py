from .views_imports import *


@swagger_auto_schema(methods=["get"],
                     responses={status.HTTP_200_OK: BotLinkSerializer()})
@api_view(["GET"])
@csrf_exempt
def get_bot_link(request):
    serialized = BotLinkSerializer(data={'link': settings.BOT_LINK})
    if serialized.is_valid(raise_exception=True):
        print(serialized.initial_data)
        return Response(serialized.data, status=200)


@swagger_auto_schema(methods=["post"],
                     request_body=LoginSerializer,
                     responses={status.HTTP_200_OK: LoginSerializer()})
@api_view(['POST'])
@csrf_exempt
def logIn(request):
    serialized = LoginSerializer(data=request.data)
    if serialized.is_valid(raise_exception=True):
        user = MyUser.objects.filter(email=serialized.data.get("email"))
        if not user.exists():
            return Response({"message": "Sign up instead"}, 400)
        else:
            user = authenticate(request, password=serialized.data.get("password"),
                                username=serialized.data.get("email"))
            if user is None:
                return Response({"message": "Incorrect Credentials"}, status=400)
            else:
                token = AuthToken.objects.create(user=user)[1]
                login(request, user)
                return Response({
                    "email": user.email,
                    "token": token,
                }, status=200)


@swagger_auto_schema(methods=["post"],
                     request_body=SignUpSerializer)
@api_view(['POST'])
@csrf_exempt
def signup(request):
    serialized = SignUpSerializer(data=request.data)
    if serialized.is_valid(raise_exception=True):
        user = MyUser.objects.filter(email=serialized.validated_data.get("email"))
        if user.exists():
            return Response({"message": "User already exists"}, 400)
        else:
            try:
                user = serialized.save()
                code = token_generator.make_token(user=user)
                bot = Bot()
                bot.send_account_creation_code(code, serialized.data.get("telegram_userID"))
                return Response({"message": "Code sent"}, 200)
            except Exception as e:
                return Response({"message": str(e)}, status=400)
    else:
        return Response({"message": "Invalid request"}, 400)


@swagger_auto_schema(methods=["post"],
                     responses={200: LoginSerializer()})
@api_view(['POST'])
@csrf_exempt
def activate_account(request, code):
    user = MyUser.objects.get(id=uuid.UUID(cache.get(code)[0]))
    if user.is_active:
        return Response({"message": "User already active"})
    else:
        user.is_active = True
        user.save()
        token = AuthToken.objects.create(user=user)[1]
        login(request, user)
        return Response({
            "email": user.email,
            "token": token,
        }, status=200)
