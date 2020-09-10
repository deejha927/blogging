from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
from blogging import settings
# Create your models here.

class register(models.Model):
    user_email=models.CharField(max_length=100)
    user_pass=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    profile_pic=models.ImageField(upload_to="",default="user.png",null=True,blank=True)
    age=models.DateField(null=True,blank=True)
    account_created_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
         return self.user_email
def upload_path(instance, filename):
    # change the filename here is required
    return os.path.join(BASE_DIR,"static/images")

class blog_post(models.Model):
    title=models.CharField(max_length=300)
    publisher=models.ForeignKey(register,on_delete=models.CASCADE,null=True,blank=True)
    body=models.TextField()
    published_date=models.DateField(auto_now_add=True,null=True,blank=True)
    blog_image=models.ImageField(upload_to="",null=True,blank=True)
    blog_color=models.CharField(default="#ffffff",max_length=8)

    def __str__(self):
        return self.title
