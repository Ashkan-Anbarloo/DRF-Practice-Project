from rest_framework import serializers

class VipUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)
    age = serializers.IntegerField()
