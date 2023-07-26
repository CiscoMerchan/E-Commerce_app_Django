from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.

from item.models import Item

#The @login_required decorator is to requirer that for those actions the user need to be login 
@login_required
def index(request):
    items= Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html',{
        'items': items,
    }) 

