from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Item.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('due_date')
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


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detailed view of the item, edit/delete functionality for owner.
    """
    serializer_class = ItemSerializer
    permission_classes = [IsOwner]
    queryset = Item.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-due_date')
