from django.shortcuts import render , get_object_or_404
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


class UpdateUserAPIView(APIView):
    def get_object(self , pk):
        try:
            return VipUser.objects.get(id=pk)
        except VipUser.DoesNotExist:
            return None

    def put(self , request , pk):
        # vip_user = get_object_or_404(VipUser , id=pk)
        # vip_user = VipUser.objects.get(id=pk)
        vip_user = self.get_object(pk)

        if not vip_user:
            return Response({'error':'Vip user not found'} , status=status.HTTP_404_NOT_FOUND)
        
        serializer = VipUserSerializer(instance=vip_user , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'ok'} , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        vip_user = self.get_object(pk)
        if not vip_user:
            return Response({'error':'Vip user not found'} , status=status.HTTP_404_NOT_FOUND)
        vip_user.delete()
        return Response({'status':'OK'} , status=status.HTTP_200_OK)
            

