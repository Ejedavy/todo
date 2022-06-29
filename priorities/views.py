from .views_imports import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_priorities(request):
    pass


@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def priority(request, priorityID):
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

