from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

import warnings
from django.http import HttpResponse

import random
# Create your views here.

def index(request):
    return HttpResponse("Test flight")

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_move(request):
    """
    Returns a move
    """
    board = filter_board(request.data['board'])
    # You now have the board as data. Implement your logic

    # Return the move as an integer 0 through 6 inclusive
    move = random.randrange(0, 7)
    print(move)
    return Response(move)

def filter_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
                board[i][j] = 0
    return board
