from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_lists(request):
    pass


@api_view(['GET','PUT', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def list_(request, listID):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method =='DELETE':
        pass
    else:
        return Response({'message':'Invalid request method'}, 400)
