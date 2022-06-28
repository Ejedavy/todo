from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_user_profile(request):
    pass


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_profile(request):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    pass
