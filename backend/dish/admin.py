from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')

class StructureAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Weight', 'recipe')


admin.site.register(Product, ProductAdmin)
admin.site.register(Structure, StructureAdmin)
