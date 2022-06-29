from .views_imports import *


@swagger_auto_schema(methods=["get"],
                     responses={200: UserSerializer()})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_user_profile(request):
    serialized = UserSerializer(instance=request.user)
    return Response(serialized.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_profile(request):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    pass
