from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, blank=True)
    last_name = models.CharField(max_length=500, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True ,blank=True ,null=True)
    updated_at = models.DateTimeField(auto_now=True ,blank=True,null=True)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 