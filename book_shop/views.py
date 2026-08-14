from django.shortcuts import render , get_object_or_404
from .models import Book
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import BlocklistPermissions , BookPermissions
from rest_framework import status
# Create your views here.


class BookApiView(APIView):
    def get(self , request):
        books = Book.objects.all()
        serializer = BookSerializer(books , many=True)
        return Response(serializer.data)
    
class UserInfoApiView(APIView):
    permission_classes = [BlocklistPermissions]
    def get(self , request):
        user = request.user
        return Response({
            'username':user.username,
            'email' : user.email,
            'id' : user.id,
        })


class BookManageApiView(APIView):
    permission_classes = [BookPermissions] 
    def get_object(self , pk):
        book = get_object_or_404(Book , id=pk)
        self.check_object_permissions(self.request , book)
        return book

    def get(self , request , pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def delete(self , request , pk):
        book = self.get_object(pk)
        book.delete()
        return Response({'message':'book deleted'} , status=status.HTTP_204_NO_CONTENT)