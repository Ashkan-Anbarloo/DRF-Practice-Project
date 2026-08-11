from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from rest_framework import status
from .serializer import BookSerializer
# Create your views here.

class BookApiView(APIView):
    def get(self , request):
        books = Book.objects.all()
        # data = []
        # for book in books :
        #     data.append({
        #         'id':book.id,
        #         'title':book.title,
        #         'author':book.author,
        #         'year':book.year,
        #     })
        serializer = BookSerializer(books , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        # title = request.data.get('title')
        # author = request.data.get('author')
        # year = request.data.get('year')
        # if not all([title , author , year]):
        #     return Response({'error':"تمام فیلد ها الزلمی است ."},status=status.HTTP_400_BAD_REQUEST)
        
        # book = Book.objects.create(title=title , author=author , year=int(year))
        # return Response({'id':book.id , 'title':book.title , 'author':book.author , 'year':book.year} , status=status.HTTP_201_CREATED)
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            book = Book.objects.create(**data)
            return Response(BookSerializer(book).data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
