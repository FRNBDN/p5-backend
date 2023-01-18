from django.db.models import Count
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwner


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles.
    Post Method is handled by signals, so its not included.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Profile detai view, update functionality for owner.
    """
    queryset = Profile.objects.annotate(
        list_count=Count('owner__list', distinct=True),
        item_count=Count('owner__item', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]