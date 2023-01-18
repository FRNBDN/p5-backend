from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_file(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError(
                'File size is larger than 10MB'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'list', 'owner',
                  'profile_id', 'profile_image', 'is_owner', 'due_date',
                  'overdue', 'priority', 'state', 'file']
