from django.contrib import admin
from .models import User,Contact
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address')
    list_filter = ('address',)
    search_fields = ('address', 'email', 'first_name', 'last_name')
    ordering = ('last_name',)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'date')
    list_filter = ('name', 'email', 'subject', 'message', 'date')
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-date',)





admin.site.register(User, UserAdmin)
admin.site.register(Contact,ContactAdmin)