from rest_framework import serializers
from .models import Book , Author , Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    category = CategorySerializer(many=True , required=False)
    #-------------------
    # author = serializers.SlugRelatedField(slug_field='name' , queryset=Author.objects.all())
    # category = serializers.SlugRelatedField(slug_field='title' , queryset=Category.objects.all() , many=True)
    #-------------------
    # author = serializers.StringRelatedField()
    # category = serializers.StringRelatedField(many=True)
    #-------------------
    # author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all())
    # category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all() , many=True)
    #-------------------
    class Meta:
        model = Book
        fields = '__all__'