from django.shortcuts import render
from rest_framework.views import APIView
from .models import VipUser
from .serializer import VipUserSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class VipUserAPIView(APIView):
    def get(self , request):
        vip_user = VipUser.objects.all()
        serializer = VipUserSerializer(vip_user , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self , request):
        serializer = VipUserSerializer(data = request.data)
        if serializer.is_valid():
            # data = serializer.validated_data
            # print(data)
            serializer.save()
            # vip_user = VipUser.objects.create(**data)
            return Response({'status':'ok'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)

