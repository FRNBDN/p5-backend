from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    list = serialzers.ReadOnlyField(source='list.title')
    list_id = serialzers.ReadOnlyField(source='list.id')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'list', 'list.id', 'owner',
                  'profile_id', 'profile_image', 'is_owner', 'due_date',
                  'overdue', 'priority', 'state', 'file']
