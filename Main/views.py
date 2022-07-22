from django.shortcuts import render


from .models import MenuItem
from User.models import Contact

# Create your views here.

#Home function
def home(request):
    MenuItems = MenuItem.objects.all()
    #print(MenuItems)
    return render(request,'Main/home.html',{'MenuItems':MenuItems})

# item detail function
def item_detail(request,id):
    return render(request,'Main/item_detail.html',{'id':id})

# Contact us function
def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            contact = Contact(name=name,email=email,subject=subject,message=message)
            contact.save()
            return render(request,'Main/contact.html',{'success':'Message sent successfully'})
        except:
            return render(request,'Main/contact.html',{'error':'Message not sent'})
    else:
        return render(request,'Main/contact.html')