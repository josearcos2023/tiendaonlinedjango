from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from tienda.models import Categoria,Producto
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer
)

class IndexView(APIView):
    
    def get(self,request):
        lista_categorias = Categoria.objects.all()
        serializer_categoria = CategoriaSerializer(lista_categorias,many=True)
        return Response(serializer_categoria.data)
    
class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg  = 'categoria_id'
    serializer_class = CategoriaSerializer
    
class ProductoViewSet(APIView):
    
    def get(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)

    
class ProductoView(APIView):
    def get(self,request):
        dataProducto = Producto.objects.all()
        serProductos = ProductoSerializer(dataProducto,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
