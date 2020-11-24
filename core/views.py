from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class TestView(APIView):
    
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
