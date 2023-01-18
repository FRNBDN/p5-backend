from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwner
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List of all comments, create a comment.
    when comment created, owner is set to user.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'item'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Comment detail, update or delete functionality for owner.
    """
    permission_classes = [IsOwner]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()