from rest_framework import serializers
from .models import stumodel


class serializerst(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rollno = serializers.IntegerField()
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return stumodel.objects.create(**validated_data)
