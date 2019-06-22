from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Item

# Create your views here.
def items_delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('items_index')

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = ''

def items_index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})