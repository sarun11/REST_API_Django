from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TestView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        qs = Post.objects.all()
        # post = qs.last()
        serializer = PostSerializer(qs, many=True)
        # serializer = PostSerializer(post)
        return Response(serializer.data)
          
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)       

# def test_view(request):
#     data = {
#         'book': 30,
#         'Pen': 10
#     }
#     return JsonResponse(data)
