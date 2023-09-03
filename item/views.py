from collections import UserDict
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import items, Category
from item.forms import NewItemForm, EditItemForm
from django.db.models import Q


def search_item(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    serch_result = items.objects.filter(is_sold=False)

    if category_id:
        serch_result = items.objects.filter(item_cat_id=category_id)

    if query:
        serch_result = serch_result.filter(name__icontains=query | Q(discription__icontains=query))

    return render(request, 'item/browse.html', {
        'item': serch_result,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(items, pk=pk)

    # getting the related item by searching the item category id 95
    related_item = items.objects.filter(item_cat_id=item.item_cat, is_sold=False).exclude(pk=pk)[0:3]
    # render the template
    return render(request, 'detail.html', {
        'item': item,
        'related_item': related_item
    })


# adding the new item

@login_required
def new(request):
    if request.method == 'POST':
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


@login_required
def edit(request, pk):
    item = get_object_or_404(items, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

        return redirect('/')

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })


@login_required
def delete(request, pk):
    # getting the data from the database
    item = get_object_or_404(items, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
