from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class PostView(mixins.ListModelMixin, 
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# class TestView(APIView):
    
#     permission_classes = (IsAuthenticated,)
    
#     def get(self, request, *args, **kwargs):
        
#         qs = Post.objects.all()
#         # post = qs.last()
#         serializer = PostSerializer(qs, many=True)
#         # serializer = PostSerializer(post)
#         return Response(serializer.data)
          
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)       

# def test_view(request):
#     data = {
#         'book': 30,
#         'Pen': 10
#     }
#     return JsonResponse(data)
