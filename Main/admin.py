from django.contrib import admin
from .models import  MenuItem, Card, Order,Review



from django.contrib.auth.models import Group
admin.site.unregister(Group)

# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()


class  MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'about')
    list_filter = ('type',)
    search_fields = ('name',)
    ordering = ('name',)


class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_item', 'quantity', 'total', 'date', 'status')
    list_filter = ('user', 'menu_item', 'date', 'status')
    search_fields = ('user', 'menu_item', 'total')
    ordering = ('-date',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'total', 'date', 'status')
    list_filter = ('user', 'date', 'status')
    search_fields = ('user', 'phone', 'address', 'total')
    ordering = ('-date',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_item', 'review', 'date', 'rating')
    list_filter = ('user', 'menu_item', 'date', 'rating')
    search_fields = ('user', 'menu_item', 'review')
    ordering = ('-date',)


admin.site.register(Review,ReviewAdmin)
admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Order,OrderAdmin)


