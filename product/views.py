from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet




# Create your views here.
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({
                "status":True,
                "Massage":"Successfully deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status":False,
                "Massage":"book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer




class ProductDetailApiView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            serializer_data = ProductSerializer(product).data
            
            data = {    
                "status": "Successfull",
                "book": serializer_data
                
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"status": "False",
                             "massage": "Product is not found"}, status=status.HTTP_404_NOT_FOUND)
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class ProductUpdateApiView(APIView):
    def put(self, request, pk):
        product = get_object_or_404(Product.objects.all(), id=pk)
        data = request.data
        serializer = ProductSerializer(instance=product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({
            "status":True,
            "massage":f"Product {product_saved} updated successfully"
        })
        
class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    
class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer