from rest_framework import generics, permissions
from .models import List
from .serializers import ListSerializer
from drf_api.permissions import IsOwner


class ListList(generics.ListCreateAPIView):
    """
    Lists all the Lists
    The create method adds the user to owner field of the list.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwner]
    queryset = List.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detailed view of the list, edit/delete functionality for owner.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwner]
    queryset = List.objects.all()