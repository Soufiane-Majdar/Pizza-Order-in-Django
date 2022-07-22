from django.shortcuts import render,HttpResponse
from .models import User

# Create your views here.

# Login function
def login(request):
    return render(request,'User/login.html')

# Register function
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        try:
            user = User.objects.get(email=email)
            return render(request,'User/register.html',{'error':'Email already exists'})
        except User.DoesNotExist:
            user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,address=address,city=city,zipcode=zip_code)
            user.save()
            return render(request,'User/register.html',{'success':'Registration Successful'})
    else:
            return render(request,'User/register.html')

# logout function
def logout(request):
    return HttpResponse("Logout")

# profile function
def profile(request):
    return render(request,'User/profile.html')
