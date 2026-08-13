from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response
# Create your views here.


class BookApiView(APIView):
    def get(self , request):
        books = Book.objects.all()
        serializer = BookSerializer(books , many=True)
        return Response(serializer.data)