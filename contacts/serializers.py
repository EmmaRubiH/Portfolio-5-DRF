from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    contact_name = serializers.ReadOnlyField(source='contact.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Contacts
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'created_at',
            'updated_at', 'contact', 'contact_name', 'is_owner', 'name',
        ]


class ContactsDetailSerializer(ContactsSerializer):
    contact = serializers.ReadOnlyField(source='contact.id')
