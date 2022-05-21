
from django.shortcuts import render
from rest_framework.response import Response

from parser import Search
from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer

class ProductListAPi(APIView):
    # def Parse(self,request):
        
    def get(self,request,num):
        print(request)
        Search(num)
        print("hi")
        queryset = Product.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)

# Create your views here.
