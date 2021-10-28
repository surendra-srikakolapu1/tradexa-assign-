from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','weight','price','image','created_at' , 'updated_at']

# Register your models here.
admin.site.register(Product,ProductAdmin)

