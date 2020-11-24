from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def test_view(request):
    data = {
        'book': 30,
        'Pen': 10
    }
   
    return JsonResponse(data)
