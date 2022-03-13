from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("shop",views.shop,name="shop"),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("checkout",views.checkout,name='checkout')
]
