from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_priorities(request):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_priority(request, priorityID):
    pass


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_priority(request, priorityID):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_priority(request, priorityID):
    pass
