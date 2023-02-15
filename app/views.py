from django.shortcuts import render
import requests
import json
from django.contrib import messages

# Create your views here.


def home(request):
    endpoint = 'http://127.0.0.1:8000/contact_api/'
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        response = requests.post(endpoint, json={'name': name, 'email': email, 'course': subject, 'message' : message})
    
    return render(request, 'index.html')

def signup(request):
    endpoint = 'http://127.0.0.1:8000/api/'
    
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        
        response = requests.post(endpoint, json={'name': name, 'email': email, 'course': course})
        res = response.json()
        
        if res['status'] == 201:
            messages.success(request, 'Signup successful, you will recieve a mail for validation!')
        
        if res['status'] == 400:
            messages.warning(request, 'You are signed up with this email address!')
    
    return render(request, 'signup.html')


def django(request):
        
    return render(request, 'django.html')

def frontend(request):
        
    return render(request, 'basic-fronthend.html')

def science(request):
        
    return render(request, 'data-science.html')

def data(request):
        
    return render(request, 'data-analysis.html')

def python(request):
        
    return render(request, 'python.html')

def react(request):
        
    return render(request, 'react.html')



