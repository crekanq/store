from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)

admin.site.register(Product)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
