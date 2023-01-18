from rest_framework import generics, permissions
from .models import Item
from .serializers import ItemSerializer
from drf_api.permissions import IsOwner


class ItemList(generics.ListCreateAPIView):
    """
    Lists all the Items
    The create method adds the user to owner field of the item.
    """
    serializer_class = ItemSerializer
    permission_classes = [IsOwner]
    queryset = Item.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detailed view of the item, edit/delete functionality for owner.
    """
    serializer_class = ItemSerializer
    permission_classes = [IsOwner]
    queryset = Item.objects.all()
