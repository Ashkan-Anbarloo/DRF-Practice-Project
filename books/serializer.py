from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_lenght = 120)