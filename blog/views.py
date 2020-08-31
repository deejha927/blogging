from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import datetime

# Create your views here.
from django.utils.dateparse import parse_date
def homepage(request):
    return render(request,"index.html")
    
def firstpage(request):
    data=blog_post.objects.all().order_by('-id')
    return render(request,"homepage.html",{"data":data})

class detail(DetailView):
    model=blog_post
    template_name="articles.html"

class explore(DetailView):
    model=blog_post
    template_name="explore_article.html"

def myblog(request):
    uid=request.session.get('userid')
    reg=register.objects.get(pk=uid)
    myblog=blog_post.objects.filter(publisher_id=reg.id).order_by('-id')
    return render(request,"myblog.html",{"myblog":myblog})


def login(request):
    if request.method=="POST":
        f=0
        reg=register.objects.all()
        usermail=request.POST["mail"]
        userpass=request.POST["password"]
        for val in reg:
            if val.user_email==usermail and val.user_pass==userpass:
                request.session["userid"]=val.id
                f=1
        if f==1:
            return render(request,"index.html")
        else:
            return render(request,"login.html",{"msg":"Email Or Password Wrong"})
    return render(request,"login.html")

def logout(request):
    del request.session["userid"]
    return render(request,"index.html")

def user_register(request):
    f=0
    if request.method=="POST":
        check=register.objects.all()
        for val in check:
            if val.user_email==request.POST["mail"]:
                f=1
        if f==1:
            return render(request,"signup.html",{"msg":"You Already Have An Account."})
        else:
            reg=register()
            reg.user_email=request.POST["mail"]
            reg.user_pass=request.POST["password"]
            reg.first_name=request.POST["fname"]
            reg.last_name=request.POST["lname"]
            reg.save()
            return render(request,"login.html",{"msg1":"Successfully Registered. Now You Can Login."})
    return render(request,"signup.html")

def updatecontent(request):
    data=json.loads(request.body)
    if "userid" in request.session:
        update_blog=blog_post.objects.get(pk=data["blogid"])
        update_blog.body=data["textdata"]
        update_blog.save()
        return JsonResponse("Your Blog Content Has Been Changed",safe=False)
    return JsonResponse("You Are Not Logined",safe=False)


def updateimg(request):
    if request.method=="POST":
        if "userid" in request.session:
            files = request.FILES  # multivalued dict
            image = files.get("image")
            blog_id=request.POST["title"]
            update_blog=blog_post.objects.get(pk=blog_id)
            update_blog.blog_image=image
            update_blog.save()
            uid=request.session.get('userid')
            reg=register.objects.get(pk=uid)
            myblog=blog_post.objects.filter(publisher_id=reg.id)
            return render(request,"myblog.html",{"myblog":myblog})
    return render(request,"index.html")

def colorupdate(request):
    data=json.loads(request.body)
    if "userid" in request.session:
        colorscheme=blog_post.objects.get(pk=data["blogid"])
        colorscheme.blog_color=data["color"]
        colorscheme.save()
        return JsonResponse("Theme Updated",safe=False)
    return JsonResponse("You Are Not Logined",safe=False)

def deleteblog(request):
    data=json.loads(request.body)
    print(data["blogid"])
    if 'userid' in request.session:
         blog=blog_post.objects.get(pk=data["blogid"])
         blog.delete()
    return JsonResponse("Deleted",safe=False)

def newart(request):
    if request.method=="POST":
        if 'userid' in request.session:
            files = request.FILES  # multivalued dict
            image = files.get("image")
            print(image)
            print(request.POST["title"])
            print(request.POST["text1"])
            uid=request.session.get('userid')
            reg=register.objects.get(pk=uid)
            valid_user=User.objects.get()
            uid=valid_user.id
            blog=blog_post()
            blog.title=request.POST["title"]
            blog.publisher=reg
            blog.body=request.POST["text1"]
            blog.blog_image=image
            blog.save()
            reg=register.objects.get(pk=uid)
            myblog=blog_post.objects.filter(publisher_id=reg.id).order_by('-id')
            return render(request,"myblog.html",{"myblog":myblog})
        else:
            return render(request,"homepage.html")   
    return render(request,"new_article.html")


def profile(request):
    if 'userid' in request.session:
        uid=request.session.get('userid')
        reg=register.objects.get(pk=uid)
        blogs=blog_post.objects.filter(publisher_id=reg).count()
    return render(request,"profile.html",{"reg":reg,"count":blogs})

def changeprofile(request):
    if 'userid' in request.session:
        uid=request.session.get('userid')
        reg=register.objects.get(pk=uid)
        blogs=blog_post.objects.filter(publisher_id=reg).count()
        if request.method=="POST":
            files = request.FILES  # multivalued dict
            image = files.get("image")
            reg.first_name=request.POST["fname"]
            reg.last_name=request.POST["lname"]
            reg.user_email=request.POST["mail"]
            reg.profile_pic=image
            reg.save()
    return render(request,"profile.html",{"reg":reg,"count":blogs})
