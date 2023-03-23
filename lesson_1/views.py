from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def bio(request, user_name):
    print(f"Hello {user_name}")
    return render(request, 'index.html')

def get_user(request, user_id):
    return HttpResponse("Get user by id")

def get_all_users(request):
    print(type(request))
    print(request)
    return HttpResponse("Get all users")