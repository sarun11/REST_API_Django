from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TestView(APIView):
    
    def get(self, request, *args, **kwargs):
        data = {
            'book': 30,
            'Pen': 10
        } 
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        data = {
            'book': 40,
            'Pen': 10
        } 
        return Response(data)
        

# def test_view(request):
#     data = {
#         'book': 30,
#         'Pen': 10
#     }
#     return JsonResponse(data)
