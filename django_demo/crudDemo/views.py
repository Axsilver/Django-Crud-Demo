from django.shortcuts import render, HttpResponse
from .models import myItem
from .forms import *

# Create your views here.
def home(request):
    return render(request, "home.html")

def myItems(request):
    return render(request, "myItems.html", {"myItems": myItem.objects.all()})

def addItem(request):
    form = myItemForm(request.POST)
    if form.is_valid():
        if myItem.objects.filter(title = form.data.get('title')).exists():
            item = myItem.objects.get(title = form.data.get('title'))
            print(item.title, item.desc)
            item.desc = form.data.get('desc')
            item.save()
        else:
            form.save()
    return render(request, "addItem.html", {'form': form})

def deleteItem(request):
    form = myItemDeleteForm(request.POST)
    if form.is_valid():
        myItem.objects.filter(title = form.data.get('title')).delete()
    return render(request, "deleteItem.html", {'form': form})