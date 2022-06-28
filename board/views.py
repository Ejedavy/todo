from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_boards(request):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_board(request, boardID):
    pass


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_board(request, boardID):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_board(request, boardID):
    pass
