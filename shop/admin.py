from django.contrib import admin
from .models import *


# Register your models here.
class cat_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


admin.site.register(category, cat_admin)


class prod_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'image', 'available']
    list_editable = ['price', 'stock', 'image', 'available']


admin.site.register(product, prod_admin)
