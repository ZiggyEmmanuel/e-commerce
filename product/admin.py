#product/admin

from django.contrib import admin
from .models import Category, Product, ProductImage, Review

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'stock', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Review)
