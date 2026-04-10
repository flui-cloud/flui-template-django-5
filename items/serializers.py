from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(min_length=1, max_length=500)
    createdAt = serializers.CharField(read_only=True)
