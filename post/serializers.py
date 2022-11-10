from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField
    profile_id = serializer.ReadOnlyField(source= 'owner.profile.id')
    profile_image = serializer.ReadOnlyField(source= 'owner.profile.image.url')
