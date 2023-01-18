from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from drf_api.permissions import isOwnerOrReadOnly

class ItemList(APIView):
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(
            items,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(
            data=request.data,
            context={'request': request},
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    serializer_class = ItemSerializer
    permission_classes = [isOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            item = Item.objects.get(pk=pk)
            self.check_object_permissions(self.request, item)
            return item
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(
            item,
            context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(
            item,
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )