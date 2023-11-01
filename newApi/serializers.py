from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    number = serializers.IntegerField()
    address = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Change this line to update the instance fields
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.address = validated_data.get('address', instance.address)

        # Save the instance to persist the changes
        instance.save()
        return instance
