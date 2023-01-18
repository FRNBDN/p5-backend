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
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwner]