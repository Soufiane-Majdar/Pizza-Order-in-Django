from django.shortcuts import render,HttpResponse

# Create your views here.

#Home function
def home(request):
    return HttpResponse("Home")

# item detail function
def item_detail(request,id):
    return HttpResponse("Item Detail: " + str(id))

# Contact us function
def contact(request):
    return HttpResponse("Contact us")