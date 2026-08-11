from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=120)
    author = serializers.CharField(max_length=120)
    year = serializers.IntegerField()