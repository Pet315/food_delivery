from django.contrib import admin
from main.models import *
from import_export.admin import ImportExportModelAdmin


class ShopAdmin(ImportExportModelAdmin):
    pass


class ProductAdmin(ImportExportModelAdmin):
    pass


class CartAdmin(ImportExportModelAdmin):
    pass


class OrderAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
