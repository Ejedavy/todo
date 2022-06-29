from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_items(request):
    pass


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def item(request, itemID):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return Response({'message': 'Invalid request method'}, 400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def item_create(request):
    pass
