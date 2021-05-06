from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',
                    'created_at', 'image', 'slug',)


admin.site.register(Images)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'new_price',
                    'old_price', 'amount', 'status', 'image')

    inlines = [ProductImageInline]


admin.site.register(SliderImage)
admin.site.register(RightImage)
