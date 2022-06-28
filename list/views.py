from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_lists(request):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_list(request, listID):
    pass


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_list(request, listID):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_list(request, listID):
    pass
