from .views_imports import *


@swagger_auto_schema(methods=["get"],
                     responses={200: UserSerializer()})
@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def view_user_profile(request):
    if request.method == 'GET':
        serialized = UserSerializer(instance=request.user)
        return Response(serialized.data)
    elif request.method == 'DELETE':
        pass
    else:
        return Response({'message': 'Invalid request method'}, 400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_profile(request):
    pass
