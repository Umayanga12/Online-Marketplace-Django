from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

from item.models import items


@login_required
def index(request):
    Item = items.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {
        'item': Item,
    })


