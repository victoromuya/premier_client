from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    response = requests.get('http://127.0.0.1:8000/courses/')
    print(response.json())
    
    return render(request, 'index.html')
