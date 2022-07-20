from django.shortcuts import render,HttpResponse

# Create your views here.

# Login function
def login(request):
    return render(request,'User/login.html')

# Register function
def register(request):
    return render(request,'User/register.html')

# logout function
def logout(request):
    return HttpResponse("Logout")

# profile function
def profile(request):
    return render(request,'User/profile.html')
