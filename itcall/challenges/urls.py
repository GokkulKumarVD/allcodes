from os import name
from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.jan),
    # path("february", views.feb)
    path("", views.mainpage), 
    path("<int:month>", views.indexnum),
    path("<str:month>", views.index, name="mm") #use <> to make it dynamic page
]

