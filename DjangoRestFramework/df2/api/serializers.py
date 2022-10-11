from rest_framework import serializers

class studentser(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    rollno=serializers.IntegerField()
    address=serializers.CharField(max_length=100)
