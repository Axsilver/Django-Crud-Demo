from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("myItems", views.myItems, name="myItems"),
    path("addItem", views.addItem, name="addItem"),
    path("deleteItem", views.deleteItem, name="deleteItem")
]
