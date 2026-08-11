from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET'])
def hello_world(request):
    name = request.query_params.get('name' , 'کاربر ناشناس')
    return Response({'message':f'Hello, {name}'})

class HelloAPIView(APIView):
    def get(self , request):
        name = request.query_params.get('name' , 'کاربر ناشناس')
        return Response({'message':f'hello , {name}'})

    def post(self , request):
        name = request.data.get('name' , 'not found')
        return Response({'message':f"Hello {name} (post)"})