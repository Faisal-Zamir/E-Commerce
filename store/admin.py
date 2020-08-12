from django.contrib import admin
from . models import Product, Category,Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','address','phone','status','date']

admin.site.register(Order, AdminOrder)
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)