from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = List.objects.annotate(
        items_count=Count('item', distinct=True)
    ).order_by('items_count')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile'
    ]
    search_fields = [
        'owner__username',
        'title'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detailed view of the list, edit/delete functionality for owner.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwner]
    queryset = queryset = List.objects.annotate(
        items_count=Count('item', distinct=True)
    ).order_by('items_count')