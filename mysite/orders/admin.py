from django.contrib import admin

# Register your models here.

from .models import Customer, Order, Status, Product_order, Product

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class ProductOrdersInline(admin.TabularInline):
    model = Product_order
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('customer_id', 'status_id')
    inlines = [ProductOrdersInline]

class ProductOrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'quantity')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status)
admin.site.register(Product_order, ProductOrdersAdmin)
admin.site.register(Product, ProductAdmin)