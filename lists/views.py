from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import List
from .serializers import ListSerializer
from drf_api.permissions import isOwnerOrReadOnly


class ListList(APIView):
    """
    Lists all the TodoLists
    Post method is handled by signals, so its not included
    """
    serializer_class = ListSerializer
    permission_classes = [
        permissions.IsAuthenticated
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


class ListDetail(APIView):
    serializer_class = ListSerializer
    permission_classes = [isOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            list = List.objects.get(pk=pk)
            self.check_object_permissions(self.request, list)
            return list
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        list = self.get_object(pk)
        serializer = ListSerializer(
            list,
            context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        list = self.get_object(pk)
        serializer = ListSerializer(
            list,
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        list = self.get_object(pk)
        list.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )