from django.shortcuts import render

# Create your views here.

#Home function
def home(request):
    return render(request,'Main/home.html')

# item detail function
def item_detail(request,id):
    return render(request,'Main/item_detail.html',{'id':id})

# Contact us function
def contact(request):
    return render(request,'Main/contact.html')