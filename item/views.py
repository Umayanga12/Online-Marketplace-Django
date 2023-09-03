from collections import UserDict
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import items, Category
from item.forms import NewItemForm


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(items, pk=pk)

    #getting the related item by searching the item category id 95
    related_item = items.objects.filter(item_cat_id=item.item_cat, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'detail.html', {
        'item': item,
        'related_item': related_item
    })


# adding the new item

@login_required
def new(request):
    form = NewItemForm(request.POST, request.FILES)
    if form.is_valid():
        newItem = form.save(commit=False)
        newItem.created_by = request.user
        newItem.save()

        return redirect('/')
    
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

