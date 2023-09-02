from django.shortcuts import render, get_object_or_404
from .models import items


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(items, pk=pk)

    return render(request, 'detail.html', {
        'item': item
    })
