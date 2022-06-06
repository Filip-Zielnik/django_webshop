from django.contrib import admin
from .models import Address, Category, Comment, Product, Profile


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


admin.site.register(Address, AddressAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
