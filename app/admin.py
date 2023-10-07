from django.contrib import admin
from app.models import Product, Category, Vendor, ProductImages, ProductReview, Wishlist, CategoryImages

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class CategoryImagesAdmin(admin.TabularInline):
    model = CategoryImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['title', 'product_image', 'featured', 'description','product_status','file']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image','description']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
