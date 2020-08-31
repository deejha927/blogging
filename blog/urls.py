from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path("myblog",views.firstpage,name="myblog"),
    path("article/<int:pk>",detail.as_view(),name="article"),
    path("explore/<int:pk>",explore.as_view(),name="explore"),
    path("login",views.login,name="login"),
    path("signup",views.user_register,name="signup"),
    path("blogs",views.myblog,name="blogs"),
    path("logout",views.logout,name="logout"),
    path("update_con",views.updatecontent,name="update_con"),
    path("update_img",views.updateimg,name="update_img"),
    path("color",views.colorupdate,name="color"),
    path("delete",views.deleteblog,name="delete"),
    path("profile",views.profile,name="profile"),
    path("new",views.newart,name="new"),
    path("updateprofile",views.changeprofile,name="updateprofile")



]