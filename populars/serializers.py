from django.db import IntegrityError
from rest_framework import serializers
from populars.models import Popular


class PopularSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model
    The create method handles the unique constraint on 'owner' and 'post'
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Popular
        fields = ["id", "created_at", "owner", "post"]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
