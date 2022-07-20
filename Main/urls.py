from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('contact/', views.contact, name='contact'),
    
]
