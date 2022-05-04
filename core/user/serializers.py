from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','name', 'last_name','email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']
