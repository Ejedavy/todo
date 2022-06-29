from .views_imports import *


@swagger_auto_schema(methods=["get"],
                     responses={200: BoardSerializer(many=True)})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_boards(request):
    boards = Board.objects.filter(created_by=request.user).all()
    serialized = BoardSerializer(boards, many=True)
    return Response(serialized.data, status=200)


@swagger_auto_schema(methods=["GET"],
                     responses={200: BoardSerializer(many=True)})
@swagger_auto_schema(methods=["PATCH"],
                     request_body=BoardSerializer,
                     responses={200: BoardSerializer(many=True)})
@swagger_auto_schema(methods=["DELETE"])
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def board(request, boardID):
    board_ = get_object_or_404(Board, id=boardID)
    if request.method == 'GET':
        serialized = BoardSerializer(board_, many=False)
        return Response(serialized.data, status=200)
    elif request.method == 'PATCH':
        data = request.data
        serialized = BoardSerializer(instance=board_, partial=True, data=data)
        if serialized.is_valid(raise_exception=True):
            board_ = serialized.save()
            return Response(BoardSerializer(board_, many=False).data, status=200)
    elif request.method == 'DELETE':
        board_.delete()
        return Response({}, status=200)
    else:
        return Response({'message': 'Invalid request method'}, 400)


@swagger_auto_schema(methods=["post"],
                     request_body=BoardSerializer,
                     responses={200: BoardSerializer(many=False)})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def board_create(request):
    data = request.data
    serialized = BoardSerializer(data=data)
    if serialized.is_valid(raise_exception=True):
        board_ = serialized.save(created_by=request.user)
        return Response(BoardSerializer(board_, many=False).data, status=200)
