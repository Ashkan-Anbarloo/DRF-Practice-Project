from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import BlocklistPermissions
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