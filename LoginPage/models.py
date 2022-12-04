from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 
from django.contrib.auth.models import AbstractUser
from UserLogin import settings
from django.contrib.auth import get_user_model

# class Profile(AbstractUser):
#     email = models.EmailField(unique=True)
#     is_verified = models.BooleanField(default=False)
#     company = models.CharField(max_length=255,blank=False)
#     role = models.CharField(max_length=255,blank=False)

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    company = models.CharField(max_length=255,blank=False)
    role = models.CharField(max_length=255,blank=False)
    intrest = models.CharField(max_length=255,blank = True)
    
    def __str__(self):
        return self.user.first_name + " " +  self.user.last_name

 
@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)

    instance.profile.save()
    
@receiver(post_save, sender = User)
def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()
    

class Trigger(models.Model):
    
    patient  = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING)
    assignment = models.TextField(null=True,max_length=255)
    
    def __str__(self):
        return self.patient.username
    
    