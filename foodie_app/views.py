from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# create views here 

def index(request):
    item_list = Item.objects.all()
    
    context = {
      'item_list': item_list,
    }
    return render(request, 'foodie_app/index.html', context)

def item(request):
    return HttpResponse('<h2>This is an item</h2>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = { 
        'item': item,
    }

    return render(request, 'foodie_app/detail.html', context)
