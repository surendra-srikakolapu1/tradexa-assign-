from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','user','first_name','last_name','email','created_at' , 'updated_at']


admin.site.register(Profile,ProfileAdmin) 