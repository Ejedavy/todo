from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_items(request):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_item(request, itemID):
    pass


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_item(request, itemID):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, itemID):
    pass
