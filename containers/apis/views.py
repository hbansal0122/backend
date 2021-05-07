from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def containers(request):
    """
    List all containers, or create a new container.
    """
    if request.method == 'GET':
        return Response({"message":"data of all containers"}, status=status.HTTP_200_OK)

    elif request.method == 'POST':     
        print (request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)
