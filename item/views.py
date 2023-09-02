from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import items,Category
from .forms import NewItemForm

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(items, pk=pk)

    # related_items = items.objects.filter(category = '')
    related_item = items.objects.filter(item_cat_id=item.item_cat, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'detail.html', {
        'item': item,
        'related_item': related_item
    })

#adding the new item

@login_required
def new(request):
    form = NewItemForm()

    return render(request, 'item/form.html',{
        'form': form
    })
