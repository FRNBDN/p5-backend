from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import List
from .serializers import ListSerializer


class ListList(APIView):
    """
    Lists all the TodoLists
    Post method is handled by signals, so its not included
    """
    serializer_class = ListSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(
            lists,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ListSerializer(
            data=request.data,
            context={'request': request},
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)