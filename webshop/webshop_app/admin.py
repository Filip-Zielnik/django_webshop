from django.contrib import admin
from .models import Address, Category, Product, Profile, Cart, Order


class AddressAdmin(admin.ModelAdmin):
    """
    Modifies addresses toolbar in Django admin site
    """
    list_display = ('profile', 'city', 'country')


class ProductAdmin(admin.ModelAdmin):
    """
    Modifies products toolbar in Django admin site
    """
    list_display = ('product', 'category', 'price', 'available')
    list_editable = ('available',)


class CartAdminView(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user')
    list_editable = ('quantity',)


admin.site.register(Address, AddressAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(Cart, CartAdminView)
admin.site.register(Order)
