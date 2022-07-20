from django.shortcuts import render,HttpResponse

# Create your views here.

# Login function
def login(request):
    return HttpResponse("Login")

# Register function
def register(request):
    return HttpResponse("Register")

# logout function
def logout(request):
    return HttpResponse("Logout")

# profile function
def profile(request):
    return HttpResponse("Profile")
