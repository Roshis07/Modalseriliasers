from rest_framework import serializers


class userSerializer(serializers.Serializer):
    id = serializers.ImageField(read_only=True)
    name = serializers.StringRelatedField()
    number = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
